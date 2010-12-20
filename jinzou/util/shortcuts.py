def get_command_string(command):
    from jinzou.util.config import settings

    return settings['core']['command_format'].format(command)

