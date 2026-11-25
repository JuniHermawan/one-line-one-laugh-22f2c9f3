"""One Line, One Laugh — make.fun entry.

Writes a single hilarious one-liner to /output/entry.txt.
Deterministic, stdlib only, no network, no reads outside the repo.
"""

import os

ENTRY = "I tried to quit coffee. Day one, I filed a missing person's report for myself."


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
