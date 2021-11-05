#!/bin/bash

# create blank Makefile and associated requirements file
touch Makefile
touch requirements.txt

#c create blank Dockerfile
touch Dockerfile

# create circleci folder and config file
mkdir .circleci

# pause
sleep 5s

cd .circleci
touch config.yml
