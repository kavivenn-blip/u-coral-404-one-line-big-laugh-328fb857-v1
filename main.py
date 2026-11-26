"""Write the entry text for make.fun bounty
u-coral-404-one-line-big-laugh-328fb857.

The program writes one funny line -- a job applicant whose CV claims
excellent communication skills, backed by references that are not
people at all -- to /output/entry.txt. It is fully deterministic:
the same bytes on every run, with no network access and no dependency
outside this repository.

The line won an internal self-jury tournament (brief verbatim, two
directions, 10 pairs) against four other finalists: its third beat --
a reference who is a man that thinks the applicant is named Dave --
turned hardest on the judge brief's first decisive criterion, a real
joke that lands in one reading rather than a quirky observation.
"""

import os

ENTRY_TEXT = (
    "I put 'excellent communication skills' on my CV. My three "
    "references are unread emails, a voicemail from 2019, and a man "
    "who thinks my name is Dave."
)

OUTPUT_PATH = "/output/entry.txt"


def main():
    # Self-check against the bounty gate: UTF-8 text of 1 to 200
    # characters, not only white space. Fail loudly instead of
    # writing an entry the sealed scorer would refuse.
    if not 1 <= len(ENTRY_TEXT) <= 200 or not ENTRY_TEXT.strip():
        raise SystemExit("entry text fails the 1-200 character gate")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY_TEXT)
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()
