import fileinput
import sys
from sys import stdin

print("Hey! This is a test app to write something to stdin using standard utilities. Feel free to type something.")
stdin.write("test")
for line in fileinput.input():
    if line.lower().replace('\n', '') == 'n':
        print("Bye!")
        sys.exit(0)
    elif line.lower().replace('\n', '') == 'y':
        print("Feel free to type anything!")
        continue
    print(f'You\'ve just typed: {line}')
    print(f'Do you want to type something else? (y/n)')
