#!/usr/bin/env bash
# Restarts the HolbertonnBnB WSGI application servers
pkill gunicorn
gunicorn --bind 0.0.0.0:5001 web_flask.hbnb:app --daemon
gunicorn --bind 0.0.0.0:5002 api.v1.app:app --daemon
