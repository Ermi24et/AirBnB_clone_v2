#!/usr/bin/python3
"""
a fabric script that distributes an archive to the web servers
using the function do_deploy
"""

import os.path
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

    if not os.path.exists('versions'):
        local("mkdir -p versions")

    tim = datetime.utcnow().strftime('%Y%m%d%H%M%S')
    arch_name = 'versions/web_static_{}.tgz'.format(tim)

    outp = local('tar -cvzf {} web_static'.format(arch_name))

    if outp.succeeded:
        print('Packing web_static to {}'.format(arch_name))
        return arch_name
    else:
        return None


def do_deploy(archive_path):
    """ disributes an archive """
    if not os.path.exists(archive_path):
        return False

    try:
        path_file = archive_path.split("/")[-1]
        file_no_extn = path_file.split(".")[0]

        uncompr_arch = "/data/web_static/releases/" + file_no_extn + "/"
        put(archive_path, "/tmp/")
        run("mkdir -p {}".format(uncompr_arch))
        run("tar -xzf /tmp/{} -C {}".format(path_file, uncompr_arch))
        run("rm /tmp/{}".format(path_file))
        run("mv {}web_static/* {}".format(uncompr_arch, uncomr_arch))
        run("rm -rf {}web_static".format(uncompr_arch))
        link = "/data/web_static/current"
        run("rm -rf {}".format(link))
        run("ln -s {} {}".format(uncompr_arch, link))
        print("New version deployed!")
        return True

    except Exception:
        return False
