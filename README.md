# Script for automatic stitching and splitting of images in ImageJ
This script will take a directory filled with TIFF images grouped in seperate folders and stitch them together using the [Grid/Collection stitching](https://imagej.net/plugins/grid-collection-stitching) plugin from ImageJ. The type of stitching is set to *Unknown position*. 

## Prerequisites
- Fiji (ImageJ 2)
- Python 3
- PyImageJ (Python Package)
- Apache Maven

## Installation steps

### Fiji
Download and unpack Fiji as described on their website.
https://imagej.net/software/fiji/downloads

### Python
To check if you have Python installed open a command prompt. (Start --> Run --> cmd.exe)
Type in `python` and hit enter. If you see some text popping up with a Python version number and the bottom row had `>>>` then Python is installed. 

If Python is not yet installed you can download it from [Python.org](https://www.python.org/downloads/).
**During installation of Python make sure you click the checkbox to add Python to your _PATH_.**

### PyImageJ Python Package
When Python is installed you can install the required Python package using pip.
Open a command prompt (Start --> Run --> cmd.exe), type in `pip install pyimagej` and hit enter. If you do not have admin rights on your computer you might have to install via `pip install pyimagej --user`.

**Note:** You have to enter these pip commands in a command prompt, not in Python. So if your command prompt still shows `>>>` from the previous step pres `Ctrl+Z` and hit enter.

### Apache Maven
In some cases you might run into an error while running the script that something called "mvn" has not been found. In that case you will have to install Apache Maven manually.

1. Download the latest *Binary zip archive* from the [Maven download page](https://maven.apache.org/download.cgi). Unzip this folder somewhere where you can find it again.
2. Now you will have to add the path to the *bin* folder inside the folder you just unzipped to your *PATH environment variables*. To do this in the *Start menu* search for `environment` you will likely find two items *Edit the system environment variables* and *Edit environment variables for your account*. Choose the one for your account (editing the system variable requires admin rights). If you get a system properties window, click advanced at the bottom.
3. In the top half of the screen you will see the user variables for your Windows account, in the bottom half those for the whole system (again these require admin rights to edit). 
   In the top half double click the *Path* variable, a new window should pop up allowing you to edit this variable. Click new and fill in the path to the binary folder you just unzipped, e.g if you unzipped in your documents folder it will be something like `C:\Users\<username>\Documents\apache-maven-3.8.4\bin` (the numbers may be different depending on which version of Maven you had downloaded).
4. To verify if Maven was installed correctly open up a new command prompt (Start --> Run --> cmd.exe) and type `mvn -v`.