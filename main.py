import os
import time
import imagej
import scyjava
import tkinter
from tkinter.filedialog import askdirectory
from tkinter import simpledialog

from stitch_functions import stitchImages, getInputFiles, makeOutputDirectory
from split_channels_functions import splitChannels

try:
    # Start a timer
    total_start = time.time()
    
    # Initialize user prompt windows
    tk_window = tkinter.Tk()
    tk_window.withdraw()

    # Prompt user for info
    imageJInstallPath = askdirectory(title='Select ImageJ install folder')
    sourceDirectory = askdirectory(title='Select input directory')
    outputRoot = askdirectory(title='Select output directory')
    memory = simpledialog.askstring(title='Memory for ImageJ', prompt='How much memory can ImageJ use? (GB)')

    # Output prompted info
    print('ImageJ installation path: \n{0}'.format(imageJInstallPath), end='\n\n')
    print('Input directory: \n{0}'.format(sourceDirectory), end='\n\n')
    print('Output directory: \n{0}'.format(outputRoot), end='\n\n')
    print('Amount of memory allocated for ImageJ: {} GB'.format(memory), end='\n\n')

    # Initialize ImageJ
    def initializeImageJ(memory, path):
        scyjava.config.add_option('-Xmx'+ memory + 'g')
        imagejObject = imagej.init(path)
        return imagejObject
    # Create ImageJ object
    ij = initializeImageJ(memory, imageJInstallPath)
    
    # Create some indexes
    stitch_index = 0
    split_index = 0

    #==================
    #|Stitching Images|
    #==================
    
    # Loop through folder in input directory
    for directory in os.listdir(sourceDirectory):
        
        # For some reason on Win7 the Explorer accesses the Thumbs.db file which breaks the script
        if directory == 'Thumbs.db':
            pass
        
        # Since folder are named with the mouse number we output that here
        print('Processing images with mouse number: {0}'.format(directory))
        
        # Construct path to the folder with the to-be stitched images
        directory_path = os.path.join(sourceDirectory, directory)
        
        # Retrieve a string in the format ImageJ expects with the amount of to-be stitched .tif files
        inputFileNames = getInputFiles(directory, directory_path)
        
        # Create an output folder with the name of the mouse number.
        # If a folder with this name already exists the variable 'already_exists' is returned as True.
        # If the 'already_exists' variable is True, a folder is not created
        outputDirectory, already_exists = makeOutputDirectory(directory, outputRoot)
        
        # If the output folder was created call the ImageJ stitch macro and increment the index
        if not already_exists:
            stitchImages(ij, directory_path, outputDirectory, inputFileNames, directory)
            stitch_index += 1
        # If the output folder was not created skip that mouse number
        else:
            print('A folder with number: {0} already exists. \nSkipping...'.format(directory))
    
    # Return amount of mouse numbers that have been processed
    print('Processed {0} mouse numbers!'.format(stitch_index))


    #================
    #|Split Channels|
    #================

    # Loop through the output directory
    for subdirectory, directory, files in os.walk(outputRoot):
        
        # Skip the first entry since this is the output root directory
        if not subdirectory.endswith(outputRoot):

            # If there is exactly one file in the output directory start the split channel process
            if len(files) == 1:
                
                # Construct path to file
                inputFile = os.path.join(subdirectory, files[0])
                
                # Get mouse number from the file name
                mouse_number = files[0].split('.')[0]

                # Call the ImageJ split channels macro and increment the index
                splitChannels(ij, inputFile, subdirectory, mouse_number)
                split_index += 1
            
            # If there is more than one file in the output directory we assume that the channel have already been split
            # This prevents accidental overwriting
            elif len(files) > 1:
                print(subdirectory + ' has more than 1 file! \nAssuming channels are already split.') 
    
    # Return amount of multichannel images that have been processed.
    print('Processed {0} multichannel images for splitting!'.format(split_index))

    # Stop the timer
    total_end = time.time()
    # Calculate total processing time
    total_time = total_end - total_start
    
    print('Completed everything in {0} seconds!'.format(round(total_time, 2)))

except Exception as e:
    print('An error occured with the following message.')
    print(e.args)