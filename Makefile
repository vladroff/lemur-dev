.PHONY: init-lemur

init-lemur:
	docker-compose exec -w /app/lemur backend lemur init -p password

start-lemur:
	docker-compose up

create-cert-volume:
	tar -C ./certs -c -f- . | docker run --rm -i -v lemur_certs:/certs alpine tar -C /certs -xv -f-