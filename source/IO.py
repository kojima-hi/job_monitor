#!/bin/usr/env python
# -*- coding: utf-8 -*-
import os
import sys
import json


def get_command_dict():
    script_path = os.path.dirname(os.path.abspath(__file__))
    command_dict_path = os.path.join(script_path, '../data/command_dict.txt')

    f = open(command_dict_path, 'r')
    return json.load(f)


def get_mail_address():
    script_path = os.path.dirname(os.path.abspath(__file__))
    command_dict_path = os.path.join(script_path, '../data/mail_address.txt')

    f = open(command_dict_path, 'r')
    return f.readline().strip()


def get_stat_command(sname):
    command_dict = get_command_dict()

    if not sname in command_dict.keys():
        print(command_dict)
        sys.exit('%s is not registered as server name'%(sname))

    return command_dict[sname]


def main():
    return


if __name__ == "__main__":
    main()