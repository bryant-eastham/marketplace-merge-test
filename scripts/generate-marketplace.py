#!/usr/bin/env python3
import json, os, sys

base_path = ".claude-plugin/marketplace-base.json"
output_path = ".claude-plugin/marketplace.json"
plugin_dir = "plugin"

if not os.path.exists(base_path):
    print(f"Error: {base_path} not found", file=sys.stderr)
    sys.exit(1)

with open(base_path, encoding="utf-8") as f:
    base = json.load(f)

plugins = []
if os.path.isdir(plugin_dir):
    for entry in sorted(os.listdir(plugin_dir)):
        plugin_json = os.path.join(plugin_dir, entry, ".claude-plugin", "plugin.json")
        if os.path.isfile(plugin_json):
            with open(plugin_json, encoding="utf-8") as f:
                plugin = json.load(f)
            plugin["source"] = f"./plugin/{entry}"
            plugins.append(plugin)

plugins.sort(key=lambda p: p.get("name", ""))

base["metadata"]["totalPlugins"] = len(plugins)
base["plugins"] = plugins

with open(output_path, "w", encoding="utf-8") as f:
    json.dump(base, f, indent=2, ensure_ascii=False)
    f.write("\n")

print(f"Generated {output_path} with {len(plugins)} plugin(s)")
