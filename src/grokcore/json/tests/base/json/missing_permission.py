"""
A permission has to be defined first (using grok.Permission for example)
before it can be used in grok.require() in an JSON class.

  >>> from grokcore.json import testing

  # PY2 - remove '+IGNORE_EXCEPTION_DETAIL'  when dropping Python 2 support:
  >>> testing.grok(__name__)  # doctest: +IGNORE_EXCEPTION_DETAIL
  Traceback (most recent call last):
  ...
  zope.configuration.config.ConfigurationExecutionError: \
  martian.error.GrokError: Undefined permission 'doesnt.exist' in \
  <class 'grokcore.json.tests.base.json.missing_permission.MissingPermission'>. \
  Use grok.Permission first...

"""  # noqa: E501 line too long

import zope.interface
import grokcore.json as grok


class MissingPermission(grok.JSON):
    grok.context(zope.interface.Interface)
    grok.require('doesnt.exist')

    def foo(self):
        pass
