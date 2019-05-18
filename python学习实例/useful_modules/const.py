class _const:
    class ConstErroe(TypeError): pass

    def __setattr__(self, name, value):
        if name in self.__dict__:
            raise self.ConstErroe("Can't rebind const %s" %name)
        self.__dict__[name] = value

import sys

const = _const()
sys.modules[__name__] = const

# 常量在下面定义
