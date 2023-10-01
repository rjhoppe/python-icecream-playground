from icecream import ic

def first():
  return 'first'
def second():
  return 'second'
def third():
  return 'third'

def foo():
  ic()
  a = first()
  if a == 'first':
    ic()
    a = second()
  else:
    ic()
    a = third()

foo()