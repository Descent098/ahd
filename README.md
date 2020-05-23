![ahd-logo](https://raw.githubusercontent.com/Descent098/ahd/master/docs/img/ahd-logo.png) [![DeepSource](https://static.deepsource.io/deepsource-badge-light-mini.svg)](https://deepsource.io/gh/Descent098/ahd/?ref=repository-badge)

# Ad-Hoc Dispatcher

*Create ad-hoc macros to be dispatched within their own namespace.*

## Table of contents

- [What does this do?](#what-does-this-do?)
  - [Use Cases](#use-cases)
- [Why should I use it?](#why-should-I-use-it)
- [Who is this for?](who-is-this-for?)
- [Features & Roadmap](#features-&-roadmap)
  - [Path Expansion](#path-expansion)
  - [Cross Platform](#cross-platform)
  - [Organized](#organized)
  - [Dynamic](#dynamic)
  - [Roadmap](#roadmap)
- [Quick Start](#quick-start)
  - [Dependencies](#dependencies)
  - [Installation](#installation)
    - [From PyPi](#from-pypi)
    - [From Source](#from-source)
  - [Usage](#usage)
    - [Register](#register)
    - [Using a Registered Command](#using-a-registered-command)
    - [List](#list)
    - [Docs](#docs)
    - [Config](#config)

## Additional Documentation

Additional user and development/contribution documentation will be available at [https://ahd.readthedocs.io/en/latest/](https://ahd.readthedocs.io/en/latest/), API documentation is available at [https://kieranwood.ca/ahd](https://kieranwood.ca/ahd).



## What does this do? 

Simply put, it allows you to take annoying to remember commands and make it easier to re-use them along with providing extra functionality like cross-platform support. 

### Use cases

For example it can be used to update every git repo in a directory, organize your downloads folder by various filetypes, or even do multi-stage project compilation in various directories. Really the possibilities are only limited to what you can type in your regular terminal.

## Why should I use it?

The easiest way to understand why this project is useful is with an example. Let's say you want to write a simple script to take all the PDF's in a directory and put them in a ```.7z``` archive and then remove them. Well all you need is this simple command ```7za a -t7z PDFs.7z *.pdf && rm *.pdf```...

Yeah, pretty awful to remember. Assuming we want to do this every so often let's make a script we can call. Currently with bash you need to drop the script in ```usr/bin``` (and try to remember what you called it), or add it to your bash/fish/zsh aliases (assuming you use the alias file, or ```.bashrc``` etc. if you don't), and on windows it's just not even worth it.

Enter ahd, you can register a command (lets call it zip-pdfs) using the same annoying command in this case ```sudo ahd register zip-pdfs "7za a -t7z PDFs.7z *.pdf && rm *.pdf" "."```. Now when we want to re-use this command in the directory we're in you just type ```ahd zip-pdfs```. If you forget the name there's a list command, and if you use a longer name there's bash autocomplete (fish and zsh support coming later).

## Who is this for?

Lots of people. ahd can be used by developers looking to speed up annoying workflows, it can be used to create a common set of macros across servers for devops specialists, or a common config for people who dual-boot, or just people who are sick of having a bunch of random scripts everywhere and want one config file for complex commands.



## Features & Roadmap

### Path Expansion
Commands can take full advantage of wildcards + regex to match directories. For example if you wanted to delete all PDFs in all folders on the desktop you can use ```sudo ahd register no-pdfs "rm *.pdf" "~/Desktop/*"```.

### Cross platform
Not only just that it runs on windows, but if your directory structure and tools are similar across platform you can 1:1 bring the config file from linux to windows to mac. For example if you want to write a command that git pulls in a folder called ```/development``` on your desktop using the \*nix standard ```~/Desktop/development/*``` works on both \*nix and windows.

### Organized
The commands you are running are all in one place that uses a simple YAML format to define each command, making it possible to manually update the configuration if you so choose (though built-in options are available).

### Dynamic
Paths and commands can be overwritten on each use, meaning that if you wrote a macro to delete all the PDF's in your downloads folder you can use the same macro and just change the path for that run to remove them from your documents folder.

### Roadmap

A full roadmap for each project version can be found here: https://github.com/Descent098/ahd/projects



## Quick-start

### Dependencies

- Python 3.6+ (or is at least only tested and officially supported for 3.6+)
- pip for python



### Installation

Once you have python3 and pip you have a few installation options.



#### From Pypi

Run ```pip install ahd``` or ```sudo pip3 install ahd``` (need a network connection)

#### From source

1. Clone this repo: (https://github.com/Descent098/ahd)
2. Run ```pip install .``` or ```sudo pip3 install .```in the root directory (one with setup.py)



### Usage

```bash
Usage:
    ahd list [-l]
    ahd [-h] [-v] [-d]
    ahd docs [-a] [-o]
    ahd config [-e] [-i CONFIG_FILE_PATH]
    ahd register <name> [<command>] [<paths>]
    ahd <name> [<command>] [<paths>]

Options:
-h, --help            show this help message and exit
-v, --version         show program's version number and exit
-l, --long            Shows all commands in configuration with paths and commands
-a, --api             shows the local API docs
-o, --offline         shows the local User docs instead of live ones
-e, --export          exports the configuration file
-i CONFIG_FILE_PATH, --import CONFIG_FILE_PATH
                    imports the configuration file
```

#### Register

The register command allows you to register a command to be used later on. 

<u>Required Arguments:</u>

- *\<name\>*;  This is a **positional** placeholder value for the name of a command you  are registering. Once the command is registered you can run it by using ```ahd <name>```.

- *\<command\>*;  This is a **positional** placeholder value for the macro you want to run when the command is used after being registered. For example if you wanted to delete all the PDF's in a directory the macro you would normally run is ```rm *.pdf``` and so you would do ```ahd register <name> "rm *.pdf" <paths>```. 

  It is generally advised to use encapsulating quotes since this avoids argument parsing artifacts.

- *\<paths\>*;  This is a **positional** placeholder value for the path(s) that you want the command to run the macro in by default. For example if you wanted to a command to execute a macro on the desktop when it's run you can do ```ahd register <name> <command> "~/Desktop"```.

  It is generally advised to use encapsulating quotes since this avoids argument parsing artifacts. Additionally you can specify multiple directories through comma delimiting, for example: ```ahd register <name> <command> "~/Desktop, ~/Documents, ~/Pictures"```, or you can use **path expansion** which will match directories through regex or wildcards. For example to run a command in all directories **within** the desktop you could do ```ahd register <name> <command> "~/Desktop/*"``` or just use regex to match paths more explicitly for example to only include folders on the desktop that are numbers between 0-9 you could do: ```ahd register <name> <command> "~/Desktop/[0-9]"```.



#### Using a Registered Command

You can use a registered command by simply typing ```ahd <name>```, where ```<name>``` is whatever name you gave to the command.

<u>Optional Arguments:</u>

- *\<command\>*; This is an optional positional argument that lets you overwrite the command, while retaining the registered paths. For example lets say you have a set of paths registered with a command that typically runs ```git pull``` over the specified paths. You want to run a different command on the paths (lets say remove all the pdfs in the folder) You can do: ```ahd <name> "rm *.pdf"``` which will execute ```rm *.pdf``` instead of ```git pull``` on the defined paths.

  It is generally advised to use encapsulating quotes since this avoids argument parsing artifacts.
- *\<paths\>*; This is an optional positional argument that lets you overwrite the paths the command will run against. To retain the original command you must use a ".". So for example lets say you have a command registered that runs ```git pull``` against ```~/Desktop/*```, but now you want to run ```git pull``` against ```~/Documents/*``` you can use ```ahd <name> "." "~/Documents/*"``` and it will run the macro against ```~/Documents/*``` instead of ```~/Desktop/*```

  It is generally advised to use encapsulating quotes since this avoids argument parsing artifacts. Additionally you can specify multiple directories through comma delimiting, for example: ```ahd register <name> <command> "~/Desktop, ~/Documents, ~/Pictures"```, or you can use **path expansion** which will match directories through regex or wildcards. For example to run a command in all directories **within** the desktop you could do ```ahd register <name> <command> "~/Desktop/*"``` or just use regex to match paths more explicitly for example to only include folders on the desktop that are numbers between 0-9 you could do: ```ahd register <name> <command> "~/Desktop/[0-9]"```.



#### list

The list command shows a list of your current registered commands.

<u>Optional Arguments:</u>

- *\-l or \-\-long*: Shows all commands in configuration with the registered paths and macros.



#### docs

The docs command is designed to bring up documentation as needed, you can run ```ahd docs``` to open the documentation site in the default browser.



<u>Optional Arguments:</u>

- *\-a or \-\-api*: Used to serve local API documentation (Not yet implemented)

- *\-o or \-\-offline*: Used to serve local user documentation (Not yet implemented)



#### config

This command is used for configuration management, due to the amount of preprocessing involved in keeping ahd cross platform it is recomended to use [register](#register) to register/update commands. The config command is for managing configurations manually take a look at the documentation for details about [manual configuration](https://ahd.readthedocs.io/en/latest/usage#wildcards-and-cross-platform-paths).



<u>Optional Arguments:</u>

  \-e \-\-export: Export the current configuration file (called ```ahdconfig.yml```)

  \-i \-\-import: Import a configuration file; takes the path to the config file as an argument









