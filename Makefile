VENV = environment
PYTHON = ${VENV}/bin/python3
PIP = ${VENV}/bin/pip

setup:
	python3 -m venv ${VENV}
	${PIP} install -r resources/dependencies/requirements.txt

clean:
	rm -rf __pycache__
	rm -rf .pytest_cache
	rm -rf ${VENV}
