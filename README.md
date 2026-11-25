# tool-calls

A Claude Code mod that opens a **Tool calls** pane beside the chat and keeps a
live list of every tool call in the session. Each call shows as `runs <Tool>`
while it runs and dims to `done <Tool>` when it finishes. The last 200 calls
are kept for the session, and they survive a reload of the mod.

The pane opens when a session starts. If you close it, type `/tool-calls` to
open it again.

## Install

At the prompt of a Claude Code terminal session:

```
/plugin install tool-calls --marketplace dnlwrthstr/tool-calls-mod
```

Answer `y` to add the marketplace, then pick a scope (user scope is first;
press Enter).

From a shell:

```bash
claude plugin install tool-calls --marketplace dnlwrthstr/tool-calls-mod
```

In the Claude desktop app, where `/plugin` does not run: click **+** next to
the prompt box, then **Plugins**, **Add marketplace** with
`dnlwrthstr/tool-calls-mod`, then **Add plugin**.

## License

MIT. See [LICENSE](LICENSE).
