#!/usr/bin/python3
"""
a fabric script that distributes an archive to the web servers
using the function do_deploy
"""

import os
from fabric.api import run, env, put

env.hosts = ["100.26.169.125", "52.207.134.230"]


def do_deploy(archive_path):
    """ a function that distributes an archive to web server """
    if not os.path.exists(archive_path):
        return False

    try:
        path_file = archive_path.split("/")[-1]
        file_no_extn = path_file.split(".")[0]

        put(archive_path, "/tmp/")
        uncompr_arch = "/data/web_static/releases/" + file_no_extn + "/"
        run("mkdir -p {}".format(uncompr_arch))
        run("tar -xzf /tmp/{} -C {}".format(file_no_extn, uncompr_arch))
        run("rm /tmp/{}".format(path_file))
        link = "/data/web_static/current"
        run("ln -s {} {}".format(uncompr_arch, link))
        print("New version deployed!")
        return True

    except Exception:
        return False
