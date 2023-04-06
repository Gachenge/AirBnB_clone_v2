#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from the contents of the web_static
folder of your AirBnB Clone repo, using the function do_pack.
"""
from fabric.api import local
from datetime import datetime


def do_pack():
    """pack all web static into a tgz archive"""
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    file = "versions/web_static_{}.tgz".format(date)

    try:
        local("mkdir -p versions")
        local("tar -cvzf {} web_static/".format(file))
        return file
    except Exception:
        return None
