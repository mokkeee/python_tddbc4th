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
    def test_現在は18歳以上の男子と16歳以上の女子が結婚できる(self, person1, person2, marriable):
        assert marriage_rule.can_marry(person1, person2, self.judge_day) == marriable


class Test結婚判定_after_1947_12_22:
    current_law_start_day = date(1947, 12, 22)

    male_18_in_1947 = Person('佐藤', '昭一', MALE, current_law_start_day.replace(year=1947-18))
    male_17_in_1947 = Person('三浦', '太郎', MALE, current_law_start_day.replace(year=1947-18, day=22+1))
    female_16_in_1947 = Person('鈴木', '弘子', FEMALE, current_law_start_day.replace(year=1947-16))
    female_15_in_1947 = Person('森本', '文子', FEMALE, current_law_start_day.replace(year=1947-16, day=22+1))

    @pytest.mark.parametrize(("person1", "person2", "marriable"),[
        (male_18_in_1947, female_16_in_1947, True),
        (female_16_in_1947, male_18_in_1947, True),
        (male_18_in_1947, female_15_in_1947, False),
        (male_17_in_1947, female_16_in_1947, False),
        (Person('次の日', '生まれた子', MALE, current_law_start_day.replace(day=23)), female_16_in_1947, False),    # male not birth
        (male_18_in_1947, Person('次の日', '生まれた子', FEMALE, current_law_start_day.replace(day=23)), False),    # female not birth
    ])
    def test_1947年12月22以降は18歳以上の男子と16歳以上の女子が結婚できる(self, person1, person2, marriable):
        assert marriage_rule.can_marry(person1, person2, self.current_law_start_day) == marriable


class Test結婚判定_between_1898_07_16_and_1947_12_21:
    meiji_law_start_day = date(1898, 7, 16)
    meiji_law_end_day = date(1947, 12, 21)

    male_17_in_1898 = Person('佐藤', '昭一', MALE, meiji_law_start_day.replace(year=1898-17))
    male_18_in_1898 = Person('田中', '雄造', MALE, meiji_law_start_day.replace(year=1898-18))
    male_16_in_1898 = Person('三浦', '太郎', MALE, meiji_law_start_day.replace(year=1898-17, day=16+1))
    female_15_in_1898 = Person('鈴木', '弘子', FEMALE, meiji_law_start_day.replace(year=1898-15))
    female_16_in_1898 = Person('高橋', '葉子', FEMALE, meiji_law_start_day.replace(year=1898-16))
    female_14_in_1898 = Person('森本', '文子', FEMALE, meiji_law_start_day.replace(year=1898-15, day=16+1))

    @pytest.mark.parametrize(("person1", "person2", "judge_day", "marriable"),[
        (male_17_in_1898, female_15_in_1898, meiji_law_start_day, True),
        (female_16_in_1898, male_18_in_1898, meiji_law_start_day, True),
        (male_17_in_1898, female_14_in_1898, meiji_law_start_day, False),
        (male_16_in_1898, female_15_in_1898, meiji_law_start_day, False),
        (male_16_in_1898, female_14_in_1898, meiji_law_start_day.replace(day=16+1), True),
        (Person('次の日', '生まれた子', MALE, meiji_law_start_day.replace(day=16+1)), female_16_in_1898, meiji_law_start_day, False),    # male not birth
        (male_18_in_1898, Person('次の日', '生まれた子', FEMALE, meiji_law_start_day.replace(day=16+1)), meiji_law_start_day, False),    # female not birth
    ])
    def test_1898年7月16日から1947年12月21日の間は17歳以上の男子と15歳以上の女子が結婚できる(self, person1, person2, judge_day, marriable):
        assert marriage_rule.can_marry(person1, person2, judge_day) == marriable

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
