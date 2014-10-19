#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import date
from acme.person import Person


__MARRIABLE_AGE_MALE_MIN = 18
__MARRIABLE_AGE_FEMALE_MIN = 16


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

    male_age = male.age(judge_day)
    if male_age is None or male_age < __MARRIABLE_AGE_MALE_MIN:
        return False

    female_age = female.age(judge_day)
    if female_age is None or female_age < __MARRIABLE_AGE_FEMALE_MIN:
        return False

    return True