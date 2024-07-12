#!/usr/bin/python3
"""
This script distributes an archive to web servers
"""

from fabric.api import env, put, run
import os

env.hosts = ['54.158.211.229', '54.160.72.36']  # Replace with your web-01 and web-02 IPs

def do_deploy(archive_path):
    """
    Distributes an archive to the web servers
    """
    if not os.path.exists(archive_path):
        return False

    try:
        # Upload the archive to /tmp/ directory
        archive_name = archive_path.split("/")[-1]
        archive_folder = archive_name.split(".")[0]
        remote_tmp_path = "/tmp/{}".format(archive_name)
        put(archive_path, remote_tmp_path)

        # Uncompress the archive
        release_path = "/data/web_static/releases/{}".format(archive_folder)
        run("mkdir -p {}".format(release_path))
        run("tar -xzf {} -C {}".format(remote_tmp_path, release_path))

        # Remove the archive from the remote server
        run("rm {}".format(remote_tmp_path))

        # Move the content out of the extracted folder
        run("mv {}/web_static/* {}".format(release_path, release_path))
        run("rm -rf {}/web_static".format(release_path))

        # Remove the old symbolic link
        run("rm -rf /data/web_static/current")

        # Create a new symbolic link
        run("ln -s {} /data/web_static/current".format(release_path))

        return True
    except Exception as e:
        return False
