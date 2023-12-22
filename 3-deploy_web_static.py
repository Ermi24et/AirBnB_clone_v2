#!/usr/bin/python3
"""
a fabric script that distributes an archive to the web servers
using the function do_deploy
"""

from os.path import exists, isdir
from fabric.api import run, env, put, local
from datetime import datetime

env.hosts = ["100.26.169.125", "52.207.134.230"]


def deploy():
    """ distributing and creating an archive """
    path_file = do_pack()
    if path_file is None:
        return False
    return do_deploy(path_file)


def do_pack():
    """ generate a tar archive """

    try:
        tim = datetime.now().strftime("%Y%m%d%H%M%S")
        if isdir("versions") is False:
            local("mkdir -p versions")
        arch_name = "versions/web_static_{}.tgz".format(tim)

        local('tar -cvzf {} web_static'.format(arch_name))
        print('Packing web_static to {}'.format(arch_name))
        return arch_name
    except Exception:
        return None


def do_deploy(archive_path):
    """ disributes an archive """
    if exists(archive_path) is False:
        return False

    try:
        path_file = archive_path.split("/")[-1]
        file_no_extn = path_file.split(".")[0]

        path = "/data/web_static/releases/"
        put(archive_path, "/tmp/")
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
