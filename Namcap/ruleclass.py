# Copyright (C) 2003-2023 Namcap contributors, see AUTHORS for details.
# SPDX-License-Identifier: GPL-2.0-or-later

from .types import Diagnostic

"""
This module defines the base classes from which Namcap rules are derived
and how they are meant to be used.
"""


# python 3 does not need classes to derive from object
class AbstractRule(object):
    "The parent class of all rules"

    enable: bool = True

    def __init__(self):
        self.errors: list[Diagnostic] = []
        self.warnings: list[Diagnostic] = []
        self.infos: list[Diagnostic] = []


class PkgInfoRule(AbstractRule):
    "The parent class of rules that process package metadata"


class PkgbuildRule(AbstractRule):
    "The parent class of rules that process PKGBUILDs"


class TarballRule(AbstractRule):
    "The parent class of rules that process tarballs"
