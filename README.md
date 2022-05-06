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


## Configuration

Set environment variables using a ".env" file approach:

```sh
touch .env
echo KEY="..." >> .env

```

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

###
#start with drop downs, driver names, statistics 
form with 2 drop downs and submission button 
#form will have method of post and action of some kind of route 
#set up another route to handle form data 
#route we send data to will make request to API for given name & characteristic 
#get data back 
#that route will render another page
#pass driver data to page (FROM FUNCTIONS)

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

Running the Script in Production:
Once you've deployed the source code to the Heroku server, login to the server to see the files there, and take an opportunity to test your ability to run the script that now lives on the server.

```sh
heroku run bash # login to the server
# ... whoami # see that you are not on your local computer anymore
# ... ls -al # optionally see the files, nice!
# ... python -m app.daily_briefing # see the output, nice!
# ... exit # logout
```


