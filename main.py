#!/usr/bin/env python3
"""Write the funniest honest appliance error message to /output/entry.txt."""

import os

LINE = "UNBALANCED LOAD: I HAVE WALKED 4 INCHES ACROSS THE FLOOR TRYING TO SPIN ONE WET HOODIE. PLEASE REDISTRIBUTE."


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
