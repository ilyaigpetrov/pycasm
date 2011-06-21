#
# God knows what this program does
# but pycasm has to run it well.
#

..def python(body, version):
	return adaptor.createFromType(HEX, 'B3F20D0A')

..def stamp(body, time):
	return adaptor.createFromType(HEX, '00000000')

..def argcount(body, number):
	return adaptor.createFromType(HEX, '00000000')

..def nlocals(body, number):
	return adaptor.createFromType(HEX, '00000000')

..def stacksize(body, size):
	return adaptor.createFromType(HEX, '03000000')

..def flags(body, flags):
	return adaptor.createFromType(HEX, '40000000')

..def code(body):
	# count body length in # of chars <- have to expand opcodes, that is, future transformation step is needed	
	# FUTURE: what we need is a way to take piece of
	# ast-result of some transformation stage and say "hey, convert it
	# to the end bytecode, I need it's length!"
	# for now here is a hack (which does the same as described)
	import marshal
	from pycasm.syntax import pycasmSymnameWalker
	body_ast = body
	nodes = antlr3.tree.CommonTreeNodeStream(body_ast)
	snwalker = pycasmSymnameWalker(nodes)
	new_body = snwalker.block().tree # this has to be hex + some tokens such as ROOT, BLOCK, mb more
	body_as_hex = ''.join( [h.getText() for h in new_body.children] )
	body_len = marshal.dumps(len(body_as_hex)/2)[1:].encode('hex')
	new_body.children.insert(0, adaptor.createFromType(HEX, '73'+body_len) ) # 73 is a hex code for 's'
	return new_body

..def consts(body):
	if body:
		cn = len(body.children)
	else:
		body = adaptor.nil()
		cn = 0
	import marshal
	hn = marshal.dumps(cn)[1:].encode('hex')
	body.children.insert(0, adaptor.createFromType(HEX, '28'+hn)) # 28 is hex for '('
	return body

..def None(body):
	return adaptor.createFromType(HEX, '4e')

..def names(body):
	b = adaptor.createFromType(BLOCK, 'BLOCK')
	b.addChild( adaptor.createFromType(HEX, '28') )
	b.addChild( adaptor.createFromType(HEX, '00000000') )
	return b

..def varnames(body):
	b = adaptor.createFromType(BLOCK, 'BLOCK')
	b.addChild( adaptor.createFromType(HEX, '28') )
	b.addChild( adaptor.createFromType(HEX, '00000000') )
	return b

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

.pycfile
	.python this
	.stamp now
	.codeobject
		.argcount 0				# 00 00 00 00
		.nlocals 0				# 00 00 00 00
		.stacksize 3			# 03 00 00 00
		.flags nofree			# 40 00 00 00
		.code					# 73 1A 00 00 00
			load_const 00 00 	# 01 00 00 00
			print_item 			# 47
			print_newline 		# print_newline
			load_const 01 00 	# 02 00 01 00
			return_value		# 53
		.consts					# 28 0200 0000
			s'hello pycasm'
			.None
		.names					# 28 0000 0000
		.varnames
		.freevars
		.cellvars
		.filename
			s'hello.py'
		.name
			s'<module>'
		.firstlineno
			0100 0000
		.lnotab
			s''
	.end codeobject
