class Solution:
    def hammingDistance(self, x: int, y: int):
        xb = bin(x)
        yb = bin(y)


x = 5
y = 54721
xb = bin(x)[2:].zfill(4)
yb = bin(y)[2:].zfill(4)

print(xb, yb)
