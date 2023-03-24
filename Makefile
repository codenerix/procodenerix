.PHONY: prepare
prepare:
	sudo apt-get -y install python3-pip python3-virtualenv

venv:
	-### Launching server...
	virtualenv -p python3 venv

.PHONY: requirements
requirements:
	(. ./venv/bin/activate && pip install -r requirements.txt)

.PHONY: test
test:
	(. ./venv/bin/activate && python -m pytest -s -vv )

.PHONY: dev
dev:
	(. ./venv/bin/activate && ./src/manage.py runserver )
