# -*- coding: utf-8 -*-
"""「式の展開」の問題編ページと別冊（解答）ページを作る。build_oni.py から呼ばれる。"""
import re, html
from tenkai_data import EX, FINAL, UNIT


LIM = 26
def _vis(t):
    t = re.sub(r"\\(?:left|right|quad|qquad|Rightarrow|to|cdot|cdots|ldots|dfrac|frac|sqrt|text)", "", t)
    t = re.sub(r"[{}\\ ]", "", t)
    return sum(1.8 if ord(c) > 0x2000 else 1 for c in t)

def _split_top(t, seps, paren=False):
    """波かっこ・\\left\\right の外側にある seps の位置で分け、[(区切り, 本体)] を返す。"""
    out, depth, i, start, sep = [], 0, 0, 0, ""
    while i < len(t):
        if t.startswith("\\left", i): depth += 1; i += 5; continue
        if t.startswith("\\right", i): depth -= 1; i += 6; continue
        if t[i] == "\\" and i + 1 < len(t) and t[i+1] in "{}": i += 2; continue
        if paren and t[i] in "([": depth += 1; i += 1; continue
        if paren and t[i] in ")]": depth -= 1; i += 1; continue
        if t[i] == "{": depth += 1
        elif t[i] == "}": depth -= 1
        elif depth == 0:
            hit = next((x for x in seps if t.startswith(x, i)), None)
            if hit:
                out.append((sep, t[start:i])); sep = hit; i += len(hit); start = i; continue
        i += 1
    out.append((sep, t[start:]))
    return out

def fmt(t):
    """長い式を、等号・矢印・コンマの位置で折り返して複数行にする。"""
    t = t.strip()
    if "\\begin" in t or _vis(t) <= LIM: return t
    m = t.find("\\text{のとき")
    if m >= 0:
        j = t.index("}", m) + 1
        cond, rest = t[:m].rstrip(" \\"), t[j:].lstrip(" \\")
        parts = [b.strip(" \\") for _, b in _split_top(cond, [","])]
        lines, cur = [], ""
        for k, p in enumerate(parts):
            piece = p + ("," if k < len(parts) - 1 else "")
            if cur and _vis(cur + piece) > LIM: lines.append(cur); cur = piece
            else: cur = (cur + "\\ " + piece) if cur else piece
        lines.append(cur + "\\ \\text{のとき、}")
        lines.append(rest)
        return "\\begin{gathered}" + " \\\\ ".join(lines) + "\\end{gathered}"
    segs = _split_top(t, [",\\quad", ",\\ "])
    if len(segs) > 1:
        lines = [(b.strip() + ("," if k < len(segs) - 1 else "")) for k, (_, b) in enumerate(segs)]
        return "\\begin{gathered}" + " \\\\ ".join(lines) + "\\end{gathered}"
    segs = _split_top(t, ["\\Rightarrow", "\\to", "="])
    if len(segs) <= 1:
        segs = [x for x in _split_top(t, ["+", "-"], True)]
        if len(segs) <= 1: return t
    lines, cur = [], ""
    for sep, body in segs:
        piece = (sep + " " if sep else "") + body.strip()
        if cur and _vis(cur + piece) > LIM: lines.append(cur); cur = "&" + piece
        else: cur = (cur + " " + piece) if cur else piece
    lines.append(cur)
    if len(lines) == 1: return t
    lines[0] = "&" + lines[0] if not lines[0].startswith("&") else lines[0]
    return "\\begin{aligned}" + " \\\\ ".join(lines) + "\\end{aligned}"

def tx(s):
    s = html.escape(s, quote=False)
    s = re.sub(r"\$\$(.+?)\$\$", lambda m: "\n\\[" + fmt(m.group(1)) + "\\]\n", s, flags=re.S)
    s = re.sub(r"\$(.+?)\$", lambda m: "\\(" + m.group(1) + "\\)", s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
    out = []
    for line in s.split("\n"):
        line = line.strip()
        if not line: continue
        out.append(line if line.startswith("\\[") else f"<p>{line}</p>")
    return "\n".join(out)

def plain(s): return s.replace("$", "")

def abox(ans, head="【答案（テストに書く形）】", cls=""):
    return f'<div class="abox {cls}"><p class="ah">{head}</p>\n\\[{fmt(ans)}\\]\n<p class="ans-mark">答</p></div>'

GROUPS = [("係数を拾う", [1]), ("展開の工夫", [2, 3, 4]), ("かたまりで置き換える・対称式", [5, 6, 7, 8]), ("次数を下げる", [9])]
def inl(s): return tx(s).replace("<p>", "").replace("</p>", "")
def fname(i): return f"tenkai-{i}.html"

def make(page, AD_TOP, AD_BTM):
    n = len(EX)
    out = {}
    def card(href, badge, title): return f'<a class="ecard" href="{href}"><span class="ebadge">{badge}</span><span class="et">{title}</span></a>'
    cards = ""
    for g, ids in GROUPS:
        cards += f'<h3 class="gh">{g}</h3><div class="ecards">' + "".join(card(fname(i), f"例題 {i}", inl(EX[i-1]["title"])) for i in ids) + "</div>"
    cards += '<h3 class="gh">章末問題</h3><div class="ecards">' + card("tenkai-final.html", "章末問題", f"例題1〜{n}の総まとめ（9問）") + "</div>"
    body = f"""
<p class="crumb"><a href="index.html">ホーム</a> ＞ <a href="subject-1.html">数学I</a> ＞ {UNIT}</p>
{AD_TOP}
<h1 class="lh"><span class="lbadge">数学I</span><span class="lsub">{UNIT}</span></h1>
<section class="bar"><h2>この単元の進め方</h2>
<p>例題で「考え方 → STEP」の手順をつかみ、同じ手順で練習問題を解きます。練習問題の解答は、各例題ページの「解答を見る（別冊）」から見られます。</p>
<p class="dl">PDF：<a href="pdf/tenkai-mondai-hen.pdf">問題編</a>　<a href="pdf/tenkai-bessatsu.pdf">別冊（解答）</a></p></section>
{cards}
{AD_BTM}
<div class="pn"><a href="subject-1.html">← 数学Iの単元一覧</a><span></span></div>
"""
    out["tenkai.html"] = page(UNIT, "数学Iの「式の展開」の難問。係数比べ・展開の工夫・対称式・次数下げを、例題の手順で練習できます。", body)

    def nav(i):
        prev = (fname(i-1), f"← 例題{i-1}") if i > 1 else ("tenkai.html", "← 例題一覧")
        nxt = (fname(i+1), f"例題{i+1} →") if i < n else ("tenkai-final.html", "章末問題 →")
        return f'<div class="pn"><a href="{prev[0]}">{prev[1]}</a><a href="tenkai.html">例題一覧</a><a href="{nxt[0]}">{nxt[1]}</a></div>'
    for i, e in enumerate(EX, 1):
        steps = "".join(f'<div class="step"><div class="step-h"><span class="badge">STEP {k}</span> {inl(t)}</div><div class="step-b">{tx(b)}</div></div>' for k, (t, b) in enumerate(e["steps"], 1))
        prac = "".join(f"<li>{inl(p)}</li>" for p in e["prac"])
        body = f"""
<p class="crumb"><a href="index.html">ホーム</a> ＞ <a href="subject-1.html">数学I</a> ＞ <a href="tenkai.html">{UNIT}</a> ＞ 例題{i}</p>
{AD_TOP}
<h1 class="lh"><span class="lbadge">例題 {i}</span><span class="lsub">{inl(e['title'])}</span></h1>
<div class="qbox">{tx(e['q'])}</div>
<div class="bar"><h2>解き方（まず考え方）</h2>{tx(e['idea'])}<p class="small"><strong class="ok">コツ</strong>　{inl(e['tip'])}</p></div>
<div class="bar"><h2>解答</h2>{steps}</div>
{abox(e['ans'])}
<div class="bar"><h2>練習問題{i}</h2><ol class="prac big">{prac}</ol></div>
<p><a class="btn" href="kaito-tenkai-{i}.html">解答を見る（別冊）</a></p>
{AD_BTM}
{nav(i)}
<p class="dl">PDF：<a href="pdf/tenkai-mondai-hen.pdf">問題編（全ページ）</a>　<a href="pdf/tenkai-bessatsu.pdf">別冊 練習問題の解答</a></p>
"""
        out[fname(i)] = page(f"例題{i} {plain(e['title'])}｜{UNIT}", f"{UNIT}の例題{i}。{plain(e['title'])}。", body)
    fin = "".join(f"<li>{inl(q)}</li>" for q, *_ in FINAL)
    body = f"""
<p class="crumb"><a href="index.html">ホーム</a> ＞ <a href="subject-1.html">数学I</a> ＞ <a href="tenkai.html">{UNIT}</a> ＞ 章末問題</p>
{AD_TOP}
<h1 class="lh"><span class="lbadge">章末問題</span><span class="lsub">{UNIT}</span></h1>
<div class="bar"><p>例題1〜{n}で学んだ手順だけで解ける問題です。まず、どの例題の型かを見分けるところから始めましょう。</p><ol class="prac big">{fin}</ol></div>
<p><a class="btn" href="kaito-tenkai-final.html">解答を見る（別冊）</a></p>
{AD_BTM}
<div class="pn"><a href="{fname(n)}">← 例題{n}</a><a href="tenkai.html">例題一覧</a><a href="kaito-tenkai-final.html">別冊（解答） →</a></div>
<p class="dl">PDF：<a href="pdf/tenkai-mondai-hen.pdf">問題編（全ページ）</a>　<a href="pdf/tenkai-bessatsu.pdf">別冊 練習問題の解答</a></p>
"""
    out["tenkai-final.html"] = page(f"章末問題｜{UNIT}", f"{UNIT}の章末問題。", body)

    def kname(i): return f"kaito-tenkai-{i}.html"
    PDFL = '<p class="dl">PDF：<a href="pdf/tenkai-mondai-hen.pdf">問題編（全ページ）</a>　<a href="pdf/tenkai-bessatsu.pdf">別冊 練習問題の解答</a></p>'
    def kpage(key, label, title, inner, prev, nxt, desc):
        ex_href = fname(key) if key != "final" else "tenkai-final.html"
        body = f"""
<p class="crumb"><a href="index.html">ホーム</a> ＞ <a href="subject-1.html">数学I</a> ＞ <a href="tenkai.html">{UNIT}</a> ＞ <a href="{ex_href}">{label}</a> ＞ 別冊（解答）</p>
{AD_TOP}
<h1 class="lh"><span class="lbadge">別冊</span><span class="lsub">{title}</span></h1>
<p class="small">まず自分で解いてから見ましょう。<a href="{ex_href}">← 問題にもどる</a></p>
{inner}
{AD_BTM}
<div class="pn">{prev}<a href="{ex_href}">{label}にもどる</a>{nxt}</div>
{PDFL}
"""
        return page(f"{label} 別冊（解答）｜{UNIT}", desc, body)
    for i, e in enumerate(EX, 1):
        inner = ""
        for k, (p, (sol, a)) in enumerate(zip(e["prac"], e["pans"]), 1):
            inner += f'<div class="bar"><p><strong>({k})</strong>　{inl(p)}</p>{tx(sol)}</div>{abox(a, "【答案】", "sm")}'
        prev = f'<a href="{kname(i-1)}">← 別冊 例題{i-1}</a>' if i > 1 else "<span></span>"
        nxt = f'<a href="{kname(i+1)}">別冊 例題{i+1} →</a>' if i < n else '<a href="kaito-tenkai-final.html">別冊 章末問題 →</a>'
        out[kname(i)] = kpage(i, f"例題{i}", f"練習問題{i}の解答　{inl(e['title'])}", inner, prev, nxt, f"{UNIT}の練習問題{i}の解答。")
    inner = ""
    for k, (q, t, sol, a) in enumerate(FINAL, 1):
        inner += f'<div class="bar"><p><strong>{k}.</strong>　{inl(q)}</p>{tx(sol)}<p class="small">（例題{t}の型）</p></div>{abox(a, "【答案】", "sm")}'
    out["kaito-tenkai-final.html"] = kpage("final", "章末問題", "章末問題の解答", inner, f'<a href="{kname(n)}">← 別冊 例題{n}</a>', '<a href="subject-1.html">数学Iの単元一覧 →</a>', f"{UNIT}の章末問題の解答。")
    return out
