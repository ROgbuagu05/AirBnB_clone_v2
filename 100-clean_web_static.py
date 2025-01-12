#!/usr/bin/python3
"""Deletes out-of-date archives"""
import os
from fabric.api import *

env.hosts = ["54.172.84.11', '18.210.17.119"]
env.user = 'ubuntu'
env.identity = '~/.ssh/school'

def do_clean(number=0):
    """
    Deletes out-of-date archives

    Args:
    number (int): The number of archives to keep.

    If number is 0 or 1, keeps only the most recent archive. If
    number is 2, keeps the most and second-most recent archives,
    etc.
    """
    number = 1 if int(number) == 0 else int(number)

    archives = sorted(os.listdir("versions"))
    [archives.pop() for i in range(number)]
