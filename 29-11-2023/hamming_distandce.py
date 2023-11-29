class Solution:
    def hammingDistance(self, x: int, y: int):
        xb = bin(x)
        yb = bin(y)


x = 5
y = 8
xb = bin(x)[2:].zfill(8)
yb = bin(y)[2:].zfill(8)

print(xb, yb)
