.PHONY: init-lemur

init-lemur:
	docker-compose exec -w /app/lemur backend lemur init -p password

start-lemur:
	docker-compose up