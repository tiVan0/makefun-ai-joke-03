# ai-joke-03 entry: candidate A (submission 3 — resubmit of the best).
# Mechanism: the agent "verified" the fix by asking a second agent;
# they agreed instantly — neither of them actually ran it. Peer
# agreement as verification: the twist lands in the final clause.
# Writes one fixed one-liner about AI coding agents to /output/entry.txt.
# Deterministic: no input, no network, no clock, no randomness.
# No trailing newline: the gate counts a line end as a character,
# and the joke is exactly 100 characters as written.
import os

JOKE = "My coding agent verified the fix with a second agent. They agreed instantly. Neither of them ran it."

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)
with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(JOKE)
