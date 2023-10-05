#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from the contents
"""
from datetime import datetime
from fabric.api import local
import os

def do_pack():
    """Generates a .tgz archive from the contents of the web_static folder"""
    try:
        # Create the versions directory if it doesn't exist
        local("mkdir -p versions")

        # Create the archive name
        archive_name = "web_static_" + datetime.now().strftime("%Y%m%d%H%M%S") + ".tgz"
        archive_path = "versions/" + archive_name

        # Compress the web_static folder into the archive
        local("tar -czvf {} web_static".format(archive_path))

        # Check if the archive has been correctly generated
        if local("test -f {}".format(archive_path)).succeeded:
            return archive_path
        else:
            return None
    except Exception as e:
        return None
