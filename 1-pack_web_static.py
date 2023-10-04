#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from the contents of the
web_static folder of your AirBnB Clone repo , using the function do_pack.
"""
from datetime import datetime
from fabric.api import local
import os

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
