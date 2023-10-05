#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from the contents
"""
from datetime import datetime
from fabric.api import local, settings
import os

def do_pack():
    """Generates a .tgz archive from the contents"""
    datetime_now = datetime.utcnow().strftime("%Y%m%d%H%M%S")
    archive_path = "versions/web_static_{}.tgz".format(datetime_now)
    cmd_compress = "tar -cvzf {} web_static/".format(archive_path)
    local("mkdir -p versions")
    with settings(warn_only=True):
        result = local(cmd_compress, capture=True)
    if result.failed:
        return None
    return archive_path
