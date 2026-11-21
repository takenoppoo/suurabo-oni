# -*- coding: utf-8 -*-
"""数ラボ鬼：データ(UNITS)からサイトHTMLとPDFを作る共通ライブラリ"""
import re, os, html, subprocess, shutil, sys
HERE=os.path.dirname(os.path.abspath(__file__))
ROOT=os.path.dirname(HERE)
OUT=os.path.join(ROOT,"docs")
FIG=os.path.join(OUT,"fig"); PDFD=os.path.join(OUT,"pdf")
for d in (FIG,PDFD): os.makedirs(d,exist_ok=True)
SITE_NAME="数ラボ鬼"

def I(s): return "\\("+s.replace("<","&lt;")+"\\)"
def D(s): return "\\["+s.replace("<","&lt;")+"\\]"
def step(n,t,b): return f'<div class="step"><div class="sh2"><span class="badge">STEP {n}</span> {t}</div><div class="sb">{b}</div></div>'
def wtable(head,rows):
    """表。head=見出しのリスト、rows=行のリスト（各セルはHTML／数式は \\( \\) で書く）"""
    h="".join(f"<th>{c}</th>" for c in head)
    r="".join("<tr>"+"".join(f"<td>{c}</td>" for c in row)+"</tr>" for row in rows)
    return f'<table class="tbl"><tr>{h}</tr>{r}</table>'
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
    fig.savefig(os.path.join(FIG,name+".svg"),bbox_inches="tight",pad_inches=0.18,transparent=False,facecolor="white")
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
.lesson{line-height:1.65;overflow-wrap:anywhere}.lesson .katex-display{overflow-x:auto;overflow-y:hidden;max-width:100%;padding:.5em 0 .45em}.lesson img{max-width:100%;height:auto}.lesson svg:not(.katex svg){max-width:100%;height:auto}
.lesson .lh{display:flex;align-items:center;gap:10px;border-bottom:3px solid #b81f36;padding-bottom:6px;margin:0 0 10px;flex-wrap:wrap}
.lesson .lb{background:#b81f36;color:#fff;font-weight:700;padding:3px 12px;font-size:1.12em;white-space:nowrap}
.lesson .ls{font-size:.98em;color:#333}
.lesson .qbox{background:#FDF0F2;border:1.5px solid #D6455A;border-radius:10px;padding:4px 14px;margin:8px 0}
.lesson .qbox p{margin:3px 0}
.lesson .qbox .katex-display{font-size:1.35em;margin:.35em 0}
.lesson .bar{background:#F8F4F4;border-left:4px solid #b81f36;padding:5px 12px 7px;margin:9px 0}
.lesson .bar.sol{background:#fff;border:1.5px solid #e2c3c9;border-left:5px solid #b81f36;border-radius:8px;padding:8px 16px 10px;box-shadow:0 1px 4px rgba(0,0,0,.08)}
.lesson ol.cl{background:#fff;border:1.5px solid #e2c3c9;border-left:5px solid #b81f36;border-radius:8px;padding:8px 16px 8px 2.4em;box-shadow:0 1px 4px rgba(0,0,0,.08)}
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
.lesson .item{margin:10px 0;padding:6px 16px 6px;background:#fff;border:1.5px solid #e2c3c9;border-left:5px solid #b81f36;border-radius:8px;box-shadow:0 1px 4px rgba(0,0,0,.08)}
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


def ucfig(name,th,cx,sy,thtxt=r"\theta",reftxt="",w=42,label=True):
    """単位円の図。th=角（ラジアンの実数）、cx,sy=P の座標（数式文字列）、thtxt=角のラベル、reftxt=基準角のラベル（空なら描かない）。imgタグを返す"""
    import numpy as np
    from matplotlib.patches import Arc
    def fn(ax):
        ax.set_aspect("equal"); ax.set_xlim(-2.1,2.1); ax.set_ylim(-1.5,1.5); ax.axis("off")
        t=np.linspace(0,2*np.pi,300); ax.plot(np.cos(t),np.sin(t),color="#555",lw=1.3)
        ax.annotate("",xy=(1.5,0),xytext=(-1.5,0),arrowprops=dict(arrowstyle="->",lw=1,color="#333"))
        ax.annotate("",xy=(0,1.42),xytext=(0,-1.42),arrowprops=dict(arrowstyle="->",lw=1,color="#333"))
        ax.text(1.5,-.2,"x",fontsize=10); ax.text(.07,1.38,"y",fontsize=10)
        px,py=np.cos(th),np.sin(th)
        ax.plot([0,px],[0,py],color=RED,lw=2); ax.plot([px],[py],"o",color=RED,ms=6,zorder=5)
        ax.plot([px,px],[0,py],color="#999",lw=1,ls="--"); ax.plot([0,px],[py,py],color="#999",lw=1,ls="--")
        a1,a2=(0,np.degrees(th)) if th>=0 else (np.degrees(th),0)
        ax.add_patch(Arc((0,0),.5,.5,theta1=a1,theta2=a2,color="#1f6fb8",lw=1.6))
        m=th/2; ax.text(.3*np.cos(m),.3*np.sin(m),"$"+thtxt+"$",fontsize=11,color="#1f6fb8",ha="center",va="center")
        if reftxt:
            k=round(th/np.pi); base=k*np.pi if abs(th-k*np.pi)<np.pi/2+1e-9 else k*np.pi
            ax.add_patch(Arc((0,0),1.1,1.1,theta1=min(np.degrees(th),np.degrees(base)),theta2=max(np.degrees(th),np.degrees(base)),color="#1f8a5b",lw=1.8))
            mm=(th+base)/2; ax.text(.78*np.cos(mm),.78*np.sin(mm),"$"+reftxt+"$",fontsize=10,color="#1f8a5b",ha="center",va="center",bbox=dict(fc="white",ec="none",pad=1.2))
        if label:
            dx=.1 if px>=0 else -.1; dy=.12 if py>=0 else -.2
            ax.text(px+dx,py+dy,"P$\\left("+cx+",\\ "+sy+"\\right)$",fontsize=10,ha=("left" if px>=0 else "right"),va="center")
    make_fig(name,fn,size=(3.6,3.4))
    return img(name,w)

def uceq(name,fn,v,pts=(),arcs=(),w=46):
    """単位円で方程式・不等式を解く図。fn='sin'|'cos'|'tan'、v=値（実数）、pts=[(角,ラベル)]、arcs=[(始角,終角)]（答えの範囲を太線にする）"""
    import numpy as np
    from matplotlib.patches import Wedge
    def fn_(ax):
        ax.set_aspect("equal"); ax.set_xlim(-2.0,2.0); ax.set_ylim(-1.55,1.55); ax.axis("off")
        t=np.linspace(0,2*np.pi,400); ax.plot(np.cos(t),np.sin(t),color="#555",lw=1.3)
        ax.annotate("",xy=(1.55,0),xytext=(-1.55,0),arrowprops=dict(arrowstyle="->",lw=1,color="#333"))
        ax.annotate("",xy=(0,1.45),xytext=(0,-1.45),arrowprops=dict(arrowstyle="->",lw=1,color="#333"))
        for a,b in arcs:
            ax.add_patch(Wedge((0,0),1,np.degrees(a),np.degrees(b),fc="#cfe2f5",ec="none",alpha=.8,zorder=0))
            tt=np.linspace(a,b,100); ax.plot(np.cos(tt),np.sin(tt),color="#1f6fb8",lw=4,solid_capstyle="butt")
        if fn=="sin": ax.plot([-1.3,1.3],[v,v],color=RED,ls="--",lw=1.4); ax.text(1.35,v,"$y=%s$"%("%.3g"%v),fontsize=9,color=RED,va="center")
        elif fn=="cos": ax.plot([v,v],[-1.3,1.3],color=RED,ls="--",lw=1.4); ax.text(v,1.36,"$x=%s$"%("%.3g"%v),fontsize=9,color=RED,ha="center")
        else:
            ax.plot([1,1],[-1.45,1.45],color="#999",lw=1,ls="-"); ax.text(1.05,-1.4,"$x=1$",fontsize=8,color="#666")
            ax.plot([-1.5,1.5],[-1.5*v,1.5*v],color=RED,ls="--",lw=1.2)
            ax.plot([1],[v],"s",color=RED,ms=5)
        for ang,lab in pts:
            px,py=np.cos(ang),np.sin(ang); ax.plot([px],[py],"o",color=RED,ms=6,zorder=5)
            ax.text(px*1.22+(.04 if px>=0 else -.04),py*1.22+(.16 if py>=0 else -.16),"$"+lab+"$",fontsize=10,ha=("left" if px>=0 else "right"),va="center",color="#222")
    make_fig(name,fn_,size=(4.0,3.3))
    return img(name,w)

def normfig(name,a,b,w=50):
    """標準正規分布の曲線で P(a<=Z<=b) の面積を塗る。a,b は数値かNone(無限)"""
    import numpy as np
    lo=-4.0 if a is None else float(a); hi=4.0 if b is None else float(b)
    def fn_(ax):
        xs=np.linspace(-3.8,3.8,400); ys=np.exp(-xs**2/2)/np.sqrt(2*np.pi)
        ax.plot(xs,ys,color="#b81f36",lw=2)
        m=(xs>=lo)&(xs<=hi); ax.fill_between(xs[m],0,ys[m],color="#cfe2f5",alpha=.9)
        ax.axhline(0,color="#333",lw=1); ax.axvline(0,color="#999",lw=.8,ls="--")
        for v in (a,b):
            if v is not None: ax.plot([float(v)]*2,[0,np.exp(-float(v)**2/2)/np.sqrt(2*np.pi)],color="#1f6fb8",lw=1.5); ax.text(float(v),-0.035,"%g"%float(v),ha="center",va="top",fontsize=9)
        ax.text(0,-0.035,"0",ha="center",va="top",fontsize=9); ax.set_xlim(-3.9,3.9); ax.set_ylim(-0.08,0.45); ax.axis("off")
    make_fig(name,fn_,size=(4.2,2.4))
    return img(name,w)

def ucsum(name,a,b,sign,cx,sy,w=46):
    """加法定理用の単位円。角α、β（度）と α±β の動径を描き、α±β の点の座標を書く。imgタグを返す"""
    import numpy as np
    from matplotlib.patches import Arc
    T=a+sign*b
    def fn(ax):
        ax.set_aspect("equal"); ax.set_xlim(-2.1,2.1); ax.set_ylim(-1.9,1.5); ax.axis("off")
        t=np.linspace(0,2*np.pi,300); ax.plot(np.cos(t),np.sin(t),color="#555",lw=1.3)
        ax.annotate("",xy=(1.5,0),xytext=(-1.5,0),arrowprops=dict(arrowstyle="->",lw=1,color="#333"))
        ax.annotate("",xy=(0,1.42),xytext=(0,-1.42),arrowprops=dict(arrowstyle="->",lw=1,color="#333"))
        for ang,col,lab,rr in [(a,"#1f6fb8",r"\alpha=%d^\circ"%a,1.0),(b,"#1f8a5b",r"\beta=%d^\circ"%b,1.0),(T,RED,r"\alpha%s\beta=%d^\circ"%("+" if sign>0 else "-",T),1.0)]:
            r_=np.radians(ang); ax.plot([0,np.cos(r_)],[0,np.sin(r_)],color=col,lw=2 if col==RED else 1.4,ls="-" if col==RED else "--")
            ax.plot([np.cos(r_)],[np.sin(r_)],"o",color=col,ms=5)
            ax.text(1.15*np.cos(r_)+(.04 if np.cos(r_)>=0 else -.04),1.15*np.sin(r_)+(.12 if np.sin(r_)>=0 else -.12),"$"+lab+"$",fontsize=9,color=col,ha=("left" if np.cos(r_)>=0 else "right"))
        ax.text(0,-1.42,"P$\\left("+cx+",\\ "+sy+"\\right)$（赤い点の座標）",fontsize=10,color="#222",ha="center",va="top")
        lo,hi=sorted([0,T]); ax.add_patch(Arc((0,0),.5,.5,theta1=lo,theta2=hi,color=RED,lw=1.6))
    make_fig(name,fn,size=(4.2,3.3))
    return img(name,w)
# ---------- 部品 ----------
def lh(badge,sub): return f'<h1 class="lh"><span class="lb">{badge}</span><span class="ls">{sub}</span></h1>'
def isM(p): return p.startswith("\\(") or p.startswith("<") or "\\(" in p or ("\\text{" not in p and any(ord(ch)>0x3000 for ch in p))
def _split_text(p):
    """長い \\text{日本語} を含む式は、日本語を本文・式の部分だけ数式にして、折り返せるようにする"""
    toks=re.split(r'(\\text\{[^{}]*\})',p)
    out=""
    for t in toks:
        if t.startswith("\\text{"): out+=html.escape(t[6:-1],quote=False)
        else:
            m=re.sub(r'^(?:\\ |\s)+|(?:\\ |\s)+$','',t)
            if m: out+=" "+I(m)+" "
    return out.strip()
def M(p):
    if re.search(r'\\text\{[^{}]{8,}\}',p): return _split_text(p)
    return p if isM(p) else I(p)

def ex_block(i,e,sub,with_prac=True):
    pr="".join(f"<li>{M(p)}</li>" for p in e['practice'])
    return (lh(f"例題 {i}",f"{sub}　"+e['title'])+
     f'<div class="qbox"><p>{e["problem"]}</p></div>'
     f'<div class="bar"><h2>解き方（まず考え方）</h2>{e["approach"]}<div class="kotsu"><b>コツ</b>{e["kotsu"]}</div></div>'
     f'<div class="bar sol"><h2>解答</h2>{"".join(e["steps"])}</div>'
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
PCSS='@page{size:A4;margin:11mm}.figbox img.fig{max-height:44mm;width:auto!important;max-width:100%}body{margin:0;color:#222;font-family:"Noto Sans CJK JP",sans-serif}.lesson{font-size:12pt}.pg{page-break-after:always;width:188mm}.pg:last-child{page-break-after:auto}.step,.abox,.item,.qbox,.gbox,.lesson p,.lesson li,.katex-display,.katex,.figbox,.tbl,.kotsu{break-inside:avoid;page-break-inside:avoid}.lesson .katex{line-height:1.5}.lesson .sb p,.lesson .bar p,.lesson li{padding-top:1px}'
def pdf_html(pages):
    body="".join(f'<section class="pg"><div class="lesson">{p}</div></section>' for p in pages)
    return ('<!DOCTYPE html><html lang="ja"><head><meta charset="utf-8"><link rel="stylesheet" href="katex/katex.min.css"><link rel="stylesheet" href="lesson.css"><style>'+PCSS+'</style></head><body>'+body+
     '<script src="katex/katex.min.js"></script><script src="katex/auto-render.min.js"></script><script>renderMathInElement(document.body,{delimiters:[{left:"\\\\[",right:"\\\\]",display:true},{left:"\\\\(",right:"\\\\)",display:false}],throwOnError:false});'
     'document.querySelectorAll(".pg").forEach(function(pg){var L=pg.firstChild;var h=L.getBoundingClientRect().height;var z=1;if(h>1015){z=1015/h;if(z<0.72){z=Math.min(0.85,2000/h);}}var sw=L.scrollWidth,cw=L.clientWidth;if(sw>cw+1){z=Math.min(z,cw/sw*0.98);}pg.style.zoom=z;});</script></body></html>')
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
