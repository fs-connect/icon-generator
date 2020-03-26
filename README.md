# icon-generator
Create eyeExtend Connect compatible set of icons from any jpg, jpeg, or png file. 
## What is icon-generator
Icon generator will convert any 1:1 aspect ratio image file to properly sized set of four icons:
Base Icon, 
Grayscale Icon, 
Waiting Icon, 
Failed Icon.

## Installation
This tool leverages Python 3 and you must have 'Pillow' package installed.
'sudo pip install Pillow'
## Usage
1) Installed the pre-req library and version of Python
2) Run 'python3 icon_generator.py sample.jpeg' (Image with 1:1 aspect ration and formats png, jpg and jpeg supported)
3) Ensure you have the "waiting.png" and "failed.png" files in the folder where you running the code
4) Successful run will result in following files being created
   * connect_icon.png
   * gray_connect_icon.png
   * waiting_connect_icon.png
   * failed_connect_icon.png
  
