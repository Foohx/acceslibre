.PHONY: messages
messages:
	python3 manage.py makemessages --ignore=node_modules --all --no-location
	django-admin makemessages -d djangojs --all --pythonpath=/home/mlaure/dev/acceslibre --ignore=node_modules --no-location
