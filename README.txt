Java branch is obsolete but I still use it to compare with python implementation in buggy situations.

If you have some feedback, want to collaborate or just to drop me a link:
petrov.ilya@gmail.com

__END__

 To run some examples: 'hello pycasm', greate common divisor, factorial, -- do:
 `
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
 `.
 To generate all recognizers (lexer, parser and so) and run tests on then:
 `
 G:\pycasm_\tests> python .\test_them_all_python.py
 `.
 To run tests:
 `
 G:\pycasm_\tests> python .\TestPycasm.py
 `.