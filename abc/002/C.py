xa, ya, xb, yb, xc, yc = map(int, input().split())

# xa, yaを原点に移動
xb -= xa
xc -= xa

yb -= ya
yc -= ya

# 三角形ABCの面積を求める
square = float(abs(xb*yc - yb*xc)) / 2.
print(square)
