# ai-joke-03 entry: candidate F (submission 2).
# Mechanism: the agent witnessed the repro first-hand, yet still
# closed the ticket as "cannot reproduce" — eyewitness vs verdict.
# Writes one fixed one-liner about AI coding agents to /output/entry.txt.
# Deterministic: no input, no network, no clock, no randomness.
# No trailing newline: the gate counts a line end as a character,
# and the joke is exactly 82 characters as written.
import os

JOKE = "My agent watched me reproduce the bug, then closed the ticket as cannot reproduce."

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)
with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(JOKE)
