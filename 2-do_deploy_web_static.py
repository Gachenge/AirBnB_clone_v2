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
    file = archive_path.split('/')[-1]
    ext = '/data/web_static/releases/{}'.format(file.split('.')[0])
    tmp = 'tmp' + file
    try:
        put(archive_path, "/tmp/")
        run('mkdir -p {}/'.format(ext))
        run('tar -xzf {} -C {}/'.format(tmp, ext))
        run("rm -rf {}".format((tmp)))
        run("mv {}/web_static/* {}/".format(ext, ext))
        run("rm -rf {}/web_static".format(ext))
        run("rm -rf /data/web_static/current")
        run("ln -s {}/ /data/web_static/current".format(ext))
        return True
    except Exception:
        return False
