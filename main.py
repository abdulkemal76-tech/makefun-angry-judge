"""Angry Judge: The Short Rant Contest entry.

Writes one short funny rant about a small everyday annoyance to
/output/entry.txt (max 400 characters).
"""

import os

RANT = (
    "My shower has two settings: ice bath and soup. "
    "One millimetre on the knob and I go from shivering to being boiled "
    "alive like a dumpling. There is no middle. "
    "There has never been a middle. "
    "Three plumbers have looked at it, shrugged, and left. "
    "Every morning I shower the way hostages negotiate: slowly, in small "
    "movements, apologising to the tap."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(RANT)


if __name__ == "__main__":
    main()
