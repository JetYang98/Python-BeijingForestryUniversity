class _const:
    class ConstError(TypeError): pass

    def __setattr__(self, name, value):
        if name in self.__dict__:
            raise self.ConstError("Can't rebind const %s" %name)
        self.__dict__[name] = value

import sys

const = _const()
sys.modules[__name__] = const

# 常量在下面定义
