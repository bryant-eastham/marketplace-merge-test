#!/usr/bin/env python3
import json, sys

ancestor_file, our_file, their_file = sys.argv[1], sys.argv[2], sys.argv[3]

def load(path):
    with open(path) as f:
        return json.load(f)

ancestor = load(ancestor_file)
ours = load(our_file)
theirs = load(their_file)

anc_plugins = ancestor.get("plugins", [])
our_plugins = ours.get("plugins", [])
their_plugins = theirs.get("plugins", [])

our_additions = [p for p in our_plugins if p not in anc_plugins]
their_additions = [p for p in their_plugins if p not in anc_plugins]

seen = set()
merged_plugins = []
for p in anc_plugins + our_additions + their_additions:
    if p not in seen:
        seen.add(p)
        merged_plugins.append(p)

merged = ancestor
merged["plugins"] = merged_plugins
merged["metadata"]["totalPlugins"] = len(merged_plugins)

with open(our_file, "w") as f:
    json.dump(merged, f, indent=2)
    f.write("\n")

sys.exit(0)
