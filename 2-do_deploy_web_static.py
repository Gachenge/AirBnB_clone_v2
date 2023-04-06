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
    put(archive_path, '/tmp')
    file = path.basename(archive_path)
    ext = path.splitext(file)[0]
    run('mkdir -p /data/web_static/releases/{}/'.format(ext))
    run('tar -xzf /tmp/{} -C /data/web_static/releases/{}/'.format(file, ext))
    run('rm -rf /tmp/{}'.format(file))
    run('sudo rm -rf /data/web_static/current')
    run('sudo ln -s /data/web_static/releases/{}/ /data/web_static/current'
        .format(ext))
    return True
