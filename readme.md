Clipboard Image Auto Saver is a Python script which monitors the windows clipboard and auto saves image data that changes.

## Installation

1. Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the packages "pywin32", and "pillow".
(type into windows Command Prompt)

```bash
 py -m pip install pillow pywin32
```
2. On this github page click code > download .zip
3. Extract the zip and add your desired screenshot save path to the save_path.cfg file, so it looks like this

## Usage

4. Run the start_stop.bat file. The batch file is provided to launch and manage the python script. it should pop up a window that lists the folder you defined in step 3. the python window needs to be running when ever you want to autosave. 
5. Use WindowKey + Shift +S to take a screenshot, the cmd window should say:
`Attempting to keep transparency...
Saving image...
`
6. to stop autosaving simply close the CMD window. 

Notes:
-(from Epiic Penguin) : i broke the bit in the .bat after:
`py clipboard_img_auto_saver.py
echo Press any key to continue and kill script...`
if someone who can actually code (i cant) wants to fix it that would be awesome. 
-I did try and user pyinstaller to make a bin file at one point but there was some sort of failure and I don't have time to try and troubleshoot it.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
