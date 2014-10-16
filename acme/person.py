#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Person:
    def __init__(self, family_name, first_name):
        if family_name is None or family_name.strip() == "":
            raise RuntimeError("family_name must required.")
        elif first_name is None or first_name.strip() == "":
            raise RuntimeError("first_name must required.")

        self._family_name = family_name
        self._first_name = first_name

    @property
    def family_name(self):
        """
        苗字
        """
        return self._family_name

    @property
    def first_name(self):
        """
        名前
        """
        return self._first_name

    @property
    def full_name(self):
        """
        氏名
        """
        return self._family_name + self._first_name
