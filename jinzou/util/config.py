import json

def load(filename):
    """ Receives a filename and returns it's parsed JSON object. """

    data_file = open('configuration/%s.json' % filename, 'r')
    data = json.load(data_file)
    data_file.close()

    del data_file
    return data

# Get our IRC network list
networks = load('networks')

# Get information about our bot loaduration
settings = load('settings')

