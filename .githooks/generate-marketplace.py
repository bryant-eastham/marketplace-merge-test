#!/usr/bin/env python3
import json, os, sys

base_path = ".claude-plugin/marketplace-base.json"
output_path = ".claude-plugin/marketplace.json"
plugin_dir = "plugin"

if not os.path.exists(base_path):
    print(f"Error: {base_path} not found", file=sys.stderr)
    sys.exit(1)

with open(base_path) as f:
    base = json.load(f)

plugin_files = sorted(os.listdir(plugin_dir)) if os.path.isdir(plugin_dir) else []
plugin_files = [p for p in plugin_files if os.path.isfile(os.path.join(plugin_dir, p))]

base["metadata"]["totalPlugins"] = len(plugin_files)
base["plugins"] = plugin_files

with open(output_path, "w") as f:
    json.dump(base, f, indent=2)
    f.write("\n")

print(f"Generated {output_path} with {len(plugin_files)} plugin(s)")
