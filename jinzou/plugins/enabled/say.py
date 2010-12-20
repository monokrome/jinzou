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
        """ Recieves private messages, and says things if asked to. """

        if channel == client.nickname:
            destination = user.split('!', 1)[0]
        else:
            destination = channel

        message_info = message.split(' ', 1)

        if len(message_info) >= 2 and message_info[0].lower() == 'say':
            client.msg(destination, message_info[1])

say = Say()

