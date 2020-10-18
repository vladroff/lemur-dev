# Lemur Development

Repo helps with development of [Lemur](https://github.com/Netflix/lemur) and [lemur-ejbca-plugin](https://github.com/c2company/lemur-ejbca-plugin).

After cloning the repo, to populate submodules run:

```shell script
git submodule update --init
```

You need to have `Docker` and `docker-compose` installed.

Lemur default credentials: `lemur`:`password`

## Setup

### Init EJBCA certs
Create docker volume with certificates required by EJBCA plugin.

1. Place all certificates in `./certs/lemur_ejbca` directory.
2. Run `make lemur-cert-volume`
3. Volume will be mounted to `/usr/share/loca/certs` 
4. Lemur config `lemur.conf.py` has hardcoded paths to EJBCA certificates.

# Run

To start Lemur, run:

```shell script
make start-lemur
```

### Init DB

To initialize Lemur database, run:

```shell script
make init-lemur-db
```


Open browser at `http://localhost:3000`