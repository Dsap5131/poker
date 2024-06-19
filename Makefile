VENV = environment
PYTHON = ${VENV}/bin/python3
PIP = ${VENV}/bin/pip

setup: clean
	python3 -m venv ${VENV}
	${PIP} install -r resources/dependencies/requirements.txt

clean:
	rm -rf .pytest_cache
	rm -rf ${VENV}
	rm -rf .coverage
	find . -depth -name '__pycache__' -type d -exec rm -r "{}" \;
	rm -rf htmlcov

lint: setup	
	${VENV}/bin/pylint src/ --exit-zero
	${VENV}/bin/pylint testing/ --exit-zero

just_lint:	
	${VENV}/bin/pylint src/ --exit-zero
	${VENV}/bin/pylint testing/ --exit-zero

test: lint
	${VENV}/bin/coverage run -m pytest testing/
	${VENV}/bin/coverage report -m

just_test:	
	${VENV}/bin/coverage run -m pytest testing/
	${VENV}/bin/coverage report -m
