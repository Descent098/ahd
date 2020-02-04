![ahd-logo](https://raw.githubusercontent.com/Descent098/ahd/master/docs/img/ahd-logo.png)



# ahd; Ad-Hoc Dispatcher

Create ad-hoc commands to be dispatched in their own namespace.



## Why?

This package seeks to make the tedius task of creating one off bash scripts obsolete. The idea is to write an annoying command once, give it a name, and be able to recall it without an issue. It also has the benefit of namespacing commands that would normally be keywords for ease of use. See the quick-start guide for more details.



## Features

- Execution of any valid bash/wsl commands.
- Specification of multiple paths (including [wildcards](/en/latest/usage/#wildcards-and-cross-platform-paths))
- Autocomplete (\*nix only; with bash, and plans to add zsh and fish later)
- A namespace with only 3 reserved keywords (docs, register, config)
- Cross-platform support



## "Limitations"

- Autocompletion not supported on windows (not my fault)
- Technically without vendoring you also can't use ```ahd``` as a command for any other purpose



# Upgrading to V 0.2.x from V0.1.x

One thing to note if you are updating to V0.2.x from V0.1.x, the way that the preprocessing of paths works has been changed. Originally it was being stored as a "list" (though this isn't actually the case), and  now it is just a string of comma-delimited paths. Here are the steps to migrate:



1. Export your current configuration by running:
    ```ahd config -e```

2. Edit the configuration file in a text editor (in this example I will use nano):
    ```nano .ahdconfig```

3. Change any paths for commands to string representations instead of lists(remove the square brackets). For example:
    This

```ini
[git-upt]
command = git pull
paths = [C:\Users\Kieran\Desktop\Development\personal\*, C:\Users\Kieran\Desktop\Development\Canadian Coding\*]
```

Would become

```ini
[git-upt]
command = git pull
paths = ~/Desktop/Development/personal/*, ~/Desktop/Development/Canadian Coding/*
```

​    

