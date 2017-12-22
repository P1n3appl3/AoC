generators = [512, 191]
factors = (16807, 48271)
divisor = 2147483647

total = 0
for i in range(40000000):
    for j in range(2):
        generators[j] = generators[j] * factors[j] % divisor
    total += generators[0] & 0xFFFF == generators[1] & 0xFFFF

print "Part 1:", total
