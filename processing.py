#Part 1
def max_value(data, key):
 acc = ""
 for dict in data:
  if acc < dict[key]:
   acc = dict[key]
 return acc

def init_dictionary(data, key):
  acc = {}
  for dict in data:
    if key in dict.keys():
      v = dict[key]
      acc[v] = 0
  return acc

def sum_matches(data, key, value1, key2):
  acc = 0
  for dict in data:
    if dict[key] == value1:
      acc += dict[key2]
  return acc

def copy_matching(data,key, value):
  acc = []
  for dict in data:
    if dict[key] == value:
      acc.append(dict)
  return acc
