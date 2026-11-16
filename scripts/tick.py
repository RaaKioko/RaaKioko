"""Rewrite the day counter inside assets/tile-pong.svg. Run daily by the workflow."""
import datetime, json, re, zoneinfo

START = datetime.date(2026, 6, 17)  # first commit of Microsoft-Access-Pong
today = datetime.datetime.now(zoneinfo.ZoneInfo("Africa/Nairobi")).date()
days = (today - START).days

spec = json.load(open("assets/digits.json"))
x, uses = 0.0, []
for c in str(days):
    uses.append(f'<use href="#d{c}" x="{x:.1f}"/>')
    x += spec["adv"][c] + spec["gap"]

path = "assets/tile-pong.svg"
svg = open(path).read()
new, n = re.subn(r"(<!--D-->).*?(<!--/D-->)", lambda m: m.group(1) + "".join(uses) + m.group(2), svg, flags=re.S)
assert n == 1, "counter markers not found"
if new != svg:
    open(path, "w").write(new)
print(days)
