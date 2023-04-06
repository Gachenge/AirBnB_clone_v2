#!/usr/bin/python3
"""
script to distribute an archive to web servers
based on 1-pack_web
"""
from fabric.api import *
from os import path

env.hosts = ['54.144.197.148', '52.204.61.125']


def do_deploy(archive_path):
    """deploy web static to the servers"""
    if not path.exists(archive_path):
        return False

    try:
        put(archive_path, '/tmp/')
        file = path.split("/")[-1]
        ext = file.split(".")[0]
        path = "/data/web_static/releases/"
        run('mkdir -p {}{}'.format(path, ext))
        run('tar -xzf /tmp/{} -C {}{}/'.format(file, path, ext))
        run(f'mv {path}{ext}/web_static/* {path}{ext}/')
        run('ln -sf {}{}/ /data/web_static/current'.format(path, ext))
        run('rm -rf /tmp/{}'.format(file))
        run('rm -rf {}{}/web_static'.format(path, ext))
        return True
    except Exception:
        return False
