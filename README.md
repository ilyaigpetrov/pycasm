Pycasm
------

Pycasm is an assembly language for .pyc files of CPython VM, which takes it's inspiration from [Jasmin](http://jasmin.sourceforge.net/) assembler of Java world.

How it works
------------

In short:

```
$ python pycasm.py hello.pyc.asm
```
triggers:

input.pyc.asm | pycasmLexer | pycasmParser | pycasmDirectiveWalker | pycasmGenerativeWalker | pycasmSymnameWalker | pycasmBytecodeGenerator | input.pyc

What it lives
-------------

Pycasm strives hard to breathe. Bugs have covered its whole body. It keeps a hope to be rewritten one day. Till then pycasm has nothing to do but to keep going. No matter where, no matter how. I'm here to help it to make another step.

I want to change pycasm assembly line presented above augmenting it with one new intermediate form holding PyObjects. I want it to look like:

input.pyc.asm | pycasmLexer | pycasmParser | pycasmDirectiveWalker | pycasmGenerativeWalker | pycasmSymnameWalker | pycasmPyObjectGenerator | pycasmMarshal | input.pyc

Doing so it would be possible to have multiple marshal 'codecs' inside pycasmMarshal and it would be easier to integrate pycasm with other projects (UnPyc, which has it's own PyObject class).

When it's done, disassembling part of pycasm could be worked on.

The alternative to this scheme is to create an AST form which is easily transformable to PyObject and back to assembly for purposes of disassembling.


If you have some feedback, want to collaborate or just to drop me a link:
petrov.ilya@gmail.com

Examples
--------
 Update: you have to cahnge python version tag in assembly files to make the lines below work.

 To run some examples: 'hello pycasm', greate common divisor, factorial, -- do:
 ```
 G:\pycasm_\src\python> python pycasm.py hello.pyc.asm
 G:\pycasm_\src\python> python hello.pyc
 hello pycasm
 G:\pycasm_\src\python> python pycasm.py fact.pyc.asm
 G:\pycasm_\src\python> python fact.pyc
 24
 G:\pycasm_\src\python> python pycasm.py nod.pyc.asm
 G:\pycasm_\src\python> python nod.pyc
 7
 G:\pycasm_\src\python> rm *.pyc
 ```.
 To generate all recognizers (lexer, parser and so) and run tests on then:
 ```
 G:\pycasm_\tests> python .\test_them_all_python.py
 ```.
 To run tests:
 ```
 G:\pycasm_\tests> python .\TestPycasm.py
 ```.
