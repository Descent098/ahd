## Glossary

- **Command**; What you would type into your terminal to do something. For example ```cd``` is the command to change directories.
- **Path**; A location on a computer, such as a folder (or folders), or file.
- **Macro**; A combination of a defined command and path. For example you could write a macro to delete all pdf's (the command) in your downloads folder (the path).
- **Dispatch**; To execute a macro
- **Ad-hoc**; To do something as needed. For example you can register macros as needed, so you could say you are ad-hoc registering macros.
- **Namespace**; The collection of valid names to dispatch with. ahd has it's own namespace meaning you can use names defined in other namespaces (like ```cd```, ```user``` etc.). For example on your system your "global namespace" would be where commands like ```cd``` come from (on *nix this is ```~/.bashrc``` and the ```PATH``` on windows). 
- **Path Expansion** (AKA globbing); To take a representation of a path (or paths) and expand it to a real (absolute) path, or set of absolute paths. For example ```~/Desktop``` would expand to ```/Home/Desktop``` on *nix and ```%USERPROFILE%\Desktop``` on windows.