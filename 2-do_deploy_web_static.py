#!/usr/bin/python3
"""
Fabric script based on the file 1-pack_web_static.py that distributes an
archive to the web servers
"""

from fabric.api import *
from os.path import exists
env.hosts = ['52.86.27.65', '100.25.13.63']


def do_deploy(archive_path):
    """distributes an archive to the web servers"""
    if exists(archive_path) is False:
        return False
    try:
        file = archive_path.split("/")[-1]
        ext = file.split(".")[0]
        path = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run('sudo mkdir -p {}{}/'.format(path, ext))
        run('sudo tar -xzf /tmp/{} -C {}{}/'.format(file, path, ext))
        run('sudo rm /tmp/{}'.format(file))
        run('sudo mv {0}{1}/web_static/* {0}{1}/'.format(path, ext))
        run('sudo rm -rf {}{}/web_static'.format(path, ext))
        run('sudo rm -rf /data/web_static/current')
        run('sudo ln -s {}{}/ /data/web_static/current'.format(path, ext))
        return True
    except Exception:
        return False
