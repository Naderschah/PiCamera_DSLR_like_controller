# Functions regarding image loading, file name parsing, data saving will be located here


module IO_dp

include("./Datastructures.jl")
import .Datastructures

include("./ImagePlacement.jl")

export GenerateFileName, GenerateFinalFileName, FixPath, GrabIdentifiers, GetFocusedIdentifiers, GetFocusedImageGrid, LoadDNGLibRaw, RowColumnIndexNaming

# Generate pre focus file naming patterns
function GenerateFileName(x,y,z,exp)
    if typeof(exp) == Int
        return "$(x)_$(y)_$(z)_exp$(exp)mus.dng"
    else
        return "$(x)_$(y)_$(z)_$(exp).dng"
    end
end

function GenerateFinalFileName(x,y,e)
    return "Focused_y=$(x)_z=$(y)_e=$(e).png"
end

function FixPath(path)
    if endswith(path, "/")
        return path
    else
        return path*"/"
    end
end


# Get image identifiers from directory
function GrabIdentifiers(image_directory)
    files = readdir(image_directory)
    x_y_z_exp = [split(i, "_") for i in files]
    x_y_z = [[parse(Int, String(i[1])),parse(Int, String(i[2])), parse(Int, String(i[3]))] for i in x_y_z_exp]
    exp = []
    try
        exp = unique([parse(Int, String(split(i[4], ".")[1])[4:end-3]) for i in x_y_z_exp])
    catch # For one exposure
        exp = ["NoIR"]
    end
    x = unique([i[1] for i in x_y_z])
    y = unique([i[2] for i in x_y_z])
    z = unique([i[3] for i in x_y_z])
    # We will only do one yz pos for starters
    x = sort(x)
    y = sort(y)
    z = sort(z)
    
    return Datastructures.ImagingGrid(x,y,z,exp)
end

function GetFocusedIdentifiers(ImagingParams::Datastructures.ProcessingParameters)
    files = readdir(ImagingParams.save_path)
    f_y_z_exp = [split(i, "_") for i in files]
    f_y_z = [ endswith(i[end], ".png") ? [i[1],parse(Int, String(split(i[2],"=")[2])), parse(Int, String(split(i[3], "=")[2]))] : ["F", -1, -1] for i in f_y_z_exp]
    y = unique([i[2] for i in f_y_z])
    z = unique([i[3] for i in f_y_z])
    y = sort(y)
    if -1 in y
        deleteat!(y, findall(x->x==-1, y))
    end
    z = sort(z)
    if -1 in z
        deleteat!(z, findall(x->x==-1, z))
    end
    return y, z
end

function GetFocusedImageGrid(ImagingParams::Datastructures.ProcessingParameters,fnamefunc=GenerateFinalFileName, exp="NoIR")
    #=
    Here we jsut make an array of the image names to be loaded
    =#
    x, y = GetFocusedIdentifiers(ImagingParams)
    x = reverse(x)
    y = reverse(y)
    img_name_grid = Array{String}(undef,length(y), length(x))
    img_pos_grid = Array{Float64}(undef,length(y), length(x), 2)
    for i in eachindex(x)
        for j in eachindex(y)
            img_name_grid[j,i]  = fnamefunc(x[i],y[j],exp)
            # Below doesnt work ause needs imagingparams not processing
            #img_pos_grid[j,i,:] = GeneratePxCoordinates([x[i],y[j]], ImagingParams)
        end
    end
    return img_name_grid[end:-1:1,end:-1:1]#, img_pos_grid[end:-1:1,end:-1:1,:]
end



# Load DNG images
function LoadDNGLibRaw(path, size=(3,3040,4056))
    # Uses C API LibRaw to load image char array
    # Size should be Color, height, width
    # img is to be populated by the ccall
    img = Array{UInt16}(undef, size[1]*size[2]*size[3])
    success = Ref{Cint}(0)
    @ccall "./C_stuff/LibRaw_LoadDNG.so".LoadDNG(img::Ref{Cushort},path::Ptr{UInt8},success::Ref{Cint})::Cvoid
    # Grab the reference from mem
    #print("success : $(success[])")
    if success[] == 0
        # TODO: Find a way to actually change the value of success in the C-code for some reason i cant figuer it out
        println("\033[93m   Error loading image : $(path) \033[0m") 
        println(success)
        img .= 0
    end
    # The array is linear so we need to reshape it to get the correct data
    order = [1,3,2]
    size = size[order]
    img = permutedims(reshape(img, size), (3,2,1))
    return img
end


function RowColumnIndexNaming(ImagingParams::Datastructures.ProcessingParameters, img_name_grid=nothing)
    #=
    Function for Fiji MIST, renames from  y z coordinates to row column

    We use save path as this runs after focus stacking
    =#
    # We get the formated frid for names
    if isnothing(img_name_grid)
        img_name_grid = GetFocusedImageGrid(ImagingParams)
    end
    # And generate the names for the files
    new_names = Array{String}(undef, size(img_name_grid))
    for i in 1:size(img_name_grid,1)
        for j in 1:size(img_name_grid,2)
            #Move file to new name
            new_name = "r$(i)_c$(j).png"
            if isfile(ImagingParams.save_path*img_name_grid[i,j])
                mv(ImagingParams.save_path*img_name_grid[i,j], ImagingParams.save_path*new_name)
                println("Moving $(ImagingParams.save_path*img_name_grid[i,j]) to $(ImagingParams.save_path*new_name)")
            end
        end
    end
    return img_name_grid
end

end # module

