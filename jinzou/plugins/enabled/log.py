from zope.interface import implements
from twisted.plugin import IPlugin
from jinzou.plugins import JinzouPlugin

class JinzouLogger(object):
    """ A module that provides some basic logging facilities for Jinzou. """

    implements(IPlugin, JinzouPlugin)

    name='jinzou_logger'

    def log(self, msg):
        """ Receives a message and logs it to stdout. """

        # TODO: Modify this to use logging backends, IE PostgreSQL
        print msg

    def signedOn(self, client):
        """ Called immediately after Jinzou connects to a server. """

        self.log('Signed on as %s' % client.nickname)

    def join(self, client, channel):
        """ Called when a Jinzou client tries to join a channel. """

        self.log('Joining channel: {0}'.format(channel))

    def privmsg(self, client, user, channel, message):
        self.log('{0} <{1}> {2}'.format(channel, user, message))

logger = JinzouLogger()

