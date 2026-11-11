# Origami campaign management

Manage outreach in [Origami](https://origami.chat) from ChatGPT or Claude. List campaigns, pause or resume them, edit follow-up delays, find leads, stop outreach to a lead, review or redraft replies, and start campaign builds or background tasks.

## Connect

Connect to `https://origami.chat/mcp` through OAuth as an administrator of an active, paid, API-enabled primary Origami organization. Consent selects the organization; these tools cannot switch projects or access another organization. Never paste credentials into chat.

Campaign management requires `openid`, `user:org:read`, `origami:mcp`, `origami:plugin`, and `offline_access`. Existing draft-only connections must reconnect and explicitly grant the expanded permission. An old token remains draft-only even after another token grants expanded access.

## What can change

- Pause or resume an existing campaign.
- Change a follow-up delay, with the previous delay returned for restoration.
- Stop messaging or remove a lead from a campaign.
- Regenerate a drafted reply or supply information it needs.
- Start, inspect, answer, or stop supported background tasks.
- Record supported business knowledge and read its history.

Actions that require approval ask before running. Hosts must require a real user approval for confirmation tools. Background work consumes normal Origami credits. Read the returned results to distinguish a completed change, a refusal, a pending action, and a task still running.

Campaign message-copy editing is not exposed by this release. Launch new drafts and send replies in Origami. Autopilot plays use the separate Origami Autopilot connector. Knowledge stored as documents is edited in the app. Older saved drafts remain readable and their jobs can be continued or cancelled.

## Example requests

- How did my outreach do last night, and what needs my attention?
- Pause my dental practices campaign.
- Change the first follow-up delay on my test campaign to four days.
- Find a lead and show me the reply Origami drafted.

## Data and permissions

Your requests and explicitly supplied task answers are sent to Origami. The connection can read campaign, lead, reply, task and knowledge information within the consented organization and make supported changes. The package contains no executable hooks, credentials, or bundled server. Guidance comes from the authenticated server's tool descriptions and instructions.

[Privacy](https://origami.chat/privacy-policy) · [Terms](https://origami.chat/terms) · [Support](https://origami.chat/contact)

## Release status

Version 0.2.0 is a preparation candidate. Production revision verification, Clerk scope setup, renewed host consent, and live editing/approval tests must pass before submission. See `review/acceptance.md`.

## License

Copyright 2026 AirSplash Inc. All rights reserved. See LICENSE.
