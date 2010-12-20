from zope.interface import implements
from twisted.plugin import IPlugin
from jinzou.plugins import JinzouPlugin

# TODO: Nicknames list should be a generator.

class NickChange(object):
    """ Changes Jinzou's nickname based on the client's nickname
        generator when the originally chosen nickname is already
        taken.
    """

    implements(IPlugin, JinzouPlugin)

    def irc_ERR_NICKNAMEINUSE(self, client, prefix, params):
        try:
            client.factory.nicknames.pop(0)
            new_nickname = client.factory.nicknames[0]

            client.setNick(new_nickname.encode('UTF-8'))

        except IndexError:
            self.quit()

logger = NickChange()

