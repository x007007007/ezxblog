from fabric.api import run, env, roles

env.hosts = ['main']
env.passwords = {
    'main': "ubuntu@xuxingci.com:22"
}

env.roledefs = {
    'db': ['main',],
    'web': ['main',],
    'linux': ['main']
}


@roles("linux")
def taskA():
    run('ls')

@roles("linux")
def taskB():
    run('whoami')