## Background

In the move from version 0.4.0 to version 0.5.0 the configuration system has drastically changed from the configparser INI style to YAML. Because of this there needs to be a migration done on any existing configuration files. Currently there is a built in migration that will be removed as part of the version 0.6.0 update. This **migration will run automatically the first time you run any command in ahd** after updating.


For example here is an old config file:

```.ahdconfig```

```ini
[git-upt]
command = git pull
paths = ~/Desktop/development/*

[remove-pdf]
command = rm *.pdf
paths = ~/Desktop/
```

Here is the new equivalent file:

```ahd.yml```

```yaml
macros:
  git-upt:
    command: git pull
    paths: ~/Desktop/development/*
  remove-pdf:
    command: rm *.pdf
    paths: ~/Desktop/
  add-pdf:
    command: mkdir *.pdf
    paths: ~/Desktop/
```



## Steps

1. Update ahd to the latest version using ```pip install --upgrade ahd```
2. Run any command in ahd. This could be a registered macro, or any top level command such as ```ahd list```
3. You will receive a message letting you know there is an old configuration file detected, and then a new file will be automatically generated off the existing one. 
4. You will then be asked if you want to delete the new file, respond with ```y``` for yes, or ```n``` for no. To be completely safe I would recommend saying no the first time, and running an ```ahd list``` to make sure nothing got missed, and then say yes the second time. 

You shouldn't need to do this verification, but if you did some incorrect formatting with manual modification of a configuration in the past, something may be missed. After that you are good to go with the new version of ahd.