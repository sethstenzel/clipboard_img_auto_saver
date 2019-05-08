# tested on windows 10 and python 3.7
# pip install pillow pywin32

import os
from datetime import datetime
from PIL import ImageGrab, Image
import win32clipboard as clipboard
from time import sleep


def defaults_setup():
    last_image = ''  
    if check_clipboard_image_available():
        last_image = ImageGrab.grabclipboard()
    save_path = load_save_path()
    main_loop(last_image, save_path)


def main_loop(last_image, save_path):
    while True:  # The event loop  
        if check_clipboard_image_available():
            if clipboards_not_equal(last_image):
                last_image = process_clipboard(save_path)   
        sleep(0.5) # To ease cpu load.


def check_clipboard_image_available():
    return clipboard.IsClipboardFormatAvailable(8)


def load_save_path():
    save_path = ''
    if os.path.exists("save_path.cfg"):
        with open('save_path.cfg', 'r') as f:
            defaults = f.readlines()
            if len(defaults) >= 1:
                save_path = defaults[0].replace('PATH="','').replace('"','').strip('\n')
                print(save_path)
            else:
                save_path = str(os.getcwd())
    else:
        save_path = str(os.getcwd())
    return save_path


def clipboards_not_equal(last_image):
    if last_image == '':
        return True
    new_image = ImageGrab.grabclipboard()
    return str(list(new_image.getdata())) != str(list(last_image.getdata()))


def process_clipboard(save_path):
    im = ImageGrab.grabclipboard()
    tim = keep_transparency(im)
    save_image(tim, 'PNG', save_path)
    return im


def keep_transparency(im):
    print('Attempting to keep transparency...')
    try:
        im = im.convert("RGBA")
        tim = Image.new('RGBA', im.size, (255,255,255,0))
        tim.paste(im, (0,0), mask=im.split()[3])
        return tim
    except Exception as e:
        print('Unable to save transparency', e)
        return im
    

def save_image(im, img_format, save_path):
    print('Saving image...')
    file_timeestamp = datetime.now().strftime('%B_%m.%d.%Y_%I.%M.%S_%p') + '.'
    try:
        im.save(save_path + file_timeestamp + img_format.lower(), img_format)

    except PermissionError as default_config_path_write_error:
        print(default_config_path_write_error, save_path, '\nUnable to print to defaults.cfg directory...\nAttempting to print to script directory')
        print('Are you sure you have permission to write to this folder?\n',save_path)
        try:
            im.save(str(os.getcwd()) + file_timeestamp + img_format.lower(), img_format)
        except PermissionError as script_dir_write_error:
            print(script_dir_write_error, save_path, '\nUnable to print to script\'s directory...\n\nExiting...')
            print('Are you sure you have permission to write to this folder?\n',save_path)
            print('Image not saved, please check folder permissions and space availability.')
        except Exception as e:
            print('An error occured', e)
            sleep(5)
            quit()
    except Exception as e:
        print('An error occured', e)
        sleep(5)
        quit()



if __name__ == '__main__':
     defaults_setup()