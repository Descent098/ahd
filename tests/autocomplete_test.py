import pytest

from ahd.autocomplete import generate_bash_autocomplete, command, _stringify_list

def test_bash_generation():
    pass

def test_stringify_list():
    """Testing the _stringify_list method from autocomplete module"""

    # Regular case
    assert _stringify_list(["-a", "--api", "-o", "--offline"]) == ' -a --api -o --offline'

    # Empty list case
    assert _stringify_list([]) == ''

    # Tuple case
    assert _stringify_list(("-a", "--api", "-o", "--offline")) == ' -a --api -o --offline'

    # String case
    with pytest.raises(ValueError):
        _stringify_list(" -a --api -o --offline")