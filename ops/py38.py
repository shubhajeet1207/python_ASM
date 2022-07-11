import sys
from opcode import opmap, cmp_op
from typing import TYPE_CHECKING, Any

from ops.abc import Opcode, AbsJumpOp, RelJumpOp
if TYPE_CHECKING:
    from serializer import Label


class ROT_FOUR(Opcode):
    def __init__(self):
        super().__init__(opmap["ROT_FOUR"], 0)


if sys.version_info < (3, 9):
    class BEGIN_FINALLY(Opcode):
        def __init__(self):
            super().__init__(opmap["BEGIN_FINALLY"], 0)


class END_ASYNC_FOR(Opcode):
    def __init__(self):
        super().__init__(opmap["END_ASYNC_FOR"], 0)


if sys.version_info < (3, 9):
    class CALL_FINALLY(RelJumpOp):
        def __init__(self, arg: 'Label'):
            super().__init__(opmap["CALL_FINALLY"], arg)


    class POP_FINALLY(Opcode):
        def __init__(self, arg: bool = False):
            super().__init__(opmap["POP_BLOCK"], arg)