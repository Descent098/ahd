# Quick-start

Everything you need to know to get started using ahd.



## Installation

### From Pypi

Run ```pip install ahd``` or ```sudo pip3 install ahd```



### From source

1. Clone the repo: ([https://github.com/Descent098/ahd](https://github.com/Descent098/ahd))
2. Run ```pip install .``` or ```sudo pip3 install .```in the root directory



## Example

In this example I will show you how to setup a name called ```rmtmp``` that when called will delete all files in the ~/tmp folder. First for any command you will need to register it, registering is in the form of ```ahd register <name> [<command>] [<paths>]``` so for this example:



```ahd register rmtmp "rm *" "~/tmp"```



Now to run the command you use the form ```ahd <name>```, so in this case:

```ahd rmtmp```



This will effectively run ```cd ~/tmp && rm *``` then cd back to your current directory. Although this is a toy example it allows you to specify the execution of what would normally be tedius commands from anywhere. If you are looking for some more robust examples check out the [usage](/en/latest/usage) section.
