def pipeFunctions(*fns):
  i = fns[0]
  result = []

  for func in fns[1:]:
    i = func(i)
    result.append(i)

  return result