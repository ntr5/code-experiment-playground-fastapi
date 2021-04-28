# Code Experiment FastAPI Playground
This is a playground built during the Code Experiment meetup. We will slowly be building a Todo app with authentication. If you would like to join please head over to https://code-experiment.netlify.app/ and join our slack, we meet every Tuesday at 6:00 pm MST.
If you want to catchup, please clone this repo and follow the steps below.
## Environment Setup
**Create Virtual Environment:**
> Wherever you run this command it will create a `venv` folder. If you want the folder to be called something different change the second `venv`.
> Make sure you are inside the `code_experiment_playground` folder when you run this command.
```
# Mac
$ python3 -m venv venv
# PC
$ python -m venv venv
```
**Activate The Virtual Environment:**
> Make sure you are inside the `code_experiment_playground` folder when you run this command.
```
# Mac
$ source venv/bin/activate
(venv) $ _
# Windows
$ venv\Scripts\activate
(venv) $ _
```
**Installing Packages:**
> Make sure you are inside the `code_experiment_playground` folder when you run this command.
```
(venv) $ pip install -r requirements.txt
```
> You might need to remove the `uvloop` package on windows.
## Run The Uvicorn Server
> Make sure you are inside the `code_experiment_playground` folder when you run this command.
```
(venv) $ uvicorn app.main:app --reload
```
## Interactive Docs
Open your favorite browser and head to http://localhost:8000/docs for the docs.
## Running tests
We're using pytest for our testing you can learn more at https://docs.pytest.org/en/stable/
- Run all tests
```
(venv) $ python -m pytest
```
- Run all tests from a single file
```
(venv) $ python -m pytest folder/file_name.py
```
- Run a single test from a single file
```
(venv) $ python -m pytest folder/file_name.py::test_function_name
```
- Run all tests that contain a certain marker
```
(venv) $ python -m pytest -m marker_name
```
## Testing
- Fixtures:
  - https://docs.pytest.org/en/stable/fixture.html
- Setting up the database/fixture research:
  - https://github.com/tiangolo/fastapi/issues/831
  - https://github.com/timhughes/example-fastapi-sqlachemy-pytest
- Configuration:
  - https://docs.pytest.org/en/stable/customize.html
## Warnings:
- Currently we have a warning from `python-jose` and it looks to be almost fixed. It is just a warning so we should be ok.
  - https://github.com/mpdavis/python-jose/pull/207
```
CryptographyDeprecationWarning: int_from_bytes is deprecated, use int.from_bytes instead
```
- It seems this issue is coming from aiofiles and they have a fix in release v0.6. We need to figure out what installed this. Is it ok for us to just go update this package?
  - https://github.com/Tinche/aiofiles/issues/84
```
DeprecationWarning: "@coroutine" decorator is deprecated since Python 3.8, use "async def" instead
```
