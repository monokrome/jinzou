from zope.interface import implements
from twisted.plugin import IPlugin
from jinzou.plugins import JinzouPlugin

class NickservAuth(object):
    """ Authenticates Jinzou against nickserv. """

    implements(IPlugin, JinzouPlugin)

    def signedOn(self, client):
        authentication_info = getattr(client.factory, 'authentication', False)

        if authentication_info is False or authentication_info['type'] != 'nickserv':
            return True

        nickserv_nickname = 'nickserv'
        nickserv_command = 'identify {0} {1}'

        command_format_data = [
            client.nickname,
            authentication_info['password'],
        ]

        client.msg(nickserv_nickname, nickserv_command.format(*command_format_data))

nickserv_auth = NickservAuth()

