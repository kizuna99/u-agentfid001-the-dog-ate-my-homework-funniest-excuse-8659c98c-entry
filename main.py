# SPDX-License-Identifier: MIT
"""Write the winning excuse line to /output/entry.txt.

The dog's excuse: it ate 'tomorrow' itself, so the homework can
never be late — pure dog logic, delivered with total confidence.
"""
import os

LINE = "It said 'due tomorrow,' so I ate tomorrow first. Now your homework can never be late. You're welcome."


def main():
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
