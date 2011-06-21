
..def python(body, version):
	import imp
        return adaptor.createFromType(HEX, imp.get_magic().encode('hex'))

..def stamp(body, time):
        return adaptor.createFromType(HEX, '00000000')

..def argcount(body, number):
        return adaptor.createFromType(HEX, marshal.dumps(int(number.children[0].getText()))[1:].encode('hex'))

..def nlocals(body, number):
        return adaptor.createFromType(HEX, marshal.dumps(int(number.children[0].getText()))[1:].encode('hex'))

..def stacksize(body, size):
        return adaptor.createFromType(HEX, marshal.dumps(int(size.children[0].getText()))[1:].encode('hex'))

..def flags(body, flags=None):
	if flags is not None:
	        return adaptor.createFromType(HEX, '40000000')
	else:
		return body

..def code(body):
        import marshal
        from pycasm.syntax import pycasmSymnameWalker
        body_ast = body
        nodes = antlr3.tree.CommonTreeNodeStream(body_ast)
        snwalker = pycasmSymnameWalker(nodes)
        new_body = snwalker.block().tree
        body_as_hex = ''.join( [h.getText() for h in new_body.children] )
        body_len = marshal.dumps(len(body_as_hex)/2)[1:].encode('hex')
        new_body.children.insert(0, adaptor.createFromType(HEX, '73'+body_len) )
        return new_body

..def consts(body):
        if body:
                cn = len(body.children)
        else:
                body = adaptor.nil()
                cn = 0
        import marshal
        hn = marshal.dumps(cn)[1:].encode('hex')
        body.children.insert(0, adaptor.createFromType(HEX, '28'+hn))
        return body

..def None(body):
        return adaptor.createFromType(HEX, '4e')

..def names(body):
	if body is None:
		body = adaptor.createFromType(BLOCK,'BLOCK')
	h = adaptor.createFromType(HEX,'')
	import marshal
	h.token.setText('28'+(marshal.dumps(len(body.children))[1:].encode('hex') if body.children else '00000000'))
	body.children.insert(0, h)
	return body

..def varnames(body):
	if body is None:
		body = adaptor.createFromType(BLOCK,'BLOCK')
	h = adaptor.createFromType(HEX,'')
	import marshal
	h.token.setText('28'+(marshal.dumps(len(body.children))[1:].encode('hex') if body.children else '00000000'))
	body.children.insert(0, h)
	return body

..def freevars(body):
        b = adaptor.createFromType(BLOCK, 'BLOCK')
        b.addChild( adaptor.createFromType(HEX, '28') )
        b.addChild( adaptor.createFromType(HEX, '00000000') )
        return b

..def cellvars(body):
        b = adaptor.createFromType(BLOCK, 'BLOCK')
        b.addChild( adaptor.createFromType(HEX, '28') )
        b.addChild( adaptor.createFromType(HEX, '00000000') )
        return b

..def filename(body):
        return body

..def name(body):
        return body

..def firstlineno(body):
        return adaptor.createFromType(HEX, '01000000')

..def lnotab(body):
        return body

..def int(body, value):
	int_as_str = value.children[0].toString()[1:-1]
	import re
	int_as_str = re.match(r'(\d+)', int_as_str).group(1)
	import marshal
	return adaptor.createFromType(HEX, marshal.dumps(int(int_as_str)).encode('hex'))

..def str(body, value):
	str_as_uni = value.children[0].toString()[2:-2]
	import marshal
	return adaptor.createFromType(HEX, marshal.dumps(str(str_as_uni)).encode('hex'))


.python this
.stamp now
.codeobject
	.argcount 0
	.nlocals 0
	.stacksize 3
	.flags nofree
	.code
		load_const 0000
		make_function 0000
		store_name 0000
		load_name 0000
		load_const 0100
		load_const 0200
		call_function 0200
		print_item
		print_newline
		load_const 0300
		return_value
	.consts
		.codeobject
			.argcount 2
			.nlocals 3
			.stacksize 3
			.flags
				43000000
			.code
				load_global 0000
				load_fast 0000
				call_function 0100
				load_global 0000
				load_fast 0100
				call_function 0100
				rot_two
				store_fast 0000
				store_fast 0100
				load_fast 0000
				load_fast 0100
				binary_modulo
				store_fast 0200
				setup_loop 2200
				load_fast 0200
				jump_if_false 1a00
				pop_top
				load_fast 0100
				store_fast 0000
				load_fast 0200
				store_fast 0100
				load_fast 0000
				load_fast 0100
				binary_modulo
				store_fast 0200
				jump_absolute 2600
				pop_top
				pop_block
				load_fast 0100
				return_value
			.consts
				.None
			.names
				.str('int')
			.varnames
				.str('a')
				.str('b')
				.str('c')
			.freevars
			.cellvars
			.filename
				.str('nod.py')
			.name
				.str('nod')
			.firstlineno
				04000000
			.lnotab
				73
				0e000000
				00011901
				0a010a01
				06010601
				0f01
		.int(28)
		.int(21)
		.None
	.names
		.str('nod')
	.varnames
	.freevars
	.cellvars
	.filename
		.str('nod.py')
	.name
		.str('<module>')
	.firstlineno
		04000000
	.lnotab
		73
		02000000
		0909
0a
