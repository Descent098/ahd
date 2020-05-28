![ahd-logo](https://raw.githubusercontent.com/Descent098/ahd/master/docs/img/ahd-logo.png)



# Ad-Hoc Dispatcher

*Create ad-hoc macros to be dispatched within their own namespace.*

If you are confused about terminology used then take a look at the [glossary section](#https://ahd.readthedocs.io/en/latest/glossary/) of the docs.

## What does ahd do? 

ahd allows you to take annoying to remember commands and organize them into easy to re-use macros.

## Features & Roadmap

### Path Expansion

- Macros can take full advantage of wildcards + regex to pattern match directories. 
  For example if you wanted to delete all PDFs in all folders on the desktop you can use ```sudo ahd register no-pdfs "rm *.pdf" "~/Desktop/*"```.
- *nix and windows path adages are cross-platform. For example ```~``` is converted to ```%USERPROFILE%``` on windows,  ```\``` paths are converted to ```/``` on *nix systems and vice-versa.

### Cross platform

- ahd natively supports windows and any *nix systems (including Mac OS). 
- Supports copy-paste cross platform configurations (assuming the same commands and file structure are on both)
For example if you want to write a command that git pulls in a folder called ```/development``` on your desktop using the \*nix standard ```~/Desktop/development/*``` works on both \*nix and windows.

### Dynamic Execution & Organization
- One YAML file contains the configuration for all your macros instead of being all over the place.
- Macros can be updated manually (editing the YAML file), or simply re-registered.
- The defined Paths and commands can be overwritten on each use (see [overriding](https://ahd.readthedocs.io/en/latest/usage#overriding) for details).

### Roadmap

A full roadmap for each project version can be found here: https://github.com/Descent098/ahd/projects

## Example use cases

Really the possibilities are only limited to what you can type in your regular terminal, but here are some good examples:
- Update every git repo in a directory
- Organize your downloads folder by various filetypes
- Multi-stage project compilation/build in various directories


## Why should I use ahd?

The easiest way to understand why this project is useful is with an example. Let's say you want to write a simple script to take all the PDF's in a directory and put them in a ```.7z``` archive and then remove them. Well all you need is this simple command ```7za a -t7z PDFs.7z *.pdf && rm *.pdf```...

Yeah, pretty awful to remember. Assuming we want to do this every so often let's make a script we can call. Currently with bash you need to drop the script in ```usr/bin``` (and try to remember what you called it), or add it to your bash/fish/zsh aliases (assuming you use the alias file, or ```.bashrc``` etc. if you don't), and on windows it's just not even worth it.

Enter ahd, you can register a macro (lets call it zip-pdfs) using the same annoying command, in this case ```sudo ahd register zip-pdfs "7za a -t7z PDFs.7z *.pdf && rm *.pdf" "."```. Now when we want to re-use this macro in the directory we're in you just type ```ahd zip-pdfs```. 

If you forget the name there's a list command, and if you use a longer name there's bash autocomplete (fish and zsh support coming later).

## Who is ahd for?

The primary audience is developers looking to speed up annoying workflows. However there are a number of other people it could benefit, such as:
- devops specialists; can use ahd to create a common set of macros across servers .
- dual booters; people who want one common config for multiple OS's.
- testers; if you need to execute multiple tests on various systems you can write one macro to run them all.
- etc; people who are sick of having a bunch of random scripts everywhere and want one config file for complex commands.