#!/usr/bin/python3
import os
from fabric.api import *

env.hosts = ['52.86.177.160', '34.229.69.158']

def do_clean(number=0):
    """Del out-of-date archives

    args:
        numb (int): the number of archives to keep

    if number is 0 or 1, keeps only the most recent arch
    if num is 2, keeps the sec-most recent archs
    """
    number = 1 if int(number) == 0 else int(number)

    archives = sorted(os.listdir("versions"))
    [archives.pop() for i in range(number)]
    with lcd("version"):
        [local("rm ./{}".format(a)) for a in archives]

    with cd("/data/web_static/releases"):
        arhives = run("ls -tr").split()
        archives = [a for a in archives if "web_static_" in a]
        [archives.pop() for i in range(number)]
        [run("rm -rf ./{}".format(a)) for a in archives]
