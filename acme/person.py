#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Person:
    def __init__(self, family_name, first_name):
        self._family_name = family_name
        self._first_name = first_name

    @property
    def family_name(self):
        return self._family_name

    @property
    def first_name(self):
        return self._first_name

    @property
    def full_name(self):
        return self._family_name + self._first_name

