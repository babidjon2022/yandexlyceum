import sys
print(*sorted(sys.stdin.read().split(), key=lambda x: x.lower()))
