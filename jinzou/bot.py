#!/usr/bin/env python

# TODO: Convert nickname functionality into a plugin

from twisted.words.protocols import irc
from twisted.internet import protocol
import jinzou.plugins.loader

class JinzouClient(irc.IRCClient):
    nicknames = ['jinzou','jnzu',]
    channels = ['#testing',]

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

        if inherited_method:
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

    # TODO: Once Twisted decides that new-style classes are worth losing
    # a bit of backwards compatibility, do something like this:
    #
    #    def __getattribute(self, name):
    #        return lambda *args, **kwargs: self.call_plugins(self, name, *args, **kwargs)
    #
    # But until then, we get to do this:

    def sendLine(self, *args, **kwargs):
        self.call_plugins('sendLine', *args, **kwargs)

    def created(self, *args, **kwargs):
        self.call_plugins('created', *args, **kwargs)

    def yourHost(self, *args, **kwargs):
        self.call_plugins('yourHost', *args, **kwargs)

    def myInfo(self, *args, **kwargs):
        self.call_plugins('myInfo', *args, **kwargs)

    def luserClient(self, *args, **kwargs):
        self.call_plugins('luserClient', *args, **kwargs)

    def bounce(self, *args, **kwargs):
        self.call_plugins('bounce', *args, **kwargs)

    def isupport(self, *args, **kwargs):
        self.call_plugins('isupport', *args, **kwargs)

    def luserChannels(self, *args, **kwargs):
        self.call_plugins('luserChannels', *args, **kwargs)

    def luserOp(self, *args, **kwargs):
        self.call_plugins('luserOp', *args, **kwargs)

    def luserMe(self, *args, **kwargs):
        self.call_plugins('luserMe', *args, **kwargs)

    def privmsg(self, *args, **kwargs):
        self.call_plugins('privmsg', *args, **kwargs)

    def joined(self, *args, **kwargs):
        self.call_plugins('joined', *args, **kwargs)

    def left(self, *args, **kwargs):
        self.call_plugins('left', *args, **kwargs)

    def noticed(self, *args, **kwargs):
        self.call_plugins('noticed', *args, **kwargs)

    def modeChanged(self, *args, **kwargs):
        self.call_plugins('modeChanged', *args, **kwargs)

    def pong(self, *args, **kwargs):
        self.call_plugins('pong', *args, **kwargs)

    def signedOn(self, *args, **kwargs):
        self.call_plugins('signedOn', *args, **kwargs)

    def kickedFrom(self, *args, **kwargs):
        self.call_plugins('kickedFrom', *args, **kwargs)

    def nickChanged(self, *args, **kwargs):
        self.call_plugins('nickChanged', *args, **kwargs)

    def userJoined(self, *args, **kwargs):
        self.call_plugins('userJoined', *args, **kwargs)

    def userLeft(self, *args, **kwargs):
        self.call_plugins('userLeft', *args, **kwargs)

    def userQuit(self, *args, **kwargs):
        self.call_plugins('userQuit', *args, **kwargs)

    def userKicked(self, *args, **kwargs):
        self.call_plugins('userKicked', *args, **kwargs)

    def action(self, *args, **kwargs):
        self.call_plugins('action', *args, **kwargs)

    def topicUpdated(self, *args, **kwargs):
        self.call_plugins('topicUpdated', *args, **kwargs)

    def userRenamed(self, *args, **kwargs):
        self.call_plugins('userRenamed', *args, **kwargs)

    def receivedMOTD(self, *args, **kwargs):
        self.call_plugins('receivedMOTD', *args, **kwargs)

    def join(self, *args, **kwargs):
        self.call_plugins('join', *args, **kwargs)

    def leave(self, *args, **kwargs):
        self.call_plugins('leave', *args, **kwargs)

    def kick(self, *args, **kwargs):
        self.call_plugins('kick', *args, **kwargs)

    def topic(self, *args, **kwargs):
        self.call_plugins('topic', *args, **kwargs)

    def mode(self, *args, **kwargs):
        self.call_plugins('mode', *args, **kwargs)

    def say(self, *args, **kwargs):
        self.call_plugins('say', *args, **kwargs)

    def msg(self, *args, **kwargs):
        self.call_plugins('msg', *args, **kwargs)

    def notice(self, *args, **kwargs):
        self.call_plugins('notice', *args, **kwargs)

    def away(self, *args, **kwargs):
        self.call_plugins('away', *args, **kwargs)

    def back(self, *args, **kwargs):
        self.call_plugins('back', *args, **kwargs)

    def whois(self, *args, **kwargs):
        self.call_plugins('whois', *args, **kwargs)

    def register(self, *args, **kwargs):
        self.call_plugins('register', *args, **kwargs)

    def setNick(self, *args, **kwargs):
        self.call_plugins('setNick', *args, **kwargs)

    def quit(self, *args, **kwargs):
        self.call_plugins('quit', *args, **kwargs)

    def me(self, *args, **kwargs):
        self.call_plugins('me', *args, **kwargs)

    def ping(self, *args, **kwargs):
        self.call_plugins('ping', *args, **kwargs)

    def dccSend(self, *args, **kwargs):
        self.call_plugins('dccSend', *args, **kwargs)

    def dccResume(self, *args, **kwargs):
        self.call_plugins('dccResume', *args, **kwargs)

    def dccAcceptResume(self, *args, **kwargs):
        self.call_plugins('dccAcceptResume', *args, **kwargs)

    def irc_ERR_PASSWDMISMATCH(self, *args, **kwargs):
        self.call_plugins('irc_ERR_PASSWDMISMATCH', *args, **kwargs)

    def irc_ERR_NICKNAMEINUSE(self, *args, **kwargs):
        self.call_plugins('irc_ERR_NICKNAMEINUSE', *args, **kwargs)

    def irc_RPL_WELCOME(self, *args, **kwargs):
        self.call_plugins('irc_RPL_WELCOME', *args, **kwargs)

    def irc_JOIN(self, *args, **kwargs):
        self.call_plugins('irc_JOIN', *args, **kwargs)

    def irc_PART(self, *args, **kwargs):
        self.call_plugins('irc_PART', *args, **kwargs)

    def irc_QUIT(self, *args, **kwargs):
        self.call_plugins('irc_QUIT', *args, **kwargs)

    def irc_MODE(self, *args, **kwargs):
        self.call_plugins('irc_MODE', *args, **kwargs)

    def irc_PING(self, *args, **kwargs):
        self.call_plugins('irc_PING', *args, **kwargs)

    def irc_PRIVMSG(self, *args, **kwargs):
        self.call_plugins('irc_PRIVMSG', *args, **kwargs)

    def irc_NOTICE(self, *args, **kwargs):
        self.call_plugins('irc_NOTICE', *args, **kwargs)

    def irc_NICK(self, *args, **kwargs):
        self.call_plugins('irc_NICK', *args, **kwargs)

    def irc_KICK(self, *args, **kwargs):
        self.call_plugins('irc_KICK', *args, **kwargs)

    def irc_TOPIC(self, *args, **kwargs):
        self.call_plugins('irc_TOPIC', *args, **kwargs)

    def irc_RPL_TOPIC(self, *args, **kwargs):
        self.call_plugins('irc_RPL_TOPIC', *args, **kwargs)

    def irc_RPL_NOTOPIC(self, *args, **kwargs):
        self.call_plugins('irc_RPL_NOTOPIC', *args, **kwargs)

    def irc_RPL_MOTDSTART(self, *args, **kwargs):
        self.call_plugins('irc_RPL_MOTDSTART', *args, **kwargs)

    def irc_RPL_MOTD(self, *args, **kwargs):
        self.call_plugins('irc_RPL_MOTD', *args, **kwargs)

    def irc_RPL_ENDOFMOTD(self, *args, **kwargs):
        self.call_plugins('irc_RPL_ENDOFMOTD', *args, **kwargs)

    def irc_RPL_CREATED(self, *args, **kwargs):
        self.call_plugins('irc_RPL_CREATED', *args, **kwargs)

    def irc_RPL_YOURHOST(self, *args, **kwargs):
        self.call_plugins('irc_RPL_YOURHOST', *args, **kwargs)

    def irc_RPL_MYINFO(self, *args, **kwargs):
        self.call_plugins('irc_RPL_MYINFO', *args, **kwargs)

    def irc_RPL_BOUNCE(self, *args, **kwargs):
        self.call_plugins('irc_RPL_BOUNCE', *args, **kwargs)

    def irc_RPL_LUSERCLIENT(self, *args, **kwargs):
        self.call_plugins('irc_RPL_LUSERCLIENT', *args, **kwargs)

    def irc_RPL_LUSEROP(self, *args, **kwargs):
        self.call_plugins('irc_RPL_LUSEROP', *args, **kwargs)

    def irc_RPL_LUSERCHANNELS(self, *args, **kwargs):
        self.call_plugins('irc_RPL_LUSERCHANNELS', *args, **kwargs)

    def irc_RPL_LUSERME(self, *args, **kwargs):
        self.call_plugins('irc_RPL_LUSERME', *args, **kwargs)

    def irc_unknown(self, *args, **kwargs):
        self.call_plugins('irc_unknown', *args, **kwargs)

    def ctcpQuery(self, *args, **kwargs):
        self.call_plugins('ctcpQuery', *args, **kwargs)

    def ctcpQuery_ACTION(self, *args, **kwargs):
        self.call_plugins('ctcpQuery_ACTION', *args, **kwargs)

    def ctcpQuery_PING(self, *args, **kwargs):
        self.call_plugins('ctcpQuery_PING', *args, **kwargs)

    def ctcpQuery_FINGER(self, *args, **kwargs):
        self.call_plugins('ctcpQuery_FINGER', *args, **kwargs)

    def ctcpQuery_VERSION(self, *args, **kwargs):
        self.call_plugins('ctcpQuery_VERSION', *args, **kwargs)

    def ctcpQuery_SOURCE(self, *args, **kwargs):
        self.call_plugins('ctcpQuery_SOURCE', *args, **kwargs)

    def ctcpQuery_USERINFO(self, *args, **kwargs):
        self.call_plugins('ctcpQuery_USERINFO', *args, **kwargs)

    def ctcpQuery_CLIENTINFO(self, *args, **kwargs):
        self.call_plugins('ctcpQuery_CLIENTINFO', *args, **kwargs)

    def ctcpQuery_ERRMSG(self, *args, **kwargs):
        self.call_plugins('ctcpQuery_ERRMSG', *args, **kwargs)

    def ctcpQuery_TIME(self, *args, **kwargs):
        self.call_plugins('ctcpQuery_TIME', *args, **kwargs)

    def ctcpQuery_DCC(self, *args, **kwargs):
        self.call_plugins('ctcpQuery_DCC', *args, **kwargs)

    def dcc_SEND(self, *args, **kwargs):
        self.call_plugins('dcc_SEND', *args, **kwargs)

    def dcc_ACCEPT(self, *args, **kwargs):
        self.call_plugins('dcc_ACCEPT', *args, **kwargs)

    def dcc_RESUME(self, *args, **kwargs):
        self.call_plugins('dcc_RESUME', *args, **kwargs)

    def dcc_CHAT(self, *args, **kwargs):
        self.call_plugins('dcc_CHAT', *args, **kwargs)

    def dccDoSend(self, *args, **kwargs):
        self.call_plugins('dccDoSend', *args, **kwargs)

    def dccDoResume(self, *args, **kwargs):
        self.call_plugins('dccDoResume', *args, **kwargs)

    def dccDoChat(self, *args, **kwargs):
        self.call_plugins('dccDoChat', *args, **kwargs)

    def ctcpUnknownQuery(self, *args, **kwargs):
        self.call_plugins('ctcpUnknownQuery', *args, **kwargs)

    def ctcpMakeReply(self, *args, **kwargs):
        self.call_plugins('ctcpMakeReply', *args, **kwargs)

    def ctcpMakeQuery(self, *args, **kwargs):
        self.call_plugins('ctcpMakeQuery', *args, **kwargs)

    def ctcpReply(self, *args, **kwargs):
        self.call_plugins('ctcpReply', *args, **kwargs)

    def ctcpReply_PING(self, *args, **kwargs):
        self.call_plugins('ctcpReply_PING', *args, **kwargs)

    def ctcpUnknownReply(self, *args, **kwargs):
        self.call_plugins('ctcp_UnknownReply', *args, **kwargs)

    def badMessage(self, *args, **kwargs):
        self.call_plugins('badMessage', *args, **kwargs)

    def quirkyMessage(self, *args, **kwargs):
        self.call_plugins('quirkyMessage', *args, **kwargs)

    def connectionMade(self, *args, **kwargs):
        self.call_plugins('connectionMade', *args, **kwargs)

    def dataReceived(self, *args, **kwargs):
        self.call_plugins('dataReceived', *args, **kwargs)

    def lineReceived(self, *args, **kwargs):
        self.call_plugins('lineReceived', *args, **kwargs)

    def handleCommand(self, *args, **kwargs):
        self.call_plugins('handleCommand', *args, **kwargs)

    def signedOn(self):
        self.call_plugins('signedOn')

        self.setNick(self.nicknames[0])

        for channel in self.channels:
            self.join(channel)

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

