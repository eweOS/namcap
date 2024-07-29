# Copyright (C) 2003-2023 Namcap contributors, see AUTHORS for details.
# SPDX-License-Identifier: GPL-2.0-or-later

from Namcap.tests.pkgbuild_test import PkgbuildTest
from Namcap.rules.pkginfo import CapsPkgnameRule, LicenseRule, NonUniqueSourcesRule, UrlRule


class NamcapInvalidPkgNameTest(PkgbuildTest):
    pkgbuild1 = """
# Maintainer: Arch Linux <archlinux@example.com>
# Contributor: Arch Linux <archlinux@example.com>

pkgname=MyPackage
pkgver=1.0
pkgrel=1
pkgdesc="A package"
arch=('i686' 'x86_64')
url="http://www.example.com/"
license=('GPL-3.0-or-later')
depends=('glibc')
options=('!libtool')
source=(ftp://ftp.example.com/pub/mypackage-0.1.tar.gz)
md5sums=('abcdefabcdef12345678901234567890')

build() {
  cd "${srcdir}"/${pkgname}-${pkgver}
  ./configure --prefix=/usr
  make
}

package() {
  cd "${srcdir}"/${pkgname}-${pkgver}
  ./configure --prefix=/usr
  make DESTDIR="${pkgdir}" install
}
"""

    test_valid = PkgbuildTest.valid_tests

    def preSetUp(self):
        self.rule = CapsPkgnameRule

    def test_example1(self):
        # Example 1
        r = self.run_on_pkg(self.pkgbuild1)
        self.assertEqual(r.errors, [("package-name-in-uppercase", ())])
        self.assertEqual(r.warnings, [])
        self.assertEqual(r.infos, [])


class NamcapLicenseTest(PkgbuildTest):
    pkgbuild1 = """
# Maintainer: Arch Linux <archlinux@example.com>
# Contributor: Arch Linux <archlinux@example.com>

pkgname=mypackage
pkgver=1.0
pkgrel=1
pkgdesc="A package"
arch=('i686' 'x86_64')
url="http://www.example.com/"
depends=('glibc')
options=('!libtool')
source=(ftp://ftp.example.com/pub/mypackage-0.1.tar.gz)
md5sums=('abcdefabcdef12345678901234567890')

build() {
  cd "${srcdir}"/${pkgname}-${pkgver}
  ./configure --prefix=/usr
  make
}

package() {
  cd "${srcdir}"/${pkgname}-${pkgver}
  ./configure --prefix=/usr
  make DESTDIR="${pkgdir}" install
}
"""
    test_valid = PkgbuildTest.valid_tests

    def preSetUp(self):
        self.rule = LicenseRule

    def test_example1(self):
        # Example 1
        r = self.run_on_pkg(self.pkgbuild1)
        self.assertEqual(r.errors, [("missing-license", ())])
        self.assertEqual(r.warnings, [])
        self.assertEqual(r.infos, [])


class NamcapUrlTest(PkgbuildTest):
    pkgbuild1 = """
# Maintainer: Arch Linux <archlinux@example.com>
# Contributor: Arch Linux <archlinux@example.com>

pkgname=mypackage
pkgver=1.0
pkgrel=1
pkgdesc="A package"
arch=('i686' 'x86_64')
depends=('glibc')
license=('GPL-3.0-or-later')
options=('!libtool')
source=(ftp://ftp.example.com/pub/mypackage-0.1.tar.gz)
md5sums=('abcdefabcdef12345678901234567890')

build() {
  cd "${srcdir}"/${pkgname}-${pkgver}
  ./configure --prefix=/usr
  make
}

package() {
  cd "${srcdir}"/${pkgname}-${pkgver}
  ./configure --prefix=/usr
  make DESTDIR="${pkgdir}" install
}
"""

    test_valid = PkgbuildTest.valid_tests

    def preSetUp(self):
        self.rule = UrlRule

    def test_example1(self):
        # Example 1
        r = self.run_on_pkg(self.pkgbuild1)
        self.assertEqual(r.errors, [("missing-url", ())])
        self.assertEqual(r.warnings, [])
        self.assertEqual(r.infos, [])


class NamcapNonUniqueSourceTest(PkgbuildTest):
    pkgbuild1 = """
pkgname=mypackage
pkgver=1.0
pkgrel=1
pkgdesc="A package"
arch=('x86_64')
depends=('glibc')
license=('GPL-3.0-or-later')
source=("https://github.com/foobar/software/archive/refs/tags/v${pkgver}.tar.gz")
md5sums=('abcdefabcdef12345678901234567890')

build() {
  cd "${srcdir}"/${pkgname}-${pkgver}
}

package() {
  cd "${srcdir}"/${pkgname}-${pkgver}
}
"""

    pkgbuild2 = """
pkgname=secondpackage
pkgver=1.0
pkgrel=1
pkgdesc="B package"
arch=('x86_64')
depends=('glibc')
license=('GPL-3.0-or-later')
source=("git+https://salsa.debian.org/debian/distro-info-data.git#tag=debian/$pkgver")
md5sums=('abcdefabcdef12345678901234567890')

build() {
  cd "${srcdir}"/${pkgname}-${pkgver}
}

package() {
  cd "${srcdir}"/${pkgname}-${pkgver}
}
"""

    test_valid = PkgbuildTest.valid_tests

    def preSetUp(self):
        self.rule = NonUniqueSourcesRule

    def test_example1(self):
        r = self.run_on_pkg(self.pkgbuild1)
        self.assertEqual(r.errors, [])
        self.assertEqual(r.warnings, [("non-unique-source-name %s", ("v1.0.tar.gz"))])
        self.assertEqual(r.infos, [])

        r = self.run_on_pkg(self.pkgbuild2)
        self.assertEqual(r.errors, [])
        self.assertEqual(r.warnings, [])
        self.assertEqual(r.infos, [])
