#!/usr/bin/env python3
"""Alien Field Notes: The Two Day Earth Review.

Writes a one-line review of planet Earth by an alien tourist to
/output/entry.txt (UTF-8, 1-200 characters): after two days of
observation, the visitor has worked out who is really in charge.
"""

import os

LINE = (
    "Day two: the tall hairless ones are walked twice daily by "
    "their small furry rulers and carry the rulers' droppings home "
    "in bags, unpaid, smiling. Five stars. I have applied to be walked."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
