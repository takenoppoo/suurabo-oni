# -*- coding: utf-8 -*-
"""「式の展開」の問題編ページと別冊（解答）ページを作る。build_oni.py から呼ばれる。"""
import re, html
from tenkai_data import EX, FINAL, UNIT

def tx(s):
    s = html.escape(s, quote=False)
    s = re.sub(r"\$\$(.+?)\$\$", lambda m: "\n\\[" + m.group(1) + "\\]\n", s, flags=re.S)
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
    return f'<div class="abox {cls}"><p class="ah">{head}</p>\n\\[{ans}\\]\n<p class="ans-mark">答</p></div>'

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
<p>例題で「考え方 → STEP」の手順をつかみ、同じ手順で練習問題を解きます。練習問題の解答は<a href="tenkai-kaitou.html">別冊（解答）</a>にあります。</p>
<p class="dl">PDF：<a href="pdf/tenkai-mondai-hen.pdf">問題編</a>　<a href="pdf/tenkai-bessatsu.pdf">別冊（解答）</a></p></section>
{cards}
<p style="margin-top:18px"><a class="btn" href="tenkai-kaitou.html">別冊（解答）を見る</a></p>
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
<div class="bar"><h2>練習問題{i}</h2><ol class="prac big">{prac}</ol><p class="small">解答は<a href="tenkai-kaitou.html#a{i}">別冊（解答）</a>へ。</p></div>
{AD_BTM}
{nav(i)}
"""
        out[fname(i)] = page(f"例題{i} {plain(e['title'])}｜{UNIT}", f"{UNIT}の例題{i}。{plain(e['title'])}。", body)
    fin = "".join(f"<li>{inl(q)}</li>" for q, *_ in FINAL)
    body = f"""
<p class="crumb"><a href="index.html">ホーム</a> ＞ <a href="subject-1.html">数学I</a> ＞ <a href="tenkai.html">{UNIT}</a> ＞ 章末問題</p>
{AD_TOP}
<h1 class="lh"><span class="lbadge">章末問題</span><span class="lsub">{UNIT}</span></h1>
<div class="bar"><p>例題1〜{n}で学んだ手順だけで解ける問題です。まず、どの例題の型かを見分けるところから始めましょう。</p><ol class="prac big">{fin}</ol><p class="small">解答は<a href="tenkai-kaitou.html#final">別冊（解答）</a>へ。</p></div>
{AD_BTM}
<div class="pn"><a href="{fname(n)}">← 例題{n}</a><a href="tenkai.html">例題一覧</a><a href="tenkai-kaitou.html">別冊（解答） →</a></div>
"""
    out["tenkai-final.html"] = page(f"章末問題｜{UNIT}", f"{UNIT}の章末問題。", body)

    ans = f"""
<p class="crumb"><a href="index.html">ホーム</a> ＞ <a href="subject-1.html">数学I</a> ＞ <a href="tenkai.html">{UNIT}</a> ＞ 別冊（解答）</p>
{AD_TOP}
<h1 class="lh"><span class="lbadge">別冊</span><span class="lsub">{UNIT}　練習問題・章末問題の解答</span></h1>
<p class="small">まず自分で解いてから見ましょう。<a href="tenkai.html">← 問題編へもどる</a></p>
"""
    for i, e in enumerate(EX, 1):
        ans += f'<section id="a{i}"><h2 class="sh">練習問題{i}の解答　{tx(e["title"]).replace("<p>","").replace("</p>","")}</h2>'
        for k, (p, (sol, a)) in enumerate(zip(e["prac"], e["pans"]), 1):
            ans += f'<div class="bar"><p><strong>({k})</strong>　{tx(p).replace("<p>","").replace("</p>","")}</p>{tx(sol)}</div>{abox(a, "【答案】", "sm")}'
        ans += "</section>"
    ans += '<section id="final"><h2 class="sh">章末問題の解答</h2>'
    for k, (q, t, sol, a) in enumerate(FINAL, 1):
        ans += f'<div class="bar"><p><strong>{k}.</strong>　{tx(q).replace("<p>","").replace("</p>","")}</p>{tx(sol)}<p class="small">（例題{t}の型）</p></div>{abox(a, "【答案】", "sm")}'
    ans += f'</section>\n{AD_BTM}\n<div class="pn"><a href="tenkai.html">← 問題編へ</a><a href="subject-1.html">数学Iの単元一覧 →</a></div>'
    p2 = page(f"{UNIT}（別冊・解答）", "「式の展開」の練習問題と章末問題の解答。", ans)
    out["tenkai-kaitou.html"] = p2
    return out
