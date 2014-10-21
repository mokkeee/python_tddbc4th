#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import date
from acme.person import Person


__CURRENT_LAW_START_DAY = date(1947, 12, 22)
__MARRIABLE_AGE_MALE_MIN = 18
__MARRIABLE_AGE_FEMALE_MIN = 16

__MEIJI_LAW_START_DAY = date(1898, 7, 16)

def can_marry(person1, person2, judge_day=date.today()):
    if type(person1) is not Person:
        raise RuntimeError("person1 must be Person.")
    if type(person2) is not Person:
        raise RuntimeError("person2 must be Person.")
    if type(judge_day) is not date:
        raise RuntimeError("judge_day must be date.")

    if person1.gender == person2.gender:
        return False

    if person1.is_male():
        male = person1
        female = person2
    else:
        male = person2
        female = person1

    if judge_day >= __CURRENT_LAW_START_DAY:
        marriable_age_male_min = 18
        marriable_age_female_min = 16
    elif judge_day >= __MEIJI_LAW_START_DAY:
        marriable_age_male_min = 17
        marriable_age_female_min = 15
    else:
        marriable_age_male_min = 0
        marriable_age_female_min = 0

    male_age = male.age(judge_day)
    if male_age is None or male_age < marriable_age_male_min:
        return False

    female_age = female.age(judge_day)
    if female_age is None or female_age < marriable_age_female_min:
        return False

    return True