import sys


# return argument input
def parsearg(arg, standardvalue=None, type=str):
  foundarg = False
  for i,a in enumerate(sys.argv):
    if a == arg:
      index = i
      foundarg = True
      break
  if not foundarg:
    if standardvalue:
      return standardvalue
    return None
  return type(sys.argv[index+1])


# check if argument is given
def checkarg(arg):
  return arg in sys.argv
