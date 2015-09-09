# Tiny for Python

A reversible base62 ID obfuscater

Tiny is a two-way integer obfuscator that converts integers to a string of characters, and a string of characters to an integer. This gives developers the ability to expose unique identifiers for resources in APIs that does not reveal the number of records in your database if you index your records using auto-incrementing primary keys. See the Usage section below for how easy it is to use!

Inspired https://github.com/zackkitzmiller/tiny-php

## Usage

```python
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
```

## Configuration

You must instanciate a new instance of Tiny with a random alpha-numeric set where each character must only be used exactly once. Do NOT change this once you start using Tiny, as you won't be able to reverse.
