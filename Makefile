.PHONY: init-lemur start-lemur lemur-cert-volume

help: ## Show this help
	@egrep '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

init-lemur-db: ## Initializes Lemur database, run it only once, the fist time starting Lemur
	docker-compose exec -w /app/lemur backend lemur init -p password

start-lemur: ## Start lemur (frontend, backend, postgres, redis)
	docker-compose up

lemur-cert-volume: ## Create named docker volume, that contains all certificates required by lemur plugins, see paths in lemur.conf.py
	tar -C ./certs -c -f- . | docker run --rm -i -v lemur_certs:/certs alpine tar -C /certs -xv -f-