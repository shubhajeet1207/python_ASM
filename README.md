# python_asm 

python_ASM is a python project which is designed to help modify bytecode in a little bit easy manner.
The API design is loosely based on `objectweb:asm` for Java.

## 📌 Features

### 🚩 Deconstruct code objects

You can use the `Deserializer` class to convert a code object into a list of opcodes

```python
>>> def my_function(x: int = 1) -> int:
...     if x > 20:
...         return x / 20
...     return x
... 
>>> deserializer = Deserializer(my_function.__code__)
>>> deserializer.deserialize()  # Below is formatted for readability
[
    LOAD_FAST(id=124, arg='x'), 
    LOAD_CONST(id=100, arg=20), 
    COMPARE_OP(id=107, arg=4), 
    POP_JUMP_IF_FALSE(id=114, arg=Label(0x7fd2fbeb0d60)), 
    LOAD_FAST(id=124, arg='x'), 
    LOAD_CONST(id=100, arg=20), 
    BINARY_TRUE_DIVIDE(id=27, arg=0), 
    RETURN_VALUE(id=83, arg=0), 
    Label(0x7fd2fbeb0d60), 
    LOAD_FAST(id=124, arg='x'), 
    RETURN_VALUE(id=83, arg=0)
]
```

### 🚩 Construct code objects

Conversely, you can also turn a list of opcodes into a code object using `Serializer`

```python
>>> dummy = lambda x: None
>>> serializer = Serializer([   # Bytecode for `return x * 20`
...     LOAD_FAST("x"),
...     LOAD_CONST(20),
...     BINARY_MULTIPLY(),
...     RETURN_VALUE()
... ], dummy.__code__)
>>> dummy.__code__ = serializer.serialize()
>>> dummy(10)
200
```

### 🚩 Jumps

A big issue when modifying bytecode is jumps. We solve this by using `Label`:

```python
>>> lbl = Label()
>>> ops = [
...     LOAD_CONST(10),
...     LOAD_CONST(20),
...     COMPARE_OP("<"),
...     POP_JUMP_IF_FALSE(lbl),     # jump to where lbl is located
...     LOAD_CONST(True),
...     RETURN_VALUE(),
...     lbl,                        # jump to here
...     LOAD_CONST(False),
...     RETURN_VALUE()
... ]
```

This way, no matter how many instructions you place between the jump and the label, it will always resolve correctly 👦🏻👍🏻.
