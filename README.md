# Collocations API

## Setup Using Docker Environment

### Prerequisites

We need `Docker` and `Docker Compose` to be installed in advance.

### Prepare configurations

Copy, rename and reconfigure below files:

| File                | Sample                     | Meaning                                                                                   |
| ------------------- | -------------------------- | ----------------------------------------------------------------------------------------- |
| .env                | .env_sample                | Basic environment variables that mostly used by Docker/Docker Compose to connect services |
| config/database.yml | config/database_sample.yml | Database configurations                                                                   |
| config/secret.yml   | config/secret_sample.yml   | Secret keys                                                                               |

**Note:**
Please make sure that configurations on `config/database.yml` file need to match with environment `FLASK_ENV` and `MYSQL_*` configurations on `.env` file.

### Build and run

Run this command:

```bash
docker-compose up
```

## Setup using No Docker Environment

- Create database `collocations_db` and `collocations_db_test`

in your database server.

- Go to `config/database.yml` to change the config match your database settings.

- Create virtualenv `python3 -m venv venv` or `py -m venv venv`

- Install needed packages `source venv/bin/activate && pip install -r requirements.txt`

- Run migrate `flask db upgrade`

- Start application `flask run`

- Access `http://localhost:5000` for testing.

- Try run test with `pytest -v`

###
