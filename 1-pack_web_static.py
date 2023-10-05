#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from the contents
"""
from datetime import datetime
from fabric.api import local
import os

def do_pack():
    """Generates a .tgz archive."""
    try:
        now = dt.now()
        local("mkdir -p versions/")
        time_format = now.strftime("%Y%m%d%H%M%S")
        archive_name = "web_static_" + time_format + ".tgz"
        archive_path = os.path.join("versions", archive_name)
        return archive_path
    except Exception as e:
        return None
