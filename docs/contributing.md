# Contribution & Development Guide

Here is everything you need to know about getting started for contributing to the project (thanks for doing so by the way).



## Development guide

### Basic rules

1. Commenting/documentation is **not** optional. See [minimum documentation](#minimum-documentation) for minimum requirements to have a pull request accepted.
2. Breaking platform compatibility for ease of development is **not** acceptable.
3. Do **everything** through [github](https://github.com/Descent098/ahd/issues/new/choose) (it's all been setup for you).



### Development Dependencies

To grab the specified development dependencies simply run ```pip install adh[dev]```, this will grab everything you need.



If for some reason this does not work, here are a list of development dependencies:

```
nox    # Used to run automated processes
pytest # Used to run the test code in the tests directory
mkdocs # Used to create HTML versions of the markdown docs in the docs directory
```



#### Running tests

Testing is implemented using [pytest](https://docs.pytest.org/en/latest/), and can be run 1 of 2 ways:

1. Run the tests through nox using ```nox -s tests```, this will automatically run the tests against python 3.5-3.8 (assuming they are installed on system).
2. Go to the root directory and run ```pytest```, this should automatically detect the /tests folder and run all tests.



#### Building the package

This is not necessary for pull requests, (or even development) but if you want to validate that it doesn't break buildability here is how to do it. You can use ```nox -s build```, this will create a source distribution for you using pythons' [setuptools module](https://setuptools.readthedocs.io/en/latest/).

#### Building user docs

If you are contributing to the user documentation (found in /docs) you can verify the documentation by first installing [mkdocs](https://www.mkdocs.org/) (```pip install mkdocs```) then running ```mkdocs serve``` and finally going to [http://localhost:8000](http://localhost:8000).



#### Building "API" docs

API docs are useful if you want an easily navigatable version of the in-line documentation. The best way to do this currently is to download [pdoc3](https://pdoc3.github.io/pdoc/doc/pdoc/); ```pip install pdoc3``` then (assuming ahd is installed) run ```pdoc ahd --http localhost:8080```. Go to a browser and type in [http://localhost:8080/ahd](http://localhost:8080/ahd).



### Nox integration

If you have never used [nox](https://nox.readthedocs.io/) before it is a great system for automating tedious tasks (builds, distributions, testing etc). This project uses nox for a number of things and in the following sections I will explain each. 


## Contribution guide

Below you will find everything you need to know about how to contribute.



### Minimum Documentation
If you are submitting a pull request, this is the minimum **inline** documentation you must provide.

1. All classes/functions/methods must have a [numpy-style docstring](https://numpydoc.readthedocs.io/en/latest/format.html#docstring-standard) (minimum example below) that includes a short description, attributes/parameters, and return types/methods.
2. If you wrote a new feature include user documentation on how it works, or mention you haven't and at least give some detail in the pull request.
3. Add [PEP-484](https://www.python.org/dev/peps/pep-0484/) type hints to any methods or functions

Here is an example of a minimum function/method:

```python
def add(number_1:int, number_2:int) -> int:
    """Takes two values and adds them together
    
    Parameters
    ----------
    number_1: int
        The first number that will be added
    number_2: int
        The second number that will be added
    
    Returns
    -------
    int:
        The value of number_1 + number_2
    """
    return number_1 + number_2
```



Here is an example of a minimum class:

```python
class Dog:
   """Each instance represents a dog
   
   Attributes
   ----------
   name: (str)
       The name of the dog
   age: (int)
       The current age of the dog (in years)
       
   Methods
   -------
   age_to_human_years:
   	   Takes the Dog instances' age and returns the human equivalent
   """
   def __init__(self, name:str, age:int):
       self.name = name
       self.age = age
   
   def age_to_human_years(self) -> int:
       """Takes the Dog instances' age and returns the human equivalent
       
       Returns
       -------
       int:
           The human representation of the dogs age
       """
       return self.age * 7
```



Ideally you can also include type hints, examples, notes and references where it makes sense.






### Bug Reports & Feature Requests

Submit all bug reports and feature requests on [github](https://github.com/Descent098/ahd/issues/new/choose), the format for each is pre-defined so just follow the outlined format



### Pull requests

Pull requests should be submitted through github and follow the default pull request template specified. If you want the rundown of what needs to be present:

1. Provide a clear explanation of what you are doing/fixing
2. Feature is tested on Windows & *nix (unless explicitly incompatible)
3. All Classes, modules, and functions must have docstrings that follow the [numpy-style guide](https://numpydoc.readthedocs.io/en/latest/format.html).
4. Unless feature is essential it cannot break backwards compatibility

