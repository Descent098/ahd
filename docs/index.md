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

