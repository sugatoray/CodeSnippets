# Sanity check
print("Hello World")

# Some nonsense class
class WhatIs(object):
	question: str = None
	answer:  str = None

	def __init__(self, question: str=None, answer: str=None):
		self.question = question
		self.answer = answer

	def __repr__(self):

		s = "{name}(question={question}, answer={answer})"
		return s.format(
			name = self.__class__.__name__, 
			question = self.question, 
			answer = self.answer
		)

	def __call__(self):
		return self.answer

# Update question and answer
whatis = WhatIs(
	question="What is your address?", 
	answer="2000 W. Allen Rd., Riverdale XX 12345"
)

# Returns the answer
whatis()

##############################################################