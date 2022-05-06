# Formula 1 Driver Analysis

## Setup

Create virtual environment:

```sh
conda create -n formula1-env python=3.8
```

```sh
conda activate formula1-env
```

Install packages:

```sh
pip install -r requirements.txt
```

## Downloading the CSV file
First, create a csv file titled "driverresults.csv" in the root directory. 
In your command line enter:

```sh
python -m app.results
```
It might take a while... We apologize! This will ensure faster processing speed when using the web app.

## Usage

Run the flask app:

on Mac:
```sh
FLASK_APP=web_app flask run
```
on Windows:
```sh
export FLASK_APP=web_app
flask run
```


## Testing

Running tests:

```sh
pytest

#in CI mode:
CI=true pytest
```

## [Deploying](/DEPLOYING.md)
Prerequisites:
Sign up for a Heroku account and install the Heroku CLI.

```sh
heroku login # only when you use heroku for the first time

heroku apps # at this time, results might be somewhat empty
```

Server Setup:
IMPORTANT: run the following commands from the root directory of your repository!
Use the online Heroku Dashboard or the command-line (instructions below) to create a new application server, specifying a unique name (e.g. "notification-app-123", but yours will need to be different):
```sh
heroku create notification-app-123 # choose your own name
```
Verify the app has been created:
```sh
heroku apps
```
Verify this step has associated the local repo with a remote address called "heroku":
```sh
git remote -v
```

Deploying:
After this configuration process is complete, you are finally ready to "deploy" the application's source code to the Heroku server.
```sh
git push heroku main
```



