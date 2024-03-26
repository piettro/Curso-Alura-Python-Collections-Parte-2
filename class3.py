dictionare = {
  "Guilherme" : 1,
  "dog" : 2,
  "name" : 2,
  "go" : 1
}

print(dictionare['Guilherme'])
print(dictionare.get('xpto',0))

del dictionare["dog"]

print(dictionare)

print('dog' in dictionare)

for i in dictionare:
    print(i)

for key, value in dictionare.items():
    print(key, value)

list_of_dictionare_keys = [f'word {key}' for key in dictionare.keys()]
print(list_of_dictionare_keys)