import re

A, B = map(int, input().split())
S = input()

# f-string と raw string literal を組み合わせる
# {{}} で {} をエスケープする
print('Yes' if re.fullmatch(fr'\d{{{A}}}-\d{{{B}}}', S) else 'No')
