#!/usr/bin/python3
"""
This script generates and distributes an archive to web servers
"""

from fabric.api import env, put, run, local
from datetime import datetime
import os

env.hosts = ['54.158.211.229', '54.160.72.36']  # Replace with your web-01 and web-02 IPs

def do_pack():
    """
    Generates a .tgz archive from the contents of the web_static folder.
    Returns the archive path if the archive has been correctly generated.
    Otherwise, returns None.
    """
    try:
        if not os.path.exists("versions"):
            os.makedirs("versions")

        now = datetime.now()
        archive_name = "versions/web_static_{}.tgz".format(now.strftime("%Y%m%d%H%M%S"))
        local("tar -cvzf {} web_static".format(archive_name))
        return archive_name
    except Exception as e:
        return None

def do_deploy(archive_path):
    """
    Distributes an archive to the web servers
    """
    if not os.path.exists(archive_path):
        return False

    try:
        archive_name = archive_path.split("/")[-1]
        archive_folder = archive_name.split(".")[0]
        remote_tmp_path = "/tmp/{}".format(archive_name)
        put(archive_path, remote_tmp_path)
        release_path = "/data/web_static/releases/{}".format(archive_folder)
        run("mkdir -p {}".format(release_path))
        run("tar -xzf {} -C {}".format(remote_tmp_path, release_path))
        run("rm {}".format(remote_tmp_path))
        run("mv {}/web_static/* {}".format(release_path, release_path))
        run("rm -rf {}/web_static".format(release_path))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(release_path))
        return True
    except Exception as e:
        return False

def deploy():
    """
    Packs and deploys the web_static content to web servers
    """
    archive_path = do_pack()
    if not archive_path:
        return False
    return do_deploy(archive_path)
