dictionary_file = open("slowa.txt")
words = dictionary_file.read().split('\n')

def generate_subsets(char_list, left, generated=""):
  if left == 0:
    yield generated

  for char in char_list:
    new_list = char_list.copy()
    new_list.remove(char)
    yield from generate_subsets(new_list, left-1, generated + char)

def apply_pattern(pattern, word):
  for c in word:
    pattern = pattern.replace('.', c, 1)

  return pattern


pattern = ""
letters = ""

while True:
  letters = input()
  while True:
    pattern = input()
    if pattern == ',':
      break
    char_set = [l for l in letters]
    for l in [i for i in pattern if i != '.']:
      try:
        char_set.remove(l)
      except ValueError:
        print("nie da się ułożyć słowa")
        break

    subsets = generate_subsets(char_set, pattern.count('.'))
    
    print()

    for s in subsets:
      s = apply_pattern(pattern, s)
      if s in words:
        print(s)

    print("=== koniec ===")
