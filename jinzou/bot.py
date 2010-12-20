#!/usr/bin/env python

from twisted.words.protocols import irc
from twisted.internet import protocol
import jinzou.plugins.loader

plugin_exports = (
    'sendLine',
    'created',
    'yourHost',
    'MyInfo',
    'luserClient',
    'privmsg',
    'bounce',
    'isupport',
    'luserChannels',
    'luserOp',
    'luserMe',
    'joined',
    'left',
    'noticed',
    'modeChanged',
    'pong',
    'signedOn',
    'kickedFrom',
    'nickChanged',
    'userJoined',
    'userLeft',
    'userQuit',
    'userKicked',
    'action',
    'topicUpdated',
    'userRenamed',
    'receivedMOTD',
    'join',
    'leave',
    'kick',
    'topic',
    'mode',
    'say',
    'msg',
    'notice',
    'away',
    'back',
    'whois',
    'register',
    'setNick',
    'quit',
    'me',
    'ping',
    'dccSend',
    'dccResume',
    'dccAcceptResume',
    'irc_ERR_PASSWDMISMATCH',
    'irc_ERR_NICKNAMEINUSE',
    'irc_RPL_WELCOME',
    'irc_JOIN',
    'irc_PART',
    'irc_QUIT',
    'irc_MODE',
    'irc_PING',
    'irc_PRIVMSG',
    'irc_NOTICE',
    'irc_NICK',
    'irc_KICK',
    'irc_TOPIC',
    'irc_RPL_TOPIC',
    'irc_RPL_NOTOPIC',
    'irc_RPL_MOTDSTART',
    'irc_RPL_MOTD',
    'irc_RPL_ENDOFMOTD',
    'irc_RPL_CREATED',
    'irc_RPL_YOURHOST',
    'irc_RPL_MYINFO',
    'irc_RPL_BOUNCE',
    'irc_RPL_LUSERCLIENT',
    'irc_RPL_LUSEROP',
    'irc_RPL_LUSERCHANNELS',
    'irc_RPL_LUSERME',
    'irc_unknown',
    'ctcpQuery',
    'ctcpQuery_ACTOUN',
    'ctcpQuery_PING',
    'ctcpQuery_FINGER',
    'ctcpQuery_VERSION',
    'ctcpQuery_SOURCE',
    'ctcpQuery_USERINFO',
    'ctcpQuery_CLIENTINFO',
    'ctcpQuery_ERRMSG',
    'ctcpQuery_TIME',
    'ctcpQuery_DCC',
    'dcc_SEND',
    'dcc_ACCEPT',
    'dcc_RESUME',
    'dcc_CHAT',
    'dccDoSend',
    'dccDoResume',
    'dccDoChat',
    'dccUnknownQuery',
    'dccMakeReply',
    'dccMakeQuery',
    'ctcpReply',
    'ctcpReply_PING',
    'ctcpUnknownReply',
    'badMessage',
    'quirkyMessage',
    'connectionMade',
    'dataReceived',
    'lineReceived',
    'handleCommand',
)

class JinzouClient(irc.IRCClient):
    nicknames = ['unnamed',]
    channels = ['#jinzou',]

    def __init__(self):
        self.original_nicknames = self.nicknames
        self.original_channels = self.channels

    def call_plugins(self, method, *args, **kwargs):
        """ Receives an attribute name as well as args and kwargs, and calls
            the specified method on each plugin registered with this client.
        """

        # Every plugin is passed a referece to the client as it's first arg
        args = list(args)
        args.insert(0, self)

        for plugin in self.plugins:
            plugin_method = getattr(plugin, method, False)

            # If we've found a callable in the plugin - call it.
            if plugin_method is not False and callable(plugin_method):
                if plugin_method(*args, **kwargs) is False:
                    return False

        inherited_method = getattr(irc.IRCClient, method, False)

        if inherited_method is not False:
            return inherited_method(*args, **kwargs)
        else:
            return True

    @property
    def nickname(self):
        return self.nicknames[0]

    @property
    def plugins(self):
        """ Get a list of plugins usable on this specific network. """

        plugin_list = jinzou.plugins.loader.all()

        return plugin_list

def get_plugin_handler(export):
    def plugin_handler(self, *args, **kwargs):
        return self.call_plugins(export, *args, **kwargs)

    return plugin_handler

# Loop through plugin exports and assign the plugin handler to them
for export in plugin_exports:
    setattr(JinzouClient, export, get_plugin_handler(export))

class JinzouFactory(protocol.ClientFactory):
    protocol = JinzouClient

    host_info = {
        'network': 'localhost',
        'port': 6667,
        'use_ssl': False,
    }

    def __init__(self, *args, **kwargs):
        for kwarg in kwargs:
            setattr(self, kwarg, kwargs[kwarg])

if __name__ == '__main__':
    from twisted.internet import reactor
    from util import config

    def setup_client(client):
        network_name = client['host_info']['network']

        if network_name not in config.networks:
            raise ValueError("The specified network {0} was not found in networks configuration.".format(network_name))

        network_addr = config.networks[network_name]['servers'][0]
        network_port = client['host_info']['port']
        network_ssl = client['host_info']['use_ssl']

        reactor.connectTCP(network_addr, network_port, JinzouFactory())

    for client in config.settings['clients']:
        setup_client(client)

    reactor.run()

