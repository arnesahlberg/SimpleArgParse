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


# return argument input where several arguments are valid, 
# i.e. -i or --input cound mean the same thing. then call
# parseargs(["-i", "--input"]
def parseargs(args, standardvalue=None, type=str):
  for arg in args:
    parsed = parsearg(arg, standardvalue=standardvalue, type=type)
    if parsed is not None:
      return parsed
  return None # if none of the arguments were found


# check if argument is given
def checkflag(arg):
  return arg in sys.argv


# check any of a list of arguments are given
def checkflags(args):
  for arg in args:
    check = checkflag(arg)
    if check:
      return True
  return False
  


# main mehtod for testing
if __name__ == "__main__":
  a = parseargs(["-i", '--input'])
  if a is not None:
    print("Input", a, "given.")

  b = checkflags(["-f", "--flag"])
  if b:
    print("Found flag -f or --flag.")


