#!/bin/bash
clear
echo "Warming up the dev server"
echo "initializing the database"
python run.py db init
echo "creating the first migration"
python run.py db migrate
echo "upgrading to the first migration"
python run.py db upgrade

