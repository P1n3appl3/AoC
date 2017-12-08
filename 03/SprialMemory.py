from math import sqrt

n = 347991

ring = 0
while 4 * (ring**2 + ring) < n:
    ring += 1
ring -= 1
temp = n - 4 * (ring**2 + ring) - 1

print "Part 1:", ring * 2 + sum(([1] + [-1] * ring + ([1] * (ring + 1) + [-1] * (ring + 1)) * 3 + [1] * (ring + 1))[:temp])
