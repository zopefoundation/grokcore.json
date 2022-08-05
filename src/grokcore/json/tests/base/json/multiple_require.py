"""
Multiple calls of grok.require in one class are not allowed.

  >>> from grokcore.json import testing
  >>> testing.grok(__name__)
  Traceback (most recent call last):
    ...
  martian.error.GrokError: grok.require was called multiple times in \
  <class 'grokcore.json.tests.base.json.multiple_require.MultipleJSON'>. It may \
  only be set once for a class.

"""  # noqa: E501 line too long
import zope.interface

import grokcore.json as grok


class One(grok.Permission):
    grok.name('permission.1')


class Two(grok.Permission):
    grok.name('permission.2')


class MultipleJSON(grok.JSON):
    grok.context(zope.interface.Interface)
    grok.require(One)
    grok.require(Two)

    def render(self):
        pass
