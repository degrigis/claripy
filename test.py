import nose
import logging
l = logging.getLogger("claripy.test")

import claripy, claripy.backends

def test_actualization():
    ba = claripy.backends.BackendAbstract()
    bc = claripy.backends.BackendConcrete()
    a = claripy.E([ba], obj=5, variables=set(), symbolic=False)
    b = a+a
    b.actualize([bc])
    nose.tools.assert_equal(b._obj, 10)

#def test_fallback_abstraction():
#   ba = claripy.backends.BackendAbstract()
#   bc = claripy.backends.BackendConcrete()
#   a = claripy.expressions.Expression([bc, ba], obj=5, variables=set(), symbolic=False)
#   b = claripy.expressions.Expression([bc, ba], obj=claripy.expressions.AbstractCall(op='BitVec', args=('x', 32)), variables={'x'}, symbolic=True)
#
#   b = a+a
#   b.actualize([bc])
#   nose.tools.assert_equal(b._obj, 10)
#
#def test_expressions():
#   # to and from actual
#   a = claripy.expressions.AbstractExpression(op='BitVec', args=('x', 32), variables={'x'}, symbolic=True)
#   z = claripy.backends.BackendZ3()
#   b = a.actualize(z)
#   c = b+b
#   nose.tools.assert_equal(str(c), 'ActualExpression(x + x)')
#   d = c.abstract().actualize(z)
#   nose.tools.assert_true(d.symbolic)
#   nose.tools.assert_equal(str(d), str(c))
#
#   # concrete stuff
#   #b_c = claripy.backends.BackendConcrete()
#   #a = claripy.expressions.AbstractExpression(op='BitVecVal', args=(0, 32), variables=set(), symbolic=False)
#   #b = claripy.expressions.AbstractExpression(op='BitVecVal', args=(1, 32), variables=set(), symbolic=False)
#   #b = a.actualize(z)
#   #c = b+b
#   #nose.tools.assert_equal(str(c), 'ActualExpression(x + x)')
#   #d = c.abstract().actualize(z)
#   #nose.tools.assert_equal(str(d), str(c))

if __name__ == '__main__':
    test_actualization()
    print "WOO"
