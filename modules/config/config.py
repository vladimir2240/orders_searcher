import configparser

def settings(config) -> dict:
    # If adding any other config rules, describe them here
    quotes = config['PairsPreset'].get('quotes', list())
    if quotes:
        quotes = quotes.replace(' ', '').split(',')
    else:
        quotes = list()
    current_pairs = config['PairsPreset'].get('exact_pairs', list())
    if current_pairs:
        # Delete trash from config preset (spaces, lower letters)
        current_pairs = current_pairs.replace(' ', '').upper().split(',')
    else:
        current_pairs = list()
    volume_multiplicator = float(config['VolumesPreset'].get('volume_multiplicator', 1000).replace(' ', ''))
    return {'quotes': quotes, 'exact_pairs': current_pairs, 'volume_multiplicator': volume_multiplicator}

def init_config() -> dict:
    '''
    :return: Dict of rules, where keys are config value, values for quotes are quotes :)
    Current pairs are exact pairs that needs to be added to the scanner
    '''

    config = configparser.ConfigParser()
    # While creating .env, create general dir to config!
    config.read("config.ini")
    return settings(config)
