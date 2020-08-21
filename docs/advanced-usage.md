# Advanced Usage

This section is all about the smaller details, and advanced techniques that are useable in ahd.


## Overriding

You can override a macros' registered command, or paths of a name ad-hoc. Overriding can be useful in circumstances where you may want to vary the command (and maintain the paths) or paths (and maintain the command) of a macro. 



### Command Overriding

Let's say you have registered the name "environments", this contains all the paths to the root directories of application instances you have running on a server. For example:

```ahd register environments "" "~/path/to/application, ~/path/to/application-2, ~/path/to/application-3"```



You'll notice I left the command blank since it will be overriden anyway later on. You can now use command overriding to run commands accross all of your application instances. In this example let's say you wanted to pull the latest git code on all the application instances, you could just use:

```ahd environments "git pull"```



Since only the ```<command>``` is being overridden ```ahd``` will execute ```git pull``` in all the specified paths, in this case ```~/path/to/application, ~/path/to/application-2, ~/path/to/application-3```.



### Path Overriding

Let's take the following example of running ```docker compose up``` in various paths. First register the macro  with a name, in this case we will call it ```buildapp```:

```ahd register buildapp "docker compose up" "."```



This means by default if we run ```ahd buildapp``` it will run in the same directory you are in (because ```.``` is relative to your cwd), but we could override the paths and execute it in multiple places. The way this works is by "overriding" the command to "." this is a built-in convention that means "skip overridding the command value for now". In this case we could run:

```ahd buildapp "." "~/path/to/application, ~/path/to/application-2, ~/path/to/application-3"```



The above command would  execute ```docker compose up``` (the registered command for the macro) in all 3 locations (```~/path/to/application, ~/path/to/application-2, ~/path/to/application-3```).



## All about paths

In ahd paths are normalized across os's and [globbing](#globbing)(regex + wildcards) is supported.



### Platform normalization steps

**TL;DR**: use unix-style paths (/ and include ~ for the home directory) even on windows.



**The long version**: Paths in ahd are automatically platform agnostic (unless you manually edit the config file). This means that when you register a command in windows the paths are preprocessed to change ```\``` to ```/``` in the config file, and ```~``` to the ```USERPROFILE``` environment variable, then postprocessed back when running commands. Functionally this means you can use the exact same configuration across platforms if you use the unix path idiosyncrasies (~ and /).



### Relative paths

**ALL** relative paths are converted to absolute path on both registration, and at runtime. The **only exception** is ```.``` which can be used to signify "in the current directory". 

Functionally this means that if you register a macro like this:

```ahd register my-macro <command> /folder-1```

Then the path that is registered is the **absolute path** to folder 1 not the **relative path**. So for example if ```/folder-1``` is on the desktop, then the path ```~/Desktop/folder-1``` is registered.



### Globbing

Globbing (also known as path expansion) can be used to pattern-match paths. This is facilitated by the [glob](https://docs.python.org/3/library/glob.html) module in python. There are typically two types of pattern used, regex & wildcards (they can also be used together).



#### Wildcards

A wildcard is basically a symbol that represents "all directories" in this case wildcards are invoked by asterisk(s). So for example if you wanted to register a macro (Called update) to ```git pull``` in all folders on the desktop you could use:

```powershell
ahd register update "git pull" "~/Desktop/*"
```



Here is the tree for ```~/Desktop/``` (in this case on windows with a user called ```kieran```:

```
├── /Desktop
|   └── /Development
|      ├── /project_1
|      ├── /project_2
|      ├── /project_3
|      └── /project_4
```



So this means that when you run ```ahd update``` it will run the same as:

```powershell
cd C:\Users\Kieran\Desktop\project_1 && git pull

cd C:\Users\Kieran\Desktop\project_2 && git pull

cd C:\Users\Kieran\Desktop\project_3 && git pull

cd C:\Users\Kieran\Desktop\project_4 && git pull
```



#### Regex 
It is possible to pattern match using regex to find your paths. For example to only include folders on the desktop that are numbers between 0-9 you could do: ```ahd register <name> <command> "~/Desktop/[0-9]"```.




## Transferring Configurations
To transfer your configuration you simply need to export your configuration file, and then import it on the machine you want to use the configuration on. This functionality is built into the [config command](../usage#config). 

Here are the steps to transfer the config:

1. Export your config from the host machine using ```ahd config -e``` or ```ahd config --export```. There will now be a file in your cwd called ```ahdconfig.yml```.
2. Copy the ```ahdconfig.yml``` file to the machine you want to use the configuration on, and then use ```ahd config -i "ahdconfig.yml"``` or ```ahd config --import "ahdconfig.yml"```. You will recieve a message on the terminal saying ```importing ahdconfig.yml to <path to config file>```.

If you receive no errors it worked. Note that you may need to restart your shell for autocomplete to function with the new config.



## Manual configuration

Although not recommended you can opt to do manual configuration, though there are a few drawbacks:

1. Autocomplete will not update until you register a new command through ```ahd register```
2. If you write a path incorrectly (spelling mistake etc.) the command will error out when you try to run it



That being said, if you prefer to manually update your config here is what you need to know:

- All macros fall under the main macro object with two sub-objects for the command and path respectively.
- All paths should be specified in unix style (use / instead of \\), even if intended to be used on windows.
- Make sure your command is encapsulated with quotes if you are unsure of proper YAML escaping.

Here is an example configuration for the macro ```git upt``` with the command ```git pull``` and the paths ```~/Desktop/development/*```:

```yaml
macros:
  git-upt:
    command: git pull
    paths: ~/Desktop/development/*
```



## Autocompletion

There is built in autocompletion for top level (config, docs etc), and for macros that have been registered through ```register``` and not manually.

### Bash
Bash autocomplete is generated as soon as a command is registered through ```ahd register```. Remember that for the autocomplete to update you need to restart the shell.

### Windows
As far as I am aware it is not possible to implement autocomplete for commands on windows. I tried to look into it, but no interfaces exist for **commands**, only paths.

### ZSH, fish etc. 

There are plans to fully support zsh and fish in the future . A temporary solution is to use a module called [docopt-completion](https://github.com/Infinidat/infi.docopt_completion) (install using ```pip install infi.docopt-completion```). Once installed you can run ```docopt-completion ahd``` to generate autocompletion on the **TOP-LEVEL** (register, docs, config) commands. Unfortunately there is no solution for autocompletion on ahd registered commands for these shells (yet).



## Vendoring

It is possible to vendor ahd to solve a few potential issues

- If for some reason ahd has a collision with another app called ahd
- You want something shorter than 3 letters to type each time you use it

Let's assume you want to instead use ```q``` instead of ```ahd```, you only need to do the following:

1. Download the source code ```git clone https://github.com/Descent098/ahd``` or just hit this link ```https://github.com/Descent098/ahd/archive/master.zip```

2. Open ```setup.py``` in a text editor/IDE

3. change the ```name``` and ```entry_points``` parameters in ```setuptools.setup()```. 
   By default they will be:

```python
   setuptools.setup(
       name = "ahd",
   	...
       entry_points = { 
              'console_scripts': ['ahd = ahd.cli:main']
          },
   	...
   )
```

   In our case we would want to make them:

```python
   setuptools.setup(
       name = "q",
   	...
       entry_points = { 
              'console_scripts': ['q = ahd.cli:main']
          },
   	...
   )
```

4. Open the root directory (the one with ```setup.py``` in it), and run ```pip install .``` or ```sudo pip3 install .```.

Now you will be able to run ```q``` instead of ```ahd```.

