# Copyright (C) 2003-2023 Namcap contributors, see AUTHORS for details.
# SPDX-License-Identifier: GPL-2.0-or-later

from types import ModuleType

import Namcap.ruleclass

# Tarball rules
# PKGBUILD and metadata rules
from . import (  # noqa: F401
    anyelf,
    arrays,
    badbackups,
    carch,
    dbus1location,
    elffiles,
    emptydir,
    externalhooks,
    extravars,
    fhs,
    filenames,
    fileownership,
    gnomemime,
    hardlinks,
    hookdepends,
    infodirectory,
    invalidstartdir,
    javafiles,
    libtool,
    licensepkg,
    lotsofdocs,
    makedepends,
    makepkgfunctions,
    missingbackups,
    missingvars,
    pathdepends,
    pcdepends,
    perllocal,
    permissions,
    pkginfo,
    pkgnameindesc,
    py_mtime,
    pydepends,
    qmldepends,
    rpath,
    runpath,
    scrollkeeper,
    sfurl,
    shebangdepends,
    sodepends,
    sphinxbuildcachefiles,
    splitpkgbuild,
    symlink,
    systemdlocation,
    unusedsodepends,
)

all_rules = {}
for name, value in dict(locals()).items():
    if not isinstance(value, ModuleType):
        continue
    if name == "Namcap.ruleclass":
        continue
    for n, v in value.__dict__.items():
        if isinstance(v, type) and issubclass(v, Namcap.ruleclass.AbstractRule) and hasattr(v, "name"):
            all_rules[v.name] = v
