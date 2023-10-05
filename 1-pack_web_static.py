#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from the contents
"""
from datetime import datetime
from fabric.api import local
from fabric.decorators import runs_once
import os

@runs_once
def do_pack():
    """Generates a .tgz archive from the contents"""
    local("mkdir -p versions")
    path = ("versions/web_static_{}.tgz"
            .format(datetime.strftime(datetime.now(), "%Y%m%d%H%M%S")))
    result = local("tar -cvzf {} web_static"
                   .format(path))

    if result.failed:
        return None
    return path
