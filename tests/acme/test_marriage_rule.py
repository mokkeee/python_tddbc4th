#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import date
import pytest
from acme import marriage_rule
from acme.person import Person, MALE, FEMALE


class Test結婚判定:
    judge_day = date(2014, 10, 19)

    male_18 = Person('佐藤', '一郎', MALE, judge_day.replace(year=2014-18))  # 18 years old.
    male_19 = Person('田中', '雄二', MALE, judge_day.replace(year=2014-19))  # 19 years old.
    male_17 = Person('三浦', '智士', MALE, judge_day.replace(year=2014-17))  # 17 years old. cannot marry.
    female_16 = Person('鈴木', '花子', FEMALE, judge_day.replace(year=2014-16)) # 16 years old.
    female_17 = Person('高橋', '裕美', FEMALE, judge_day.replace(year=2014-17)) # 17 years old.
    female_15 = Person('森本', '由紀', FEMALE, judge_day.replace(year=2014-15)) # 15 years old. cannot marry.

    @pytest.mark.parametrize(("person1", "person2", "marriable"),[
        (male_18, female_16, True),
        (female_17, male_19, True),
        (male_18, male_19, False),      # male and male
        (female_16, female_17, False),  # female and female
        (female_16, male_17, False),    # male is under 18 years old
        (male_18, female_15, False),    # female is under 16 years old
        (Person('次の日', '生まれた子', MALE, judge_day.replace(day=20)), female_16, False),    # male not birth
        (male_18, Person('次の日', '生まれた子', FEMALE, judge_day.replace(day=20)), False),    # female not birth
    ])
    def test_18歳以上の男子と16歳以上の女子が結婚できる(self, person1, person2, marriable):
        assert marriage_rule.can_marry(person1, person2, self.judge_day) == marriable


class Test不正パラメータ:
    male = Person('佐藤', '一郎', MALE, date.today())
    female = Person('鈴木', '花子', FEMALE, date.today())

    @pytest.mark.parametrize(("person1", "person2", "judge_day"), [
        (None, female, date.today()),
        (male, None, date.today()),
        (male, female, None),
        ("male_str", female, date.today()),
        (male, "female_str", date.today()),
        (male, female, "2014/10/19"),
    ])
    def test_パラメータ不正でcan_marry実行時RuntimeErrorとなること(self, person1, person2, judge_day):
        with pytest.raises(RuntimeError):
            marriage_rule.can_marry(person1, person2, judge_day)
