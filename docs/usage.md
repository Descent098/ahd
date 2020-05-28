# Usage

This section will give you a high level overview of the commands, arguments and flags available in the ahd CLI. 



For details on more advanced topics like:

- macro overriding
- wildcards
- Autocompletion

See the [advanced usage section](../advanced-usage) of the docs for details.

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
## CLI Commands

### Register

The register command allows you to register a command to be used later on. 

<u>Required Arguments:</u>

- *<name\>*;  This is a **positional** placeholder value for the name of a command you  are registering. Once the command is registered you can run it by using ```ahd <name>```.


- *<command\>*;  This is a **positional** placeholder value for the macro you want to run when the command is used after being registered. For example if you wanted to delete all the PDF's in a directory the macro you would normally run is ```rm *.pdf``` and so you would do ```ahd register <name> "rm *.pdf" <paths>```. 
	- It is generally advised to use encapsulating quotes since this avoids argument parsing artifacts.


- *<paths\>*;  This is a **positional** placeholder value for the path(s) that you want the command to run the macro in by default. For example if you wanted to a command to execute a macro on the desktop when it's run you can do ```ahd register <name> <command> "~/Desktop"```.
    - Use encapsulating quotes since this avoids argument parsing artifacts.
    - You can use a ```"."``` to have the macro run in whatever the current directory (at runtime) is.
    - You can specify multiple directories through comma delimiting, for example: ```ahd register <name> <command> "~/Desktop, ~/Documents, ~/Pictures"```.
    - More details about paths can be found in the [all about paths section](../advanced-usage#all-about-paths) (Particularly globbing and wildcards).



### Using a Registered Command

You can use a registered command by simply typing ```ahd <name>```, where ```<name>``` is whatever name you gave to the command.

<u>Optional Arguments:</u>

- *<command\>*; This is an optional positional argument that lets you overwrite the command, while retaining the registered paths. See [command overriding for details](../advanced-usage#command-overriding).

- *<paths\>*; This is an optional positional argument that lets you overwrite the paths the command will run against. See [path overriding for details](../advanced-usage#path-overriding).



### list

The list command shows a list of your current registered macros.

<u>Optional flags:</u>

- *\-l or \-\-long*: Shows all macros in configuration with the registered paths and commands.



### docs

The docs command is designed to bring up documentation as needed, you can run ```ahd docs``` to open the documentation site in the default browser.



<u>Optional Flags:</u>

- *\-a or \-\-api*: Used to serve local API documentation **(Not yet implemented)**

- *\-o or \-\-offline*: Used to serve local user documentation **(Not yet implemented)**



### config

This command is primarily used for **manual** configuration management, It is recommended to use [register](#register) to register/update commands as opposed to the config command. Take a look at the [manual configuration section](../advanced-usage#manual-configuration) to learn more. This command does also allow for transferring configurations, the details for which can be found in the [transferring configurations section](../advanced-usage#transferring-configurations).



<u>Optional flags:</u>

  \-e or \-\-export: Export the current configuration file (called ```ahdconfig.yml```)

  \-i or \-\-import: Import a configuration file; takes the path to the config file as an argument
