from zope.interface import implements
from twisted.plugin import IPlugin
from jinzou.plugins import JinzouPlugin

class BootStrap(object):
    """ Sets up Jinzou's initial nickname. """

    implements(IPlugin, JinzouPlugin)

    def signedOn(self, client):
        client.setNick(client.factory.nicknames[0])

        for channel in client.factory.channels:
            client.join(channel.encode('UTF-8'))

bootstrapper = BootStrap()

