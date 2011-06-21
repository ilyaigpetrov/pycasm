# Copyright (c) 2011, Petrov Ilya
# All rights reserved.

# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#     * Redistributions of source code must retain the above copyright
#       notice, this list of conditions and the following disclaimer.
#     * Redistributions in binary form must reproduce the above copyright
#       notice, this list of conditions and the following disclaimer in the
#       documentation and/or other materials provided with the distribution.
#     * The name of the author may not be used to endorse or promote products
#       derived from this software without specific prior written permission.

# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL PETROV ILYA BE LIABLE FOR ANY
# DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import antlr3

class StandardErrorReporter():

	def isDebug(self):
		return True

	def putErrorMessage(self, message):
		self.errorMessage = message

	def takeErrorMessage(self):
		if hasattr(self, 'errorMessage'):
			msg = self.errorMessage
		else:
			msg = ''
		self.errorMessage = ''
		return msg

	def raiseRecognitionException(self, e, message):
		self.putErrorMessage(message)
		raise e

	def reportError(self, e):
		super(self.__class__, self).reportError(e)
		raise e
		
	def getErrorMessage(self, e, tokenNames):
		debugMsg = '\n'
		message = self.takeErrorMessage()
		if message:
			debugMsg = '\nerror message: '+message+'\n'
		stack = self.getRuleInvocationStack()
		if stack:
			debugMsg = "\nantlr stack: " + str(stack) + debugMsg
		debugMsg += "type: " + e.__class__.__name__ +"\n"
		from pycasm.syntax.pycasmParser import tokenNames
		if self._state.type:
			debugMsg += 'last token matched: '+str(tokenNames[self._state.type])+'\n'
		def LT2str(i):
			'''Transorms return values of LT.'''
			if self.input.index() + i + 1 < 0:
				return '' # over the beginning
			r = self.input.LT(i)
			if isinstance(r,unicode) or isinstance(r,str):
				return r
			if r == antlr3.EOF:
				return '<EOF>'
			if isinstance(r, antlr3.Token):
				if isinstance(r.getText(), type(None)):
					return ''
				return r.getText()
			if isinstance(r, antlr3.tree.CommonTree):
				return '<'+r.toString()+'>'
			return ''
		if isinstance(e, antlr3.EarlyExitException):
			# Some repetition rule (..)+ can't be matched.
			# F.e. happens when .end without a name is encountered.
			if LT2str(-1):
				debugMsg += "previous token:" + LT2str(-1) + "\n"
			debugMsg += "hint: seems like some required token that must follow the previous accepted is missing\n"
		def hull(rawStr):
			import re
			m = re.match(r"[a-z]?[']([^']*)'?" , repr(rawStr))
			if not m:
				m = re.match(r'[a-z]?"([^"]*)"?' , repr(rawStr))
			return m.group(1) if m else ''

		inputContext = ''
		backCount = min(10, self.input.index()-1)
		for bi in range(1,backCount+1):
			s = LT2str(-bi) # If bi > index then LT is undefined.
			inputContext = s + inputContext
			if not s:
				break
		inputContext = 'context:' + hull(inputContext)
		after = ''
		forwardCount = 10
		for fi in range(1,forwardCount+1):
			s = LT2str(fi)
			after += s
			if not s or s == '<EOF>':
				break
		inputContext = '\n' + inputContext + hull(after) + '\n' + ' '*len(inputContext) + '^'
		debugMsg += "antlr message: " + super(self.__class__, self).getErrorMessage(e, tokenNames)
		debugMsg += inputContext
		msg = ''
		if self.isDebug():
			msg = debugMsg
		else:
			msg = "stumbled after '"+e.token.getText()+"', more details:\n"+debugMsg
		return msg+'\n'

	def getErrorHeader(self, e):
		line = e.line if e.line is not None else self.input.LT(1).getLine()
		column = e.charPositionInLine if e.charPositionInLine is not None else self.input.LT(1).getCharPositionInLine()
		return '\n'+self.__class__.__name__+' error: '+('in file '+self.getSourceName() if self.getSourceName() else '')+' line %s:%s' % (str(line) if line is not None else '?', str(column) if column is not None else '?')

	# Adds additional details to token string representation.
	def getTokenErrorDisplay(self, t):
		if isinstance(t, antlr3.CommonToken):
			# this patches the case when str(t) throws exception when start and stop are None
			t.start = -1 if t.start is None else t.start
			t.stop = -1 if t.stop is None else t.stop
		from pycasm.syntax.pycasmParser import tokenNames
		return str(t)+('{'+tokenNames[t.type]+'}' if t and isinstance(t.type, int) else '')

	# Rocovery methods.
	def recoverFromMismatchedToken(self, input, ttype, follow):
		#if self.isDebug():
		#	print("follow:"+str(follow)) # this could work if only I understand how to dissect follow frozenset into readable pieces
		raise antlr3.MismatchedTokenException(ttype, input)

	def recoverFromMismatchedSet(self, input, e, follow):
		print('%%%')
		if self.isDebug():
			print("follow:"+str(follow))
		raise e
