import os

from flask import current_app
from flask.cli import AppGroup
from sqlalchemy import create_engine

from app import db
from test.factories import RatingFactory

database_cli = AppGroup('database')


@database_cli.command('setup')
def setup():
    DatabaseCommand.create_db()
    DatabaseCommand.migrate()
    DatabaseCommand.seed()


@database_cli.command('reset')
def reset():
    DatabaseCommand.drop_db()
    DatabaseCommand.create_db()
    DatabaseCommand.migrate()
    DatabaseCommand.seed()


@database_cli.command('create')
def create():
    DatabaseCommand.create_db()


@database_cli.command('migrate')
def migrate():
    DatabaseCommand.migrate()


@database_cli.command('rollback')
def rollback():
    DatabaseCommand.rollback()


@database_cli.command('drop')
def drop():
    DatabaseCommand.drop_db()


@database_cli.command('seed')
def seed():
    DatabaseCommand.seed()


class DatabaseCommand:
    @classmethod
    def create_db(cls):
        print(f"CREATING DATABASE `{current_app.config['DATABASE']}`... ", end="")

        conn = cls.create_connection()
        conn.execute(f"CREATE DATABASE IF NOT EXISTS {current_app.config['DATABASE']}")
        conn.close()

        print('DONE')

    @classmethod
    def drop_db(cls):
        print(f"DROPPING DATABASE `{current_app.config['DATABASE']}`... ", end="")

        conn = cls.create_connection()
        conn.execute(f"DROP DATABASE IF EXISTS {current_app.config['DATABASE']}")
        conn.close()

        print('DONE')

    @classmethod
    def migrate(cls):
        print("MIGRATING")

        os.system('flask db upgrade')

        print("MIGRATION IS DONE")

    @classmethod
    def rollback(cls):
        print("ROLLING BACK")

        os.system('flask db downgrade')

        print("ROLLBACK IS DONE")

    @classmethod
    def seed(cls):
        print("SEEDING")

        cls.seed_ratings()

        print("SEED IS DONE")

    @classmethod
    def seed_ratings(cls):
        print("SEEDING RATINGS")

        ratings = RatingFactory.build_batch(10)

        db.session.bulk_save_objects(ratings)
        db.session.commit()

        print("SEED RATINGS IS DONE")

    @classmethod
    def create_connection(cls):
        engine = create_engine('mysql+pymysql://{0}:{1}@{2}:{3}'.format(
            current_app.config["USERNAME"],
            current_app.config["PASSWORD"],
            current_app.config["HOST"],
            current_app.config["PORT"]
        ))
        return engine.connect()
