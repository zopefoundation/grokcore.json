"""
Multiple calls of grok.require in one class are not allowed.

  >>> from grokcore.json import testing
  >>> testing.grok(__name__)
  Traceback (most recent call last):
    ...
  GrokError: grok.require was called multiple times in <class 'grokcore.json.tests.json.multiple_require.MultipleJSON'>. It may only be set once for a class.

"""
import grokcore.json as grok
import zope.interface


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
