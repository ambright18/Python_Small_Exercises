# a pyton exercise to check whether a system is big-endian or little-endian
import sys

print()

#let's use an if statment to check if the byte order of the platform is little or big

if sys.byteorder == "little":
    print("Little-endian platform.")
else:
    print("Big-endian platform")

print()