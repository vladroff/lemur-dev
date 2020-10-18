.PHONY: init-lemur

init-lemur-db:
	docker-compose exec -w /app/lemur backend lemur init -p password

start-lemur:
	docker-compose up

lemur-cert-volume:
	tar -C ./certs -c -f- . | docker run --rm -i -v lemur_certs:/certs alpine tar -C /certs -xv -f-