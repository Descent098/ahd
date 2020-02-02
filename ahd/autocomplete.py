from collections import namedtuple

command = namedtuple("command", ["name", "arguments"])


def _generate_root_autocomplete(commands:list , arguments:list = [], root:str = "ahd"):



    arguments = _stringify_list(arguments)

    root_template = f"""_{root}()
    {{
        local cur
        cur=\"${{COMP_WORDS[COMP_CWORD]}}\"

        if [ $COMP_CWORD -eq 1 ]; then
            COMPREPLY=( $( compgen -fW '{arguments} {_stringify_list(commands)}' -- $cur) )
        else
            case ${{COMP_WORDS[1]}} in
    """

    for command in commands:
        root_template += f"""
                {command})
                _{root}_{command}
            ;;
        """

    root_template+="""
            esac

        fi
    }
    """

    return root_template
        




def _generate_command_autocomplete(command:str, arguments:list, root:str = "ahd"):
    """Generates a bash autocomplete block for a single command"""
    
    if arguments:
        arguments = _stringify_list(arguments)
    else:
        arguments = " "
    command_result = f"""_{root}_{command}()
    {{
        local cur
        cur=\"\${{COMP_WORDS[COMP_CWORD]}}\"

        if [ $COMP_CWORD -ge 2 ]; then
            COMPREPLY=( $( compgen -W '{arguments}' -- $cur) )
        fi
    }}
    """

    return command_result


def _stringify_list(arguments:list):
    """Takes a list and stringifies it to a useable format for autocomplete files"""
    stringified = ""
    for argument in arguments: # Preprocess arguments into appropriate string form
        stringified += f" {argument}"
    
    return stringified


def generate_bash_autocomplete(commands:list, root:str = "ahd"):

    sub_commands = [root] # list of just top level sub-commands
    for command in commands: # Iterate through and pull just subcommands from commands list
        sub_commands.append(command.name)

    arguments = ["-h", "--help", "-v", "--version"]
    for command in commands:
        for argument in command.arguments:
            arguments.append(argument)
    
    autocomplete_text = _generate_root_autocomplete(sub_commands, arguments)

    for command in commands:
        autocomplete_text += _generate_command_autocomplete(command.name, command.arguments)


    autocomplete_text += f"\ncomplete -o bashdefault -o default -o filenames -F _{root} {root}\n"

    return autocomplete_text

if __name__ == "__main__":
    commands =  [ # Used for autocompletion generation
        command("docs", ["-a", "--api", "-o", "--offline"]),
        command("register", [])
    ]
    print(generate_bash_autocomplete(commands))