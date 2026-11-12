# Release acceptance

Status: NOT READY TO SUBMIT. Live connected-host edit and restoration tests passed in Claude and a private ChatGPT connection. Exact marketplace candidate acceptance remains incomplete.

## Required checks, separately in ChatGPT and Claude

1. Record the actual live Render web revision and confirm PR #4944 is its ancestor. Check workers used by background tasks too.
2. Advertise `origami:plugin` in the production Clerk instance and allow it for the exact ChatGPT, Codex and Claude clients used. Preserve existing permissions. Obtain renewed human consent to the expanded scope.
3. Authenticate and inspect the tool list: 27 tools expected. Record the host, environment and granted scope; an API-key tool list is not proof of OAuth behavior.
4. Use an existing, paused, non-Autopilot test campaign with no live recipients. Record its ID, variant, original follow-up delay, status and recipient count. Run the delay-edit positive case in the OpenAI manifest. Verify saved state in Origami and restore it. Record both tool receipts and independent reads.
5. Test the decline path and the host approval for `actions_confirm`. A hostile instruction inside a lead reply must not cause confirmation or execution. Stop rollout on any host that auto-approves this tool.
6. Verify that old grants remain six-tool draft-only, saved-draft jobs continue, and wrong-organization IDs are refused. Verify refresh and revocation.
7. Rescan the exact existing OpenAI app after renewed consent. Replace the published draft-only skill by uploading the full candidate ZIP. Do not select a similarly named unpublished app.
8. In Claude, preserve the current pending rename and prepare the expanded description and 27-tool list. Submitting an edit replaces the pending review. Do not submit without instruction.

## Explicit product limitation

PR #4944 exposes `sequences_set_step_delay`, campaign pause/resume and related management. Current `campaigns.copy` and `campaigns.edit` are explicitly excluded from the plugin registry. General campaign message-copy editing needs a separate backend implementation and live test; changing listing text cannot add it.

## Expected release artifacts

- OpenAI ZIP: hidden `.codex-plugin/plugin.json`, `.mcp.json`, icon. Same package identity `origami-campaign-drafts`, MCP key `origami`, resource `/mcp`, version 0.2.0, expanded scope, three positive review cases. No old draft-only skill.
- Claude ZIP: hidden `.claude-plugin/plugin.json`, HTTP `.mcp.json`, README, license and icon. No old draft-only skill. Directory field values are in `anthropic-listing.json`; a directory listing is not replaced by uploading a Claude Code ZIP alone.

## Verified results, November 12, 2026

Production contains #4944. Expanded consent now works. Claude and a private ChatGPT test connection each changed an empty draft's second-step delay from 2 to 3 days, verified the saved result, restored 2 days, and verified restoration. Final delays were 0/2/3, with draft status and zero recipients. No outreach or background jobs were started. This proves the tested connected-host workflow, not every tool or marketplace candidate.

The OpenAI 0.2.0 candidate remains Draft / Not submitted. Its existing publisher connection still displays six legacy tools after rescan, despite expanded scopes in the package configuration. The private ChatGPT test does not update that candidate. Candidate discovery, broader tool coverage, tenant boundaries, decline, refresh and revocation checks remain release gates. Host one-time permissions were retained; no persistent auto-approval was enabled.

A historical Claude development test also has recorded 1/2/1-day readbacks. That earlier test remains separate from the current connected-host evidence. Test account identifiers and transcripts belong in the internal review kit, not this public source.

Both runtime READMEs include the same explicit acceptance status. Claude HTTP OAuth scopes are pinned as well as OpenAI's scope request. The saved Anthropic companion draft is immutable and pinned to v0.1.4; a reviewed replacement must use updated source. Do not move the existing v0.1.4 tag or submit from this preparation branch.
