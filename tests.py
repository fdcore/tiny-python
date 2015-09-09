from tiny import Tiny

t = Tiny('5SX0TEjkR1mLOw8Gvq2VyJxIFhgCAYidrclDWaM3so9bfzZpuUenKtP74QNH6B')

print t.encode(5)
# E

print t.decode('E')
# 5

print t.encode(126)
# XX

print t.decode('XX')
# 126

print t.encode(999)
# vk

print t.decode('vk')
# 999

# Generate secret key
print t.generate_set()
# 5SX0TEjkR1mLOw8Gvq2VyJxI...
