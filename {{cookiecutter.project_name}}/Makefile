# Makefile for {{cookiecutter.project_name}}
all: run

rebuild_venv:
	rm -rf venv
	make venv

venv:
	test -d venv || virtualenv venv
	venv/bin/pip3 install -Ur requirements.txt
	venv/bin/pip3 install -Ur dev_requirements.txt

run: venv
	@echo "Running {{cookiecutter.project_name}}..."

check: test

test: venv
	@venv/bin/python3 -m nose -s

lint: venv
	@venv/bin/python3 -m pylint ./{{cookiecutter.project_name}}/*.py

