#############################################################################
#
# Copyright (c) 2006-2007 Zope Foundation and Contributors.
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
"""JSON Grokking elements.
"""
import martian
import grokcore.component
from grokcore.component import context
from grokcore.security import require
from grokcore.json import JSON
from grokcore.view import layer, make_checker
from zope.interface import Interface
from zope.publisher.interfaces.browser import IDefaultBrowserLayer


class JSONGrokker(martian.MethodGrokker):
    """Grokker for methods of a `grok.JSON` subclass.

    When an application defines a `grok.JSON` view, we do not actually
    register the view with the Component Architecture.  Instead, we grok
    each of its methods separately, placing them each inside of a new
    class that we create on-the-fly by calling `type()`.  We make each
    method the `__call__()` method of its new class, since that is how
    Zope always invokes views.  And it is this new class that is then
    made the object of the two configuration actions that we schedule:
    one to activate it as a JSON adapter for the context, and the other
    to prepare a security check for the adapter.

    """
    martian.component(JSON)
    martian.directive(context)
    martian.directive(require, name='permission')
    martian.directive(layer, default=IDefaultBrowserLayer)

    def execute(
            self, factory, method, config, context, permission, layer, **kw):
        # Create a new class with a __view_name__ attribute so the
        # JSON class knows what method to call.
        method_view = type(
            factory.__name__, (factory,),
            {'__view_name__': method.__name__})

        adapts = (context, layer)
        name = method.__name__

        config.action(
            discriminator=('adapter', adapts, Interface, name),
            callable=grokcore.component.provideAdapter,
            args=(method_view, adapts, Interface, name))

        config.action(
            discriminator=('protectName', method_view, '__call__'),
            callable=make_checker,
            args=(factory, method_view, permission))

        return True
