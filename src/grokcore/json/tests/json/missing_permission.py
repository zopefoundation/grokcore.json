"""
A permission has to be defined first (using grok.Permission for example)
before it can be used in grok.require() in an JSON class.

  >>> from grokcore.json import testing
  >>> testing.grok(__name__)
  Traceback (most recent call last):
  ConfigurationExecutionError: martian.error.GrokError: Undefined permission 'doesnt.exist' in <class 'grokcore.json.tests.json.missing_permission.MissingPermission'>. Use grok.Permission first.
  ...

"""

import zope.interface
import grokcore.json as grok


class MissingPermission(grok.JSON):
    grok.context(zope.interface.Interface)
    grok.require('doesnt.exist')

    def foo(self):
        pass
