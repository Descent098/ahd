# Quick-start

Everything you need to know to get started using ahd including installation, and a quick example. For full details about the CLI see [the usage section](../usage).



## Dependencies

- Python 3.6+ (or is at least only tested and officially supported for 3.6+)
- pip for python



## Installation

Once you have python3 and pip you have a few installation options.



### From Pypi

Run ```pip install ahd``` or ```sudo pip3 install ahd``` (need a network connection)

### From source

1. Clone this repo: (https://github.com/Descent098/ahd)
2. Run ```pip install .``` or ```sudo pip3 install .```in the root directory (one with setup.py)



## Example

In this example I will show you how to setup a macro called ```update``` that when dispatched will ```git pull``` (**update** to the latest git code) on all folders inside ```~/Desktop/Development```. For this example let's assume you are currently in the ```~/Documents``` directory, and the ```~/Desktop/Development``` directory structure looks like this:

```
├── /Desktop
|   └── /Development
|      ├── /project_1
|      ├── /project_2
|      ├── /project_3
|      └── /project_4
```



1. First for any macro you will need to register it, registering is in the form of ```ahd register <name> [<command>] [<paths>]``` so for this example:
```ahd register update "git pull" "~/Desktop/Development/*"```
2. Now to run the macro you use the form ```ahd <name>```, so in this case:
    ```ahd update```

  Running ```ahd update``` will:

  1. Expand ```~/Desktop/Development/*```, so for this example with the above directory tree it would be:
     ```~/Desktop/Development/project_1```, ```~/Desktop/Development/project_2```, ```~/Desktop/Development/project_3```, and ```~/Desktop/Development/project_4```

  2. Change into each directory and run the command associated with ```update```. In this case the dispatch would produce the same result as:

     ```cd ~/Desktop/Development/project_1 && git pull && cd ~/Desktop/Development/project_2 cd && git pull && cd ~/Desktop/Development/project_3 && git pull && cd ~/Desktop/Development/project_4 && git pull ```

  3. Changes directory back to the original directory you started from.

Although this is a toy example  you can see how much time it saves. The approach to path expansion also makes executing commands dynamic, meaning if you added more folders to ```~/Desktop/Development/``` they would automatically be included. For more specific usage details check out the [usage](../usage) section.