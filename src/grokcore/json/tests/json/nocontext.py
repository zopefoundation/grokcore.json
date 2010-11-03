"""

Context-determination follows the same rules as for adapters. We just check
whether it's hooked up at all:

  >>> from grokcore.json import testing
  >>> testing.grok(__name__)
  Traceback (most recent call last):
    ...
  GrokError: No module-level context for
  <class 'grokcore.json.tests.json.nocontext.TestJSON'>, please use the
  'context' directive.

"""
import grokcore.json as grok


class TestJSON(grok.JSON):

    def foo(self):
        pass
