import os

def splitChannels(imagejObject, inputFile, outputDirectory, outputFileName):
    macro = """"
    #@ String inputFile
    #@ String outputDirectory
    #@ String outputFileName

    function action (inputFile, outputDirectory, outputFileName){
        open(inputFile);
        run("Split Channels");
        
        n = nImages();
        print("Amount of channels: " + n)

        for (i=0;i<nImages;i++) {
            selectImage(i+1);
            saveAs("Tiff", outputDirectory + "/C" + (i+1) + "-" + outputFileName);
            }
        
        run("Close All");
    }

    action(inputFile, outputDirectory, outputFileName)
    
    """

    args = {
        'inputFile' : inputFile,
        'outputDirectory': outputDirectory,
        'outputFileName': outputFileName,
    }

    imagejObject.py.run_macro(macro, args)