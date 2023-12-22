#!/usr/bin/python3
"""
a fabric script that distributes an archive to the web servers
using the function do_deploy
"""

from os.path import exists
from fabric.api import run, env, put

env.hosts = ['100.26.169.125', '52.207.134.230']


def do_deploy(archive_path):
    """
    a function that distributes an archive to the web server
    """

    if exists(archive_path) is False:
        return False

    try:
        path_file = archive_path.split("/")[-1]
        file_no_extn = path_file.split(".")[0]

        path = '/data/web_static/releases/'
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(path, file_no_extn))
        run('tar -xzf /tmp/{} -C {}{}'.format(path_file, path, file_no_extn))
        run('rm /tmp/{}'.format(path_file))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, file_no_extn))
        run('rm -rf {}{}/web_static'.format(path, file_no_extn))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path, file_no_extn))
        print("New version deployed!")
        return True

    except Exception:
        return False
