"""   Copyright 2024 Acenturies

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License."""
import os
import sys
import datetime
import pytz
import colorama
import zipfile
import json
from cmd import Cmd
colorama.init(autoreset=True)
class Oxijena(Cmd):
    prompt = '> '
    
    def __init__(self):
        super().__init__()
        self.colors = {
            'red': colorama.Fore.RED,
            'green': colorama.Fore.GREEN,
            'yellow': colorama.Fore.YELLOW,
            'blue': colorama.Fore.BLUE,
            'magenta': colorama.Fore.MAGENTA,
            'cyan': colorama.Fore.CYAN,
            'white': colorama.Fore.WHITE,
        }
        self.default_color = colorama.Fore.WHITE

    def do_color(self, arg):
        "Changes the color of all the text in the terminal"
        color = arg.lower()
        if color in self.colors:
            self.default_color = self.colors[color]
            print(self.default_color + f"Changed text color to {color}")
        else:
            print(colorama.Fore.RED + "Invalid color. Available colors: red, green, yellow, blue, magenta, cyan, white")
        
    def do_clear(self, arg):
        "Clears the text in the terminal"
        os.system('cls' if os.name == 'nt' else 'clear')
        
    def do_help(self, arg):
        "Provides Help"
        print("Available commands:")
        print("color [color] - Changes the color of all the text in the terminal")
        print("clear - Clears the text in the terminal")
        print("help - Provides help")
        print("status - Lists all the status codes")
        print("ckdir [directory] - Checks if a directory exists")
        print("mkdir [directory] - Creates a new directory")
        print("rmdir [directory] - Deletes a directory")
        print("date - Checks the current date")
        print("time - Checks the current time")
        print("timezone - Shows the current timezone")
        print("echo [string] - Displays the string that was received from the argument")
        print("gtedit [string] - Edits The Gate")
        print("ograb [string] - Loads An Oxplug")
        print("grabcompile [string] - Compiles Your Code To A Grab File")
    
    def do_status(self, arg):
        "Lists all the status codes"
        print("Common status codes:")
        print("Code 100 Continue: When The Main Part Of Installation Is Done")
        print("Code 200 OK: Installation finished successfully or Ograb compilation successful.")
        print("Code 201 Created: mkdir successfully created a new folder.")
        print("Code 204 No Content: rmdir successfully deleted the directory.")
        print("Code 302 Found: ckdir found the specified directory.")
        print("Code 404 Not Found: rmdir couldn't delete a directory because it doesn't exist or ckdir couldn't locate a directory because it doesn't exist.")
        print("Code 409 Conflict:mkdir couldn't create a new folder because it already exists or rmdir couldn't delete the folder, possibly due to it not being empty or permissions.")
        print("Code 418 I'm A Teapot: The requested entity body is short and stout, Tip me over and pour me out, This is an alternative to 501 Not Implemented.")
        print("Code 500 Internal Code Error: mkdir couldn't create a directory due to an unexpected error")
        print("Code 600 Script File Not Found: Ograb couldn't find the script file in an Oxijena plugin.")
        print("Code 501 Not Implemented: Isn't It Obvious? It's Not Implemented")
    def do_ckdir(self, arg):
        "Checks if a directory exists"
        if os.path.isdir(arg):
            print(self.default_color + f"Code 302 Found")
        else:
            print(self.default_color + f"Code 404 Not Found")
    def do_gtedit(self, arg):
        print("501 Not Implemented")
    
    def do_mkdir(self, arg):
        "Creates a new directory"
        try:
            os.makedirs(arg, exist_ok=False)
            print(self.default_color + f"Code 201 Created")
        except FileExistsError:
            print(self.default_color + f"Code 409 Conflict")
        except Exception as e:
            print(self.default_color + f"Code 500 Internal Code Error")
    
    def do_rmdir(self, arg):
        "Deletes a directory"
        try:
            os.rmdir(arg)
            print(self.default_color + f"204 No Content")
        except FileNotFoundError:
            print(self.default_color + f"404 Not Found")
        except OSError as e:
            print(self.default_color + f"Code 409 Conflict")
    
    def do_date(self, arg):
        "Checks the current date"
        print(self.default_color + datetime.datetime.now().strftime("%Y-%m-%d"))
    
    def do_time(self, arg):
        "Checks the current time"
        print(self.default_color + datetime.datetime.now().strftime("%H:%M:%S"))
    
    def do_timezone(self, arg):
        "Shows the current timezone"
        if arg != "teapot":
            print("501 Not Implemented")
        else:
            print("418 I'm A Teapot")
    def do_echo(self, arg):
        "Displays the string that was received from the argument"
        print(self.default_color + arg)
    
    def default(self, line):
        print(colorama.Fore.RED + f"Code 400 Bad Request")
    
    def postcmd(self, stop, line):
        print(self.default_color, end='')  # Reset color after each command
    
    def do_ograb(self, zip_file_path):
        "Loads An Oxplug"
        config_filename = 'info.json'
        temp_dir = './ptemp'
        zipcurrent = "C:/Oxijena/packet"+zip_file_path+".ograb"

        # Open the ZIP file
        with zipfile.ZipFile(zipcurrent, 'r') as zip_ref:
            # Check if the config file exists in the ZIP archive
            if config_filename in zip_ref.namelist():
                # Extract the config file to a temporary location
                zip_ref.extract(config_filename, path=temp_dir)
                
                # Read the configuration from the extracted config file
                config_file_path = os.path.join(temp_dir, config_filename)
                with open(config_file_path, 'r') as f:
                    config = json.load(f)
                
                # Get the filename to execute from the config
                file_to_execute = config.get('file')
                
                # Check if the file to execute exists in the ZIP archive
                if file_to_execute in zip_ref.namelist():
                    # Extract the file to a temporary location
                    zip_ref.extract(file_to_execute, path=temp_dir)
                    
                    # Execute the extracted file
                    extracted_file_path = os.path.join(temp_dir, file_to_execute)
                    exec(open(extracted_file_path).read())
                    
                    # Clean up: delete the temporary files
                    os.remove(extracted_file_path)
                else:
                    print(f"Code 600 Script File Not Found ")
                
                # Clean up: delete the extracted config file
                os.remove(config_file_path)
            else:
                print(f"Code 605 Configuration File Not Found")
    def do_grabcompile(self, folder_path):
      if folder_path != "teapot":
        print("Code 501 Not Implemented")
      else:
        print("Code 418 I'm A Teapot.")

if __name__ == '__main__':
    terminal = Oxijena()
    terminal.cmdloop("Welcome To Oxijena 1.0.0 (c) Acenturies 2024-Present, 'help' For Help.")
