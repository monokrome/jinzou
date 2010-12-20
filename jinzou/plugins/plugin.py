from zope.interface import Interface, Attribute

class JinzouPlugin(Interface):
    def __init__(self):

        # By default, a plugin's name is it's classname converted to lowercase
        if not hasattr(self, 'name'):
            self.name = self.__class__.__name__.lower()

