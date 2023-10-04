#!/usr/bin/python3
"""
A script that creates and distributes an archive to your web servers
"""
import os.path
from datetime import datetime
from fabric.api import env
from fabric.api import local
from fabric.api import put
from fabric.api import run

env.hosts = ['54.172.84.11', '18.210.17.119']
env.user = 'ubuntu'

def do_pack():
    """Generates a .tgz archive."""
    datetime_now = datetime.utcnow().strftime("%Y%m%d%H%M%S")
    archive_path = "versions/web_static_{}.tgz".format(datetime_now)
    cmd_compress = "tar -cvzf {} web_static/".format(archive_path)
    local("mkdir -p versions")
    archived = local(cmd_compress)
    if archived.failed:
        return None
    return archive_path

def do_deploy(archive_path):
    """Distributes an archive to your web servers

    Args:
        archive_path (str): The path of the archive to distribute.
    Returns:
        If the file doesn't exist at archive_path or an error occurs - False.
        Otherwise - True.
    """
    if os.path.isfile(archive_path) is False:
        return False
    file = archive_path.split("/")[-1]
    name = file.split(".")[0]

    if put(archive_path, "/tmp/{}".format(file)).failed is True:
        return False
    if run("rm -rf /data/web_static/releases/{}/".
           format(name)).failed is True:
        return False
    if run("mkdir -p /data/web_static/releases/{}/".
           format(name)).failed is True:
        return False
    if run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".
           format(file, name)).failed is True:
        return False
    if run("rm /tmp/{}".format(file)).failed is True:
        return False
    if run("mv /data/web_static/releases/{}/web_static/* "
           "/data/web_static/releases/{}/".format(name, name)).failed is True:
        return False
    if run("rm -rf /data/web_static/releases/{}/web_static".
           format(name)).failed is True:
        return False
    if run("rm -rf /data/web_static/current").failed is True:
        return False
    if run("ln -s /data/web_static/releases/{}/ /data/web_static/current".
           format(name)).failed is True:
        return False
    return True

def deploy():
    """Creates and distributes an archive to your web servers"""
    file = do_pack()
    if file is None:
        return False
    return do_deploy(file)
