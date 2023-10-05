#!/usr/bin/python3
"""Deletes out-of-date archives"""
import os
from fabric.api import *

env.hosts = ["54.172.84.11', '18.210.17.119"]
env.user = 'ubuntu'
env.identity = '~/.ssh/school'

def do_clean(number=0):
    """Deletes out-of-date archives"""
    number = int(number)
