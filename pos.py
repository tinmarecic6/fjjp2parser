from pyparsing import *


x = Word(alphas)
parsR = Forward()
pars = '(' + x + parsR + ZeroOrMore(parsR) + ')'
parsR <<= pars | x

s = "(bla (asd (s (a ks))) (a (r f) (s t)))"
for match in pars.scanString(s):
	print(match[0])