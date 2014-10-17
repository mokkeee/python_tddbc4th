#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import date, timedelta
from wsgiref.validate import assert_
import pytest
from acme.person import Person, MALE, FEMALE


class Test佐藤一郎:
    birthday = date(1965, 10, 10)
    佐藤一郎 = Person('佐藤', '一郎', MALE, birthday)

    def test_佐藤一郎はPersonである(self):
        assert type(self.佐藤一郎) is Person

    def test_佐藤一郎の苗字は佐藤である(self):
        assert self.佐藤一郎.family_name == '佐藤'

    def test_佐藤一郎の名前は一郎である(self):
        assert self.佐藤一郎.first_name == '一郎'

    def test_佐藤一郎の氏名は佐藤一郎である(self):
        assert self.佐藤一郎.full_name == '佐藤一郎'

    def test_佐藤一郎は男である(self):
        assert self.佐藤一郎.gender is MALE
        assert self.佐藤一郎.is_male() == True

    def test_佐藤一郎は女ではない(self):
        assert self.佐藤一郎.gender is not FEMALE
        assert self.佐藤一郎.is_female() == False

    def test_佐藤一郎の誕生日が取得できること(self):
        assert self.佐藤一郎.birthday == self.birthday

class Test鈴木花子:
    鈴木花子 = Person('鈴木', '花子', FEMALE)

    def test_鈴木花子の名字は鈴木である(self):
        assert self.鈴木花子.family_name == '鈴木'

    def test_鈴木花子の名前は花子である(self):
        assert self.鈴木花子.first_name == '花子'

    def test_鈴木花子の氏名は鈴木花子である(self):
        assert self.鈴木花子.full_name == '鈴木花子'

    def test_鈴木花子は女である(self):
        assert self.鈴木花子.gender is FEMALE
        assert self.鈴木花子.is_female() == True

    def test_鈴木花子は男ではない(self):
        assert self.鈴木花子.gender is not MALE
        assert self.鈴木花子.is_male() == False

class Test結婚出来るか:
    佐藤一郎 = Person('佐藤', '一郎', MALE)
    田中雄二 = Person('田中', '雄二', MALE)
    鈴木花子 = Person('鈴木', '花子', FEMALE)
    高橋裕美 = Person('高橋', '裕美', FEMALE)

    @pytest.mark.parametrize(("person1", "person2", "we_can"),[
        (佐藤一郎, 田中雄二, False),
        (佐藤一郎, 鈴木花子, True),
        (鈴木花子, 高橋裕美, False),
        (高橋裕美, 佐藤一郎, True),
    ])
    def test_異性と結婚できて同性とは結婚できない(self, person1, person2, we_can):
        assert person1.can_marry(person2) == we_can

class Test不正パラメータ:
    @pytest.mark.parametrize(("family_name", "first_name", "gender"),[
        ("佐藤", "", MALE),
        ("", "一郎", MALE),
        ("", "", None),
        ("佐藤", None, MALE),
        (None, "一郎", MALE),
        (None, None, None),
        ("佐藤", " ", MALE),
        ("  ", "一郎", MALE),
        ("佐藤", "一郎", None),
        ("佐藤", "一郎", 0),
        ("佐藤", "一郎", 3),
    ])
    def test_不正パラメータでRuntimeErrorとなること(self, family_name, first_name, gender):
        with pytest.raises(RuntimeError):
            Person(family_name, first_name, gender)

    @pytest.mark.parametrize(("birthday"), [
        (None),
        ("2014/10/17"), # not date
        (date.today() + timedelta(days=1)), # future
    ])
    def test_誕生日指定不正のときRuntimeErrorとなること(self, birthday):
        with pytest.raises(RuntimeError):
            Person("未来", "子", FEMALE, birthday)
