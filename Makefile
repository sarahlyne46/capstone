setup:
	# Create python virtualenv & source it
	python3 -m venv ~/.devops
#	source ~/.devops/bin/activate
	
install:
	# This should be run from inside a virtualenv
	pip install --upgrade pip && pip install -r requirements.txt
	# wget -O /bin/hadolint https://github.com/hadolint/hadolint/releases/download/v1.16.3/hadolint-Linux-x86_64 && chmod +x /bin/hadolint


env:
	#Show information about environment
	which python3
	python3 --version
	which pytest
	which pylint
	
test:
	# Additional, optional, tests could go here
	#python -m pytest -vv --cov=myrepolib tests/*.py
	#python -m pytest --nbval notebook.ipynb

lint:
	# See local hadolint install instructions:   https://github.com/hadolint/hadolint
	# This is linter for Dockerfiles
	hadolint Dockerfile
	# This is a linter for Python source code linter: https://www.pylint.org/
	# This should be run from inside a virtualenv
	pylint --disable=R,C,W1203 app.py

all: install env lint
