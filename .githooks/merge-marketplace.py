#!/usr/bin/env python3
import json, sys

ancestor_file, our_file, their_file = sys.argv[1], sys.argv[2], sys.argv[3]

def load(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)

def plugin_name(p):
    return p.get("name", "") if isinstance(p, dict) else str(p)

ancestor = load(ancestor_file)
ours = load(our_file)
theirs = load(their_file)

anc_plugins = ancestor.get("plugins", [])
our_plugins = ours.get("plugins", [])
their_plugins = theirs.get("plugins", [])

anc_names = {plugin_name(p) for p in anc_plugins}
our_names = {plugin_name(p) for p in our_plugins}
their_names = {plugin_name(p) for p in their_plugins}

by_name = {}
for p in anc_plugins:
    by_name[plugin_name(p)] = p
for p in our_plugins:
    by_name[plugin_name(p)] = p
for p in their_plugins:
    by_name[plugin_name(p)] = p

all_names = sorted(anc_names | our_names | their_names)

merged_plugins = [by_name[n] for n in all_names]

merged = ancestor
merged["plugins"] = merged_plugins
merged["metadata"]["totalPlugins"] = len(merged_plugins)

with open(our_file, "w", encoding="utf-8") as f:
    json.dump(merged, f, indent=2, ensure_ascii=False)
    f.write("\n")

sys.exit(0)
