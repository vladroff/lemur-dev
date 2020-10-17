# Lemur Development

Repo helps with development of [Lemur](https://github.com/Netflix/lemur) and [lemur-ejbca-plugin](https://github.com/c2company/lemur-ejbca-plugin).

After cloning the repo, to populate submodules run:

```shell script
git submodule update --init
```

You need to have `Docker` and `docker-compose` installed.

Lemur default credentials: `lemur`:`password`

To start Lemur, run:

```shell script
make start-lemur
```

To initialize Lemur database, run:

```shell script
make init-lemur
```

Open browser at `http://localhost:3000`