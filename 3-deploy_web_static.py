#!/usr/bin/python3
""" based on do pack and do deploy create and distribute an archive to
web servers
"""
from os.path import exists
from fabric.api import *
from datetime import datetime

env.use_ssh_config = True
env.hosts = ['52.86.27.65', '100.25.13.63']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/school'


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


def deploy():
    """create and distribute archive"""
    archive_path = do_pack()
    if not archive_path:
        return False
    return do_deploy(archive_path)
