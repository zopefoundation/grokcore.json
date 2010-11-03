
"""
A permission has to be defined first (using grok.Permission for example)
before it can be used in @grok.require().

  >>> from grokcore.json import testing
  >>> testing.grok(__name__)
  Traceback (most recent call last):
  ConfigurationExecutionError: martian.error.GrokError: Undefined permission 'doesnt.exist' in <class 'grokcore.json.tests.json.missing_permission2.MissingPermission'>. Use grok.Permission first.
  ...

"""

import grokcore.json as grok
import zope.interface


class MissingPermission(grok.JSON):
    grok.context(zope.interface.Interface)

    @grok.require('doesnt.exist')
    def foo(self):
        pass
