# Usage

```bash
Usage: 

    ahd [-h] [-v] [-d]

    ahd register <name> [<command>] [<paths>]

    ahd <name> [<command>] [<paths>]



Options:

-h, --help        show this help message and exit

-v, --version     show program's version number and exit

-l, --log         If present will output logs to sys.stdout

-d, --doc         If present will open up the ahd docs
```





## Arguments

### Register

The register command allows you to register a name to be used later on. For example if I wanted to create a command that dispatched running git pull in several of my directories that is activated when I type ```ahd git-upt``` then I can just run ```ahd register git-upt "git pull" "~/path/to/project, ~/path/to/project-2, ~/path/to/project-3```



### <name\>

This is a placeholder value for the name of a command you have registered. Once the command is registered you can run it by using ```ahd <name>```, additionally you can override the default set commands or paths see below for details.





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