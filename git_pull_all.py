#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Script: git_pull_all.py
# Created by: Evgeny Sidorov
# Date: 2023-06-15
# Purpose: This script performs 'git pull --all' command in each directory.

import os
import sys

def git_pull_all(base_dir):
    # Get a list of all subdirectories in the specified directory
    subdirs = [name for name in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, name))]

    # Iterate through each subdirectory and execute 'git pull --all' command
    for subdir in subdirs:
        dir_path = os.path.join(base_dir, subdir)
        if os.path.exists(os.path.join(dir_path, '.git')):
            os.chdir(dir_path)
            print("⚡ ➡️ Executing 'git pull --all' in directory:", dir_path)
            os.system('git pull --all')
            os.chdir(base_dir)

    print("All 'git pull --all' operations completed.")

if __name__ == "__main__":
    if len(sys.argv) == 1:
        base_dir = os.getcwd()
    elif len(sys.argv) == 2:
        base_dir = sys.argv[1]
        if not os.path.isdir(base_dir):
            print("The specified directory does not exist.")
            sys.exit(1)
    else:
        print("Usage: python git_pull_all.py <directory_path>")
        sys.exit(1)

    git_pull_all(base_dir)