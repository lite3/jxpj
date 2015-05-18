#!/bin/python
# -*- coding: utf-8 -*-

import os, os.path
import time
import traceback
import jxpj
import sys
import subprocess

reload(sys)
sys.setdefaultencoding('utf-8')


def create_lnk(lnkpath, targetpath):
    print u'\n\n\t该程序可能会触发安全软件提醒，请选择允许运行！\n\n'
    # time.sleep(3)
    vbspath = os.path.join(sys.path[0], 'startup.vbs')
    command = 'cmd /c ""%s" "%s" "%s""' % (vbspath, lnkpath, targetpath)
    # try:
    subprocess.check_output(command)
    # except :
    #     pass
    

def check_start_at_login():
    if sys.platform != 'win32':
        print u'目前仅支持windows开机自启动！'
        return

    lnkpath = os.environ['USERPROFILE']
    lnkpath = os.path.join(lnkpath, r'AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup')
    lnkpath = os.path.join(lnkpath, 'startup.py.lnk')
    # lnkpath = lnkpath.replace('\\', '/')

    while not os.path.exists(lnkpath):
        targetpath = os.path.join(sys.path[0], 'startup.py')
        # targetpath = targetpath.replace('\\', '/')
        create_lnk(lnkpath, targetpath)


# -------------- main --------------
if __name__ == '__main__':
    time1 = time.time()

    check_start_at_login()

    t = 10 - int(time.time() - time1)
    if t > 1:
        print u'\t为了避免刚启动时网络还未正常连接，请等待', t, u'秒'
        time.sleep(t)


    print u'\t正在评分，请稍后。。。'

    try:
        jxpj.dojxpj()
    except Exception, e:
        traceback.print_exc()
        print u'程序出问题，请联系QQ：735486078'
        os.system('pause')

