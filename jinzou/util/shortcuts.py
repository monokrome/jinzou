def get_command_string(command):
    from jinzou.util.config import settings

    return settings['core']['command_format'].format(command)

def get_reply_destination(client, user, channel):
    if channel == client.nickname:
        source = user.split('!', 1)[0]
    else:
        source = channel

    return source

