#!/bin/usr/env python
# -*- coding: utf-8 -*-
import sys
import os
import subprocess
from setting import setting


def get_monitoring_output(sname, command):
    cmd = ['ssh', sname, command]
    return (subprocess.check_output(cmd)).decode('utf-8')


def monitoring(command, monitor_str, sname, mail_address):
    interval = setting()

    output = get_monitoring_output(sname, command)
    if monitor_str not in output:
        sys.exit('monitoring string is not found!')

    while True:
        output = get_monitoring_output(sname, command)
        if monitor_str not in output:
            cmd = "echo \"\" | mail -s \"Monitoring at " + sname + " is ended\" " + mail_address
            os.system(cmd)
            break
        os.system("sleep " + interval)

    return


def main():
    return


if __name__ == "__main__":
    main()