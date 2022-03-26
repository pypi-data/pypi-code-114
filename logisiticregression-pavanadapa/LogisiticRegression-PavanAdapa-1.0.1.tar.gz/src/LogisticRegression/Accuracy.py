def accuracy(results, test):
  matches = 0
  for i in range(0, len(results)):
    if results[i] == test[i]:
      matches += 1
  return matches/len(results)