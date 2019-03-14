# const pipeFunctions = (...fns) => fns.reduce((f, g) => (...args) => g(f(...args)));
# from capitalize import capitalize
# from lowercase import lowercase
# from uppercase import uppercase
# from words import words

def pipeFunctions(*fns):
  i = fns[0]
  result = []

  for func in fns[1:]:
    i = func(i)
    result.append(i)

  return result