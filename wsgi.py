# coding=utf-8
import os
import logging

from app import create_app, celery

logger = logging.getLogger(__name__)

application = create_app(os.getenv("FLASK_ENV") or "development", celery=celery)

if __name__ == '__main__':
    application.run()
