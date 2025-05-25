import os

from fabric import Connection

env.user = os.getenv("SSH_USER")
env.password = os.getenv("SSH_PASSWORD")
env.sudo_password = os.getenv("SUDO_PASSWORD")


def show_dir():
    run("ls")


def mk_dir():
    run("mkdir -p test")  # -p evita errores si el directorio existe


def rm_dir():
    sudo("rm -rf test")
