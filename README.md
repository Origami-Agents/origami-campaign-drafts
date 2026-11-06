# Origami campaign drafts for Claude

Turn an outreach brief into an email or LinkedIn campaign draft saved in [Origami](https://origami.chat). The plugin previews the saved copy and links to Origami for review. It does not launch outreach, enroll recipients, connect senders, buy leads, or edit existing campaigns.

## Connect

Install this plugin in a supported Claude surface, then use the secure OAuth connection for the Origami server at `https://origami.chat/mcp`. Sign in as an administrator of a primary Origami organization with API access and select that organization during consent. Never paste passwords, API keys, or tokens into chat. The connection stays within the consented organization; child/project switching is unavailable in this workflow.

An existing Origami account with API access is required. Draft generation uses the account's credits. Review current access and available credits in Origami before starting; the plugin does not purchase credits or change subscriptions.

## Example

“Use Origami to draft an email campaign for my appointment reminder product, targeting independent dental practices. Ask whether missed appointments are a problem. Save a draft with a short initial email and two follow-ups.”

Describe your real offer, audience and goal. Specify email, LinkedIn or both. Claude starts one draft job, follows its status, reads the saved campaign and returns a preview. If the job requests more information, answer its questions. If work is still running, ask Claude to check the same job rather than create another draft.

Review your draft at https://origami.chat/sequences/campaigns. Add recipients, configure senders and launch only in Origami. A missing sender does not prevent saving a draft.

## Data and permissions

The plugin sends your drafting brief and explicitly supplied job answers to Origami through its declared MCP connection. It can read the connected account, retrieve campaign drafts, create a draft, check its own connection's draft jobs, answer job questions and cancel such a job. The package contains no local executable hooks or bundled server code. Generated drafts and related job information are processed by the Origami service under its privacy policy.

- [Privacy policy](https://origami.chat/privacy-policy)
- [Terms of service](https://origami.chat/terms)
- [Support](https://origami.chat/contact), in-app support chat, or hello@origamiagents.com

## Troubleshooting

If authorization fails, reconnect through OAuth using an eligible organization administrator. For access or credit errors, check the account in Origami. If a request times out, check the existing job or campaign list before retrying because a draft may already exist.

## License

Copyright 2026 AirSplash Inc. All rights reserved. See LICENSE. This package does not grant an open-source license.
