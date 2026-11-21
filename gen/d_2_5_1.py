# -*- coding: utf-8 -*-
# 微分法（接線・増減・極値）（数学II 微分・積分）
from bh import *
Z=U_(); CH=[]
_cnt=[0]
def gplane(name,xr,yr,draw,size=(4.2,3.0),w=54,xs=1,ys=1):
    xr=tuple(float(v) for v in xr); yr=tuple(float(v) for v in yr); xs=float(xs); ys=float(ys)
    def fn(ax):
        sx_=xr[1]-xr[0]; sy_=yr[1]-yr[0]
        ax.set_xlim(*xr); ax.set_ylim(*yr); ax.axis("off")
        for v in np.arange(np.ceil(xr[0]/xs)*xs,xr[1]+1e-9,xs): ax.plot([v,v],list(yr),color="#e8e8e8",lw=.6,zorder=0)
        for v in np.arange(np.ceil(yr[0]/ys)*ys,yr[1]+1e-9,ys): ax.plot(list(xr),[v,v],color="#e8e8e8",lw=.6,zorder=0)
        ax.annotate("",xy=(xr[1],0),xytext=(xr[0],0),arrowprops=dict(arrowstyle="->",lw=1.1,color="#333"))
        ax.annotate("",xy=(0,yr[1]),xytext=(0,yr[0]),arrowprops=dict(arrowstyle="->",lw=1.1,color="#333"))
        ax.text(xr[1],-0.05*sy_,"x",fontsize=11,ha="right",va="top"); ax.text(0.02*sx_,yr[1],"y",fontsize=11,va="top")
        ax.text(-0.015*sx_,-0.04*sy_,"O",fontsize=10,ha="right",va="top")
        for v in np.arange(np.ceil(xr[0]/xs)*xs,xr[1]+1e-9,xs):
            if abs(v)>1e-9: ax.text(v,-0.03*sy_,("%g"%v),fontsize=8,ha="center",va="top",color="#555")
        for v in np.arange(np.ceil(yr[0]/ys)*ys,yr[1]+1e-9,ys):
            if abs(v)>1e-9: ax.text(-0.012*sx_,v,("%g"%v),fontsize=8,ha="right",va="center",color="#555")
        draw(ax)
    make_fig(name,fn,size=size); return img(name,w)
def curve(ax,f,xr,col="#b81f36"):
    fl=sp.lambdify(x,f,"numpy"); xs_=np.linspace(xr[0],xr[1],600); ax.plot(xs_,fl(xs_)*np.ones_like(xs_),color=col,lw=2)
def mark(ax,xx,yy,lab="",dx=.0,dy=.0,col="#222"):
    ax.plot([float(xx)],[float(yy)],"o",ms=5,color=col,zorder=5)
    if lab: ax.text(float(xx)+dx,float(yy)+dy,lab,fontsize=10,color=col,ha="center")
def tline(ax,m,y0,x0,xr,col="#1f6fb8"):
    xs_=np.array(xr,dtype=float); ax.plot(xs_,float(m)*(xs_-float(x0))+float(y0),color=col,lw=1.6,ls="--")
def poly(co): return sum(c*x**(len(co)-1-i) for i,c in enumerate(co))
def vtable(pts,crit,signs,vals,open_ends=False):
    seq=[]  # (kind,payload)
    if open_ends: seq.append(("g",signs[0])); sg=signs[1:]
    else: sg=signs
    for i,p_ in enumerate(pts):
        seq.append(("p",i))
        if i<len(pts)-1 or open_ends: seq.append(("g",sg[i]))
    rx=["<th>"+I("x")+"</th>"]; r1=["<th>"+I("f'(x)")+"</th>"]; r2=["<th>"+I("f(x)")+"</th>"]
    for k,pl in seq:
        if k=="g":
            rx.append("<td></td>"); r1.append("<td>"+I("+" if pl>0 else "-")+"</td>"); r2.append("<td>"+I(r"\nearrow" if pl>0 else r"\searrow")+"</td>")
        else:
            i=pl; rx.append("<td>"+I(L(pts[i]))+"</td>"); r1.append("<td>"+(I("0") if crit[i] else "")+"</td>")
            lab=""
            if crit[i] and 0<i<len(pts)-1 or (crit[i] and open_ends):
                before=[s for kk,s in [(a,b) for a,b in seq]][0]
                # 前後の符号
                j=[idx for idx,(kk,pp) in enumerate(seq) if kk=="p" and pp==i][0]
                sb=seq[j-1][1] if j>0 else None; sa=seq[j+1][1] if j+1<len(seq) else None
                if sb is not None and sa is not None: lab="<br><small>"+("極大" if (sb>0 and sa<0) else "極小" if (sb<0 and sa>0) else "")+"</small>"
            r2.append("<td>"+I(L(vals[i]))+lab+"</td>")
    return '<table class="tbl"><tr>'+"".join(rx)+"</tr><tr>"+"".join(r1)+"</tr><tr>"+"".join(r2)+"</tr></table>"
def sgn(v): return 1 if v>0 else -1
def xl(t): return L(x-t)
# ===== 例題1 接線 =====
def b1(co,t,xr,yr,ys):
    f=poly(co); fp=sp.diff(f,x); m=fp.subs(x,t); y0=f.subs(x,t); ln=sp.expand(m*(x-t)+y0); Y=sp.Symbol('y')
    assert ln.subs(x,t)==y0 and sp.diff(ln,x)==m
    _cnt[0]+=1; nm="i251_a%d"%_cnt[0]
    def dr(ax): curve(ax,f,xr); tline(ax,m,y0,t,xr); mark(ax,t,y0,"",0,0)
    fig=gplane(nm,xr,yr,dr,ys=ys)
    st=[("導関数を求める",D(r"f'(x)=%s"%L(fp))),
        ("接線の傾き（$x=%s$ での微分係数）"%L(t),D(r"f'(%s)=%s"%(L(t),L(m)))),
        ("接点の座標",D(r"f(%s)=%s"%(L(t),L(y0)))+"<p>接点は "+I(pt(t,y0))+"。</p>"),
        ("接線の方程式","<p>"+I(r"y-f(a)=f'(a)(x-a)")+" に代入する。</p>"+D(r"%s=%s\left(%s\right)\ \Rightarrow\ y=%s"%(L(Y-y0),L(m),L(x-t),L(ln)))+fig)]
    return r"曲線 $y=%s$ 上の点 $%s$ における接線の方程式を求めよ。"%(L(f),pt(t,y0)),st,r"y=%s"%L(ln)
V=[([1,0,-3,1],2,(-3,4),(-6,10),2),([-1,3,0,1],-1,(-3,4),(-6,10),2),([1,-2,0,3],2,(-2,4),(-3,12),3),([1,3,0,-1],1,(-4,3),(-4,12),4),([2,-3,0,1],2,(-1,3),(-4,10),2)]
o=[b1(*v) for v in V]
build(Z,CH,"曲線上の点での接線",o,
 r"<p>$y=f(x)$ 上の点 $(a,\ f(a))$ における接線は、傾きが $f'(a)$ で、$$y-f(a)=f'(a)(x-a)$$ 手順：①$f'(x)$ ②傾き $f'(a)$ ③接点 $f(a)$ ④公式に代入して整理。</p>",
 "微分係数は「その点での坂の傾き」。接線は、その点で曲線にぴったり寄り添う直線。",1)
# ===== 例題2 外点からの接線 =====
def b2(co,P,xr,yr,ys):
    f=poly(co); fp=sp.diff(f,x); t=sp.Symbol('t'); tg=sp.expand(fp.subs(x,t)*(x-t)+f.subs(x,t)); eq=sp.expand(tg.subs(x,P[0])-P[1])
    rt=sp.roots(sp.Poly(eq,t)); assert all(r.is_integer for r in rt) and len(rt)>=2
    rs=sorted(rt); lns=[sp.expand(tg.subs(t,r)) for r in rs]
    for ln_ in lns: assert ln_.subs(x,P[0])==P[1]
    _cnt[0]+=1; nm="i251_b%d"%_cnt[0]
    def dr(ax):
        curve(ax,f,xr)
        for r,ln_ in zip(rs,lns): tline(ax,sp.diff(ln_,x),f.subs(x,r),r,xr); mark(ax,r,f.subs(x,r))
        mark(ax,P[0],P[1],"P",.3,.5,"#1f6fb8")
    fig=gplane(nm,xr,yr,dr,ys=ys)
    on=(f.subs(x,P[0])==P[1])
    st=[("接点を $(t,\\ f(t))$ とおく","<p>"+I(r"f'(x)=%s"%L(fp))+" より、接点 "+I(r"\left(t,\ f(t)\right)")+" での接線は</p>"+D(r"y-%s=%s\left(x-t\right)"%(L(f.subs(x,t)),L(fp.subs(x,t))))+D(r"y=%s"%L(sp.collect(tg,x)))),
        ("点 $P$ を通る条件","<p>"+I(r"x=%s,\ y=%s"%(L(P[0]),L(P[1])))+" を代入する"+("（$P$ は曲線上の点でもあるが、$P$ を通る接線は接点が $P$ とは限らない）" if on else "")+"。</p>"+D(r"%s=%s"%(L(P[1]),L(sp.expand(tg.subs(x,P[0])))))+D(L(eq)+"=0")),
        ("$t$ を求める",D(L(sp.factor(eq))+r"=0\ \Rightarrow\ t=%s"%r",\ ".join(L(r) for r in rs))),
        ("接線の方程式",("<br>".join("<p>"+I(r"t=%s"%L(r))+" のとき "+I(r"y=%s"%L(ln_))+"</p>" for r,ln_ in zip(rs,lns)))+fig)]
    return r"点 $P%s$ から曲線 $y=%s$ にひいた接線の方程式をすべて求めよ。"%(pt(*P),L(f)),st,r",\ ".join(r"y=%s"%L(ln_) for ln_ in lns)
V=[([1,0,0],(1,-3),(-3,5),(-8,12),2),([1,-2,3],(2,-1),(-2,6),(-4,14),2),([-1,4,0],(2,8),(-2,6),(-8,12),4),([1,0,-3,0],(2,-6),(-3,4),(-12,10),4),([1,0,0,0],(-2,-8),(-3,3),(-12,12),4)]
o=[b2(*v) for v in V]
build(Z,CH,"曲線外の点を通る接線",o,
 r"<p>通る点が曲線上にあるとは限らない。そこで<b>接点を $(t,\ f(t))$ とおく</b>。接線 $y=f'(t)(x-t)+f(t)$ が点 $P$ を通る条件から $t$ の方程式を作って解く。$t$ の値の個数が接線の本数。</p>",
 "接点が分からないときは、まず接点に名前（$t$）をつけて、通る条件から探し出す。",2)
# ===== 例題3 増減表と極値 =====
def b3(co,xr,yr,ys):
    f=poly(co); fp=sp.diff(f,x); cs=sorted(sp.solve(fp,x)); assert len(cs)==2 and all(c.is_integer for c in cs)
    sg=[sgn(fp.subs(x,cs[0]-1)),sgn(fp.subs(x,(cs[0]+cs[1])/2)),sgn(fp.subs(x,cs[1]+1))]; vals=[f.subs(x,c) for c in cs]
    _cnt[0]+=1; nm="i251_c%d"%_cnt[0]
    def dr(ax):
        curve(ax,f,xr)
        for c,v in zip(cs,vals): mark(ax,c,v)
    fig=gplane(nm,xr,yr,dr,ys=ys)
    mx=[(c,v) for c,v,s in zip(cs,vals,[sg[0],sg[1]]) if s>0][0]; mn=[(c,v) for c,v,s in zip(cs,vals,[sg[0],sg[1]]) if s<0][0]
    st=[("導関数を求める",D(r"f'(x)=%s=%s"%(L(fp),L(sp.factor(fp))))),
        ("$f'(x)=0$ を解く",D(r"f'(x)=0\ \Rightarrow\ x=%s,\ %s"%(L(cs[0]),L(cs[1])))),
        ("増減表をかく","<p>$f'(x)$ の符号は、各区間の値を代入して調べる。</p>"+vtable(cs,[True,True],sg,vals,open_ends=True)),
        ("極値を答える","<p>極大値 "+I(L(mx[1]))+"（"+I("x=%s"%L(mx[0]))+"）、極小値 "+I(L(mn[1]))+"（"+I("x=%s"%L(mn[0]))+"）。グラフは次のようになる。</p>"+fig)]
    return r"関数 $f(x)=%s$ の増減を調べ、極値を求めよ。また、グラフの概形をかけ。"%L(f),st,r"\text{極大値 }%s\ (x=%s),\quad \text{極小値 }%s\ (x=%s)"%(L(mx[1]),L(mx[0]),L(mn[1]),L(mn[0]))
V=[([1,-3,-9,5],(-3,5),(-26,14),10),([1,-6,9,-1],(-1,4.5),(-6,10),2),([-1,3,9,2],(-3,5),(-8,34),10),([2,-9,12,1],(-0.5,3.5),(-2,12),2),([1,0,-12,3],(-4,4),(-16,24),5)]
o=[b3(*v) for v in V]
build(Z,CH,"3次関数の増減と極値",o,
 r"<p>$f'(x)>0$ の区間で $f(x)$ は増加、$f'(x)<0$ の区間で減少。$f'(x)=0$ を解き、<b>増減表</b>をかく。$f'$ の符号が $+\to-$ と変わる点で<b>極大</b>、$-\to+$ で<b>極小</b>。極値は $f(x)$ に代入して求める。</p>",
 "山を登りきって下りに変わる点が極大、谷底から上りに変わる点が極小。変わり目は $f'(x)=0$。",3)
# ===== 例題4 係数決定 =====
def b4(p_,q_,M):
    a,b,c=sp.symbols('a b c'); f=x**3+a*x**2+b*x+c; fp=sp.diff(f,x)
    s=sp.solve([fp.subs(x,p_),fp.subs(x,q_)],[a,b]); av,bv=s[a],s[b]; cv=sp.solve((f.subs({a:av,b:bv})).subs(x,p_)-M,c)[0]
    F=f.subs({a:av,b:bv,c:cv}); fpx=sp.diff(F,x); assert sp.expand(fpx-3*(x-p_)*(x-q_))==0
    mn=F.subs(x,q_); assert sp.expand(F.subs(x,p_))==M
    st=[("極値の条件を式にする","<p>"+I(r"f'(x)=3x^2+2ax+b")+"。"+I("x=%s"%L(p_))+"、"+I("x=%s"%L(q_))+" で極値をとるから "+I("f'(%s)=0"%L(p_))+"、"+I("f'(%s)=0"%L(q_))+"。</p>"+D(r"\begin{cases}%s\\ %s\end{cases}"%(L(fp.subs(x,p_))+"=0",L(fp.subs(x,q_))+"=0"))),
        ("$a,\\ b$ を求める",D(r"a=%s,\quad b=%s"%(L(av),L(bv)))),
        ("$c$ を求める","<p>"+I(r"x=%s"%L(p_))+" で極大値 "+I(str(M))+" だから "+I(r"f(%s)=%s"%(L(p_),M))+"。</p>"+D(r"%s=%s\ \Rightarrow\ c=%s"%(L(sp.expand(F.subs(x,p_)-cv+c)),M,L(cv)))),
        ("逆に確かめる（増減表）","<p>"+I(r"f(x)=%s"%L(F))+"、"+I(r"f'(x)=%s"%L(sp.factor(fpx)))+"。</p>"+vtable([p_,q_],[True,True],[1,-1,1],[F.subs(x,p_),F.subs(x,q_)],open_ends=True)+"<p>$x=%s$ で極大、$x=%s$ で極小になり、条件に合う。極小値は "%(L(p_),L(q_))+I(L(mn))+"。</p>")]
    return r"3次関数 $f(x)=x^3+ax^2+bx+c$ が $x=%s$ で極大値 $%d$、$x=%s$ で極小値をとる。定数 $a,\ b,\ c$ の値と、極小値を求めよ。"%(L(p_),M,L(q_)),st,r"a=%s,\ b=%s,\ c=%s,\ \text{極小値 }%s"%(L(av),L(bv),L(cv),L(mn))
V=[(-1,3,10),(1,3,3),(-3,1,30),(-2,2,20),(-1,5,12)]
o=[b4(*v) for v in V]
build(Z,CH,"極値の条件から係数を決める",o,
 r"<p>$x=a$ で極値をとるなら $f'(a)=0$（<b>必要条件</b>）。ただし $f'(a)=0$ だけでは極値とは限らないので、<b>増減表で $f'$ の符号が変わることを確かめる</b>（十分性の確認）。</p>",
 "$f'(a)=0$ は「頂上の候補」。本当に頂上か（符号が変わるか）は、最後に増減表で確かめる。",4)
# ===== 例題5 閉区間の最大・最小 =====
def b5(co,al,be,xr,yr,ys):
    f=poly(co); fp=sp.diff(f,x); cs=[c for c in sorted(sp.solve(fp,x)) if al<c<be]
    pts=[sp.Integer(al)]+cs+[sp.Integer(be)]; crit=[False]+[True]*len(cs)+[False]; vals=[f.subs(x,p_) for p_ in pts]
    sg=[sgn(fp.subs(x,(pts[i]+pts[i+1])/2)) for i in range(len(pts)-1)]
    M=max(vals); m=min(vals); xM=[p_ for p_,v in zip(pts,vals) if v==M]; xm=[p_ for p_,v in zip(pts,vals) if v==m]
    for xx in np.linspace(al,be,4001): assert float(f.subs(x,xx))<=float(M)+1e-9 and float(f.subs(x,xx))>=float(m)-1e-9
    _cnt[0]+=1; nm="i251_e%d"%_cnt[0]
    def dr(ax):
        curve(ax,f,(al,be))
        for p_,v in zip(pts,vals): mark(ax,p_,v)
    fig=gplane(nm,xr,yr,dr,ys=ys)
    xs_=lambda L_: ",\\ ".join(L(z) for z in L_)
    st=[("導関数と極値の候補",D(r"f'(x)=%s=%s"%(L(fp),L(sp.factor(fp))))+"<p>"+I(r"f'(x)=0\ \Rightarrow\ x=%s"%",\\ ".join(L(c) for c in sorted(sp.solve(fp,x))))+"。このうち "+I(r"%d\leqq x\leqq %d"%(al,be))+" に入るのは "+I(r"x=%s"%",\\ ".join(L(c) for c in cs))+"。</p>"),
        ("増減表をかく（両端も入れる）",vtable(pts,crit,sg,vals)),
        ("最大値・最小値","<p>極値の候補と<b>両端の値</b>を比べる。</p>"+D(r",\ ".join(r"f(%s)=%s"%(L(p_),L(v)) for p_,v in zip(pts,vals)))+"<p>最大値 "+I(L(M))+"（"+I("x=%s"%xs_(xM))+"）、最小値 "+I(L(m))+"（"+I("x=%s"%xs_(xm))+"）。</p>"+fig)]
    return r"関数 $f(x)=%s\ (%d\leqq x\leqq %d)$ の最大値と最小値、およびそのときの $x$ の値を求めよ。"%(L(f),al,be),st,r"\text{最大値 }%s\ (x=%s),\quad \text{最小値 }%s\ (x=%s)"%(L(M),xs_(xM),L(m),xs_(xm))
V=[([1,-3,-9,5],-2,4,(-3,5),(-26,14),10),([1,-6,9,-1],0,5,(-1,6),(-4,22),5),([-1,3,9,2],-2,2,(-3,3),(-6,28),10),([2,-9,12,1],0,3,(-0.5,3.5),(-2,12),2),([1,0,-12,3],-3,3,(-4,4),(-16,24),5)]
o=[b5(*v) for v in V]
build(Z,CH,"閉区間での最大・最小",o,
 r"<p>閉区間 $[\alpha,\beta]$ での最大・最小は、<b>極値の候補（区間内のもの）と両端の値</b>を比べる。端が最大・最小になることも多い。増減表に両端を入れておくと見落とさない。</p>",
 "山の頂上だけでなく、散歩道の端（両端）も候補。いちばん高い所・低い所を、全部の候補で比べる。",5)
UNIT=finish(Z,CH,4,0,"微分・積分","微分法（接線・増減・極値）","接線、外点からの接線、増減表と極値、係数決定、閉区間の最大・最小まで、微分法の総合力を問う難問に挑みます。")
