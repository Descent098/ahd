# Changelog

## V 0.3.0; TBD

Focus for this release was on building sustainable development pipelines (logging, testing etc.), and making the project more reliable in edge cases and error handling.

Features:

- Built out the testing suite to be run before release
- Built out the logging mechanism for debugging
- Introduced many error catches for various issues.
- Split discrete actions into function in primary entrypoint
- Similarity checking; performs a check to see if a command is misstyped by checking similarity to registered commands when a command fails to run.

Bug Fixes:

- Added config command to bash autocomplete

Documentation improvements:

- Created API documentation site


## V 0.2.1; February 2nd 2020

- Added support for . as current directory path
- Fixed issue with being unable to import configuration files
- Fixed issue with docs command when running --api



## V 0.2.0; February 2nd 20202

Focus was on improving the overall useability of ahd. Note this version breaks backwards compatibility, but includes a migration guide in the docs (to be removed in V0.3.0).



Features:

- Bash Autocomplete implemented (ZSH and fish to come)
- Ability to export configuration
- Ability to import configuration
- Added a top level "docs" command to easy access documentation
- Added cross-platform wildcard support (see docs for usage)
- Added cross-platform home directory (see docs for details)



Bug fixes:

- Fixed issue where running "register" command without any flags would error out instead of printing help info
- Fixed issue with relative path tracking



Documentation improvements:

- Added issue templates for bug reports and feature requests
- Added pull request templates
- Added contribution guide
- Added migration information
- Added relevant documentation for all features released in V0.2.0



## V 0.1.0; January 28th 2020

Initial release focused on creating the basic functionality for the ahd command.

Features:

- Ability to register a command
- Ability to specify command to run
- Ability to specify the location(s) to run the command in.
- Have commands store to a configuration file using configparser
