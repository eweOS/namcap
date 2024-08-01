# Copyright (C) 2024 Namcap contributors, see AUTHORS for details.
# SPDX-License-Identifier: GPL-2.0-or-later

import unittest
import Namcap.rules


class RulesTests(unittest.TestCase):
    def test_all_rules_dict(self):
        self.assertNotEqual(Namcap.rules.all_rules, {})
