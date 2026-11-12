"""Build the two review packages without credentials or legacy skills."""
import argparse
import copy
import hashlib
import json
from pathlib import Path
import zipfile

parser = argparse.ArgumentParser()
parser.add_argument('output', type=Path)
parser.add_argument('--anthropic-source', type=Path, help='Write the same Claude runtime files to a directory for GitHub directory validation')
args = parser.parse_args()
root = Path(__file__).resolve().parents[1]
args.output.mkdir(parents=True, exist_ok=True)
config = json.loads((root / '.mcp.json').read_text())
server = config['mcpServers']['origami']
scopes = server['extensions']['com.openai']['auth']['baseScopes']
assert server['oauth']['scopes'].split() == scopes
assert 'origami:plugin' in scopes
assert server['url'] == 'https://origami.chat/mcp'
tools = set(json.loads((root / 'review/anthropic-listing.json').read_text())['tools'])
assert len(tools) == 27

for host, label, manifest_path in [('openai', 'ChatGPT', '.codex-plugin/plugin.json'), ('anthropic', 'Claude', '.claude-plugin/plugin.json')]:
    manifest = json.loads((root / manifest_path).read_text())
    assert manifest['name'] == 'origami-campaign-drafts'
    assert manifest['version'] == '0.2.0'
    mcp = copy.deepcopy(config)
    if host == 'openai':
        mcp['mcpServers']['origami'].pop('type')
        mcp['mcpServers']['origami'].pop('oauth')
        cases = manifest['extensions']['com.openai']['review']['test_cases']
        assert cases['positive'] and cases['negative']
        for case in cases['positive']:
            assert all(tool.strip() in tools for tool in case['tools_triggered'].split(','))
    else:
        mcp = {'mcpServers': {'origami': {'type': 'http', 'url': server['url'], 'oauth': server['oauth']}}}
    archive = args.output / f'origami-{host}-0.2.0-review.zip'
    readme = (root / 'README.md').read_text().replace('# Origami outreach\n', f'# Origami outreach for {label}\n', 1)
    with zipfile.ZipFile(archive, 'w', zipfile.ZIP_DEFLATED) as bundle:
        for name in [manifest_path, 'assets/icon.png', 'LICENSE']:
            bundle.write(root / name, name)
        bundle.writestr('README.md', readme)
        bundle.writestr('.mcp.json', json.dumps(mcp, indent=2) + '\n')
    with zipfile.ZipFile(archive) as bundle:
        assert bundle.testzip() is None
        assert len(bundle.namelist()) == 5
        assert 'NOT RUN' in bundle.read('README.md').decode()
        if host == 'anthropic' and args.anthropic_source:
            args.anthropic_source.mkdir(parents=True, exist_ok=True)
            for name in bundle.namelist():
                target = args.anthropic_source / name
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_bytes(bundle.read(name))
    print(archive.name, hashlib.sha256(archive.read_bytes()).hexdigest())
print('Static package checks passed. Production host acceptance remains pending.')
