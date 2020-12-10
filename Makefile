test:
	yarn --cwd ./tests/typescript run test
	cd ./tests/python & pipenv run test