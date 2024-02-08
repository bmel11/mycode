#!/usr/bin/env python3

# import additional code to complete the task
import shutil
import os

def main():
    # move into working directory
    os.chdir('/home/student/mycode/')

    # copy files
    shutil.move('raynor.obj', 'ceph_storage/')

    # Prompt user for new name
    xname = input('What is the new name for kerrigan.obj? ')
    shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)

