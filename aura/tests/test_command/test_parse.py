#!/usr/bin/env python2

##
# Aura
# https://github.com/leosartaj/aura.git
#
# Copyright (c) 2014 Sartaj Singh
# Licensed under the MIT license.
##

import unittest
from aura import command as cmd

class Testparse(unittest.TestCase):
    """
    tests the parse, validate and separate function in command module
    """
    def setUp(self):
        self.prefix = 'c$'
        self.sep = '~~'

    def test_validate_without_prefix(self):
        line = 'test'
        result = cmd.validate(line, self.prefix, self.sep)
        self.assertFalse(result)

    def test_validate_without_prefix_with_initial_separator(self):
        line = self.sep + 'test'
        result = cmd.validate(line, self.prefix, self.sep)
        self.assertFalse(result)

    def test_validate_without_initial_separator(self):
        line = self.prefix + 'test'
        result = cmd.validate(line, self.prefix, self.sep)
        self.assertFalse(result)

    def test_validate_with_prefix_with_sep(self):
        line = self.prefix + self.sep + 'test'
        result = cmd.validate(line, self.prefix, self.sep)
        self.assertTrue(result)

    def test_separate_with_sep(self):
        line = 'do' + self.sep + 'dummy'
        first, second = cmd.separate(line, self.sep)
        self.assertEqual(first, 'do')
        self.assertEqual(second, 'dummy')

    def test_separate_without_sep(self):
        line = 'do' + 'dummy'
        first, second = cmd.separate(line, self.sep)
        self.assertEqual(first, None)
        self.assertEqual(second, 'dodummy')

    def test_parse_correct_command(self):
        line = self.prefix + self.sep + 'do' + self.sep + 'dummy'
        comd, val = cmd.parse(line, self.prefix, self.sep)
        self.assertEqual(comd, 'do')
        self.assertEqual(val, 'dummy')

    def test_parse_command_without_prefix(self):
        line = 'do' + self.sep + 'dummy'
        comd, val = cmd.parse(line, self.prefix, self.sep)
        self.assertEqual(comd, None)
        self.assertEqual(val, line)

    def test_parse_command_without_sep(self):
        line = self.prefix + 'do' + 'dummy'
        comd, val = cmd.parse(line, self.prefix, self.sep)
        self.assertEqual(comd, None)
        self.assertEqual(val, line)
