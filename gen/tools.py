# -*- coding: utf-8 -*-
from lib import *
import sympy as sp
def sg(c,first=False):
    if first: return "-" if c<0 else ""
    return "-" if c<0 else "+"
def term(c,m,first=False):
    """係数c・単項式m(文字列。定数項は'')のLaTeX項"""
    if c==0: return ""
    a=abs(c)
    body=(str(a) if (a!=1 or m=="") else "")+m
    return sg(c,first)+body
def poly(terms):
    out="";first=True
    for c,m in terms:
        t=term(c,m,first)
        if t: out+=t; first=False
    return out or "0"
def lin(b,v,c): return poly([(b,v),(c,"")])
def plus(s): return s if s.startswith('-') else '+'+s
def par(s): return "("+s+")"
def mulc(c,s):  # 係数cとかっこの式
    return (("" if c==1 else ("-" if c==-1 else str(c))))+par(s)

def tasuki_fig(name,l1,l2,r1,r2,c1,c2,tot):
    def fn(ax):
        ax.set_xlim(0,10); ax.set_ylim(0,6.2); ax.axis("off")
        for (x,y,t) in ((1.6,4.8,l1),(1.6,1.6,l2),(5.2,4.8,r1),(5.2,1.6,r2)):
            ax.text(x,y,"$"+t+"$",ha="center",va="center",fontsize=17)
        ax.plot([2.3,4.4],[4.5,1.9],color=RED,lw=1.8); ax.plot([2.3,4.4],[1.9,4.5],color=RED,lw=1.8)
        ax.text(7.0,4.8,"$"+c2+"$",ha="left",va="center",fontsize=14,color="#333")
        ax.text(7.0,1.6,"$"+c1+"$",ha="left",va="center",fontsize=14,color="#333")
        ax.plot([6.9,9.9],[3.2,3.2],color="#555",lw=1)
        ax.text(7.0,2.7,"合計 $"+tot+"$",ha="left",va="center",fontsize=14,color=RED)
    make_fig(name,fn,size=(5.2,2.5))

def quad2(a,b,c,d,e,f,figname,prob=None):
    """ax²+…（2文字2次式）＝(ax+by+c)(dx+ey+f) の たすき掛けの解説を作る。戻り値(問題式,STEP html list,答案)"""
    X2=a*d; XY=a*e+b*d; Y2=b*e; X1=a*f+c*d; Y1=b*f+c*e; K=c*f
    P=poly([(X2,"x^2"),(XY,"xy"),(Y2,"y^2"),(X1,"x"),(Y1,"y"),(K,"")])
    A=lin(b,"y",c); B=lin(e,"y",f)
    xc=poly([(XY,"y"),(X1,"")]); kc=poly([(Y2,"y^2"),(Y1,"y"),(K,"")])
    st=[]
    st.append(step(1,r"\(x\) について降べきの順に整理する",
      "<p>"+I("y")+" を数と同じように扱い、"+I("x^2")+"、"+I("x")+"、"+I("x")+" を含まない項に分ける。</p>"+
      D(P+"="+poly([(X2,"x^2")])+"+"+par(xc)+"x+"+par(kc)).replace("+(","+(")))
    exp=f"{par(A)}{par(B)}"
    st.append(step(2,"定数項（\\(x\\) を含まない部分）を因数分解する",
      D(kc+"="+par(A)+par(B))+
      "<p>確かめ：</p>"+D(exp+"="+poly([(b*e,"y^2"),(b*f,"y"),(c*e,"y"),(c*f,"")])+"="+kc)))
    st.append(step(3,"たすき掛けをする（図）",
      img(figname,48)+
      "<p>左の列は "+I(f"{a},\\ {d}")+"、右の列は "+I(f"{A},\\ {B}")+"。たすきにかけて足すと、</p>"+
      D(f"{a}\\cdot{par(B)}+{d}\\cdot{par(A)}="+poly([(a*e,"y"),(a*f,"")])+plus(poly([(d*b,"y"),(d*c,"")]))+"="+xc)+
      "<p>これは "+I("x")+" の係数と一致するので、たすき掛けは成功。</p>"))
    ans=f"({poly([(a,'x')])}{'+' if True else ''}{A})".replace("+-","-")
    f1=poly([(a,"x"),(b,"y"),(c,"")]); f2=poly([(d,"x"),(e,"y"),(f,"")])
    st.append(step(4,"かっこにまとめる",D(P+"="+par(f1)+par(f2))))
    return P,st,par(f1)+par(f2)
def quad2_fig(a,b,c,d,e,f,name):
    A=lin(b,"y",c); B=lin(e,"y",f)
    c1=f"{a}\\times{par(B)}={poly([(a*e,'y'),(a*f,'')])}"
    c2=f"{d}\\times{par(A)}={poly([(d*b,'y'),(d*c,'')])}"
    tasuki_fig(name,str(a),str(d),A,B,c1,c2,poly([(a*e+b*d,'y'),(a*f+c*d,'')]))

def nl(name,lo,hi,ticks,labels=None,segs=(),pts=(),w=70,size=(6.2,1.5),extra=None,pad=0.8):
    def fn(ax):
        numline(ax,lo,hi,ticks,labels,segs,pts,pad=pad)
        if extra: extra(ax)
    make_fig(name,fn,size=size)
    return img(name,w)
