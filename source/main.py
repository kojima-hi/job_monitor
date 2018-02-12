#!/bin/usr/env python
# -*- coding: utf-8 -*-
import sys
from IO import get_stat_command, get_mail_address
from monitor import monitoring


def main():
    argv = sys.argv
    argc = len(argv)

    if argc != 2 + 1:
        sys.exit('Usage: $ python main.py \"server name\" \"monitoring string\"')

    _, sname, monitor_str = argv

    monitor_command = get_stat_command(sname)
    mail_address = get_mail_address()

    monitoring(monitor_command, monitor_str, sname, mail_address)

    return


if __name__ == "__main__":
    main()
