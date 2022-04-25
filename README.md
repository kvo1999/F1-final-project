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

