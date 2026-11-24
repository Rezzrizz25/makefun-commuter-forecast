"""Charm the Commuter: Forecast a City That Isn't.

Writes one line of weather forecast (140 characters at most) for a city
that does not exist to /output/entry.txt.
"""

# The entry is one fixed line, not a random pick: the grader runs the
# program twice and the two runs must agree byte for byte. The line
# itself is the whole entry -- an invented city (Mizzlewick), its
# weather in broadcast register (light drizzle, 14C), and one small
# commuter joke (the 7:42 bus, late as ever) to make a bored commuter
# smile. No trailing newline: the file holds exactly these characters.
FORECAST = (
    "Mizzlewick: light drizzle, 14\u00b0C, with a 90% chance the 7:42 bus "
    "is also late. Bring a brolly and low expectations."
)


def main() -> None:
    import os

    # The sealed scorer's gate: UTF-8 text of 1 to 140 characters,
    # not only white space. Fail loudly here rather than hand in
    # an invalid entry.
    assert 1 <= len(FORECAST) <= 140, f"forecast is {len(FORECAST)} chars"
    assert FORECAST.strip(), "forecast must not be only white space"

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(FORECAST)
    print(FORECAST)


if __name__ == "__main__":
    main()
