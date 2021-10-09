import re
import sys

for line in sys.stdin:
    print(re.sub(r'(\S+) (że|aby|jak[iaą]|któr[zaey])', r'\1, \2', line.rstrip()))
