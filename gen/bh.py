# -*- coding: utf-8 -*-
# 数学II 用ヘルパー（sympyで式を作り、答えを自動で検算する）
from ah import *
import sympy as sp
from sympy import Rational as R, sqrt, pi, Poly
x,y,t,a,b,c,k,m,n,p,q,r=sp.symbols('x y t a b c k m n p q r')
def L(e):
    s=sp.latex(e,order='lex',mul_symbol=None)
    return s.replace(r'\frac',r'\dfrac')
def P(e): return "\\left("+L(e)+"\\right)"
def ldsteps(A,B):
    out=[];cur=sp.expand(A)
    while cur!=0 and sp.degree(cur,x)>=sp.degree(B,x):
        d=sp.degree(cur,x)-sp.degree(B,x)
        qt=sp.Poly(cur,x).LC()/sp.Poly(B,x).LC()*x**d
        sub=sp.expand(qt*B); new=sp.expand(cur-sub)
        out.append((qt,sub,new,cur)); cur=new
    return out,cur
def divtext(A,B):
    """筆算の手順（HTML）と (商,余り) を返す"""
    st,rem=ldsteps(A,B); Q=sum(s[0] for s in st)
    qq,rr=sp.div(sp.expand(A),sp.expand(B),x); assert sp.expand(qq-Q)==0 and sp.expand(rr-rem)==0
    h=""
    for qt,sub,new,cur in st:
        h+="<p>"+I(L(sp.LT(cur,x))+r"\div"+P(sp.LT(B,x))+"="+L(qt))+" を商に立てる。</p>"+D(L(cur)+"-"+P(qt)+P(B)+"="+L(new))
    return h,Q,rem
def flat(steps): return "".join("<p><b>"+T(t)+"</b></p>"+T(b) if not b.startswith("<") else "<p><b>"+T(t)+"</b></p>"+b for t,b in steps)
def fr(num,den): return r"\dfrac{"+(num if isinstance(num,str) else L(num))+"}{"+(den if isinstance(den,str) else L(den))+"}"
def sgn_terms(terms):
    """terms=[(coef or sympy num, denTeX/expr)]  → '2/(..)+3/(..)-…'"""
    s=""
    for i,(nu,de) in enumerate(terms):
        nu=sp.nsimplify(nu); neg=nu<0; an=abs(nu)
        body=fr(an,de)
        s+=("-" if neg else ("+" if i else ""))+body
    return s
def lin(r_): return x-r_      # (x - r)
def prod_(rs): 
    e=1
    for r_ in rs: e*=(x-r_)
    return e
def facs(rs): return "".join("("+L(x-r_)+")" for r_ in rs)
def mk(steps_fn):
    return steps_fn
def Cn(n_,r_): return r"{}_{%d}\mathrm{C}_{%d}"%(n_,r_)
def build(Z,CH,title,o,approach,kotsu,k):
    """o=[(prob,steps,ans)×5]  先頭を例題、1〜3を練習、4を章末に使う"""
    Z.ex(title,o[0][0],approach,kotsu,o[0][1],o[0][2],[z[0] for z in o[1:4]],[(flat(z[1]),z[2]) for z in o[1:4]])
    CH.append((o[4][0],flat(o[4][1]),o[4][2],k))
def finish(Z,CH,ci,ui,chapter,name,intro,subject="2"):
    for p_,b_,a_,k_ in CH: Z.ch(p_,b_,a_,k_)
    return Z.unit(ci,ui,chapter,name,intro,subject=subject)
def cx(re,im):
    re=sp.nsimplify(re); im=sp.nsimplify(im); s=""
    if re!=0: s+=L(re)
    if im!=0:
        t="i" if im==1 else ("-i" if im==-1 else L(im)+"i")
        if s and not t.startswith("-"): s+="+"
        s+=t
    return s or "0"
def sx(terms):
    """[(係数, '記号')...] → '3+2i-6i^2' のようなLaTeX"""
    s=""
    for c_,m_ in terms:
        c_=sp.nsimplify(c_)
        if c_==0: continue
        body=(L(abs(c_)) if (abs(c_)!=1 or m_=="") else "")+m_
        s+=("-" if c_<0 else ("+" if s else ""))+body
    return s or "0"
def synth(cs,r_):
    out=[cs[0]]
    for c_ in cs[1:]: out.append(c_+out[-1]*r_)
    return out[:-1],out[-1]
def synth_tex(cs,r_):
    q_,rem=synth(cs,r_); n_=len(cs)
    top=r" & ".join(str(c_) for c_ in cs)
    mid=r" & ".join([""]+[str(q_[i]*r_) if i<len(q_) else str(rem-cs[-1]) for i in range(n_-1)])
    bot=r" & ".join([str(v) for v in q_+[rem]])
    return r"\begin{array}{r|"+"r"*n_+r"}"+str(r_)+" & "+top+r"\\ & "+mid+r"\\ \hline & "+bot+r"\end{array}",q_,rem
def polyc(cs):
    n_=len(cs)-1; return sum(c_*x**(n_-i) for i,c_ in enumerate(cs))
import numpy as np
from math import gcd
from functools import reduce
def plane(name,xr,yr,draw,size=(3.8,3.4),w=48,grid=True,step=1):
    def fn(ax):
        ax.set_xlim(*xr); ax.set_ylim(*yr); ax.set_aspect("equal"); ax.axis("off")
        if grid:
            for v in range(int(np.ceil(xr[0])),int(np.floor(xr[1]))+1): ax.plot([v,v],list(yr),color="#e4e4e4",lw=.6,zorder=0)
            for v in range(int(np.ceil(yr[0])),int(np.floor(yr[1]))+1): ax.plot(list(xr),[v,v],color="#e4e4e4",lw=.6,zorder=0)
        ax.annotate("",xy=(xr[1],0),xytext=(xr[0],0),arrowprops=dict(arrowstyle="->",lw=1.1,color="#333"))
        ax.annotate("",xy=(0,yr[1]),xytext=(0,yr[0]),arrowprops=dict(arrowstyle="->",lw=1.1,color="#333"))
        ax.text(xr[1],-0.18,"x",fontsize=11,ha="right",va="top"); ax.text(0.12,yr[1],"y",fontsize=11,va="top")
        ax.text(-0.12,-0.12,"O",fontsize=10,ha="right",va="top")
        for v in range(int(np.ceil(xr[0])),int(np.floor(xr[1]))+1):
            if v!=0 and v%step==0: ax.plot([v,v],[-.07,.07],color="#333",lw=.8); ax.text(v,-0.16,str(v),fontsize=8,ha="center",va="top",color="#555")
        for v in range(int(np.ceil(yr[0])),int(np.floor(yr[1]))+1):
            if v!=0 and v%step==0: ax.plot([-.07,.07],[v,v],color="#333",lw=.8); ax.text(-0.14,v,str(v),fontsize=8,ha="right",va="center",color="#555")
        draw(ax)
    make_fig(name,fn,size=size); return img(name,w)
def dline(ax,p_,q_,r_,xr,yr,col="#b81f36",ls="-",lw=1.8):
    if q_==0:
        xv=-r_/p_; ax.plot([xv,xv],list(yr),color=col,ls=ls,lw=lw)
    else:
        ys=[(-r_-p_*xx)/q_ for xx in xr]; ax.plot(list(xr),ys,color=col,ls=ls,lw=lw)
    ax.set_xlim(*xr); ax.set_ylim(*yr)
def dpt(ax,xx,yy,lab="",dx=.25,dy=.25,col="#222",ms=4.5):
    ax.plot([xx],[yy],"o",ms=ms,color=col,zorder=5)
    if lab: ax.text(xx+dx,yy+dy,lab,fontsize=11,ha="center",va="center",color=col)
def lineeq(p_,q_,r_):
    p_,q_,r_=[sp.nsimplify(v) for v in (p_,q_,r_)]
    den=reduce(lambda a,b:a*b//gcd(a,b),[sp.Rational(v).q for v in (p_,q_,r_)])
    ii=[int(v*den) for v in (p_,q_,r_)]; g=reduce(gcd,[abs(v) for v in ii]) or 1; ii=[v//g for v in ii]
    first=next(v for v in ii if v!=0)
    if first<0: ii=[-v for v in ii]
    return ii
def leq(p_,q_,r_):
    a,b,c=lineeq(p_,q_,r_); return poly([(a,"x"),(b,"y"),(c,"")])+"=0"
def lthru(P1,P2):
    (x1,y1),(x2,y2)=P1,P2; return lineeq(y2-y1,-(x2-x1),(x2-x1)*y1-(y2-y1)*x1)
def pt(a_,b_): return "("+L(sp.nsimplify(a_))+",\\ "+L(sp.nsimplify(b_))+")"
def dcirc(ax,cx,cy,r_,col="#333",ls="-",lw=1.8):
    th=np.linspace(0,2*np.pi,400); ax.plot(cx+r_*np.cos(th),cy+r_*np.sin(th),color=col,ls=ls,lw=lw)
def circtex(a_,b_,r2):
    return "(x%+d)^2+(y%+d)^2=%s"%(-a_,-b_,L(r2)) if True else ""
def PI(r_): 
    r_=sp.nsimplify(r_)
    if r_==0: return "0"
    return L(r_*sp.pi)
def trigfig(name,f,xr,yr,xt,yt,hl=(),pts=(),w=62,size=(5.4,2.5),hlines=()):
    def fn(ax):
        ax.set_xlim(*xr); ax.set_ylim(*yr); ax.axis("off")
        for yy,col in hlines: ax.plot([xr[0],xr[1]],[yy,yy],color=col,lw=1,ls="--")
        ax.annotate("",xy=(xr[1],0),xytext=(xr[0],0),arrowprops=dict(arrowstyle="->",lw=1.1,color="#333"))
        ax.annotate("",xy=(0,yr[1]),xytext=(0,yr[0]),arrowprops=dict(arrowstyle="->",lw=1.1,color="#333"))
        for t_,l_ in xt:
            ax.plot([t_,t_],[-.05*(yr[1]-yr[0]),.05*(yr[1]-yr[0])],color="#333",lw=.9)
            ax.text(t_,-.09*(yr[1]-yr[0]),l_,fontsize=12,ha="center",va="top",color="#333")
        for t_,l_ in yt:
            ax.plot([-.012*(xr[1]-xr[0]),.012*(xr[1]-xr[0])],[t_,t_],color="#333",lw=.9); ax.text(-.02*(xr[1]-xr[0]),t_,l_,fontsize=11,ha="right",va="center",color="#333")
        xs_=np.linspace(xr[0]+.001,xr[1]-.001,800); ax.plot(xs_,[f(v) for v in xs_],color="#b81f36",lw=2)
        for h1,h2,hc in hl: ax.plot([h1,h2],[0,0],color=hc,lw=5,solid_capstyle="butt",zorder=4)
        for px,py,lab,dx,dy in pts:
            ax.plot([px],[py],"o",ms=4.5,color="#222",zorder=5)
            if lab: ax.text(px+dx,py+dy,lab,fontsize=9,ha="center",va="center")
        ax.text(xr[1],-.09*(yr[1]-yr[0]),"θ",fontsize=11,ha="right",va="top"); ax.text(.02*(xr[1]-xr[0]),yr[1],"y",fontsize=11,va="top")
    make_fig(name,fn,size=size); return img(name,w)
def pil(n_,d_=1):
    """π の分数ラベル（mathtext）"""
    r_=sp.Rational(n_,d_)
    if r_==0: return "0"
    num=r_.p; den=r_.q
    s=("-" if num<0 else "")
    num=abs(num)
    top=(r"\pi" if num==1 else r"%d\pi"%num)
    return "$"+s+(top if den==1 else r"\frac{%s}{%d}"%(top,den))+"$"

def cf(c_):
    c_=sp.nsimplify(c_); return "" if c_==1 else ("-" if c_==-1 else L(c_))
def fac(r_,v="t"):
    r_=sp.nsimplify(r_)
    if r_==0: return v
    return "(%s-%s)"%(v,L(r_)) if r_>0 else "(%s+%s)"%(v,L(-r_))

import re as _re
def clean(s):
    if isinstance(s,str):
        s=s.replace("--","+")
        s=_re.sub(r"\+\s*-","-",s)
        s=_re.sub(r"(?<![0-9A-Za-z\\.{^_])1(?=[xyab]\b|[xyab]\^|[xyab][xyab\\(])","",s)
        s=_re.sub(r"\+0(?![0-9.])","",s)
        return s
    if isinstance(s,list): return [clean(t) for t in s]
    if isinstance(s,tuple): return tuple(clean(t) for t in s)
    if isinstance(s,dict): return {k:clean(v) for k,v in s.items()}
    return s
def finishx(Z,CH):
    """追加分（例題6〜10・章末6〜10）"""
    assert len(Z.E)==5 and len(CH)==5
    return clean(dict(examples=Z.E,chapter_end=[(T(p_),T(b_),a_,k_) for p_,b_,a_,k_ in CH]))
