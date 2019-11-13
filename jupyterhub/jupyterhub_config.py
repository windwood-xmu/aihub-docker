import os

## Generic
c.JupyterHub.admin_access = True
#c.Spawner.default_url = '/lab'

## Authenticator
c.JupyterHub.authenticator_class = 'jupyterhub.auth.DummyAuthenticator'
c.DummyAuthenticator.password = 'xmu2019'

c.Authenticator.whitelist = {
        'a01',
        'a02',
        'a03',
        }

c.Authenticator.admin_users = { 'aihub' }


## Docker spawner
c.JupyterHub.spawner_class = 'dockerspawner.DockerSpawner'
c.DockerSpawner.image = os.environ['DOCKER_JUPYTER_CONTAINER']
c.DockerSpawner.network_name = os.environ['DOCKER_NETWORK_NAME']
# See https://github.com/jupyterhub/dockerspawner/blob/master/examples/oauth/jupyterhub_config.py
c.JupyterHub.hub_ip = os.environ['HUB_IP']


## Services
c.JupyterHub.services = [
    {
        'name': 'cull_idle',
        'admin': True,
        'command': 'python /srv/jupyterhub/cull_idle_servers.py --timeout=3600'.split(),
    },
]
