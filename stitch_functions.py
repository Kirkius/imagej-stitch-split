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
    inputFileNames = [directory]
    index = 0
    for entry in os.scandir(directory_path):
        if (entry.path.endswith("_component_data.tif")):
            inputFileNames.append(directory + "_" + str(index))
            index += 1
    inputFileNames = ' '.join(inputFileNames)
    return inputFileNames


def makeOutputDirectory(directory, outputRoot):
    already_exists = False
    outputDirectory = os.path.join(outputRoot, directory)
    if not os.path.exists(outputDirectory):
        os.mkdir(outputDirectory)
    else:
        print('Output Directory already exists! \n{0}'.format(outputDirectory))
        already_exists = True
    return outputDirectory, already_exists