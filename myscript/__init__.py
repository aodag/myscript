# -*- coding:utf-8 -*-
import os
import argparse
import json
from .projects import Project


PROJECT_FILENAME = 'project.json'


def init_commannd():
    basedir = os.getcwd()
    name = input("name: ")
    project = Project(name, basedir)
    print(project.todict())

    with open(os.path.join(basedir, PROJECT_FILENAME), "w") as f:
        json.dump(project.todict(), f)


def main():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers()
    init_parser = subparsers.add_parser("init")
    init_parser.set_defaults(func=init_commannd)
    args = vars(parser.parse_args())
    func = args.pop("func")
    func(**args)
