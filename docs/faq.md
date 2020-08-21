# Frequently Asked Questions

If you have any questions feel free to submit an issue on [github](https://github.com/Descent098/ahd) using the [question template]([https://github.com/Descent098/ahd/issues/new?assignees=Descent098&labels=documentation&template=question.md&title=%5Bquestion%5D](https://github.com/Descent098/ahd/issues/new?assignees=Descent098&labels=documentation&template=question.md&title=[question])).



## I made a mistake when registering a command, how do I change it?

There are two options:

1. You can re-register the command; anytime a command is registered that has the name of an existing command it will overwrite the existing command.
2. You can manually edit the configuration, details on how to do this can be found in the [manual configuration](../advanced-usage#manual-configuration) section.



## I'm getting a permission error when I try to register a command, what do I do?

On \*nix systems I have intentionally made it so you **MUST** use sudo when registering a command, or importing a config. Since ahd dispatches **literally** whatever you type, I have made it so you need admin privileges to make configuration modifications.



## I'm getting a permission error when I try to run a command, what do I do?

Likely the command you have registered needs sudo access, modify your configuration using one of the methods found in the first question of this page and add ```sudo``` in front of the command.



For example if you originally registered a command to ```apt-get update``` by doing ```ahd register update "apt-get update" "."```, then you will need to do ```ahd register update "sudo apt-get update" "."```.