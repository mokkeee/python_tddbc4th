#!/usr/bin/env python
# -*- coding: utf-8 -*-
from acme.person import Person


class TestPerson:
    def test_佐藤一郎の名字は佐藤である(self):
        佐藤一郎 = Person('佐藤', '一郎')
        assert 佐藤一郎.family_name == '佐藤'

    def test_佐藤一郎の名前は一郎である(self):
        佐藤一郎 = Person('佐藤', '一郎')
        assert 佐藤一郎.first_name == '一郎'

    def test_佐藤一郎の氏名は佐藤一郎である(self):
        佐藤一郎 = Person('佐藤', '一郎')
        assert 佐藤一郎.full_name == '佐藤一郎'

