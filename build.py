# -*- coding: utf-8 -*-

import os
import os.path
import re

from shutil import copyfile


class Go:
    src_path = '.pkg/LeetCode-in-Go/Algorithms'
    dst_path = 'go'
    file_match = re.compile(".*_test.go|readme.md")

    def build(self, keyword):

        if isinstance(keyword, int) or keyword.isdigit():
            path_match = re.compile("{0:04d}.*".format(int(keyword)))
        else:
            path_match = re.compile("\d+.*{}.*".format(keyword))
        for p in os.listdir(self.src_path):
            if path_match.match(p):
                self.copy_test(p)

    def copy_test(self, p: str):
        parent = os.path.join(self.src_path, p)
        if not os.path.isdir(parent):
            return
        for filename in os.listdir(parent):
            src = os.path.join(parent, filename)
            dst_parent = os.path.join(self.dst_path, p)
            dst = os.path.join(dst_parent, filename)
            if self.file_match.match(filename.lower()) and os.path.isfile(src):
                if not os.path.exists(dst_parent):
                    os.mkdir(dst_parent)
                copyfile(src, dst)


def go(keyword: str):
    """创建"""
    Go().build(keyword)


def go_all():
    Go().build("")


if __name__ == '__main__':
    from fire import Fire

    Fire()
