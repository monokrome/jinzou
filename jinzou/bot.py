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

    def sendLine(self, *args, **kwargs):
        self.call_plugins('sendLine', *args, **kwargs)
        irc.IRCClient.sendLine(self, *args, **kwargs)

    def created(self, *args, **kwargs):
        self.call_plugins('created', *args, **kwargs)
        irc.IRCClient.created(self, *args, **kwargs)

    def yourHost(self, *args, **kwargs):
        self.call_plugins('yourHost', *args, **kwargs)
        irc.IRCClient.yourHost(self, *args, **kwargs)

    def myInfo(self, *args, **kwargs):
        self.call_plugins('myInfo', *args, **kwargs)
        irc.IRCClient.myInfo(self, *args, **kwargs)

    def luserClient(self, *args, **kwargs):
        self.call_plugins('luserClient', *args, **kwargs)
        irc.IRCClient.luserClient(self, *args, **kwargs)

    def bounce(self, *args, **kwargs):
        self.call_plugins('bounce', *args, **kwargs)
        irc.IRCClient.bounce(self, *args, **kwargs)

    def isupport(self, *args, **kwargs):
        self.call_plugins('isupport', *args, **kwargs)
        irc.IRCClient.isupport(self, *args, **kwargs)

    def luserChannels(self, *args, **kwargs):
        self.call_plugins('luserChannels', *args, **kwargs)
        irc.IRCClient.luserChannels(self, *args, **kwargs)

    def luserOp(self, *args, **kwargs):
        self.call_plugins('luserOp', *args, **kwargs)
        irc.IRCClient.luserOp(self, *args, **kwargs)

    def luserMe(self, *args, **kwargs):
        self.call_plugins('luserMe', *args, **kwargs)
        irc.IRCClient.luserMe(self, *args, **kwargs)

    def privmsg(self, *args, **kwargs):
        self.call_plugins('privmsg', *args, **kwargs)
        irc.IRCClient.privmsg(self, *args, **kwargs)

    def joined(self, *args, **kwargs):
        self.call_plugins('joined', *args, **kwargs)
        irc.IRCClient.joined(self, *args, **kwargs)

    def left(self, *args, **kwargs):
        self.call_plugins('left', *args, **kwargs)
        irc.IRCClient.left(self, *args, **kwargs)

    def noticed(self, *args, **kwargs):
        self.call_plugins('noticed', *args, **kwargs)
        irc.IRCClient.noticed(self, *args, **kwargs)

    def modeChanged(self, *args, **kwargs):
        self.call_plugins('modeChanged', *args, **kwargs)
        irc.IRCClient.modeChanged(self, *args, **kwargs)

    def pong(self, *args, **kwargs):
        self.call_plugins('pong', *args, **kwargs)
        irc.IRCClient.pong(self, *args, **kwargs)

    def signedOn(self, *args, **kwargs):
        self.call_plugins('signedOn', *args, **kwargs)
        irc.IRCClient.signedOn(self, *args, **kwargs)

    def kickedFrom(self, *args, **kwargs):
        self.call_plugins('kickedFrom', *args, **kwargs)
        irc.IRCClient.kickedFrom(self, *args, **kwargs)

    def nickChanged(self, *args, **kwargs):
        self.call_plugins('nickChanged', *args, **kwargs)
        irc.IRCClient.nickChanged(self, *args, **kwargs)

    def userJoined(self, *args, **kwargs):
        self.call_plugins('userJoined', *args, **kwargs)
        irc.IRCClient.userJoined(self, *args, **kwargs)

    def userLeft(self, *args, **kwargs):
        self.call_plugins('userLeft', *args, **kwargs)
        irc.IRCClient.userLeft(self, *args, **kwargs)

    def userQuit(self, *args, **kwargs):
        self.call_plugins('userQuit', *args, **kwargs)
        irc.IRCClient.userQuit(self, *args, **kwargs)

    def userKicked(self, *args, **kwargs):
        self.call_plugins('userKicked', *args, **kwargs)
        irc.IRCClient.userKicked(self, *args, **kwargs)

    def action(self, *args, **kwargs):
        self.call_plugins('action', *args, **kwargs)
        irc.IRCClient.action(self, *args, **kwargs)

    def topicUpdated(self, *args, **kwargs):
        self.call_plugins('topicUpdated', *args, **kwargs)
        irc.IRCClient.topicUpdated(self, *args, **kwargs)

    def userRenamed(self, *args, **kwargs):
        self.call_plugins('userRenamed', *args, **kwargs)
        irc.IRCClient.userRenamed(self, *args, **kwargs)

    def receivedMOTD(self, *args, **kwargs):
        self.call_plugins('receivedMOTD', *args, **kwargs)
        irc.IRCClient.receivedMOTD(self, *args, **kwargs)

    def join(self, *args, **kwargs):
        self.call_plugins('join', *args, **kwargs)
        irc.IRCClient.join(self, *args, **kwargs)

    def leave(self, *args, **kwargs):
        self.call_plugins('leave', *args, **kwargs)
        irc.IRCClient.leave(self, *args, **kwargs)

    def kick(self, *args, **kwargs):
        self.call_plugins('kick', *args, **kwargs)
        irc.IRCClient.kick(self, *args, **kwargs)

    def topic(self, *args, **kwargs):
        self.call_plugins('topic', *args, **kwargs)
        irc.IRCClient.topic(self, *args, **kwargs)

    def mode(self, *args, **kwargs):
        self.call_plugins('mode', *args, **kwargs)
        irc.IRCClient.mode(self, *args, **kwargs)

    def say(self, *args, **kwargs):
        self.call_plugins('say', *args, **kwargs)
        irc.IRCClient.say(self, *args, **kwargs)

    def msg(self, *args, **kwargs):
        self.call_plugins('msg', *args, **kwargs)
        irc.IRCClient.msg(self, *args, **kwargs)

    def notice(self, *args, **kwargs):
        self.call_plugins('notice', *args, **kwargs)
        irc.IRCClient.notice(self, *args, **kwargs)

    def away(self, *args, **kwargs):
        self.call_plugins('away', *args, **kwargs)
        irc.IRCClient.away(self, *args, **kwargs)

    def back(self, *args, **kwargs):
        self.call_plugins('back', *args, **kwargs)
        irc.IRCClient.back(self, *args, **kwargs)

    def whois(self, *args, **kwargs):
        self.call_plugins('whois', *args, **kwargs)
        irc.IRCClient.whois(self, *args, **kwargs)

    def register(self, *args, **kwargs):
        self.call_plugins('register', *args, **kwargs)
        irc.IRCClient.register(self, *args, **kwargs)

    def setNick(self, *args, **kwargs):
        self.call_plugins('setNick', *args, **kwargs)
        irc.IRCClient.setNick(self, *args, **kwargs)

    def quit(self, *args, **kwargs):
        self.call_plugins('quit', *args, **kwargs)
        irc.IRCClient.quit(self, *args, **kwargs)

    def me(self, *args, **kwargs):
        self.call_plugins('me', *args, **kwargs)
        irc.IRCClient.me(self, *args, **kwargs)

    def ping(self, *args, **kwargs):
        self.call_plugins('ping', *args, **kwargs)
        irc.IRCClient.ping(self, *args, **kwargs)

    def dccSend(self, *args, **kwargs):
        self.call_plugins('dccSend', *args, **kwargs)
        irc.IRCClient.dccSend(self, *args, **kwargs)

    def dccResume(self, *args, **kwargs):
        self.call_plugins('dccResume', *args, **kwargs)
        irc.IRCClient.dccResume(self, *args, **kwargs)

    def dccAcceptResume(self, *args, **kwargs):
        self.call_plugins('dccAcceptResume', *args, **kwargs)
        irc.IRCClient.dccAcceptResume(self, *args, **kwargs)

    def irc_ERR_NICKNAMEINUSE(self, prefix, params):
        self.call_plugins(self, 'irc_ERR_NICKNAMEINUSE', [prefix, params])

        try:
            # TODO: Change this into a generator.
            self.nicknames.pop(0)
            new_nickname = self.nicknames[0]
            self.setNick(new_nickname)

        except IndexError:
            self.quit()

    def irc_ERR_PASSWDMISMATCH(self, *args, **kwargs):
        self.call_plugins('irc_ERR_PASSWDMISMATCH', *args, **kwargs)
        irc.IRCClient.irc_ERR_PASSWDMISMATCH(self, *args, **kwargs)

    def irc_RPL_WELCOME(self, *args, **kwargs):
        self.call_plugins('irc_RPL_WELCOME', *args, **kwargs)
        irc.IRCClient.irc_RPL_WELCOME(self, *args, **kwargs)

    def irc_JOIN(self, *args, **kwargs):
        self.call_plugins('irc_JOIN', *args, **kwargs)
        irc.IRCClient.irc_JOIN(self, *args, **kwargs)

    def irc_PART(self, *args, **kwargs):
        self.call_plugins('irc_PART', *args, **kwargs)
        irc.IRCClient.irc_PART(self, *args, **kwargs)

    def irc_QUIT(self, *args, **kwargs):
        self.call_plugins('irc_QUIT', *args, **kwargs)
        irc.IRCClient.irc_QUIT(self, *args, **kwargs)

    def irc_MODE(self, *args, **kwargs):
        self.call_plugins('irc_MODE', *args, **kwargs)
        irc.IRCClient.irc_MODE(self, *args, **kwargs)

    def irc_PING(self, *args, **kwargs):
        self.call_plugins('irc_PING', *args, **kwargs)
        irc.IRCClient.irc_PING(self, *args, **kwargs)

    def irc_PRIVMSG(self, *args, **kwargs):
        self.call_plugins('irc_PRIVMSG', *args, **kwargs)
        irc.IRCClient.irc_PRIVMSG(self, *args, **kwargs)

    def irc_NOTICE(self, *args, **kwargs):
        self.call_plugins('irc_NOTICE', *args, **kwargs)
        irc.IRCClient.irc_NOTICE(self, *args, **kwargs)

    def irc_NICK(self, *args, **kwargs):
        self.call_plugins('irc_NICK', *args, **kwargs)
        irc.IRCClient.irc_NICK(self, *args, **kwargs)

    def irc_KICK(self, *args, **kwargs):
        self.call_plugins('irc_KICK', *args, **kwargs)
        irc.IRCClient.irc_KICK(self, *args, **kwargs)

    def irc_TOPIC(self, *args, **kwargs):
        self.call_plugins('irc_TOPIC', *args, **kwargs)
        irc.IRCClient.irc_TOPIC(self, *args, **kwargs)

    def irc_RPL_TOPIC(self, *args, **kwargs):
        self.call_plugins('irc_RPL_TOPIC', *args, **kwargs)
        irc.IRCClient.irc_RPL_TOPIC(self, *args, **kwargs)

    def irc_RPL_NOTOPIC(self, *args, **kwargs):
        self.call_plugins('irc_RPL_NOTOPIC', *args, **kwargs)
        irc.IRCClient.irc_RPL_NOTOPIC(self, *args, **kwargs)

    def irc_RPL_MOTDSTART(self, *args, **kwargs):
        self.call_plugins('irc_RPL_MOTDSTART', *args, **kwargs)
        irc.IRCClient.irc_RPL_MOTDSTART(self, *args, **kwargs)

    def irc_RPL_MOTD(self, *args, **kwargs):
        self.call_plugins('irc_RPL_MOTD', *args, **kwargs)
        irc.IRCClient.irc_RPL_MOTD(self, *args, **kwargs)

    def irc_RPL_ENDOFMOTD(self, *args, **kwargs):
        self.call_plugins('irc_RPL_ENDOFMOTD', *args, **kwargs)
        irc.IRCClient.irc_RPL_ENDOFMOTD(self, *args, **kwargs)

    def irc_RPL_CREATED(self, *args, **kwargs):
        self.call_plugins('irc_RPL_CREATED', *args, **kwargs)
        irc.IRCClient.irc_RPL_CREATED(self, *args, **kwargs)

    def irc_RPL_YOURHOST(self, *args, **kwargs):
        self.call_plugins('irc_RPL_YOURHOST', *args, **kwargs)
        irc.IRCClient.irc_RPL_YOURHOST(self, *args, **kwargs)

    def irc_RPL_MYINFO(self, *args, **kwargs):
        self.call_plugins('irc_RPL_MYINFO', *args, **kwargs)
        irc.IRCClient.irc_RPL_MYINFO(self, *args, **kwargs)

    def irc_RPL_BOUNCE(self, *args, **kwargs):
        self.call_plugins('irc_RPL_BOUNCE', *args, **kwargs)
        irc.IRCClient.irc_RPL_BOUNCE(self, *args, **kwargs)

    def irc_RPL_LUSERCLIENT(self, *args, **kwargs):
        self.call_plugins('irc_RPL_LUSERCLIENT', *args, **kwargs)
        irc.IRCClient.irc_RPL_LUSERCLIENT(self, *args, **kwargs)

    def irc_RPL_LUSEROP(self, *args, **kwargs):
        self.call_plugins('irc_RPL_LUSEROP', *args, **kwargs)
        irc.IRCClient.irc_RPL_LUSEROP(self, *args, **kwargs)

    def irc_RPL_LUSERCHANNELS(self, *args, **kwargs):
        self.call_plugins('irc_RPL_LUSERCHANNELS', *args, **kwargs)
        irc.IRCClient.irc_RPL_LUSERCHANNELS(self, *args, **kwargs)

    def irc_RPL_LUSERME(self, *args, **kwargs):
        self.call_plugins('irc_RPL_LUSERME', *args, **kwargs)
        irc.IRCClient.irc_RPL_LUSERME(self, *args, **kwargs)

    def irc_unknown(self, *args, **kwargs):
        self.call_plugins('irc_unknown', *args, **kwargs)
        irc.IRCClient.irc_unknown(self, *args, **kwargs)

    def ctcpQuery(self, *args, **kwargs):
        self.call_plugins('ctcpQuery', *args, **kwargs)
        irc.IRCClient.ctcpQuery(self, *args, **kwargs)

    def ctcpQuery_ACTION(self, *args, **kwargs):
        self.call_plugins('ctcpQuery_ACTION', *args, **kwargs)
        irc.IRCClient.ctcpQuery_ACTION(self, *args, **kwargs)

    def ctcpQuery_PING(self, *args, **kwargs):
        self.call_plugins('ctcpQuery_PING', *args, **kwargs)
        irc.IRCClient.ctcpQuery_PING(self, *args, **kwargs)

    def ctcpQuery_FINGER(self, *args, **kwargs):
        self.call_plugins('ctcpQuery_FINGER', *args, **kwargs)
        irc.IRCClient.ctcpQuery_FINGER(self, *args, **kwargs)

    def ctcpQuery_VERSION(self, *args, **kwargs):
        self.call_plugins('ctcpQuery_VERSION', *args, **kwargs)
        irc.IRCClient.ctcpQuery_VERSION(self, *args, **kwargs)

    def ctcpQuery_SOURCE(self, *args, **kwargs):
        self.call_plugins('ctcpQuery_SOURCE', *args, **kwargs)
        irc.IRCClient.ctcpQuery_SOURCE(self, *args, **kwargs)

    def ctcpQuery_USERINFO(self, *args, **kwargs):
        self.call_plugins('ctcpQuery_USERINFO', *args, **kwargs)
        irc.IRCClient.ctcpQuery_USERINFO(self, *args, **kwargs)

    def ctcpQuery_CLIENTINFO(self, *args, **kwargs):
        self.call_plugins('ctcpQuery_CLIENTINFO', *args, **kwargs)
        irc.IRCClient.ctcpQuery_CLIENTINFO(self, *args, **kwargs)

    def ctcpQuery_ERRMSG(self, *args, **kwargs):
        self.call_plugins('ctcpQuery_ERRMSG', *args, **kwargs)
        irc.IRCClient.ctcpQuery_ERRMSG(self, *args, **kwargs)

    def ctcpQuery_TIME(self, *args, **kwargs):
        self.call_plugins('ctcpQuery_TIME', *args, **kwargs)
        irc.IRCClient.ctcpQuery_TIME(self, *args, **kwargs)

    def ctcpQuery_DCC(self, *args, **kwargs):
        self.call_plugins('ctcpQuery_DCC', *args, **kwargs)
        irc.IRCClient.ctcpQuery_DCC(self, *args, **kwargs)

    def dcc_SEND(self, *args, **kwargs):
        self.call_plugins('dcc_SEND', *args, **kwargs)
        irc.IRCClient.dcc_SEND(self, *args, **kwargs)

    def dcc_ACCEPT(self, *args, **kwargs):
        self.call_plugins('dcc_ACCEPT', *args, **kwargs)
        irc.IRCClient.dcc_ACCEPT(self, *args, **kwargs)

    def dcc_RESUME(self, *args, **kwargs):
        self.call_plugins('dcc_RESUME', *args, **kwargs)
        irc.IRCClient.dcc_RESUME(self, *args, **kwargs)

    def dcc_CHAT(self, *args, **kwargs):
        self.call_plugins('dcc_CHAT', *args, **kwargs)
        irc.IRCClient.dcc_CHAT(self, *args, **kwargs)

    def dccDoSend(self, *args, **kwargs):
        self.call_plugins('dccDoSend', *args, **kwargs)
        irc.IRCClient.dccDoSend(self, *args, **kwargs)

    def dccDoResume(self, *args, **kwargs):
        self.call_plugins('dccDoResume', *args, **kwargs)
        irc.IRCClient.dccDoResume(self, *args, **kwargs)

    def dccDoChat(self, *args, **kwargs):
        self.call_plugins('dccDoChat', *args, **kwargs)
        irc.IRCClient.dccDoChat(self, *args, **kwargs)

    def ctcpUnknownQuery(self, *args, **kwargs):
        self.call_plugins('ctcpUnknownQuery', *args, **kwargs)
        irc.IRCClient.ctcpUnknownQuery(self, *args, **kwargs)

    def ctcpMakeReply(self, *args, **kwargs):
        self.call_plugins('ctcpMakeReply', *args, **kwargs)
        irc.IRCClient.ctcpMakeReply(self, *args, **kwargs)

    def ctcpMakeQuery(self, *args, **kwargs):
        self.call_plugins('ctcpMakeQuery', *args, **kwargs)
        irc.IRCClient.ctcpMakeQuery(self, *args, **kwargs)

    def ctcpReply(self, *args, **kwargs):
        self.call_plugins('ctcpReply', *args, **kwargs)
        irc.IRCClient.ctcpReply(self, *args, **kwargs)

    def ctcpReply_PING(self, *args, **kwargs):
        self.call_plugins('ctcpReply_PING', *args, **kwargs)
        irc.IRCClient.ctcpReply_PING(self, *args, **kwargs)

    def ctcpUnknownReply(self, *args, **kwargs):
        self.call_plugins('ctcp_UnknownReply', *args, **kwargs)
        irc.IRCClient.ctcp_UnknownReply(self, *args, **kwargs)

    def badMessage(self, *args, **kwargs):
        self.call_plugins('badMessage', *args, **kwargs)
        irc.IRCClient.badMessage(self, *args, **kwargs)

    def quirkyMessage(self, *args, **kwargs):
        self.call_plugins('quirkyMessage', *args, **kwargs)
        irc.IRCClient.quirkyMessage(self, *args, **kwargs)

    def connectionMade(self, *args, **kwargs):
        self.call_plugins('connectionMade', *args, **kwargs)
        irc.IRCClient.connectionMade(self, *args, **kwargs)

    def dataReceived(self, *args, **kwargs):
        self.call_plugins('dataReceived', *args, **kwargs)
        irc.IRCClient.dataReceived(self, *args, **kwargs)

    def lineReceived(self, *args, **kwargs):
        self.call_plugins('lineReceived', *args, **kwargs)
        irc.IRCClient.lineReceived(self, *args, **kwargs)

    def handleCommand(self, *args, **kwargs):
        self.call_plugins('handleCommand', *args, **kwargs)
        irc.IRCClient.handleCommand(self, *args, **kwargs)

    def signedOn(self):
        self.call_plugins('signedOn')

        self.setNick(self.nicknames[0])

        for channel in self.channels:
            self.join(channel)

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
                plugin_method(*args, **kwargs)


    @property
    def nickname(self):
        return self.nicknames[0]

    @property
    def plugins(self):
        """ Get a list of plugins usable on this specific network. """

        plugin_list = jinzou.plugins.loader.all()

        return plugin_list

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

