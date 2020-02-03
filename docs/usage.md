# Usage

```bash
Usage: 
	ahd [-h] [-v] [-d]
    ahd docs [-a] [-o]
    ahd config [-e] [-i CONFIG_FILE_PATH]
    ahd register <name> [<command>] [<paths>]
    ahd <name> [<command>] [<paths>]

Options:
    -h, --help            show this help message and exit
    -v, --version         show program's version number and exit
    -a, --api             shows the local API docs
    -o, --offline         shows the local User docs instead of live ones
    -e, --export          exports the configuration file
    -i CONFIG_FILE_PATH, --import CONFIG_FILE_PATH 
                          imports the configuration file
```



## Example

Here is a quick example of creating a command that runs ```sudo apt-get update && sudo apt-get upgrade```:

1. Register the command as the name "update": ```ahd register update "sudo apt-get update && sudo apt-get upgrade"```
2. Run the command using the name "update": ```ahd update```



This example was somewhat trivial but keep in mind this effectively means you can replace any short bash scripts you are using to do things like updating multiple git repos, executing a sequence of commands to sort your downloads folder etc.



## Arguments

### docs

The docs command is designed to bring up documentation as needed, you can run ```ahd docs``` to open the documentation site in the default browser.



**Options**:

  \-a \-\-api: Used to serve local API documentation (Not yet implemented)

  \-o \-\-offline: Used to serve local user documentation (Not yet implemented)



### config

This command is used for **all** configuration management. Due to the amount of preprocessing involved in keeping ahd cross platform the dotfile is obstructed from view by default. The config command is the main interface for managing configurations manually though I would recommend using the **register** command as opposed to this, or looking at the documentation for details about [manual configuration](https://ahd.readthedocs.io/en/latest/usage#wildcards-and-cross-platform-paths).



**Options**:

  \-e \-\-export: Export the current configuration file (it's a dotfile so make sure view hidden files is enabled)

  \-i \-\-import: Import a configuration file; takes the path as an argument



### Register

The register command allows you to register a name to be used later on. For example if I wanted to create a command that dispatched running git pull in several of my directories that is activated when I type ```ahd git-upt``` then I can just run ```ahd register git-upt "git pull" "~/path/to/project, ~/path/to/project-2, ~/path/to/project-3```



#### \<name\>

This is a placeholder value for the name of a command you have registered. Once the command is registered you can run it by using ```ahd <name>```, additionally you can override the default set commands or paths, details can be found below.



## Overriding

You can override the registered command, or paths of a name ad-hoc. Overriding can be useful in circumstances where you may want to vary the command or paths being run. This also means that on top of running commands you can use ahd to specify a set of paths to execure ad-hoc commands to. Here are some examples of both.



### Commands

Let's say you have registered the name "environments", this contains all the paths to the root directories of application instances you have running on a server. For example:

```ahd register environments "" "~/path/to/application, ~/path/to/application-2, ~/path/to/application-3"```



You'll notice I left the command blank since it will be overriden anyway later on. You can now use command overriding to run commands accross all of your application instances. In this example let's say you wanted to pull the latest git code on all the application instances, you could just use:

```ahd environments "git pull"```



Since only the ```<command>``` is being overridden ahd will execute "git pull" in all the specified paths.



### Paths

Overriding paths is a bit more esoteric, there is a built-in mechanism that allows you to skip command overriding and specify a new path. Let's take the following example of running ```docker compose up``` in various paths. First register the command with a name, in this case we will call it "buildapp":

```ahd register buildapp "docker compose up" "."```



This means by default if we run ```ahd buildapp``` it will run in the same directory you are in, but we could override the paths and execute it in multiple places. The way this works is by "overriding" the command to "." this is a built-in convention that means "skip overridding the command value for now". In this case we could run:

```ahd buildapp "." "~/path/to/application, ~/path/to/application-2, ~/path/to/application-3"```



to execute ```docker compose up``` in all 3 locations.



## Wildcards and Cross platform paths

In ahd paths are normalized across os's and wildcards are supported.



### Platform normalization steps

**TL;DR**: use unix-style paths (/ and include ~ for the home directory) even on windows.



**The long version**: Paths in ahd are automatically platform agnostic (unless you manually edit the config file). This means that when you register a command in windows the paths are preprocessed to change \\ to / in the config file, and ~ to the USERPROFILE environment variable, then postprocessed back when running commands. Functionally this means you can use the exact same configuration across platforms if you use the unix path idiosyncrasies (~ and /).





### Wildcards

Additionally you can specify wildcards to say "all directories in a given pattern". Under the hood this is done through the [glob](https://docs.python.org/3/library/glob.html) module in python (note there must be an asterisk or else it will register as a literal character), but the basics are that an asterisk delimits "any directory". So for example if you wanted to register a command to "git pull" all folders in a directory you could use:

```powershell
ahd register git-upt "git pull" "C:\Users\Kieran\Desktop\Development\Canadian Coding\*"
```



Here is the tree for ```C:\Users\Kieran\Desktop\Development\Canadian Coding``` :

```powershell
C:\USERS\KIERAN\DESKTOP\DEVELOPMENT\CANADIAN CODING
├───posts
├───SSB
├───website
```



So this means that when you run ```ahd git-upt``` it will run the same as:

```powershell
cd C:\Users\Kieran\Desktop\Development\Canadian Coding\posts && git pull

cd C:\Users\Kieran\Desktop\Development\Canadian Coding\SSB && git pull

cd C:\Users\Kieran\Desktop\Development\Canadian Coding\website && git pull
```



### Manually editing paths in config

All paths should be specified in unix style (use / instead of \\), even if intended to be used on windows. This is because the preprocessor that happens when you register a command does this for you.





## Autocompletion on ZSH, fish etc.

There are plans to fully support zsh and fish in the future, but a temporary solution is to use a module called [docopt-completion](https://github.com/Infinidat/infi.docopt_completion) (install using ```pip install infi.docopt-completion```). Once installed you can run ```docopt-completion ahd``` to generate autocompletion on the **TOP-LEVEL** (register, docs, config) commands. Unfortunately there is no solution for autocompletion on ahd registered commands (yet).