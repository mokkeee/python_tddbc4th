#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import date


__MARRIABLE_AGE_MALE_MIN = 18
__MARRIABLE_AGE_FEMALE_MIN = 16


def can_marry(person1, person2, judge_day=date.today()):
    if person1.gender == person2.gender:
        return False

    if person1.is_male():
        male = person1
        female = person2
    else:
        male = person2
        female = person1

    if male.age(judge_day) < __MARRIABLE_AGE_MALE_MIN:
        return False
    if female.age(judge_day) < __MARRIABLE_AGE_FEMALE_MIN:
        return False

    return True