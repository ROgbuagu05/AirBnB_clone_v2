#!/usr/bin/python3
"""A script that distributes an archive to your web servers"""

from fabric.api import *
from fabric.operations import put, run
from datetime import datetime
import os

env.hosts = ['54.172.84.11', '18.210.17.119']
env.user = 'ubuntu'

def do_deploy(archive_path):
    """Distributes an archive to your web servers.

    Returns:
        (bool): `True` if all operations successful, `False` otherwise
    """
    if archive_path is None or not os.path.exists(archive_path):
        return False

    f_name = path.basename(archive_path)
    d_name = f_name.split('.')[0]

    put(local_path=archive_path, remote_path='/tmp/')
    run('mkdir -p /data/web_static/releases/{}/'.format(d_name))
    run('tar -xzf /tmp/{} -C /data/web_static/releases/{}/'.format(
        f_name, d_name))
    run('rm /tmp/{}'.format(f_name))
    run('mv /data/web_static/releases/{}/web_static/* '.format(d_name) +
        '/data/web_static/releases/{}/'.format(d_name))
    run('rm -rf /data/web_static/releases/{}/web_static'.format(d_name))
    run('rm -rf /data/web_static/current')
    run('ln -s /data/web_static/releases/{}/ /data/web_static/current'.format(
        d_name))

    return True
