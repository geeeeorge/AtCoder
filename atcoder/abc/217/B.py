a = input()
b = input()
c = input()

g = ['ABC', 'ARC', 'AGC', 'AHC']

for gn in g:
    if gn not in [a, b, c]:
        print(gn)
