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

    def age(self, base_date=date.today()):
        """
        指定された年月日の年齢
        :param base_date: 年齢計算の対象日 省略時は今日の日付
        :return: 誕生日以前の日付が指定された場合はNoneを返す
        """
        if type(base_date) is not date:
            raise RuntimeError("base_date must be date.")
        if self.birthday > base_date:
            return None

        year_diff = base_date.year - self.birthday.year
        if self.birthday <= base_date.replace(year=self.birthday.year):
            return year_diff
        else:
            return year_diff - 1

    def is_male(self):
        return self.gender is MALE

    def is_female(self):
        return self.gender is FEMALE
