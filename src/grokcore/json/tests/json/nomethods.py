"""
  >>> grok.testing.grok(__name__)
  Traceback (most recent call last):
    ...
  GrokError: <class 'grok.tests.json.nomethods.RemoteCaveman'> does not
  define any public methods. Please add methods to this class to enable
  its registration.

"""
import grokcore.json as grok


class Caveman(grok.Context):
    pass


class RemoteCaveman(grok.JSON):
    pass