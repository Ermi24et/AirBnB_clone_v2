#!/usr/bin/python3
"""
a fabric script that distributes an archive to the web servers
using the function do_deploy
"""

import os
from fabric.api import run, env, put

env.hosts = ["100.26.169.125", "52.207.134.230"]


def do_deploy(archive_path):
    """
    a function that distributes an archive to the web server
    """

    if not os.path.exists(archive_path):
        return False

    try:
        path_file = archive_path.split("/")[-1]
        file_no_extn = path_file.split(".")[0]

        put(archive_path, "/tmp/")
        uncompr_arch = "/data/web_static/releases/" + file_no_extn + "/"
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