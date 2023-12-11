#!/usr/bin/python3
import os.path
from datetime import datetime
from fabric.api import env
from fabric.api import local
from fabric.api import put
from fabric.api import run
from fabric.api import runs_once

env.hosts = ['52.86.177.160', '34.229.69.158']
env.user = 'ubuntu'
env.key = '~/.ssh/id_rsa'


@runs_once 
#This makes sure that the packing is done only once for both servers
def do_pack():
    """Create a tar gzipped archive of the directory web_static."""
    dt = datetime.utcnow()
    archive_path = "versions/web_static_{}{}{}{}{}{}.tgz".format(dt.year,
                                                         dt.month,
                                                         dt.day,
                                                         dt.hour,
                                                         dt.minute,
                                                         dt.second)
    if os.path.isdir("versions") is False:
        if local("mkdir -p versions").failed is True:
            return None
    if local("tar -cvzf {} web_static".format(archive_path)).failed is True:
        return None
    return archive_path
'''
This is because your do_deploy is supposed to call on the variable 'archive_path' returned from `do_pack` but your `do_pack` returned 'file' instead.
'''


def do_deploy(archive_path):
    """Distributes an archive to a web server.

    Args:
        archive_path (str): The path of the archive to distribute.
    Returns:
        If the file doesn't exist at archive_path or an error occurs - False.
        Otherwise - True.
    """
    if os.path.isfile(archive_path) is False:
        return False
    file = archive_path.split("/")[-1]
    name = file.split(".")[0]
    ...
