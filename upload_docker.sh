#!/usr/bin/env bash
# This file tags and uploads an image to Docker Hub

# Assumes that an image is built via `run_docker.sh`

# Step 1:
# Create dockerpath
dockerpath="sarahlyne46/project4-sklearn"

# Step 2:  
# Authenticate & tag
docker login --username "sarahlyne46" && docker image tag api $dockerpath
echo "Docker ID and Image: $dockerpath"

# Step 3:
docker push $dockerpath