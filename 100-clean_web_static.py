#!/usr/bin/python3
"""
This script generates and distributes an archive to web servers
and cleans up old archives
"""

from fabric.api import env, run, local, lcd
import os

env.hosts = ['54.158.211.229', '54.160.72.36']  # Replace with your web-01 and web-02 IPs

def do_clean(number=0):
    """
    Deletes out-of-date archives.
    Arguments:
    number (int): The number of archives to keep.
    If number is 0 or 1, keep only the most recent version of your archive.
    If number is 2, keep the most recent and second most recent versions of your archive, etc.
    """
    number = 1 if int(number) == 0 else int(number)

    # Local cleanup
    archives = sorted(os.listdir("versions"))
    [archives.pop() for _ in range(number)]
    with lcd("versions"):
        [local("rm ./{}".format(a)) for a in archives]

    # Remote cleanup
    for host in env.hosts:
        with cd("/data/web_static/releases"):
            archives = run("ls -tr").split()
            archives = [a for a in archives if "web_static_" in a]
            [archives.pop() for _ in range(number)]
            [run("rm -rf ./{}".format(a)) for a in archives]

