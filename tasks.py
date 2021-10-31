from invoke import Task
from invoke.tasks import task

@task
def start(ctx):
    ctx.run("python3 koodi/main.py")