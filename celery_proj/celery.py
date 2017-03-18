from __future__ import absolute_import
from celery import Celery

app = Celery('rss_contents', include=['celery_proj.tasks'])
app.config_from_object('celery_proj.config')
