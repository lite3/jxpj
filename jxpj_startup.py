#!/bin/python
# -*- coding: utf-8 -*-

import os
import time
import traceback
import jxpj

time.sleep(10)
try:
    jxpj.dojxpj()
except Exception, e:
    traceback.print_exc()
    print '程序出问题，请联系QQ：735486078'
    os.system('pause')

