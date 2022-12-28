from grokcore.component import zcml
from zope.configuration.config import ConfigurationMachine


def grok(module_name):
    config = ConfigurationMachine()
    zcml.do_grok('grokcore.component.meta', config)
    zcml.do_grok('grokcore.security.meta', config)
    zcml.do_grok('grokcore.view.meta', config)
    zcml.do_grok('grokcore.view.templatereg', config)
    zcml.do_grok('grokcore.json', config)
    zcml.do_grok(module_name, config)
    config.execute_actions()
