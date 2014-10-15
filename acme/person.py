#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Person:
    def __init__(self, family_name, first_name):
        self.__family_name = family_name
        self.__first_name = first_name

    def get_family_name(self):
        return self.__family_name

    def get_first_name(self):
        return self.__first_name

    def get_full_name(self):
        return self.__family_name + self.__first_name

