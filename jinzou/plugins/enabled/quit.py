from zope.interface import implements
from twisted.plugin import IPlugin
from jinzou.plugins import JinzouPlugin
from jinzou.util import config
from jinzou.util.shortcuts import get_command_string, get_reply_destination

# TODO: Nicknames list should be a generator.

class Quit(object):
    """ Changes Jinzou's nickname based on the client's nickname
        generator when the originally chosen nickname is already
        taken.
    """

    implements(IPlugin, JinzouPlugin)

    def privmsg(self, client, user, channel, message):
        """ Recieves private messages, and quits things if asked to. """

        message_info = message.split(' ', 1)

        if len(message_info) >= 2:
            quit_message = message_info[1]
        else:
            quit_message = config.load('settings')['core']['default_quit_message'].encode('UTF-8')

        if message_info[0].lower() == get_command_string('quit'):
            client.quit(quit_message)

quit = Quit()

