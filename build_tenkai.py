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

def make(page, AD_TOP, AD_BTM):
    n = len(EX)
    toc = "".join(f'<li><a href="#ex{i+1}">例題{i+1}　{html.escape(plain(e["title"]))}</a></li>' for i, e in enumerate(EX))
    toc += '<li><a href="#final">章末問題</a></li>'
    body = f"""
<p class="crumb"><a href="index.html">ホーム</a> ＞ <a href="subject-1.html">数学I</a> ＞ {UNIT}</p>
{AD_TOP}
<h1 class="lh"><span class="lbadge">数学I</span><span class="lsub">{UNIT}（問題編）</span></h1>
<section class="bar"><h2>この単元の進め方</h2>
<p>例題を読んで「考え方 → STEP」の手順をつかみ、同じ手順で練習問題を解きます。練習問題の解答は<a href="tenkai-kaitou.html">別冊（解答）</a>にあります。</p>
<p class="dl">PDF：<a href="pdf/tenkai-mondai-hen.pdf">問題編</a>　<a href="pdf/tenkai-bessatsu.pdf">別冊（解答）</a></p></section>
<ul class="links">{toc}</ul>
"""
    for i, e in enumerate(EX, 1):
        steps = "".join(f'<div class="step"><div class="step-h"><span class="badge">STEP {k}</span> {tx(t).replace("<p>","").replace("</p>","")}</div><div class="step-b">{tx(b)}</div></div>' for k, (t, b) in enumerate(e["steps"], 1))
        prac = "".join(f"<li>{tx(p).replace('<p>','').replace('</p>','')}</li>" for p in e["prac"])
        body += f"""
<section id="ex{i}">
<h2 class="sh">例題{i}　{tx(e['title']).replace('<p>','').replace('</p>','')}</h2>
<div class="qbox">{tx(e['q'])}</div>
<div class="bar"><h2>解き方（まず考え方）</h2>{tx(e['idea'])}<p class="small"><strong class="ok">コツ</strong>　{tx(e['tip']).replace('<p>','').replace('</p>','')}</p></div>
<div class="bar"><h2>解答</h2>{steps}</div>
{abox(e['ans'])}
<div class="bar"><h2>練習問題{i}</h2><ol class="prac big">{prac}</ol></div>
</section>"""
    fin = "".join(f"<li>{tx(q).replace('<p>','').replace('</p>','')}</li>" for q, *_ in FINAL)
    body += f"""
<section id="final">
<h2 class="sh">章末問題　{UNIT}</h2>
<div class="bar"><p>例題1〜{n}で学んだ手順だけで解ける問題です。まず、どの例題の型かを見分けるところから始めましょう。</p><ol class="prac big">{fin}</ol></div>
</section>
{AD_BTM}
<div class="pn"><a href="subject-1.html">← 数学Iの単元一覧</a><a href="tenkai-kaitou.html">別冊（解答）へ →</a></div>
"""
    p1 = page(f"{UNIT}（問題編）", "数学Iの「式の展開」の難問。係数比べ・展開の工夫・対称式・次数下げを、例題の手順で練習できます。", body)

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
    return {"tenkai.html": p1, "tenkai-kaitou.html": p2}
