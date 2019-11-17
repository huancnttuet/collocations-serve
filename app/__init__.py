# coding=utf-8
import logging

from flask import Flask
from flask_restplus import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from celery import Celery
from flask_cors import CORS

from app.extensions.celery_utils import init_celery

logger = logging.getLogger(__name__)

db = SQLAlchemy()


def make_celery(app_name=__name__):
    from config import Config
    import os
    load_env = os.getenv("FLASK_ENV") or "development"
    load_config = Config(load_env)
    return Celery(app_name, backend=load_config.CELERY_RESULT_BACKEND, broker=load_config.CELERY_BROKER_URL)


celery = make_celery()


def create_app(env, **kwargs):
    from config import Config
    from app.routes import register_routes
    from app.error_handlers import register_error_handler
    from commands import register_commands

    app = Flask(__name__)
    cors = CORS(app)
    app.config['CORS_HEADERS'] = 'Content-Type'

    if kwargs.get("celery"):
        init_celery(kwargs.get("celery"), app)
    app.config.from_object(Config(env))
    app.config.from_envvar("USI_CONFIG", silent=True)

    register_error_handler(app)

    api = Api(app, title='User Service API', version='0.0.1')

    register_routes(api, app)

    db.init_app(app)

    Migrate(app, db)

    register_commands(app)

    return app
