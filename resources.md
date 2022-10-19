# Resources for learning python

* [Python 3 Documentation Home](https://docs.python.org/3/)
* [Index of modules](https://docs.python.org/3/py-modindex.html)
* [Alphabetical General Index](https://docs.python.org/3/genindex.html)

* [Operator Precedence Summary Table](https://docs.python.org/3/reference/expressions.html#operator-precedence)

# Interesting PEPs

* [PEP 8 — Style Guide for Python](https://peps.python.org/pep-0008/)
* [PEP 20 — The Zen of Python](https://peps.python.org/pep-0020/) (`import this` for a little Easter Egg)
* [PEP 257 — Docstring Conventions](https://peps.python.org/pep-0257/)
* [PEP 308 — Conditional Expressions](https://peps.python.org/pep-0308/)
* [PEP 498 – Literal String Interpolation](https://peps.python.org/pep-0498/)
* [PEP 3101 — Advanced String Formatting # Standard Format Specifiers](https://peps.python.org/pep-3101/#standard-format-specifiers)

# Articles/Questions

* [3 Easy Ways to Find the Length of a List in Python](https://www.digitalocean.com/community/tutorials/find-the-length-of-a-list-in-python)
* [Official datastructures tutorial](https://docs.python.org/3/tutorial/datastructures.html)
* The python exception hierarchy and advice when to use each one is in the [exceptions library](https://docs.python.org/3/library/exceptions.html#exception-hierarchy)
* [Python naming conventions](https://visualgit.readthedocs.io/en/latest/pages/naming_convention.html)
* [The easiest way](https://stackoverflow.com/questions/34439/finding-what-methods-a-python-object-has) to list methods/attributes is just `dir(...)`
* The syntax of [conditional expressions](https://docs.python.org/3/reference/expressions.html#index-88) is very simple and inside-out
* A [slash signifies the end of /positional only/ parameters](https://stackoverflow.com/questions/24735311/what-does-the-slash-mean-in-help-output)
* [`del` is a statement](https://docs.python.org/3/reference/simple_stmts.html#index-21) not a function!

# Lists

Lists don't have all their methods described in one place!

* https://docs.python.org/3/library/stdtypes.html#list
* https://docs.python.org/3/library/stdtypes.html#typesseq-common
* https://docs.python.org/3/library/stdtypes.html#typesseq-mutable

The [`sorted`](https://docs.python.org/3/library/functions.html#sorted) function returns a new sorted list from an iterable.

* [List Comprehensions Tutorial](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions)

# Virtualenv/venv

Summary: venv is the new python3 feature.  It's accessed with `python3 -m venv`.  `pyenv-virtualenv` accesses venv if using python3.

* [pyenv-virtualenv on Github](https://github.com/pyenv/pyenv-virtualenv)
* [Creating virtual environments with Pyenv](https://akrabat.com/creating-virtual-environments-with-pyenv/) [Article from Rob Allen's DevNotes]
* [What is the difference between venv, pyvenv, pyenv, virtualenv, virtualenvwrapper, pipenv, etc?](https://stackoverflow.com/a/41573588/19859074) [StackOverflow]
* https://virtualenv.pypa.io/en/latest/

# Misc

* [Pandas User Guide](https://pandas.pydata.org/docs/user_guide/index.html) &emdash; This is a data handling library eg timeseries, multi-dimensional etc (but not matrices/BLAS)
* [Flask User Guide](https://flask.palletsprojects.com/en/2.2.x/)

/Tip:/ Use `python -i script.py` to run the script, and then give you a REPL.

To catch an error, and print a traceback of it, but then continue: (the `pass` is optional)

```
import traceback

try:
    print(fruits[10])
except Exception as e:
    print("error:", e)
    traceback.print_exception(e)
    pass
```
