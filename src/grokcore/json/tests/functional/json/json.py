"""
  >>> getRootFolder()['cave'] = cave = Cave()

JSON views answer a special content-type::

  >>> print(http_call(wsgi_app(), 'GET', '/cave/show'))
  HTTP/1.1 200 Ok
  Content-Length: 17
  Content-Type: application/json
  <BLANKLINE>
  "A Cavemans cave"

"""

import grokcore.json as grok


class Cave(grok.Context):
    pass


class CaveJSON(grok.JSON):
    def show(self):
        return 'A Cavemans cave'
