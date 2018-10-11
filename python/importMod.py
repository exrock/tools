#!/usr/bin/env python3
# 如果模块存在则导入，否则安装后导入

def importMod(moduleName):
    from importlib import import_module
    try:
        return import_module(moduleName)
    except:
        import os
        os.system('pip install %s' % moduleName)
        return import_module(moduleName)
