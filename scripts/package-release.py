"""Build host-specific upload archives without credentials or stale skills."""
import argparse
import hashlib
import json
from pathlib import Path
import zipfile

parser = argparse.ArgumentParser()
parser.add_argument("output", type=Path)
args = parser.parse_args()
root = Path(__file__).resolve().parents[1]
args.output.mkdir(parents=True, exist_ok=True)
config = json.loads((root / ".mcp.json").read_text())
config["mcpServers"]["origami"].pop("type", None)
openai = json.loads((root / ".codex-plugin/plugin.json").read_text())
claude = json.loads((root / ".claude-plugin/plugin.json").read_text())
assert openai["name"] == claude["name"] == "origami-campaign-drafts"
assert openai["version"] == claude["version"] == "0.2.0"
assert config["mcpServers"]["origami"]["url"] == "https://origami.chat/mcp"
assert "origami:plugin" in config["mcpServers"]["origami"]["extensions"]["com.openai"]["auth"]["baseScopes"]
cases = openai["extensions"]["com.openai"]["review"]["test_cases"]
tools = set(json.loads((root / "review/anthropic-listing.json").read_text())["tools"])
assert len(cases["positive"]) == 5
assert len(tools) == 27
for case in cases["positive"]:
    assert all(tool.strip() in tools for tool in case["tools_triggered"].split(","))

for host, manifest in [("openai", ".codex-plugin/plugin.json"), ("anthropic", ".claude-plugin/plugin.json")]:
    archive = args.output / f"{host}-origami-0.2.0-candidate.zip"
    # Claude's HTTP transport config does not consume OpenAI extension fields.
    mcp = config if host == "openai" else {"mcpServers": {"origami": {"type": "http", "url": "https://origami.chat/mcp"}}}
    with zipfile.ZipFile(archive, "w", zipfile.ZIP_DEFLATED) as bundle:
        for name in [manifest, "assets/icon.png", "LICENSE", "README.md", "review/acceptance.md"]:
            bundle.write(root / name, name)
        bundle.writestr(".mcp.json", json.dumps(mcp, indent=2) + "\n")
    with zipfile.ZipFile(archive) as bundle:
        assert bundle.testzip() is None
        assert manifest in bundle.namelist()
        assert not any("SKILL.md" in name for name in bundle.namelist())
    print(archive.name, hashlib.sha256(archive.read_bytes()).hexdigest())
print("Static package checks passed. Live host acceptance remains required.")
