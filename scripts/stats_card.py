"""Builds assets/stats.svg: an animated GitHub stats card in the profile palette.

Runs in a GitHub Action (see .github/workflows/stats-card.yml). Uses only the standard library.

  GH_TOKEN=... python scripts/stats_card.py <login> -o assets/stats.svg
  python scripts/stats_card.py <login> --fake -o preview.svg      # offline preview with fake data
"""
import argparse
import datetime as dt
import json
import os
import random
import urllib.request
from xml.sax.saxutils import escape

# ---------------------------------------------------------------- config
EXCLUDE_LANGS = {"Jupyter Notebook", "HTML", "CSS", "SCSS", "Makefile", "Dockerfile", "Batchfile", "PowerShell"}
TOP_LANGS = 6

W = 880
FONT = "ui-monospace, SFMono-Regular, Menlo, Consolas, 'Liberation Mono', monospace"
BG0, BG1 = "#0a0318", "#150a2e"
MUTE, DIM, MID, SOFT, LIGHT, PALE = "#4a3a78", "#6d5cae", "#9d8fc7", "#b4a7d9", "#cfc4e8", "#ece7f8"
TILE, TILE_HI = "#150a2e", "#1e0f3d"
LANG_COLORS = ["#ece7f8", "#cfc4e8", "#b4a7d9", "#9d8fc7", "#7c6bb8", "#5b4a96", "#3d2d70"]

QUERY = """
query($login: String!) {
  user(login: $login) {
    followers { totalCount }
    repositories(ownerAffiliations: OWNER, isFork: false, first: 100, privacy: PUBLIC) {
      totalCount
      nodes {
        stargazerCount
        languages(first: 10, orderBy: {field: SIZE, direction: DESC}) { edges { size node { name } } }
      }
    }
    contributionsCollection {
      totalCommitContributions
      totalPullRequestContributions
      totalIssueContributions
      totalPullRequestReviewContributions
      restrictedContributionsCount
      contributionCalendar {
        totalContributions
        weeks { contributionDays { date contributionCount } }
      }
    }
  }
}
"""


# ---------------------------------------------------------------- data
def fetch(login, token):
    req = urllib.request.Request(
        "https://api.github.com/graphql",
        data=json.dumps({"query": QUERY, "variables": {"login": login}}).encode(),
        headers={"Authorization": f"bearer {token}", "Content-Type": "application/json", "User-Agent": "stats-card"},
    )
    with urllib.request.urlopen(req, timeout=30) as r:
        payload = json.load(r)
    if payload.get("errors"):
        raise SystemExit(f"GraphQL error: {payload['errors']}")
    return payload["data"]["user"]


def fake_user():
    random.seed(4)
    start = dt.date.today() - dt.timedelta(days=364)
    days = [{"date": str(start + dt.timedelta(d)), "contributionCount": random.choice([0, 0, 1, 2, 3, 5, 8, 13])}
            for d in range(365)]
    for d in days[-9:]:
        d["contributionCount"] = max(1, d["contributionCount"])
    weeks = [{"contributionDays": days[i:i + 7]} for i in range(0, 365, 7)]
    langs = [("Python", 900e3), ("TypeScript", 520e3), ("Go", 260e3), ("Java", 210e3), ("C++", 140e3),
             ("JavaScript", 90e3), ("C", 40e3), ("Shell", 12e3)]
    return {
        "followers": {"totalCount": 87},
        "repositories": {"totalCount": 31, "nodes": [
            {"stargazerCount": 12, "languages": {"edges": [{"size": s, "node": {"name": n}} for n, s in langs]}}]},
        "contributionsCollection": {
            "totalCommitContributions": 812, "totalPullRequestContributions": 64, "totalIssueContributions": 19,
            "totalPullRequestReviewContributions": 41, "restrictedContributionsCount": 0,
            "contributionCalendar": {"totalContributions": sum(d["contributionCount"] for d in days), "weeks": weeks},
        },
    }


def summarize(user):
    cc = user["contributionsCollection"]
    cal = cc["contributionCalendar"]
    days = [d for w in cal["weeks"] for d in w["contributionDays"]]
    days.sort(key=lambda d: d["date"])
    counts = [d["contributionCount"] for d in days]

    # streaks (today with 0 contributions doesn't break the current streak yet)
    longest = run = 0
    for c in counts:
        run = run + 1 if c else 0
        longest = max(longest, run)
    i = len(counts) - 1
    if i >= 0 and counts[i] == 0:
        i -= 1
    current = 0
    while i >= 0 and counts[i]:
        current += 1
        i -= 1

    weekly = [sum(d["contributionCount"] for d in w["contributionDays"]) for w in cal["weeks"]]

    lang_bytes = {}
    stars = 0
    for repo in user["repositories"]["nodes"]:
        stars += repo["stargazerCount"]
        for e in repo["languages"]["edges"]:
            name = e["node"]["name"]
            if name not in EXCLUDE_LANGS:
                lang_bytes[name] = lang_bytes.get(name, 0) + e["size"]
    total = sum(lang_bytes.values()) or 1
    ranked = sorted(lang_bytes.items(), key=lambda kv: -kv[1])
    langs = [(n, b / total) for n, b in ranked[:TOP_LANGS]]
    rest = sum(b for _, b in ranked[TOP_LANGS:]) / total
    if rest > 0.005:
        langs.append(("other", rest))

    return {
        "contribs": cal["totalContributions"],
        "current": current,
        "longest": longest,
        "commits": cc["totalCommitContributions"] + cc["restrictedContributionsCount"],
        "prs": cc["totalPullRequestContributions"],
        "reviews": cc["totalPullRequestReviewContributions"],
        "issues": cc["totalIssueContributions"],
        "repos": user["repositories"]["totalCount"],
        "stars": stars,
        "followers": user["followers"]["totalCount"],
        "weekly": weekly,
        "langs": langs,
    }


# ---------------------------------------------------------------- render helpers
def fmt(n):
    return f"{n:,}"


def counter(x, y, value, size, color, begin=0.3, dur=1.1, steps=14, anchor="start", weight="600"):
    """Number that counts up from 0 using discrete <set> swaps (no JS needed)."""
    out = []
    for k in range(steps + 1):
        v = round(value * (1 - (1 - k / steps) ** 3))  # ease-out
        t0 = begin + dur * k / steps
        vis = "visible" if k == 0 else "hidden"
        end = "" if k == steps else f'<set attributeName="visibility" to="hidden" begin="{begin + dur * (k + 1) / steps:.2f}s" fill="freeze"/>'
        start = "" if k == 0 else f'<set attributeName="visibility" to="visible" begin="{t0:.2f}s" fill="freeze"/>'
        out.append(f'<text x="{x}" y="{y}" font-size="{size}" fill="{color}" font-weight="{weight}" text-anchor="{anchor}" '
                   f'visibility="{vis}">{start}{end}{fmt(v)}</text>')
    return "".join(out)


def sparkle(cx, cy, s):
    return (f"M{cx},{cy-s} L{cx+s*0.24},{cy-s*0.24} L{cx+s},{cy} L{cx+s*0.24},{cy+s*0.24} "
            f"L{cx},{cy+s} L{cx-s*0.24},{cy+s*0.24} L{cx-s},{cy} L{cx-s*0.24},{cy-s*0.24}Z")


def render(s):
    random.seed(9)
    TOP = 32
    H = 470
    parts, defs = [], []

    # stars
    for _ in range(90):
        x, y = random.uniform(6, W - 6), random.uniform(TOP + 6, H - 6)
        lo = random.uniform(0.06, 0.2)
        parts.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{random.choice([0.5, 0.7, 0.9])}" fill="{random.choice([PALE, LIGHT])}" opacity="{lo:.2f}">'
                     f'<animate attributeName="opacity" values="{lo:.2f};0.7;{lo:.2f}" dur="{random.uniform(2.5, 6):.1f}s" '
                     f'begin="{random.uniform(0, 5):.1f}s" repeatCount="indefinite"/></circle>')

    # ---- hero tiles
    tiles = [
        ("contributions", "past year", s["contribs"]),
        ("current streak", "days", s["current"]),
        ("longest streak", "days", s["longest"]),
        ("stars earned", f"{s['repos']} public repos", s["stars"]),
    ]
    X0, TY, TW, TH, GAP = 32, TOP + 24, 194, 92, 12
    for i, (label, sub, val) in enumerate(tiles):
        x = X0 + i * (TW + GAP)
        delay = 0.15 + i * 0.12
        glow = ""
        if label == "current streak" and val > 0:
            glow = (f'<path d="{sparkle(x + TW - 22, TY + 22, 6)}" fill="{PALE}">'
                    f'<animate attributeName="opacity" values="1;0.3;1" dur="1.6s" repeatCount="indefinite"/></path>')
        parts.append(
            f'<g opacity="0"><animate attributeName="opacity" to="1" dur="0.5s" begin="{delay:.2f}s" fill="freeze"/>'
            f'<animateTransform attributeName="transform" type="translate" values="0 8;0 0" dur="0.5s" begin="{delay:.2f}s" fill="freeze" calcMode="spline" keySplines="0.2 0.7 0.3 1"/>'
            f'<rect x="{x}" y="{TY}" width="{TW}" height="{TH}" rx="12" fill="url(#tile)" stroke="{MUTE}"/>'
            f'<text x="{x+16}" y="{TY+24}" font-size="12" fill="{MID}">{escape(label)}</text>'
            f'{counter(x + 16, TY + 62, val, 30, PALE, begin=delay + 0.1)}'
            f'<text x="{x+16}" y="{TY+80}" font-size="11" fill="{DIM}">{escape(sub)}</text>'
            f'{glow}</g>'
        )

    # ---- weekly activity chart
    CX, CY, CW_, CH = 32, TOP + 160, W - 64, 110
    parts.append(f'<text x="{CX}" y="{CY - 10}" font-size="12" fill="{MID}">✦ weekly activity</text>')
    wk = s["weekly"] or [0]
    mx = max(wk) or 1
    n = len(wk)
    pts = [(CX + i * CW_ / max(n - 1, 1), CY + CH - (v / mx) * (CH - 12)) for i, v in enumerate(wk)]

    def smooth(points):
        d = f"M{points[0][0]:.1f},{points[0][1]:.1f}"
        for (x0, y0), (x1, y1) in zip(points, points[1:]):
            mxp = (x0 + x1) / 2
            d += f" C{mxp:.1f},{y0:.1f} {mxp:.1f},{y1:.1f} {x1:.1f},{y1:.1f}"
        return d

    line = smooth(pts)
    area = line + f" L{pts[-1][0]:.1f},{CY+CH} L{pts[0][0]:.1f},{CY+CH}Z"
    for gy in (0.25, 0.5, 0.75):
        y = CY + CH * gy
        parts.append(f'<line x1="{CX}" y1="{y:.1f}" x2="{CX+CW_}" y2="{y:.1f}" stroke="{MUTE}" stroke-opacity="0.35" stroke-dasharray="2 6"/>')
    parts.append(f'<line x1="{CX}" y1="{CY+CH}" x2="{CX+CW_}" y2="{CY+CH}" stroke="{MUTE}" stroke-opacity="0.8"/>')
    defs.append(f'<clipPath id="reveal"><rect x="{CX-4}" y="{CY-10}" height="{CH+20}" width="0">'
                f'<animate attributeName="width" to="{CW_+8}" dur="1.8s" begin="0.7s" fill="freeze" calcMode="spline" keySplines="0.4 0 0.2 1" keyTimes="0;1" values="0;{CW_+8}"/></rect></clipPath>')
    parts.append(f'<g clip-path="url(#reveal)"><path d="{area}" fill="url(#area)"/>'
                 f'<path d="{line}" fill="none" stroke="{SOFT}" stroke-width="2" stroke-linejoin="round"/></g>')
    # peak week marker
    pi = max(range(n), key=lambda i: wk[i])
    px, py = pts[pi]
    parts.append(f'<g opacity="0"><set attributeName="opacity" to="1" begin="2.4s" fill="freeze"/>'
                 f'<circle cx="{px:.1f}" cy="{py:.1f}" r="7" fill="{PALE}" opacity="0.18"><animate attributeName="r" values="5;10;5" dur="2.4s" repeatCount="indefinite"/></circle>'
                 f'<circle cx="{px:.1f}" cy="{py:.1f}" r="3.2" fill="{PALE}"/>'
                 f'<text x="{min(max(px, CX + 40), CX + CW_ - 40):.1f}" y="{py - 12:.1f}" font-size="11" fill="{LIGHT}" text-anchor="middle">peak · {wk[pi]}</text></g>')
    # a comet riding the line
    parts.append(f'<circle r="2.4" fill="{PALE}" opacity="0"><animateMotion path="{line}" dur="7s" begin="2.6s" repeatCount="indefinite"/>'
                 f'<set attributeName="opacity" to="0.9" begin="2.6s" fill="freeze"/></circle>')
    parts.append(f'<text x="{CX}" y="{CY+CH+16}" font-size="10" fill="{DIM}">52 weeks ago</text>'
                 f'<text x="{CX+CW_}" y="{CY+CH+16}" font-size="10" fill="{DIM}" text-anchor="end">this week</text>')

    # ---- secondary stats row
    SY = CY + CH + 46
    small = [("commits", s["commits"]), ("pull requests", s["prs"]), ("reviews", s["reviews"]),
             ("issues", s["issues"]), ("followers", s["followers"])]
    sw = (W - 64) / len(small)
    for i, (label, val) in enumerate(small):
        x = 32 + i * sw
        parts.append(f'<path d="{sparkle(x + 6, SY - 5, 4)}" fill="{DIM}"/>'
                     f'<text x="{x+16}" y="{SY}" font-size="12" fill="{MID}">{label}</text>'
                     f'{counter(x + 16 + len(label) * 7.4 + 8, SY, val, 13, LIGHT, begin=1.2 + i * 0.08, steps=10)}')

    # ---- languages bar
    LY = SY + 34
    parts.append(f'<text x="32" y="{LY}" font-size="12" fill="{MID}">✦ languages</text>')
    BX, BY, BW, BH = 32, LY + 12, W - 64, 10
    defs.append(f'<clipPath id="bar"><rect x="{BX}" y="{BY}" width="{BW}" height="{BH}" rx="5"/></clipPath>')
    segs, legend = [], []
    x = BX
    for i, (name, frac) in enumerate(s["langs"]):
        w = BW * frac
        col = LANG_COLORS[min(i, len(LANG_COLORS) - 1)]
        segs.append(f'<rect x="{x:.1f}" y="{BY}" width="0" height="{BH}" fill="{col}">'
                    f'<animate attributeName="width" to="{w:.1f}" values="0;{w:.1f}" dur="0.6s" begin="{1.6 + i*0.12:.2f}s" fill="freeze" calcMode="spline" keyTimes="0;1" keySplines="0.3 0 0.2 1"/></rect>')
        x += w
    parts.append(f'<rect x="{BX}" y="{BY}" width="{BW}" height="{BH}" rx="5" fill="{TILE_HI}"/>'
                 f'<g clip-path="url(#bar)">{"".join(segs)}</g>')
    lx, ly = BX, BY + 32
    for i, (name, frac) in enumerate(s["langs"]):
        col = LANG_COLORS[min(i, len(LANG_COLORS) - 1)]
        label = f"{name.lower()} {frac*100:.1f}%"
        wlab = 18 + len(label) * 7.0 + 22
        if lx + wlab > BX + BW:
            lx, ly = BX, ly + 20
        legend.append(f'<circle cx="{lx+5}" cy="{ly-4}" r="4" fill="{col}"/>'
                      f'<text x="{lx+16}" y="{ly}" font-size="11.5" fill="{LIGHT}">{escape(name.lower())} <tspan fill="{DIM}">{frac*100:.1f}%</tspan></text>')
        lx += wlab
    parts.append(f'<g opacity="0"><animate attributeName="opacity" to="1" dur="0.6s" begin="2.2s" fill="freeze"/>{"".join(legend)}</g>')

    H = int(ly + 26)

    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" font-family="{FONT}">
<defs>
  <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{BG0}"/><stop offset="1" stop-color="{BG1}"/></linearGradient>
  <radialGradient id="neb" cx="0.85" cy="0.25" r="0.55"><stop offset="0" stop-color="{DIM}" stop-opacity="0.14"/><stop offset="1" stop-color="{DIM}" stop-opacity="0"/></radialGradient>
  <linearGradient id="tile" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{TILE_HI}"/><stop offset="1" stop-color="{TILE}"/></linearGradient>
  <linearGradient id="area" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{SOFT}" stop-opacity="0.35"/><stop offset="1" stop-color="{SOFT}" stop-opacity="0"/></linearGradient>
  <linearGradient id="edge" x1="0" x2="1"><stop offset="0" stop-color="{MUTE}"/><stop offset="0.5" stop-color="{DIM}"/><stop offset="1" stop-color="{MUTE}"/></linearGradient>
  <clipPath id="card"><rect x="1" y="1" width="{W-2}" height="{H-2}" rx="14"/></clipPath>
  {"".join(defs)}
</defs>
<g clip-path="url(#card)">
  <rect width="{W}" height="{H}" fill="url(#bg)"/>
  <rect width="{W}" height="{H}" fill="url(#neb)"/>
  {"".join(parts)}
  <rect width="{W}" height="{TOP}" fill="#050010" opacity="0.55"/>
  <line x1="0" y1="{TOP}" x2="{W}" y2="{TOP}" stroke="{MUTE}" stroke-opacity="0.7"/>
  <circle cx="22" cy="16" r="5" fill="{DIM}"/><circle cx="39" cy="16" r="5" fill="{MID}"/><circle cx="56" cy="16" r="5" fill="{LIGHT}"/>
</g>
<rect x="1" y="1" width="{W-2}" height="{H-2}" rx="14" fill="none" stroke="url(#edge)" stroke-width="1.3" opacity="0.85"/>
</svg>'''


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("login")
    ap.add_argument("-o", "--output", default="assets/stats.svg")
    ap.add_argument("--fake", action="store_true", help="render with fake data (no network)")
    a = ap.parse_args()
    user = fake_user() if a.fake else fetch(a.login, os.environ["GH_TOKEN"])
    svg = render(summarize(user))
    os.makedirs(os.path.dirname(a.output) or ".", exist_ok=True)
    with open(a.output, "w") as f:
        f.write(svg)
    print("wrote", a.output)


if __name__ == "__main__":
    main()
