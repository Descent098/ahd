"""Include your own tests as functions here"""

import os

import glob

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


