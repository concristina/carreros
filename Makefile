
bootstrap:
	python3 -m venv ./venv
	source ./venv/bin/activate
	pip install -r requirements.txt

build:
	docker-compose build

shell:
	docker-compose run backend /bin/ash
