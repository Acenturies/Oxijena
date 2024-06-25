# Oxijena
Oxijena Is A Command Terminal For Windows,  

Current Version: `1.0.0`  

Current Codename: `Timezone Teapot`


# Documentation:
## Commands:
    color [color] - Changes the color of all the text in the terminal
    clear - Clears the text in the terminal
    help - Provides help
    status - Lists all the status codes
    ckdir [directory] - Checks if a directory exists
    mkdir [directory] - Creates a new directory
    rmdir [directory] - Deletes a directory
    date - Checks the current date
    time - Checks the current time
    timezone - Shows the current timezone (Not Implemented + Easteregg, Put "timezone teapot" in the command prompt in oxijena)
    echo [string] - Displays the string that was received from the argument
    gtedit [string] - Edits The Gate (Not Implemented, as gate.json was supposed to be implemented but now isn't)
    ograb [string] - Loads An Oxplug (An Oxplug is a zip file with a .ograb file extension
    grabcompile [string] - Compiles Your Code To A Grab File (Not Implemented + Easteregg, Put "grabcompile teapot")
## Codes:
    Code 100 Continue: When The Main Part Of Installation Is Done (Deprecated)
    Code 200 OK: Installation finished successfully (Deprecated) or Ograb compilation successful.
    Code 201 Created: mkdir successfully created a new folder.
    Code 204 No Content: rmdir successfully deleted the directory.
    Code 302 Found: ckdir found the specified directory.
    Code 404 Not Found: rmdir couldn't delete a directory because it doesn't exist or ckdir couldn't locate a directory because it doesn't exist.
    Code 409 Conflict:mkdir couldn't create a new folder because it already exists or rmdir couldn't delete the folder, possibly due to it not being empty or permissions.
    Code 418 I'm A Teapot: The requested entity body is short and stout, Tip me over and pour me out, This is an alternative to 501 Not Implemented.
    Code 500 Internal Code Error: mkdir couldn't create a directory due to an unexpected error
    Code 600 Script File Not Found: Ograb couldn't find the script file in an Oxijena plugin.
    Code 501 Not Implemented: Isn't It Obvious? It's Not Implemented
