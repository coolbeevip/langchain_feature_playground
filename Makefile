init:
	@pip install -e .

test: init style
	@nosetests tests

style:
	flake8 .

clean:
	@rm -rf dist

release: clean test
	@python -m flit build

run: init
	@python main.py -H 0.0.0.0 -P 5000 --debug
