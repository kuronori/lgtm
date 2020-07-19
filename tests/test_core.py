#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 19 10:05:14 2020

@author: TakahiroKurokawa
"""


import unittest

class LgtmTest(unittest.TestCase):
    def test_lgtm(self):
        from lgtm.core import lgtm
        self.assertIsNone(lgtm())