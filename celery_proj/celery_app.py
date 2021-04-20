from __future__ import absolute_import

from celery import Celery
from celery_proj.tasks import MLTask

app = Celery('celery_proj',
             broker="redis://",
             backend="redis://",
             include=['celery_proj.tasks'])


predict_task = app.register_task(MLTask)  

if __name__ == '__main__':
    app.start()
