#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from the contents
"""
from datetime import datetime
from fabric.api import local
import os

def do_pack():
    """Generates a .tgz archive from the contents"""
    now = datetime.now().strftime("%Y%m%d%H%M%S")
    local("mkdir -p versions")
    result = local("tar -czvf versions/web_static_{}.tgz web_static"
                   .format(now))
    if result.failed:
        return None
    else:
        return result

if __name__ == "__main__":
    do_pack()
