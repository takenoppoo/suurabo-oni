# -*- coding: utf-8 -*-
"""数ラボ鬼：データ(UNITS)からサイトHTMLとPDFを作る共通ライブラリ"""
import os, html, subprocess, shutil, sys
HERE=os.path.dirname(os.path.abspath(__file__))
ROOT=os.path.dirname(HERE)
OUT=os.path.join(ROOT,"docs")
FIG=os.path.join(OUT,"fig"); PDFD=os.path.join(OUT,"pdf")
for d in (FIG,PDFD): os.makedirs(d,exist_ok=True)
SITE_NAME="数ラボ鬼"

def I(s): return "\\("+s.replace("<","&lt;")+"\\)"
def D(s): return "\\["+s.replace("<","&lt;")+"\\]"
def step(n,t,b): return f'<div class="step"><div class="sh2"><span class="badge">STEP {n}</span> {t}</div><div class="sb">{b}</div></div>'
def img(name,w=60,cap=""):
    c=f'<div class="cap">{cap}</div>' if cap else ""
    return f'<div class="figbox"><img class="fig" src="fig/{name}.svg" style="width:{w}%" alt="{html.escape(cap or name)}">{c}</div>'

# ---------- 図（matplotlib → SVG） ----------
def make_fig(name, fn, size=(5,3)):
    import matplotlib; matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    matplotlib.rcParams["svg.fonttype"]="path"
    matplotlib.rcParams["font.family"]=["Noto Sans CJK JP","DejaVu Sans"]
    matplotlib.rcParams["mathtext.fontset"]="cm"
    matplotlib.rcParams["axes.unicode_minus"]=False
    fig,ax=plt.subplots(figsize=size)
    fn(ax)
    fig.savefig(os.path.join(FIG,name+".svg"),bbox_inches="tight",transparent=False,facecolor="white")
    plt.close(fig)

RED="#b81f36"
def numline(ax,lo,hi,ticks,labels=None,segs=(),pts=(),pad=0.8):
    """数直線。segs=[(a,b)]（太線）、pts=[(x,'open'|'closed')]"""
    ax.set_xlim(lo-pad,hi+pad); ax.set_ylim(-1,1.2); ax.axis("off")
    ax.annotate("",xy=(hi+pad,0),xytext=(lo-pad,0),arrowprops=dict(arrowstyle="->",lw=1.4,color="#333"))
    for i,t in enumerate(ticks):
        ax.plot([t,t],[-.08,.08],color="#333",lw=1.2)
        lab=labels[i] if labels else str(t)
        ax.text(t,-.38,lab,ha="center",va="top",fontsize=12)
    for a,b in segs:
        a2=lo-pad if a is None else a; b2=hi+pad if b is None else b
        ax.plot([a2,b2],[0,0],color=RED,lw=5,solid_capstyle="butt")
    for x,k in pts:
        ax.plot([x],[0],"o",ms=9,mfc=("white" if k=="open" else RED),mec=RED,mew=2,zorder=5)

# ---------- CSS ----------
CSS='''
.lesson{line-height:1.65}
.lesson .lh{display:flex;align-items:center;gap:10px;border-bottom:3px solid #b81f36;padding-bottom:6px;margin:0 0 10px;flex-wrap:wrap}
.lesson .lb{background:#b81f36;color:#fff;font-weight:700;padding:3px 12px;font-size:1.12em;white-space:nowrap}
.lesson .ls{font-size:.98em;color:#333}
.lesson .qbox{background:#FDF0F2;border:1.5px solid #D6455A;border-radius:10px;padding:4px 14px;margin:8px 0}
.lesson .qbox p{margin:3px 0}
.lesson .qbox .katex-display{font-size:1.35em;margin:.35em 0}
.lesson .bar{background:#F8F4F4;border-left:4px solid #b81f36;padding:5px 12px 7px;margin:9px 0}
.lesson .bar h2{margin:0 0 3px;font-size:1em;color:#b81f36}
.lesson .bar p{margin:3px 0}
.lesson .bar .katex-display{margin:.35em 0;font-size:1.1em}
.lesson .kotsu{border:1.4px dashed #1f8a5b;border-radius:8px;background:#f1faf5;padding:3px 10px;margin:6px 0;font-size:.95em}
.lesson .kotsu b{background:#1f8a5b;color:#fff;border-radius:4px;padding:0 6px;margin-right:6px}
.lesson .step{margin:5px 0}.lesson .sh2{font-weight:700}
.lesson .badge{background:#b81f36;color:#fff;padding:1px 7px;font-size:.85em;margin-right:4px}
.lesson .sb{margin-left:3px}.lesson .sb p{margin:2px 0}.lesson .sb .katex-display{margin:.3em 0;font-size:1.05em}
.lesson .abox{border:2px solid #b81f36;border-radius:10px;padding:4px 14px;margin:9px 0;position:relative;background:#fff}
.lesson .abox .ah{font-weight:700;margin:0}
.lesson .abox .katex-display{margin:.3em 0;font-size:1.2em}
.lesson .mark{position:absolute;right:14px;bottom:6px;color:#c0283c;font-size:1.4em;font-weight:700;margin:0}
.lesson .prac{padding-left:1.5em;margin:3px 0}.lesson .prac li{margin:5px 0}
.lesson .tbl{border-collapse:collapse;margin:4px auto}.lesson .tbl th,.lesson .tbl td{border:1px solid #bbb;padding:1px 12px;text-align:center}
.lesson .cl{padding-left:1.6em}.lesson .cl li{margin:10px 0}
.lesson .item{margin:8px 0;padding-bottom:4px;border-bottom:1px solid #eee}
.lesson .item p.pq{margin:2px 0;font-weight:700}
.lesson .item .abox{margin:5px 0;padding:2px 12px}.lesson .item .abox .katex-display{font-size:1.1em;margin:.2em 0}
.lesson .item .mark{font-size:1.15em;bottom:3px}
.lesson .small{font-size:.85em;color:#666}
.lesson .figbox{text-align:center;margin:4px 0}
.lesson .fig{display:inline-block;max-width:100%;height:auto}
.lesson .cap{font-size:.82em;color:#666}
.lesson .nav2{display:flex;justify-content:space-between;gap:8px;flex-wrap:wrap;margin:16px 0}
.lesson .nav2 a{background:#b81f36;color:#fff;padding:6px 14px;border-radius:6px;text-decoration:none;font-size:.9em}
.lesson .nav2 a.g{background:#fff;color:#b81f36;border:1.5px solid #b81f36}
.lesson .dl{margin:10px 0;font-size:.95em}
'''
open(os.path.join(OUT,"lesson.css"),"w",encoding="utf-8").write(CSS)

# ---------- 部品 ----------
def lh(badge,sub): return f'<h1 class="lh"><span class="lb">{badge}</span><span class="ls">{sub}</span></h1>'
def isM(p): return p.startswith("\\(") or p.startswith("<")
def M(p): return p if isM(p) else I(p)

def ex_block(i,e,sub,with_prac=True):
    pr="".join(f"<li>{M(p)}</li>" for p in e['practice'])
    return (lh(f"例題 {i}",f"{sub}　"+e['title'])+
     f'<div class="qbox"><p>{e["problem"]}</p></div>'
     f'<div class="bar"><h2>解き方（まず考え方）</h2>{e["approach"]}<div class="kotsu"><b>コツ</b>{e["kotsu"]}</div></div>'
     f'<div class="bar"><h2>解答</h2>{"".join(e["steps"])}</div>'
     f'<div class="abox"><p class="ah">【答案（テストに書く形）】</p>{D(e["answer"])}<p class="mark">答</p></div>'
     +(f'<div class="bar"><h2>練習問題 {i}</h2><ol class="prac">{pr}</ol></div>' if with_prac else ""))
def ans_item(label,prob,steps,ans):
    ab=f'<div class="abox"><p class="ah">【答案】</p>{D(ans)}<p class="mark">答</p></div>' if ans else ""
    return f'<div class="item"><p class="pq">{label}　{M(prob)}</p><div class="sb">{steps}</div>{ab}</div>'
def prac_answers(i,e):
    return "".join(ans_item(f"({n})",e['practice'][n-1],st,an) for n,(st,an) in enumerate(e['pans'],1))
def ch_list(U):
    return "".join(f"<li>{M(p)}</li>" for p,_,_,_ in U['chapter_end'])
def ch_answers(U):
    return "".join(ans_item(f"{n}.",p,st+f'<p class="small">（例題{k}の型）</p>',an) for n,(p,st,an,k) in enumerate(U['chapter_end'],1))

# ---------- PDF ----------
FIT='''<script>
window.addEventListener("load",function(){});
function fit(){document.querySelectorAll(".pg").forEach(function(pg){var z=1;pg.style.zoom=1;
 while(pg.scrollHeight>1030&&z>0.55){z-=0.02;pg.style.zoom=z;}});}
</script>'''
PCSS='@page{size:A4;margin:11mm}body{margin:0;color:#222;font-family:"Noto Sans CJK JP",sans-serif}.lesson{font-size:12pt}.pg{page-break-after:always;width:188mm}.pg:last-child{page-break-after:auto}'
def pdf_html(pages):
    body="".join(f'<section class="pg"><div class="lesson">{p}</div></section>' for p in pages)
    return ('<!DOCTYPE html><html lang="ja"><head><meta charset="utf-8"><link rel="stylesheet" href="katex/katex.min.css"><link rel="stylesheet" href="lesson.css"><style>'+PCSS+'</style></head><body>'+body+
     '<script src="katex/katex.min.js"></script><script src="katex/auto-render.min.js"></script><script>renderMathInElement(document.body,{delimiters:[{left:"\\\\[",right:"\\\\]",display:true},{left:"\\\\(",right:"\\\\)",display:false}],throwOnError:false});'
     'document.querySelectorAll(".pg").forEach(function(pg){var L=pg.firstChild,z=1;pg.style.zoom=1;while(L.getBoundingClientRect().height>1015&&z>0.35){z-=0.02;pg.style.zoom=z;}});</script></body></html>')
def make_pdf(pages,outname):
    tmp=os.path.join(OUT,"_tmp_"+outname+".html")
    open(tmp,"w",encoding="utf-8").write(pdf_html(pages))
    pdf=os.path.join(PDFD,outname)
    subprocess.run(["google-chrome","--headless","--no-sandbox","--disable-gpu","--no-pdf-header-footer","--virtual-time-budget=15000","--print-to-pdf="+pdf,"file://"+tmp],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL,check=True)
    os.remove(tmp)
    return pdf
def unit_pdfs(U,uid):
    sub=U['chapter']
    main=[ex_block(i,e,sub) for i,e in enumerate(U['examples'],1)]
    main.append(lh("章末問題",U['name'])+f'<p>例題1〜{len(U["examples"])}で学んだ手順だけで解ける問題です。まず、どの例題の型かを見分けるところから始めましょう。</p><ol class="cl">{ch_list(U)}</ol>')
    make_pdf(main,f"{uid}-mondai.pdf")
    bk=[lh("別冊",f"練習問題 {i} の解答　"+e['title'])+prac_answers(i,e) for i,e in enumerate(U['examples'],1)]
    items=[ans_item(f"{n}.",p,st+f'<p class="small">（例題{k}の型）</p>',an) for n,(p,st,an,k) in enumerate(U['chapter_end'],1)]
    for k in range(0,len(items),3): bk.append(lh("別冊","章末問題の解答")+"".join(items[k:k+3]))
    make_pdf(bk,f"{uid}-bessatsu.pdf")
