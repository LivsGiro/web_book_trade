run:
	PYTHONPATH=$(pwd) python api/main.py

up_database:
	docker-compose --env-file .env up -d book_trade