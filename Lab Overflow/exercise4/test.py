#!/usr/bin/env python3

import unittest
import subprocess

class test(unittest.TestCase):
    def test(self):
        try:
            subprocess.check_output("make attack > res.out", shell=True)
        except:
            pass
        with open("res.out", "rb") as f:
            res = f.read()
        print(res.decode(errors="replace"))
        self.assertTrue(res.find("root:".encode()) >= 0)
        self.assertTrue(res.find("gdm:".encode()) >= 0)


if __name__ == '__main__':
    unittest.main()

