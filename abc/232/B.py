S = input()
T = input()

# a = chr(97)
# z = chr(122)
# ord('a') = 97
# ord('z') = 122

se = set()
for s, t in zip(S, T):
    se.add((ord(s) - ord(t)) % 26)
print('Yes' if len(se) == 1 else 'No')
