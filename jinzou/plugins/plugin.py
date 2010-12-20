from zope.interface import Interface, Attribute

class JinzouPlugin(Interface):
    def signedOn(client):
        pass

