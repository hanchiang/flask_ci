# Installation

1. Install [python 3.7](https://www.python.org/downloads/)
1. Create your own virtual environment.
1. Activate your virtual environment.
1. Install the requirements in the directory: `pip install -r requirements.txt`

# Run the app

The main app is in the folder called app. The main file is app.py. Basically to run the code `python app/app.py` and you can see there being 3 url where 1 is to do simple arithmetic equations and 2 to get users from the json file.

# Testing

Run tests: `pytest`

# Containers

**Development**

1. Build container: `docker build -t flask_app .`
2. Run container: `docker run --name flask_app -p 5000:5000 flask_app`
3. Server is running at `localhost:5000`

**Test**

1. `pytest`

# CI

1. The CI must run the test that you have created. You can choose whichever CI system that you prefer. (TravisCI, Jenkins, Gitlab). Use python tests.py for running the test.
2. Dockerfile must have the testing procedure as well as some kind of test for the file you wrote.

If you have a server that you want to use for Continuous Delivery, feel free to go ahead, we do not require you to do CD for this test.
