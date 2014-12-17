# -*- coding:utf-8 -*-


class Project(object):
    def __init__(self, name, basedir):
        self.name = name
        self.basedir = basedir

    def todict(self):
        return {
            "name": self.name,
        }
