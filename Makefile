.PHONY: tests coverage coverage-html clean
APP=.
COV=howl
OPTS=-vs

help:
	@echo "tests - run tests"
	@echo "coverage - run tests with coverage enabled"
	@echo "coverage-html - run tests with coverage html export enabled"
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

docs: clean-build
	pip install -e .
	pip install -e [docs]
	sphinx-apidoc --force -o docs/source/modules/ howl howl/tests/
	$(MAKE) -C docs clean
	$(MAKE) -C docs html

clean-build:
	@rm -fr build/
	@rm -fr dist/
	@rm -fr *.egg-info src/*.egg-info
	@rm -fr htmlcov/
	$(MAKE) -C docs clean
