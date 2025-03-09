# python-login-template
A web login template using python and Flask

# Error documentation
**1. ModuleNotFoundError when executing pytest**  
Error message  
```
ModuleNotFoundError: No module named 'app'  
```
Action  
```
pytest -vv  
```
Solution  
Execute
```
python -m pytest
```
Explanation  
* Running pytest with the python -m pytest command helps with this exact thing.  
* Since your current package is not yet in your $PYTHONPATH or sys.path - pytest gets this error.  
* By using python -m pytest you automatically add the working directory into sys.path for running pytest. Their documentation also mentions:  
*This is almost equivalent to invoking the command line script pytest*  
