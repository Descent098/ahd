"""Include your own tests as functions here"""

import os

import glob

from ahd.cli import _preprocess_paths, _postprocess_paths

def test_preprocess_paths():
    """ """

    # Test windows cases
    win_paths = '~/Desktop/Development/Canadian Coding/SSB, C:\\Users\\Kieran\\Desktop\\Development\\*, ~\\Desktop\\Development\\Personal\\noter, .'
    
    assert _preprocess_paths(win_paths) == "~/Desktop/Development/Canadian Coding/SSB,~/Desktop/Development/*,~/Desktop/Development/Personal/noter,."


def test_postprocess_paths():

    # Test windows cases
    paths = '~/Desktop/Development/Canadian Coding/SSB,~/Desktop/*,~/Desktop/Development/Personal/noter,.'
    
    if os.name == "nt":

        correct_paths = [f"{os.getenv('USERPROFILE')}\\Desktop\\Development\\Canadian Coding\\SSB"]
        for current_path in glob.glob(f"{os.getenv('USERPROFILE')}\\Desktop\\*"):
            correct_paths.append(current_path.replace("\\", "/"))
        correct_paths.append(f"{os.getenv('USERPROFILE')}\\Desktop\\Development\\Personal\\noter")
        correct_paths.append(os.path.abspath("."))
        assert _postprocess_paths(paths) == correct_paths
    
    
    else:
        pass


