"""
An undefined permission that's never used (because it's being shadowed
by a method-level directive) doesn't raise an error:

  >>> from grokcore.json import testing
  >>> testing.grok(__name__)

"""

import grokcore.json as grok
import zope.interface


class Permission(grok.Permission):
    grok.name('json.exists')


class MissingPermission(grok.JSON):
    grok.context(zope.interface.Interface)

    grok.require('doesnt.exist')

    @grok.require(Permission)
    def foo(self):
        pass
