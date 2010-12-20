from zope.interface import implements
from twisted.plugin import IPlugin
from jinzou.plugins import JinzouPlugin

# TODO: Nicknames list should be a generator.

class Say(object):
    """ Changes Jinzou's nickname based on the client's nickname
        generator when the originally chosen nickname is already
        taken.
    """

    implements(IPlugin, JinzouPlugin)

    def privmsg(self, client, user, channel, message):
        message_info = message.split(' ', 1)

        if len(message_info) >= 2 and message_info[0] == 'say':
            client.say(channel, message_info[1])

say = Say()

