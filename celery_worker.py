import os

from app import celery, create_app
from app.extensions.celery_utils import init_celery

app = create_app(os.getenv("FLASK_ENV") or "development")

init_celery(celery, app)
