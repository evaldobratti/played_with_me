
from huey.djhuey import crontab, periodic_task, task

@task()
def aff(param):
    print 'lol'
    return 'a'
