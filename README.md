# JamTogether!

The goal of JamTogether! is to bring musicians together and let them jam!

Our service lets band members pick music to jam on and keeps everyone else's devices
in sync. We will host some sheet music, but we also want to work with other sheet music
providers to share their libraries on this platform so their users can jam.

# Developer Setup

## Prerequisites

1. Python (v3.12 recommended)

## Setup Steps

After cloning this repository, run these commands to set up the development environment:

```bash
# Set up a Python virtualenv
python -m venv env
source env/bin/activate         # Windows: env\Scripts\Activate.bat

# Install necessary packages
pip install -r requirements-dev.txt

# Set up the database
python manage.py migrate

# Collect static files
python manage.py collectstatic --noinput

# Start the development server
daphne -p 8000 jamtogether.asgi:application
```
