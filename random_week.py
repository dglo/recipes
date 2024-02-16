#!/usr/bin/env python

import os
import random
import sys


if len(sys.argv) > 1:
    try:
        num = int(sys.argv[1])
    except ValueError:
        raise sys.exit("Bad number of lines \"%s\"" % (sys.argv[1], ))
else:
    num = 30

filelist = []
for entry in os.listdir(os.path.join(os.environ["HOME"], "recipes")):
    if not os.path.isfile(entry):
        continue
    if entry.startswith("."):
        continue
    if entry.endswith(".py"):
        continue
    if entry == "README.md":
        continue
    if entry == "meals":
        continue
    if entry == "simple_meals":
        with open(entry, "r") as fin:
            for line in fin:
                filelist.append("[" + line.rstrip() + "]")
        continue
    filelist.append(entry)

print("Found %d entries" % len(filelist), file=sys.stderr)

# make sure we don't try to print more than the total number of meals
#
if len(filelist) < num:
    num = len(filelist)

#random.seed()

final = []
for xxx in range(num):
    try:
        idx = random.randint(0, len(filelist) - 1)
    except ValueError:
        raise sys.exit("Cannot get entry from %d-entry list" % len(filelist))
    final.append(filelist[idx])
    del filelist[idx]

for name in sorted(final):
    print(name)
