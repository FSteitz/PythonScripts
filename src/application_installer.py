#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
Copyright 2016 Florian Steitz

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

  http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
"""

Installs a standard set of applications via the command line and performs further administration
tasks.

This script only works correctly on Ubuntu 16.04 and later.
"""

from subprocess import call, Popen, PIPE
from config import GIT_USERNAME, GIT_EMAIL


#=========================#
# Definition of functions #
#=========================#
def define_application_list():
    """
    Defines a list of applications to install. The flag indicates whether an application shall be
    installed or not
    """

    application_list = [
        # Applications with a graphical user interface
        ["blender", True],
        ["ca-certificates", True],
        ["cherrytree", True],
        ["chromium-browser", True],
        ["chromium-codecs-ffmpeg-extra", True],
        ["deluge", True],
        ["firefox", True],
        ["gimp", True],
        ["hunspell", True],
        ["hunspell-de-de-frami", True],
        ["inkscape", True],
        ["libreoffice", True],
        ["keepass2", True],
        ["meld", True],
        ["pidgin", True],
        ["steam", True],
        ["telegram-purple", True],  # Currently requires a PPA, e.g. ppa:nilarimogard/webupd8
        ["texlive", True],
        ["texlive-lang-german", True],
        ["texmaker", True],
        ["uget", True],
        ["virtualbox", True],
        ["virtualbox-guest-additions-iso", True],
        ["vlc", True],
        ["wireshark", True],
        ["xsane", True],

        # Applications without a graphical user interface
        ["apache2", True],
        ["curl", True],
        ["gdb", True],
        ["git", True],
        ["gvfs-backends", True],
        ["gcc", True],
        ["g++", True],
        ["nano", True],
        ["npm", True],
        ["openjdk-8-doc", True],
        ["openjdk-8-jdk", True],
        ["openjdk-8-source", True],
        ["python3", True],
        ["python3-pip", True],
        ["ruby", True],
        ["ruby-dev", True],
        ["ssh", True]
    ]

    return application_list


def execute_process(process):
    """ Executes a shell command and prints its ouput """

    return_code = None

    while return_code is None:
        # Checks whether the child process has terminated
        return_code = process.poll()
        line = process.stdout.readline()

        print line,


def install_applications(*application_list):
    """ Iterates over all applications and installs them """

    for application in application_list:
        if application[1]:
            execute_process(Popen("apt-get install -y " + application[0], stdout=PIPE, shell=True))

        print "-" * 60


#==================#
# Script execution #
#==================#
print "Initializing..."
APPLICATION_LIST = define_application_list()
print "Installing applications..."

if APPLICATION_LIST is not None:
    print "Total: ", len(APPLICATION_LIST)
    install_applications(*APPLICATION_LIST)

    print "Removing unused packages..."
    call("apt-get autoremove -y", shell=True)

    print "Cleaning local repository..."
    call("apt-get clean -y", shell=True)
else:
    print "Error: No applications defined"

print "Configuring applications..."
call("git config --global user.name \"%s\"" % GIT_USERNAME, shell=True)
call("git config --global user.email \"%s\"" % GIT_EMAIL, shell=True)
