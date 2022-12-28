import doctest
import unittest

from pkg_resources import resource_listdir

import zope.app.wsgi.testlayer
import zope.testbrowser.wsgi
from zope.app.wsgi.testlayer import http

import grokcore.json


class Layer(
        zope.testbrowser.wsgi.TestBrowserLayer,
        zope.app.wsgi.testlayer.BrowserLayer):
    pass


layer = Layer(grokcore.json, allowTearDown=True)


def http_call(app, method, path, data=None, handle_errors=False, **kw):
    """Function to help make RESTful calls.

    method - HTTP method to use
    path - testbrowser style path
    data - (body) data to submit
    kw - any request parameters
    """

    if path.startswith('http://localhost'):
        path = path[len('http://localhost'):]
    request_string = '{} {} HTTP/1.1\n'.format(method, path)
    for key, value in kw.items():
        request_string += '{}: {}\n'.format(key, value)
    if data is not None:
        request_string += '\r\n'
        request_string += data

    request_string = request_string.encode()

    result = http(app, request_string, handle_errors=handle_errors)
    return result


def suiteFromPackage(name):
    layer_dir = 'functional'
    files = resource_listdir(__name__, f'{layer_dir}/{name}')
    suite = unittest.TestSuite()
    globs = dict(
        getRootFolder=layer.getRootFolder,
        http_call=http_call,
        wsgi_app=layer.make_wsgi_app)
    optionflags = (
        doctest.ELLIPSIS +
        doctest.NORMALIZE_WHITESPACE +
        doctest.REPORT_NDIFF +
        doctest.IGNORE_EXCEPTION_DETAIL)
    for filename in files:
        if not filename.endswith('.py'):
            continue
        if filename == '__init__.py':
            continue

        dottedname = 'grokcore.json.tests.{}.{}.{}'.format(
            layer_dir, name, filename[:-3])
        test = doctest.DocTestSuite(
            dottedname,
            extraglobs=globs,
            optionflags=optionflags)
        test.layer = layer

        suite.addTest(test)
    return suite


def test_suite():
    suite = unittest.TestSuite()
    for name in ['json']:
        suite.addTest(suiteFromPackage(name))
    return suite


if __name__ == '__main__':
    unittest.main(defaultTest='test_suite')
