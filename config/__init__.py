import yaml


class Config:
    CONFIG_FILES_PATH = {
        "APP": "config/application.yml",
        "DB": "config/database.yml",
        "SECRET": "config/secret.yml",
        "CELERY": "config/celery.yml",
    }

    def __init__(self, env):
        try:
            self.ENV = env
            self.set_configs(self._app_configs())
            self.set_configs(self._db_configs())
            self.set_configs(self._secret_configs())
            self.set_configs(self._celery_configs())
        except FileNotFoundError as e:
            print(f"You need to create a configuration file in {e.filename}")

    def set_configs(self, configs):
        for key, value in configs.items():
            setattr(self, key, value)

    def _app_configs(self):
        with open(self.CONFIG_FILES_PATH["APP"]) as f:
            app_configs = yaml.load(f, Loader=yaml.Loader).get(self.ENV)
        return app_configs

    def _db_configs(self):
        with open(self.CONFIG_FILES_PATH["DB"]) as f:
            db_configs = yaml.load(f, Loader=yaml.Loader).get(self.ENV)

        db_configs["SQLALCHEMY_DATABASE_URI"] = self._sqlalchemy_database_uri(db_configs)
        return db_configs

    def _secret_configs(self):
        with open(self.CONFIG_FILES_PATH["SECRET"]) as f:
            secret_configs = yaml.load(f, Loader=yaml.Loader).get(self.ENV)

        return secret_configs

    def _celery_configs(self):
        with open(self.CONFIG_FILES_PATH["CELERY"]) as f:
            celery_configs = yaml.load(f, Loader=yaml.Loader).get(self.ENV)

        return celery_configs

    def _sqlalchemy_database_uri(self, db_configs):
        return 'mysql+pymysql://{0}:{1}@{2}:{3}/{4}'.format(
            db_configs["USERNAME"],
            db_configs["PASSWORD"],
            db_configs["HOST"],
            db_configs["PORT"],
            db_configs["DATABASE"]
        )
