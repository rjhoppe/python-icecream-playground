from icecream import ic

# When you want to disable
# ic.disable()
test_int = 120
test_str = 'test'

ic(test_int)
ic(test_str)

def first():
  return 'first'
def second():
  return 'second'
def third():
  return 'third'


def foo_ic():
  ic()
  a = third()
  if a == 'first':
    ic()
    a = second()
  else:
    ic()
    a = third()

foo_ic()