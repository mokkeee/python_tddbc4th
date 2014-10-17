#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import date

MALE = 1
FEMALE = 2
GENDER = (MALE, FEMALE)

class Person:
    def __init__(self, family_name, first_name, gender, birthday = date.today()):
        if not family_name or family_name.strip() == "":
            raise RuntimeError("family_name must required.")
        if not first_name or first_name.strip() == "":
            raise RuntimeError("first_name must required.")
        if gender not in GENDER:
            raise RuntimeError("illegal gender.")
        if type(birthday) is not date or birthday > date.today():
            raise RuntimeError("illegal birthday.")

        self._family_name = family_name
        self._first_name = first_name
        self._gender = gender
        self._birthday = birthday

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

    @property
    def birthday(self):
        """
        誕生日
        """
        return self._birthday

    def is_male(self):
        return self.gender is MALE

    def is_female(self):
        return self.gender is FEMALE

    def can_marry(self, pare):
        return self.gender is not pare.gender