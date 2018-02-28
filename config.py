#!/usr/bin/env python

import configparser
config = configparser.ConfigParser()
config.read('settings.ini')

def get_setting(section, key):
    try:
        return config[section][key]
    except:
        return None
