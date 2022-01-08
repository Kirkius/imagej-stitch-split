import os

def stitchImages(imagejObject, sourceDirectory, outputDirectory, inputFileNames, outputName):
    macro = """
    #@ String sourceDirectory
    #@ String outputDirectory
    #@ String inputFileNames
    #@ String outputName

    print(sourceDirectory)
    function action (sourceDirectory, outputDirectory, inputFileNames, outputName){
    run("Grid/Collection stitching", 
    "type=[Unknown position]" +
    " order=[All files in directory] directory=" +
    sourceDirectory + 
    " confirm_files" + 
    " output_textfile_name=TileConfiguration.txt" +
    " fusion_method=[Linear Blending]" +
    " regression_threshold=0.30" +
    " max/avg_displacement_threshold=2.50" +
    " absolute_displacement_threshold=3.50" +
    " computation_parameters=[Save computation time (but use more RAM)]" +
    " image_output=[Fuse and display] " +
    inputFileNames);

    saveAs("Tiff", outputDirectory + "/" + outputName + ".tif");
    }

    action(sourceDirectory, outputDirectory, inputFileNames, outputName)

    """

    args = {
        'sourceDirectory' : sourceDirectory,
        'outputDirectory': outputDirectory,
        'inputFileNames': inputFileNames,
        'outputName': outputName   
    }

    imagejObject.py.run_macro(macro, args)


def getInputFiles(directory, directory_path):
    # Initialize a list with the current mouse number
    inputFileNames = [directory]
   
    # Initialize an index
    index = 0
   
    # Loop over files in the provided directory
    for entry in os.scandir(directory_path):
        
        # If a files ends with _component_data.tif
        if (entry.path.endswith("_component_data.tif")):
           
            # Add it to the list in the format ImageJ expects (e.g. 123456_0)
            inputFileNames.append(directory + "_" + str(index))
            
            # Increment the index
            index += 1
    
    # Once all files have been added to the list, convert list to string
    inputFileNames = ' '.join(inputFileNames)
    
    # Return string
    return inputFileNames


def makeOutputDirectory(directory, outputRoot):
    # Initialize already_exist flag and set it to false
    already_exists = False

    # Construct output directory from the output root and the mouse number
    outputDirectory = os.path.join(outputRoot, directory)

    # If a folder with the given mouse number doens't exist yet, create it
    if not os.path.exists(outputDirectory):
        os.mkdir(outputDirectory)

    # Else return that the folder already exists and set the flag to true
    else:
        print('Output Directory already exists! \n{0}'.format(outputDirectory))
        already_exists = True
    
    # Return the path to the output directory and the flag
    return outputDirectory, already_exists