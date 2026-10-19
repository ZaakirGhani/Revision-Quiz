def mike():
    print('mike')

def dia():
    print('dia')

dictionary = {
    '1':mike,
    '2':dia,
    'problem solving':mike,
    'programming':dia
}

u = input(':')

two = dictionary.get(u)

if two:
    two()
else:
    print('all_index')