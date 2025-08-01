#############################################################################
#
# Copyright (c) 2006-2007 Zope Corporation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################

import os.path
import zope.app.testing.functional


layer = zope.app.testing.functional.ZCMLLayer(
    os.path.dirname(__file__) + '/ftesting.zcml',
    __name__, 'z3c.noop.tests.layer', allow_teardown=True)


def test_suite():
    suite = zope.app.testing.functional.FunctionalDocFileSuite(
        'README.txt')
    suite.layer = layer
    return suite
