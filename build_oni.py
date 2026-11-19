# -*- coding: utf-8 -*-
"""数ラボ鬼 サイトの土台を docs/ に作る。CONFIG だけ書き換えて python3 build_oni.py"""
import os, html, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from curriculum import SUBJECTS
SITE_NAME="数ラボ鬼"; SITE_URL="https://takenoppoo.github.io/suurabo-oni"
EMAIL="suugakuworakuni@gmail.com"
OWNER_TEXT="数学教師を目指して勉強している大学生が運営しています。"
OUT=os.path.join(os.path.dirname(os.path.abspath(__file__)),"docs")
AD_TOP="<!-- 広告枠（上）：AdSense承認後、ここに広告コードを貼る -->"
AD_BTM="<!-- 広告枠（下）：AdSense承認後、ここに広告コードを貼る -->"
def page(title,desc,body,extra_head=""):
    return f"""<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(title)} | {SITE_NAME}</title>
<meta name="description" content="{html.escape(desc)}">
<link rel="stylesheet" href="katex/katex.min.css">
<link rel="stylesheet" href="style.css?v=20261123">
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
function fitMath(){{document.querySelectorAll('.katex-display').forEach(function(d){{var k=d.querySelector('.katex');if(!k)return;k.style.fontSize='';var w=d.clientWidth;var h=k.querySelector('.katex-html'),kw=h?h.scrollWidth:0;if(kw>w){{var f=parseFloat(getComputedStyle(k).fontSize);k.style.fontSize=Math.max(f*w/kw*0.97,14)+'px';}}}});}}
fitMath();window.addEventListener('resize',fitMath);window.addEventListener('load',fitMath);
</script>
<script src="oni-bg.js"></script>
</body>
</html>
"""
def top():
    cards=""
    for S in SUBJECTS:
        n=sum(1 for _,us in S["chapters"] for _,f in us if f); t=sum(len(us) for _,us in S["chapters"])
        cards+=f'<a class="card" href="subject-{S["id"]}.html"><span class="lbadge">{S["name"]}</span><strong>{len(S["chapters"])}分野・{t}単元</strong><span class="small">公開済み {n} 単元</span></a>'
    b=f"""
<section class="hero"><span class="hm">HARD MODE</span><img src="logo.png" alt="数ラボ鬼 SUU LAB ONI">
<p>高校数学の難問に挑む問題集。「目次 → 単元 → 例題」の順にたどれます。難問も、例題の手順を1つずつ追えば解けるように解説します。単元は順に追加していきます。</p></section>
{AD_TOP}
<h2 class="sh">目次</h2>
<div class="cards">{cards}</div>
<p class="small">※「準備中」の単元は、できあがり次第公開します。</p>
{AD_BTM}
"""
    return page("高校数学の難問集","高校数学（数学I・A・II・B・III・C）の難問を、例題の手順を追って練習できる問題集。",b)
def subject(S):
    secs=""
    for ch,units in S["chapters"]:
        lis="".join((f'<li class="on"><a href="{f}">{html.escape(u)}</a></li>' if f else f'<li class="off">{html.escape(u)}<span>準備中</span></li>') for u,f in units)
        secs+=f'<h3 class="gh">{html.escape(ch)}</h3><ul class="ulist">{lis}</ul>'
    ready=any(f for _,us in S["chapters"] for _,f in us)
    b=f"""
<p class="crumb"><a href="index.html">ホーム</a> ＞ {S['name']}</p>
{AD_TOP}
<h1 class="lh"><span class="lbadge">{S['name']}</span><span class="lsub">単元一覧</span></h1>
{secs}
{AD_BTM}
"""
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
pages={"index.html":top(),"about.html":about(),"contact.html":contact(),"privacy.html":privacy()}
for S in SUBJECTS: pages[f"subject-{S['id']}.html"]=subject(S)
from build_tenkai import make as make_tenkai
pages.update(make_tenkai(page,AD_TOP,AD_BTM))
for f,h in pages.items(): open(os.path.join(OUT,f),"w",encoding="utf-8").write(h)
open(os.path.join(OUT,"robots.txt"),"w").write(f"User-agent: *\nAllow: /\nSitemap: {SITE_URL}/sitemap.xml\n")
open(os.path.join(OUT,"sitemap.xml"),"w").write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+"".join(f"<url><loc>{SITE_URL}/{f}</loc></url>\n" for f in ("index.html","about.html","contact.html","privacy.html","subject-1.html","tenkai.html","tenkai-final.html","kaito-tenkai-final.html")+tuple(f"tenkai-{i}.html" for i in range(1,10))+tuple(f"kaito-tenkai-{i}.html" for i in range(1,10)))+"</urlset>\n")
print(len(pages),"pages")
