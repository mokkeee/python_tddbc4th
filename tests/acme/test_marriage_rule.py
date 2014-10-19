#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import date
import pytest
from acme import marriage_rule
from acme.person import Person, MALE, FEMALE


class Test結婚出来るか:
    judge_day = date(2014, 10, 19)
    male_18 = Person('佐藤', '一郎', MALE, judge_day.replace(year=2014-18))  # 18 years old.
    male_19 = Person('田中', '雄二', MALE, judge_day.replace(year=2014-19))  # 19 years old.
    male_17 = Person('三浦', '智士', MALE, judge_day.replace(year=2014-17))  # 17 years old. cannot marry.
    female_16 = Person('鈴木', '花子', FEMALE, judge_day.replace(year=2014-16)) # 16 years old.
    female_17 = Person('高橋', '裕美', FEMALE, judge_day.replace(year=2014-17)) # 17 years old.
    female_15 = Person('森本', '由紀', FEMALE, judge_day.replace(year=2014-15)) # 15 years old. cannot marry.

    @pytest.mark.parametrize(("person1", "person2", "marriable"),[
        (male_18, male_19, False),
        (male_18, female_16, True),
        (female_16, female_17, False),
        (female_17, male_19, True),
        (female_16, male_17, False),
        (male_18, female_15, False),
        ])
    def test_18歳以上の男子と16歳以上の女子が結婚できる(self, person1, person2, marriable):
        assert marriage_rule.can_marry(person1, person2, self.judge_day) == marriable
