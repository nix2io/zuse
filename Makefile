test:
	yarn --cwd ./tests/typescript run test
	cd ./tests/python & pipenv run test
docs:
	cd ./scripts/mk-docs & pipenv run build