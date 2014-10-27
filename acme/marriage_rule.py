#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import date
from acme.person import Person, MALE
from abc import ABCMeta, abstractmethod


class MarryLaw(metaclass=ABCMeta):
    def __init__(self, before_law):
        self.__next = before_law

    @abstractmethod
    def is_marriable(self, age, gender, judge_day):
        pass

    def is_marriable_pair(self, person1, person2):
        return True if person1.gender != person2.gender else False

    @abstractmethod
    def is_apply_law(self, day):
        pass

    def can_marry(self, person1, person2, judge_day):
        if not self.is_apply_law(judge_day):
            return self.__next.can_marry(person1, person2, judge_day)

        if not self.is_marriable_pair(person1, person2):
            return False

        for person in [person1, person2]:
            age = person.age(judge_day)
            if age is None:
                return False
            if not self.is_marriable(age, person.gender, judge_day):
                return False
        else:
            return True

class CurrentLaw(MarryLaw):
    __LAW_START_DAY = date(1947, 12, 22)
    __MARRIABLE_AGE_MALE_MIN = 18
    __MARRIABLE_AGE_FEMALE_MIN = 16

    def is_apply_law(self, day):
        return True if day >= self.__LAW_START_DAY else False

    def is_marriable(self, age, gender, judge_day):
        if gender is MALE:
            return True if age >= self.__MARRIABLE_AGE_MALE_MIN else False
        else:
            return True if age>= self.__MARRIABLE_AGE_FEMALE_MIN else False

class MeijiLaw(MarryLaw):
    __LAW_START_DAY = date(1898, 7, 16)
    __MARRIABLE_AGE_MALE_MIN = 17
    __MARRIABLE_AGE_FEMALE_MIN = 15

    def is_apply_law(self, day):
        return True if day >= self.__LAW_START_DAY else False

    def is_marriable(self, age, gender, judge_day):
        if gender is MALE:
            return True if age >= self.__MARRIABLE_AGE_MALE_MIN else False
        else:
            return True if age>= self.__MARRIABLE_AGE_FEMALE_MIN else False

class BeforeMeijiLaw(MarryLaw):
    def is_apply_law(self, day):
        return True

    def is_marriable(self, age, gender, judge_day):
        return True

__MARRY_LAW = CurrentLaw(MeijiLaw(BeforeMeijiLaw(None)))

def can_marry(person1, person2, judge_day):
    if type(person1) is not Person:
        raise RuntimeError("person1 must be Person.")
    if type(person2) is not Person:
        raise RuntimeError("person2 must be Person.")
    if type(judge_day) is not date:
        raise RuntimeError("judge_day must be date.")

    return __MARRY_LAW.can_marry(person1, person2, judge_day)