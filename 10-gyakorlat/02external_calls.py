#!/usr/bin/env python
# -*- coding: utf-8 -*-
import subprocess
from subprocess import PIPE


# command = ["ls", "-l"]
command = ["echo", "Jo reggelt!"]

# https://github.com/aeroxis/sultan
if __name__ == '__main__':
    try:
        output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT).decode()

    except subprocess.CalledProcessError as e:
        output = e.output.decode()

    print('Process output', output)

    subprocess.call(["echo", "Masodik jo reggelt!"], shell=True)

    p = subprocess.Popen(['echo', 'Szevasz!'], shell=True, stdin=PIPE, stdout=PIPE, stderr=PIPE)
    output, err = p.communicate(b"input from stdin")
    return_code = p.returncode
    print('return code', return_code)
    print('output', output)
    print('error', err)

    # If you need to check the output (retrieve the result string):
    #   output = subprocess.check_output(args ....)
    #
    # If you want to wait for execution to end before proceeding:
    #   exitcode = subprocess.call(args ....)
    #
    # If you need more functionality like setting environment variables,
    # use the underlying Popen constructor:
    #   subprocess.Popen(args ...)
    #
    # source: https://stackoverflow.com/a/26236441/5738367

    # Legegyszerubb mod, Python 3.5 ota.
    # Lehetoseg szerint ezt hasznaljuk:
    # https://docs.python.org/3/library/subprocess.html#using-the-subprocess-module
    command = ['echo', 'hello']
    result = subprocess.run(command, shell=True, stdout=PIPE, stderr=PIPE, universal_newlines=True)
    print(result.returncode, result.stdout, result.stderr)
