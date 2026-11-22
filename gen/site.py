# -*- coding: utf-8 -*-
"""python3 gen/site.py [--nopdf] で docs/ 全体を作る（サイトHTML＋PDF）"""
import os, sys, glob, html, importlib
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from lib import *
from curriculum import SUBJECTS
SITE_URL="https://example.github.io/suu-lab-oni"
EMAIL="suugakuworakuni@gmail.com"
OWNER_TEXT="数学教師を目指して勉強している大学生が運営しています。"
AD_TOP="<!-- 広告枠（上）：AdSense承認後、ここに広告コードを貼る -->"
AD_BTM="<!-- 広告枠（下）：AdSense承認後、ここに広告コードを貼る -->"
NOPDF="--nopdf" in sys.argv

UNITS={}
for f in sorted(glob.glob(os.path.join(os.path.dirname(os.path.abspath(__file__)),"d_*.py"))):
    m=importlib.import_module(os.path.basename(f)[:-3]); U=m.UNIT
    xn="x"+os.path.basename(f)[1:-3]
    if os.path.exists(os.path.join(os.path.dirname(os.path.abspath(__file__)),xn+".py")):
        X=importlib.import_module(xn).XU; U['examples']=U['examples']+X['examples']; U['chapter_end']=U['chapter_end']+X['chapter_end']
    U['uid']=f"{U['subject']}-{U['ci']+1}-{U['ui']+1}"; UNITS[(U['subject'],U['ci'],U['ui'])]=U
def sname(sid): return [S['name'] for S in SUBJECTS if S['id']==sid][0]

import hashlib as _hl
CSSV=_hl.md5(CSS.encode()).hexdigest()[:8]
def page(title,desc,body,extra_head="",lesson=False):
    return f"""<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(title) if title==SITE_NAME else html.escape(title)+" | "+SITE_NAME}</title>
<link rel="icon" href="favicon.ico?v=1" sizes="any">
<meta name="description" content="{html.escape(desc)}">
<link rel="stylesheet" href="katex/katex.min.css">
<link rel="stylesheet" href="style.css">
<link rel="stylesheet" href="lesson.css?v={CSSV}">
<!-- AdSense承認後：ここに <script async src="https://pagead2.googlesyndication.com/..."></script> を貼る -->
{extra_head}
</head>
<body>
<header class="site-h"><div class="wrap">
<a class="logo" href="index.html"><img src="logo.png" alt="数ラボ鬼 SUU LAB ONI"></a>
<nav><a href="index.html">ホーム</a><a href="about.html">このサイトについて</a><a href="contact.html">お問い合わせ</a></nav>
</div></header>
<main class="wrap">
{body}
</main>
<footer class="site-f"><div class="wrap">
<p><a href="about.html">このサイトについて</a>｜<a href="contact.html">お問い合わせ</a>｜<a href="privacy.html">プライバシーポリシー</a></p>
<p>© {SITE_NAME}　掲載の問題・解説はすべてオリジナルです。</p>
</div></footer>
<script src="katex/katex.min.js"></script>
<script src="katex/auto-render.min.js"></script>
<script>
renderMathInElement(document.body,{{delimiters:[{{left:"\\\\[",right:"\\\\]",display:true}},{{left:"\\\\(",right:"\\\\)",display:false}}],throwOnError:false}});
function fitMath(){{document.querySelectorAll('.katex-display').forEach(function(d){{var k=d.querySelector('.katex');if(!k)return;k.style.fontSize='';var w=d.clientWidth;var h=k.querySelector('.katex-html'),kw=h?h.scrollWidth:0;if(kw>w){{var f=parseFloat(getComputedStyle(k).fontSize);k.style.fontSize=Math.max(f*w/kw*0.97,13)+'px';}}}});}}
function fitInline(){{document.querySelectorAll('.katex').forEach(function(k){{if(k.closest('.katex-display'))return;k.style.fontSize='';var c=k.closest('p,li,div');var w=c?c.clientWidth:0;var kw=k.getBoundingClientRect().width;if(w>0&&kw>w){{var f=parseFloat(getComputedStyle(k).fontSize);k.style.fontSize=Math.max(f*w/kw*0.97,11)+'px';}}}});}}
function fitAll(){{fitMath();fitInline();}}
fitAll();window.addEventListener('resize',fitAll);window.addEventListener('load',fitAll);
</script>
<script src="oni-bg.js"></script>
</body>
</html>
"""
pages={}
def W(name,h): pages[name]=h
def L(b): return f'<div class="lesson">{b}</div>'

# ----- 単元ごとのページ -----
for key,U in UNITS.items():
    uid=U['uid']; S=sname(U['subject']); ex=U['examples']; n=len(ex)
    crumb=f'<p class="crumb"><a href="index.html">ホーム</a> ＞ <a href="subject-{U["subject"]}.html">{S}</a> ＞ <a href="u-{uid}.html">{html.escape(U["name"])}</a></p>'
    lis="".join(f'<a class="card" href="e-{uid}-{i}.html"><span class="lbadge">例題 {i}</span><strong>{html.escape(e["title"])}</strong></a>' for i,e in enumerate(ex,1))
    lis+=f'<a class="card" href="c-{uid}.html"><span class="lbadge">章末</span><strong>章末問題</strong></a>'
    pdfs=f'<p class="dl">PDF：<a href="pdf/{uid}-mondai.pdf">問題編</a>｜<a href="pdf/{uid}-bessatsu.pdf">別冊（練習問題・章末問題の解答）</a></p>'
    W(f"u-{uid}.html",page(f"{U['name']}（{S}・{U['chapter']}）",f"{U['name']}の難問。例題{n}問と章末問題。",
      f'{crumb}{AD_TOP}<h1 class="lh"><span class="lbadge">{S}</span><span class="lsub">{U["chapter"]}　{html.escape(U["name"])}</span></h1><p>{U.get("intro","")}</p><div class="cards">{lis}</div>{pdfs}{AD_BTM}'))
    for i,e in enumerate(ex,1):
        prev=f'<a class="g" href="e-{uid}-{i-1}.html">← 例題{i-1}</a>' if i>1 else f'<a class="g" href="u-{uid}.html">← 単元ページ</a>'
        nxt=f'<a class="g" href="e-{uid}-{i+1}.html">例題{i+1} →</a>' if i<n else f'<a class="g" href="c-{uid}.html">章末問題 →</a>'
        body=(f'{crumb}{AD_TOP}'+L(ex_block(i,e,U['chapter'],with_prac=True)+
          f'<div class="nav2"><a href="a-{uid}-{i}.html">練習問題{i}の解答を見る</a></div><div class="nav2">{prev}{nxt}</div>')+AD_BTM)
        W(f"e-{uid}-{i}.html",page(f"例題{i} {e['title']}（{U['name']}）",f"{U['name']}の難問 例題{i}：{e['title']}",body))
        ab=L(lh("別冊",f"練習問題 {i} の解答　"+e['title'])+prac_answers(i,e)+f'<div class="nav2"><a class="g" href="e-{uid}-{i}.html">← 例題{i}にもどる</a><a class="g" href="u-{uid}.html">単元ページ</a></div>')
        W(f"a-{uid}-{i}.html",page(f"練習問題{i}の解答（{U['name']}）",f"{U['name']} 練習問題{i}の解答",f'{crumb}{ab}'))
    W(f"c-{uid}.html",page(f"章末問題（{U['name']}）",f"{U['name']}の章末問題。",
      f'{crumb}{AD_TOP}'+L(lh("章末問題",U['name'])+f'<p>例題1〜{n}で学んだ手順だけで解ける問題です。まず、どの例題の型かを見分けるところから始めましょう。</p><ol class="cl">{ch_list(U)}</ol><div class="nav2"><a href="ca-{uid}.html">章末問題の解答を見る</a></div><div class="nav2"><a class="g" href="e-{uid}-{n}.html">← 例題{n}</a><a class="g" href="u-{uid}.html">単元ページ</a></div>')+AD_BTM))
    W(f"ca-{uid}.html",page(f"章末問題の解答（{U['name']}）",f"{U['name']}の章末問題の解答。",
      f'{crumb}'+L(lh("別冊","章末問題の解答")+ch_answers(U)+f'<div class="nav2"><a class="g" href="c-{uid}.html">← 章末問題</a><a class="g" href="u-{uid}.html">単元ページ</a></div>')))
    if not NOPDF: unit_pdfs(U,uid)

# ----- トップ・科目・固定ページ -----
def top():
    cards=""
    for S in SUBJECTS:
        t=sum(len(us) for _,us in S["chapters"])
        n=sum(1 for ci,(_,us) in enumerate(S["chapters"]) for ui,_ in enumerate(us) if (S["id"],ci,ui) in UNITS)
        cards+=f'<a class="card" href="subject-{S["id"]}.html"><span class="lbadge">{S["name"]}</span><strong>{len(S["chapters"])}分野・{t}単元</strong><span class="small">公開済み {n} 単元</span></a>'
    b=f"""
<section class="hero"><span class="hm">HARD MODE</span><img src="logo.png" alt="数ラボ鬼 SUU LAB ONI">
<p>高校数学の難問に挑む問題集。「目次 → 単元 → 例題」の順にたどれます。難問も、例題の手順を1つずつ追えば解けるように、途中の計算を省かずに解説します。単元は順に追加していきます。</p></section>
{AD_TOP}
<h2 class="sh">目次</h2>
<div class="cards">{cards}</div>
<p class="small">※「準備中」の単元は、できあがり次第公開します。</p>
<h2 class="sh">関連サイト</h2>
<div class="cards"><a class="card" href="https://takenoppoo.github.io/index.html" style="grid-column:1/-1"><span class="lbadge">基礎</span><strong>基礎から学ぶ（数ラボ）</strong><span class="small">数ラボ鬼の前に、まず基礎を固めたい人向け。</span></a></div>
{AD_BTM}
"""
    return page(SITE_NAME,"高校数学（数学I・A・II・B・III・C）の難問を、例題の手順を追って練習できる問題集。",b)
def subject(S):
    secs=""; ready=False
    for ci,(ch,units) in enumerate(S["chapters"]):
        lis=""
        for ui,(u,_) in enumerate(units):
            U=UNITS.get((S["id"],ci,ui))
            if U: lis+=f'<li class="on"><a href="u-{U["uid"]}.html">{html.escape(u)}</a></li>'; ready=True
            else: lis+=f'<li class="off">{html.escape(u)}<span>準備中</span></li>'
        secs+=f'<h3 class="gh">{html.escape(ch)}</h3><ul class="ulist">{lis}</ul>'
    b=f'<p class="crumb"><a href="index.html">ホーム</a> ＞ {S["name"]}</p>{AD_TOP}<h1 class="lh"><span class="lbadge">{S["name"]}</span><span class="lsub">単元一覧</span></h1>{secs}{AD_BTM}'
    return page(f"{S['name']}の単元一覧",f"{S['name']}の難問の単元一覧。",b,"" if ready else '<meta name="robots" content="noindex">')
def about():
    return page("このサイトについて",f"{SITE_NAME}の運営方針。",f"""
<h1>このサイトについて</h1>
<section class="bar navy"><h2>サイトの目的</h2><p>{SITE_NAME}は、数ラボの難問版です。難しい問題でも手順を追って理解できるように、例題で考え方とSTEPを示します。</p></section>
<section class="bar navy"><h2>運営者</h2><p>{html.escape(OWNER_TEXT)}</p></section>
<section class="bar navy"><h2>掲載内容について</h2><p>掲載している問題・解説は、運営者がオリジナルで作成したものです。誤りに気づかれた場合は<a href="contact.html">お問い合わせ</a>からご連絡ください。</p></section>
<section class="bar navy"><h2>広告について</h2><p>運営費のために広告を掲載することがあります。詳しくは<a href="privacy.html">プライバシーポリシー</a>をご覧ください。</p></section>""")
def contact():
    return page("お問い合わせ",f"{SITE_NAME}へのお問い合わせ先。",f"""
<h1>お問い合わせ</h1>
<section class="bar navy"><h2>連絡先</h2><p>問題・解答の誤りのご指摘、ご意見、ご要望は、下記のメールアドレスまでご連絡ください。</p><p class="mail">{html.escape(EMAIL)}</p><p class="small">※返信までお時間をいただくことがあります。</p></section>""")
def privacy():
    return page("プライバシーポリシー","プライバシーポリシー。","""
<h1>プライバシーポリシー</h1>
<section class="bar navy"><h2>広告の配信について</h2><p>第三者配信の広告サービス（Google AdSense）を利用することがあります。広告配信事業者は、興味に応じた広告を表示するためにCookieを使用することがあります。詳細は<a href="https://policies.google.com/technologies/ads?hl=ja" rel="noopener">Googleのポリシーと規約</a>をご確認ください。</p></section>
<section class="bar navy"><h2>アクセス解析について</h2><p>アクセス状況を把握するためにアクセス解析ツールを利用することがあります。Cookieを使って情報を収集しますが、個人を特定するものではありません。</p></section>
<section class="bar navy"><h2>個人情報の取り扱い</h2><p>お問い合わせでいただいた情報は、ご返信の目的以外には使用しません。法令に基づく場合を除き、第三者に提供しません。</p></section>
<section class="bar navy"><h2>免責事項</h2><p>内容の正確さに努めていますが、完全性を保証するものではありません。利用により生じた損害について、責任を負いかねます。</p></section>""")
W("index.html",top()); W("about.html",about()); W("contact.html",contact()); W("privacy.html",privacy())
for S in SUBJECTS: W(f"subject-{S['id']}.html",subject(S))
for f,h in pages.items(): open(os.path.join(OUT,f),"w",encoding="utf-8").write(tidy_math(h))
open(os.path.join(OUT,"robots.txt"),"w").write(f"User-agent: *\nAllow: /\nSitemap: {SITE_URL}/sitemap.xml\n")
open(os.path.join(OUT,"sitemap.xml"),"w").write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+"".join(f"<url><loc>{SITE_URL}/{f}</loc></url>\n" for f in pages if not f.startswith(("a-","ca-","subject-")) or True)+"</urlset>\n")
print(len(pages),"pages;",len(UNITS),"units")
