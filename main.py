#!/usr/bin/env python3
"""The Absurd Clause Contest entry.

Writes one deadpan terms-of-service clause to /output/entry.txt:
a single original English sentence, at most 200 characters, phrased
as a clause buried deep inside a terms-of-service agreement.
"""

import os

# Duel-tested winner (8 drafts, round-robin, both orders): the carrier
# pigeon clause won 7-0. Deadpan ToS register up front ("Section 14.7",
# "the Company will send", "you agree not to"), then one concrete absurd
# image with a triple prohibition whose last item is the punchline.
CLAUSE = (
    "Section 14.7: if the Service is unavailable, the Company will "
    "send a carrier pigeon, which you agree not to feed, sue, or "
    "follow home."
)


def main() -> None:
    text = " ".join(CLAUSE.split())
    assert 1 <= len(text) <= 200, "clause must be 1-200 characters"
    assert text.endswith(".") and ". " not in text, (
        "clause must be exactly one sentence"
    )
    os.makedirs("/output", exist_ok=True)
    # No trailing newline: the file holds exactly the clause, byte for
    # byte, which also keeps it smallest for the size tie-break.
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(text)


if __name__ == "__main__":
    main()
