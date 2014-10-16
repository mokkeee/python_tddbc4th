#!/usr/bin/env python
# -*- coding: utf-8 -*-

MALE = 1
FEMALE = 2
GENDER = (MALE, FEMALE)

class Person:
    def __init__(self, family_name, first_name, gender = MALE):
        if not family_name or family_name.strip() == "":
            raise RuntimeError("family_name must required.")
        elif not first_name or first_name.strip() == "":
            raise RuntimeError("first_name must required.")
        elif gender not in GENDER:
            raise RuntimeError("illegal gender.")

        self._family_name = family_name
        self._first_name = first_name
        self._gender = gender

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

    @property
    def gender(self):
        """
        性別
        """
        return self._gender

    def is_male(self):
        return self.gender == MALE

    def is_female(self):
        return self.gender == FEMALE