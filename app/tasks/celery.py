from app import celery


@celery.task()
def run_tasks():
    print("Celery Task Run")
    print("done")
    return "OK"
