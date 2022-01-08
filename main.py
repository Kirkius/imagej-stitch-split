import os
from re import sub
import imagej
import scyjava

from stitch_functions import stitchImages, getInputFiles, makeOutputDirectory
from split_channels_functions import splitChannels

imageJInstallPath = r'E:\Downloads\fiji-win64\Fiji.app'
sourceDirectory = r'C:\Users\caspe\Repos\imagej-script\images\test'
outputRoot = r'C:\Users\caspe\Repos\imagej-script\images\output'

def initializeImageJ(memory, path):
    scyjava.config.add_option('-Xmx'+ memory)
    imagejObject = imagej.init(path)
    return imagejObject

ij = initializeImageJ('4g', imageJInstallPath)
# stitch_index = 0
split_index = 0

#==================
#|Stitching Images|
#==================
# for directory in os.listdir(sourceDirectory):
#     print('Processing images with mouse number: {0}'.format(directory))
#     directory_path = os.path.join(sourceDirectory, directory)
#     # print(directory_path)
#     inputFileNames = getInputFiles(directory, directory_path)
#     # print(inputFileNames)
#     outputDirectory, already_exists = makeOutputDirectory(directory, outputRoot)
#     # print(outputDirectory)
#     if not already_exists:
#         stitchImages(ij, directory_path, outputDirectory, inputFileNames, directory)
#         stitch_index += 1
#     else:
#         print('A folder with number: {0} already exists. \nSkipping...'.format(directory))
# print('Processed {0} images!'.format(stitch_index))


#================
#|Split Channels|
#================
for subdirectory, directory, files in os.walk(outputRoot):
    if not subdirectory.endswith(outputRoot):
        if len(files) == 1:
            inputFile = os.path.join(subdirectory, files[0])
            mouse_number = files[0].split('.')[0]
            splitChannels(ij, inputFile, subdirectory, mouse_number)
            split_index += 1
        elif len(files) > 1:
            print(subdirectory + ' has more than 1 file! \nAssuming channels are already split.') 
print('Processed {0} multichannel images for splitting!'.format(split_index))