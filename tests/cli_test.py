"""Include your own tests as functions here"""

import os

import glob

import pytest
from ahd.cli import *
from ahd.configuration import *
from ahd.cli import _preprocess_paths, _postprocess_paths

def test_preprocess_paths():
    """Validates that input paths are serialized in a normalized format across OS's.
    
    Cases
    -----
    - Relative paths; .
    - Home directory; ~
    - Wildcards; *
    - Windows (only on windows machine)
    - *nix/MacOS (only on *nix/MacOS machine)
    """

    if os.name == "nt": # Test windows cases
        win_paths = f'~/Desktop/Development/Canadian Coding/SSB, {os.getenv("USERPROFILE")}\\Desktop\\Development\\*, ~\\Desktop\\Development\\Personal\\noter, .'
        
        assert _preprocess_paths(win_paths) == "~/Desktop/Development/Canadian Coding/SSB,~/Desktop/Development/*,~/Desktop/Development/Personal/noter,."
    
    else: # Test *nix cases
        nix_paths = f"~/Desktop/Development/Canadian Coding/SSB, {os.getenv('HOME')}/Desktop/Development/*, ~/Desktop/Development/Personal/noter, ."

        assert _preprocess_paths(nix_paths) == "~/Desktop/Development/Canadian Coding/SSB,~/Desktop/Development/*,~/Desktop/Development/Personal/noter,."


def test_postprocess_paths():
    """Validates that pre-processed paths are deserialized properly on a per OS basis.
    
    Cases
    -----
    - Relative paths; .
    - Home directory; ~
    - Wildcards; *
    - Windows (only on windows machine)
    - *nix/MacOS (only on *nix/MacOS machine)
    """
    
    paths = '~/Desktop/Development/Canadian Coding/SSB,~/Desktop/*,~/Desktop/Development/Personal/noter,.'
    
    if os.name == "nt": # Windows case
        correct_paths = [f"{os.getenv('USERPROFILE')}\\Desktop\\Development\\Canadian Coding\\SSB"]
        for current_path in glob.glob(f"{os.getenv('USERPROFILE')}\\Desktop\\*"):
            correct_paths.append(current_path.replace("\\", "/"))
        correct_paths.append(f"{os.getenv('USERPROFILE')}\\Desktop\\Development\\Personal\\noter")
        correct_paths.append(os.path.abspath("."))
        assert _postprocess_paths(paths) == correct_paths
    
    else: # Test *nix cases
        correct_paths = [f"{os.getenv('HOME')}/Desktop/Development/Canadian Coding/SSB"]
        for current_path in glob.glob(f"{os.getenv('HOME')}/Desktop/*"):
            correct_paths.append(current_path)
        correct_paths.append(f"{os.getenv('HOME')}/Desktop/Development/Personal/noter")
        correct_paths.append(os.path.abspath("."))
        assert _postprocess_paths(paths) == correct_paths


def test_list(capsys):
    """Tests the list command"""
    CONFIG_FILE_PATH = "tests/cli_test.yaml"
    config = {"macros": {"test": {"command": ".", "paths": "."}}}
    bad_config = {"macros": {"test": {"command": "."}}}
    bad_config_2 = {"macros": {"test": {"paths": "."}}}
    list_macros(False, config)
    captured = capsys.readouterr()
    assert captured.out == "\n\x1b[38;5;6mtest\x1b[38;5;15m\n\n\n1 macros detected\n"
    list_macros(False, bad_config) # Won't error out because incorrect values are never used
    captured = capsys.readouterr()
    assert captured.out == "\n\x1b[38;5;6mtest\x1b[38;5;15m\n\n\n1 macros detected\n"
    list_macros(False, bad_config_2) # Won't error out because incorrect values are never used
    captured = capsys.readouterr()
    assert captured.out == "\n\x1b[38;5;6mtest\x1b[38;5;15m\n\n\n1 macros detected\n"
    list_macros(True, config)
    try:
        list_macros(True, bad_config)
        pytest.fail("Expected error to be thrown")
    except SystemExit: # Should error out
        pass
    try:
        list_macros(True, bad_config_2)
        pytest.fail("Expected error to be thrown")
    except SystemExit: # Should error out
        pass


def test_configure():
    """TODO: going to change when config systems are switched, not worth doing yet"""
    import ahd
    ahd.cli.CONFIG_FILE_PATH = "tests/cli_test.yaml"
    ahd.configuration.CONFIG_FILE_PATH = "tests/cli_test.yaml"
    try:
        configure()
    except SystemExit:
        ... # Should error out
    with open("tests/cli_test.yaml", "w") as f:
        f.write("")
    configure(export=False, import_config="tests/cli_test_import.yaml", config={})
    with open("tests/cli_test.yaml", "r") as f:
        assert f.read() == "macros:\n  testing1:\n    commands: echo\n    paths: .\n"
    configure(export=True, import_config=False, config={})
    with open("ahd.yml", "r") as f:
        assert f.read() == "macros:\n  testing1:\n    commands: echo\n    paths: .\n"
    os.remove("tests/cli_test.yaml")
    os.remove("ahd.yml")


def test_register():
    """Tests registering macros"""
    import ahd
    ahd.cli.CONFIG_FILE_PATH = "tests/cli_test.yaml"
    ahd.configuration.CONFIG_FILE_PATH = "tests/cli_test.yaml"

    # Valid entries
    try:
        register(macro_name="test", commands="echo", paths=".", config={})
    except SystemExit:
        ... # Should error out
    try:
        register(macro_name="test1", commands="", paths=".", config={})
    except SystemExit:
        ... # Should error out
    try:
        register(macro_name="test2", commands="echo", paths="", config={})
    except SystemExit:
        ... # Should error out
    try: # overwriting an existing macro
        register(macro_name="test", commands="", paths="", config={})
    except SystemExit:
        ... # Should error out

    # Invalid entries
    try:
        register(macro_name="register", commands="", paths="", config={})
    except ValueError:
        ... # Should error out

    os.remove("tests/cli_test.yaml")

def test_dispatch(capsys):
    """Tests dispatching macros"""
    import ahd
    ahd.cli.CONFIG_FILE_PATH = "tests/cli_test.yaml"
    ahd.configuration.CONFIG_FILE_PATH = "tests/cli_test.yaml"
    config={"macros":{"test":{"command":"echo", "paths":"."}}}   
    config_wildcards={"macros":{"testy":{"command":"echo", "paths":"./*"}}}   
    config_mixed={"macros":{"test":{"command":"echo", "paths":"."},"testy":{"command":"echo", "paths":"./*"}}}   

    # normal dispatch
    dispatch("test", False, False, config=config)
    # Nonexistant command with comparable commands
    try:
        dispatch("testy", False, False, config=config) # should 
    except SystemExit:
        captured = capsys.readouterr()
        assert "%89" in captured.out
    # Nonexistent command with no comparable commands
    try:
        dispatch("uwu", False, False, config=config) # should 
    except SystemExit:
        captured = capsys.readouterr()
        assert "any valid suggestions with %60 or higher likelyhood" in captured.out
    # Overwriting command defaults
    dispatch("test", "echo yeet", False, config=config)
    dispatch("test", False, "..", config=config)
    # No config
    try:
        dispatch("test", False, False, config={})
    except SystemExit:
        ... # Should error out

    # Wildcards
    dispatch("testy", False, False, config=config_wildcards)
    dispatch("test", False, False, config=config_mixed)
    dispatch("testy", False, False, config=config_mixed)
    os.remove("tests/cli_test.yaml")
