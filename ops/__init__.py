import dis

from ops.abc import *
from ops.py30 import *

if sys.version_info >= (3, 1, 0):
    from ops.py31 import *

if sys.version_info >= (3, 2, 0):
    from ops.py32 import *

if sys.version_info >= (3, 3, 0):
    from ops.py33 import *

if sys.version_info >= (3, 4, 0):
    from ops.py34 import *

if sys.version_info >= (3, 5, 0):
    from ops.py35 import *

if sys.version_info >= (3, 6, 0):
    from ops.py36 import *

if sys.version_info >= (3, 7, 0):
    from ops.py37 import *

if sys.version_info >= (3, 8, 0):
    from ops.py38 import *

if sys.version_info >= (3, 9, 0):
    from ops.py39 import *

if sys.version_info >= (3, 10, 0):
    from ops.py310 import *

if sys.version_info >= (3, 11, 0):
    from ops.py311 import *

ALL_OPS = {v: eval(k) for k, v in opmap.items()}

__all__ = tuple(dis.opmap.keys()) + (
    "Opcode", "JumpOp", "RelJumpOp", "AbsJumpOp",
    "NameOp", "VarOp", "ConstOp", "CellOp", "MultiOp"
)