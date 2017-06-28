#!/usr/bin/env python
import os
cmd = 'ls -l'

print os.getcwd()
for line in os.popen(cmd).readlines():
    print line,
