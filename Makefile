setup:
	python3 -m venv ~/.finance

install:
	pip install -r requirements.txt

test:
	python -m pytest -vv --cov=comprepo/*.py

lint:
	pylint --disable=R,C comprepo

all: install lint test
