.PHONY: tests coverage coverage-html devinstall docs clean
APP=.
COV=howl
OPTS=-vs

help:
	@echo "tests - run tests"
	@echo "coverage - run tests with coverage enabled"
	@echo "coverage-html - run tests with coverage html export enabled"
	@echo "devinstall - install all packages required for development"
	@echo "docs - generate Sphinx HTML documentation, including API docs"
	@echo "clean - Clean build related files"


tests:
	py.test ${OPTS} ${APP}


coverage:
	py.test ${OPTS} --cov=$(COV) --cov-report=term-missing $(APP)


coverage-html:
	py.test ${OPTS} --cov=$(COV) --cov-report=term-missing --cov-report=html $(APP)


devinstall:
	pip install -e .
	pip install -e .[tests]
	pip install -e .[docs]

docs: clean
	$(MAKE) -C docs html

clean:
	rm -fr build/
	rm -fr dist/
	rm -fr *.egg-info
	rm -fr htmlcov/
	$(MAKE) -C docs clean
