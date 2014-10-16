#!/usr/bin/env python
# -*- coding: utf-8 -*-
from wsgiref.validate import assert_
import pytest
from acme.person import Person


class Test佐藤一郎:
    佐藤一郎 = Person('佐藤', '一郎')

    def test_佐藤一郎はPersonである(self):
        assert type(self.佐藤一郎) is Person

    def test_佐藤一郎の苗字は佐藤である(self):
        assert self.佐藤一郎.family_name == '佐藤'

    def test_佐藤一郎の名前は一郎である(self):
        assert self.佐藤一郎.first_name == '一郎'

    def test_佐藤一郎の氏名は佐藤一郎である(self):
        assert self.佐藤一郎.full_name == '佐藤一郎'

class Test鈴木花子:
    鈴木花子 = Person('鈴木', '花子')

    def test_鈴木花子の名字は鈴木である(self):
        assert self.鈴木花子.family_name == '鈴木'

    def test_鈴木花子の名前は花子である(self):
        assert self.鈴木花子.first_name == '花子'

    def test_鈴木花子の氏名は鈴木花子である(self):
        assert self.鈴木花子.full_name == '鈴木花子'

class TestPerson生成エラー:
    @pytest.mark.parametrize(("family_name", "first_name"),[
        ("佐藤", ""),
        ("", "一郎"),
        ("", ""),
        ("佐藤", None),
        (None, "一郎"),
        (None, None),
        ("佐藤", " "),
        ("  ", "一郎"),
    ])
    def test_Person生成エラー(self, family_name, first_name):
        with pytest.raises(RuntimeError):
            Person(family_name, first_name)
