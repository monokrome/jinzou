from twisted.plugin import getPlugins
from jinzou.plugins import JinzouPlugin
import jinzou.plugins.enabled

def all():
    plugin_list = list(getPlugins(jinzou.plugins.JinzouPlugin, jinzou.plugins.enabled))

    return plugin_list

