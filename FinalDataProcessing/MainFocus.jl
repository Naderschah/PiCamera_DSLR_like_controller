# The code to fuse images will be located here
include("Datastructures.jl")
using .Datastructures
include("./IO_dp.jl")
import .IO_dp

include("./ContrastFunctions.jl")
import .ContrastFunctions
include("./Grey_Projectors.jl")
import .GreyProjectors
include("./ImageFusion.jl")
import .ImageFusion

using Base.Threads
using Images

println("Loaded")

path = "/media/felix/3677421f-5daf-4ea7-ba33-31b09d11edcf/Images/SmallWasp/"
save_path = "/mnt/rapid_storage_2/SmallWasp/"
blackpoint = [0,0,0]
contrast_precision = Float32 
width = 4056
height = 3040
debug = false
pp = Datastructures.ProcessingParameters(contrast_precision, ContrastFunctions.LoG, GreyProjectors.lstar, blackpoint, path, save_path,width, height, debug)


function FocusFusion(parameters::Datastructures.ProcessingParameters,tst::Bool=false)
    if tst # When profiling need to run once to initialize
        return
    end
    # Fix paths
    parameters.path         = IO_dp.FixPath(parameters.path)
    parameters.save_path    = IO_dp.FixPath(parameters.save_path)

    # Epsilons in case of Nans resulting from the weight matrix scaling
    epsilons = [1e-12,1e-10, 1e-8, 1e-6]
    printstyled("Running with $(nthreads()) threads\n", color=:blue)
    # Grab image identifiers
    ImagingGrid = IO_dp.GrabIdentifiers(parameters.path)
    #Temp override
    #ImagingGrid.exp = ["NoIR"]
    #ImagingGrid.y =[47510]
    #ImagingGrid.z = [12678]
    failed_im = []
    # Iterate the imaging grid
    total = length(ImagingGrid.y)*length(ImagingGrid.z)*length(ImagingGrid.exp)
    counter = 0
    for ei in ImagingGrid.exp
    for yi in ImagingGrid.y
    for zi in ImagingGrid.z
        counter += 1
        final_name = IO_dp.GenerateFinalFileName(yi,zi,ei)
        success = false
        # Check file doesnt exist
        if !isfile("$(save_path)$(final_name)") || parameters.debug
            fail_count = 1
            start = time()
            while fail_count <= 4
                println("Doing image $(counter) from $(total)")
                println("Focused Name: $(final_name)")
                # Generate file names
                fnames = [IO_dp.GenerateFileName(xi,yi,zi,ei) for xi in ImagingGrid.x]
                # Run stacking for yze postion
                image = ImageFusion.MKR(fnames, parameters, epsilons[fail_count])
                # Save Image check for nans
                if any(isnan.(image))
                    printstyled("Image $(final_name) has NaNs restarting\n", color=:red)
                    fail_count += 1
                else
                    Images.save("$(save_path)$(final_name)", image)
                    success = true
                    break
                end
            end

            if success
                printstyled("Completed $(final_name)\n", color=:green)
                printstyled("Time elapsed: $(time() - start)\n", color=:blue)
            else
                printstyled("Failed $(final_name)\n", color=:red)
                printstyled("Time elapsed: $(time() - start)\n", color=:red)
                failed_im = push!(failed_im, final_name)
            end
        else

            printstyled("$(final_name) already exists, skipping\n", color=:yellow)

        end
    end
    end
    end
    println("Failed images: $(failed_im)")
end

# Profiling
using Profile
#using ProfileView # using porfile view
#ProfileView.set_theme!(:dark)
#ProfileView.@profview FocusFusion(pp)
using PProf # Using PProf

if isinteractive()
    # Profilling - Runs only in repl
    
    Profile.clear()
    @profile FocusFusion(pp)
    pprof()
else
    FocusFusion(pp)
end