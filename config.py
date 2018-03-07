#!/usr/bin/env python

import configparser
config = configparser.ConfigParser()
config.read('settings.ini')

def get_setting(section, key):
    try:
        return config[section][key]
    except:
        return None

def get_setting_section_keys(section):
    try:
        return config.items(section)
    except:
        print("No")
        return None
