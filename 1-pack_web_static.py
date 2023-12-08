#!/usr/bin/python3

"""
a fabric script that generates a .tgz archive from the contents of the
web_static folder of AirBnB clone repo using the function do_pack
"""
from fabric.api import local
from datetime import datetime
import os
from collections.abc import Mapping


def do_pack():
    """ a function used to generate a .tgz archive """
    if not os.path.exists('versions'):
        local('mkdir -p versions')

    tim = datetime.utcnow().strftime('%Y%m%d%H%M%S')
    arch_name = 'versions/web_static_{}.tgz'.format(tim)

    outp = local('tar -cvzf {} web_static'.format(arch_name), capture=True)

    if result.succeeded:
        print('Packing web_static to {}'.format(arch_name))
        return arch_name
    else:
        return None
