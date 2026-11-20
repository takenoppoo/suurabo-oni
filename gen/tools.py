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

def venn2(name,a_only,both,b_only,outside,A="A",B="B",w=52,U=None):
    def fn(ax):
        from matplotlib.patches import Circle,Rectangle
        ax.set_xlim(-3.2,3.2); ax.set_ylim(-2.2,2.4); ax.set_aspect("equal"); ax.axis("off")
        ax.add_patch(Rectangle((-3.1,-2.1),6.2,4.2,fill=False,ec="#555",lw=1.4))
        ax.add_patch(Circle((-0.8,0),1.35,fc=RED,alpha=.14,ec=RED,lw=2))
        ax.add_patch(Circle((0.8,0),1.35,fc="#3a6ea5",alpha=.14,ec="#3a6ea5",lw=2))
        ax.text(-1.45,1.55,A,fontsize=15,color=RED,ha="center"); ax.text(1.45,1.55,B,fontsize=15,color="#3a6ea5",ha="center")
        ax.text(-1.55,0,a_only,ha="center",va="center",fontsize=14); ax.text(0,0,both,ha="center",va="center",fontsize=14)
        ax.text(1.55,0,b_only,ha="center",va="center",fontsize=14); ax.text(2.45,-1.65,outside,ha="center",va="center",fontsize=14)
        if U: ax.text(-2.95,1.85,U,fontsize=12,ha="left",va="center")
    make_fig(name,fn,size=(4.4,3.1))
    return img(name,w)

def graph(name,curves,xr,yr,pts=(),xticks=(),yticks=(),vlines=(),texts=(),w=56,size=(4.2,3.4),grid=False):
    """curves=[(func,color,ls,label?)]  pts=[(x,y,label,dx,dy)]"""
    import numpy as np
    def fn(ax):
        ax.set_xlim(*xr); ax.set_ylim(*yr); ax.set_aspect("auto"); ax.axis("off")
        ax.annotate("",xy=(xr[1],0),xytext=(xr[0],0),arrowprops=dict(arrowstyle="->",lw=1.2,color="#333"))
        ax.annotate("",xy=(0,yr[1]),xytext=(0,yr[0]),arrowprops=dict(arrowstyle="->",lw=1.2,color="#333"))
        ax.text(xr[1],-0.04*(yr[1]-yr[0]),"x",fontsize=12,ha="right",va="top"); ax.text(0.03*(xr[1]-xr[0]),yr[1],"y",fontsize=12,va="top")
        ax.text(-0.03*(xr[1]-xr[0]),-0.04*(yr[1]-yr[0]),"O",fontsize=11,ha="right",va="top")
        for t,l in xticks:
            ax.plot([t,t],[-.015*(yr[1]-yr[0]),.015*(yr[1]-yr[0])],color="#333",lw=1); ax.text(t,-0.05*(yr[1]-yr[0]),l,ha="center",va="top",fontsize=11)
        for t,l in yticks:
            ax.plot([-.015*(xr[1]-xr[0]),.015*(xr[1]-xr[0])],[t,t],color="#333",lw=1); ax.text(-0.025*(xr[1]-xr[0]),t,l,ha="right",va="center",fontsize=11)
        for xv,col in vlines: ax.plot([xv,xv],[yr[0],yr[1]],color=col,lw=1,ls="--")
        for c in curves:
            f,col,ls=c[0],c[1],c[2]
            xs=np.linspace(xr[0],xr[1],400); ys=np.array([f(v) for v in xs],dtype=float)
            m=(ys>=yr[0])&(ys<=yr[1]); ys=np.where(m,ys,np.nan)
            ax.plot(xs,ys,color=col,lw=2,ls=ls)
        for p in pts:
            x0,y0,lab=p[0],p[1],p[2]; dx=p[3] if len(p)>3 else 0.1*(xr[1]-xr[0]); dy=p[4] if len(p)>4 else 0
            ax.plot([x0],[y0],"o",ms=5,color=RED); ax.text(x0+dx,y0+dy,lab,fontsize=11,color=RED,ha="left",va="center")
        for x0,y0,t,col in texts: ax.text(x0,y0,t,fontsize=11,color=col)
    make_fig(name,fn,size=size)
    return img(name,w)

def semicircle(name,vals,mode="cos",w=50,size=(4.2,2.6),note=None):
    """半円（単位円の上半分）。mode='cos': x=値の縦線, 'sin': y=値の横線。vals=[(値,ラベル)]"""
    import numpy as np
    def fn(ax):
        th=np.linspace(0,np.pi,300); ax.plot(np.cos(th),np.sin(th),color="#333",lw=1.6)
        ax.set_xlim(-1.5,1.5); ax.set_ylim(-0.3,1.3); ax.set_aspect("equal"); ax.axis("off")
        ax.annotate("",xy=(1.4,0),xytext=(-1.4,0),arrowprops=dict(arrowstyle="->",lw=1.1,color="#333"))
        ax.annotate("",xy=(0,1.25),xytext=(0,-0.05),arrowprops=dict(arrowstyle="->",lw=1.1,color="#333"))
        ax.text(0,-0.12,"O",fontsize=10,ha="right",va="top"); ax.text(1.0,-0.1,"1",fontsize=10,ha="center",va="top"); ax.text(-1.0,-0.1,"-1",fontsize=10,ha="center",va="top")
        for v,lab in vals:
            if mode=="cos":
                s=float(np.sqrt(max(0,1-v*v))); ax.plot([v,v],[0,s],color=RED,lw=1.6,ls="--"); ax.plot([v],[s],"o",color=RED,ms=6); ax.text(v,-0.1,lab,fontsize=11,color=RED,ha="center",va="top"); ax.plot([0,v],[0,s],color=RED,lw=1)
            else:
                c=float(np.sqrt(max(0,1-v*v))); 
                for cc in (c,-c): ax.plot([0,cc],[v,v],color=RED,lw=1.6,ls="--"); ax.plot([cc],[v],"o",color=RED,ms=6)
                ax.text(-0.04,v,lab,fontsize=11,color=RED,ha="right",va="center")
        if note: ax.text(0,1.28,note,fontsize=10,ha="center")
    make_fig(name,fn,size=size)
    return img(name,w)

def tri(name,P,vertex_labels,sides=None,angles=None,extra=None,w=44,size=(3.8,3.0)):
    """P=[(x,y)...] 頂点, vertex_labels=['A','B','C'], sides={(i,j):'text'}, angles={i:'text'}"""
    import numpy as np
    def fn(ax):
        ax.set_aspect("equal"); ax.axis("off")
        xs=[p[0] for p in P]; ys=[p[1] for p in P]
        ax.set_xlim(min(xs)-0.9,max(xs)+0.9); ax.set_ylim(min(ys)-0.8,max(ys)+0.8)
        n=len(P)
        for i in range(n):
            a,b=P[i],P[(i+1)%n]; ax.plot([a[0],b[0]],[a[1],b[1]],color="#333",lw=1.8)
        cx=sum(xs)/n; cy=sum(ys)/n
        for i,l in enumerate(vertex_labels):
            vx,vy=P[i][0]-cx,P[i][1]-cy; r=(vx*vx+vy*vy)**.5 or 1
            ax.text(P[i][0]+0.32*vx/r,P[i][1]+0.32*vy/r,l,fontsize=14,ha="center",va="center")
        for (i,j),t in (sides or {}).items():
            mx,my=(P[i][0]+P[j][0])/2,(P[i][1]+P[j][1])/2; vx,vy=mx-cx,my-cy; r=(vx*vx+vy*vy)**.5 or 1
            ax.text(mx+0.3*vx/r,my+0.3*vy/r,t,fontsize=12,color=RED,ha="center",va="center")
        for i,t in (angles or {}).items():
            vx,vy=cx-P[i][0],cy-P[i][1]; r=(vx*vx+vy*vy)**.5 or 1
            ax.text(P[i][0]+0.55*vx/r,P[i][1]+0.55*vy/r,t,fontsize=11,color="#3a6ea5",ha="center",va="center")
        if extra: extra(ax)
    make_fig(name,fn,size=size)
    return img(name,w)

def boxfig(name,mn,q1,q2,q3,mx,outliers=(),lo=None,hi=None,w=66,size=(6.0,1.7),labels=True):
    def fn(ax):
        lo_=mn-2 if lo is None else lo; hi_=(max([mx]+list(outliers)))+2 if hi is None else hi
        ax.set_xlim(lo_,hi_); ax.set_ylim(-1.2,1.6); ax.axis("off")
        ax.annotate("",xy=(hi_,-0.55),xytext=(lo_,-0.55),arrowprops=dict(arrowstyle="->",lw=1.1,color="#333"))
        ax.plot([mn,q1],[0.5,0.5],color="#333",lw=1.8); ax.plot([q3,mx],[0.5,0.5],color="#333",lw=1.8)
        ax.plot([mn,mn],[0.25,0.75],color="#333",lw=1.8); ax.plot([mx,mx],[0.25,0.75],color="#333",lw=1.8)
        from matplotlib.patches import Rectangle
        ax.add_patch(Rectangle((q1,0.15),q3-q1,0.7,fc="#FDF0F2",ec=RED,lw=2)); ax.plot([q2,q2],[0.15,0.85],color=RED,lw=2.4)
        for o in outliers: ax.plot([o],[0.5],"x",color="#333",ms=8,mew=2)
        if labels:
            for v,t in ((mn,"最小"),(q1,"Q1"),(q2,"Q2"),(q3,"Q3"),(mx,"最大")): ax.text(v,1.15,t,ha="center",fontsize=10,color=RED)
            for v in (mn,q1,q2,q3,mx): ax.text(v,-0.8,("%g"%v),ha="center",fontsize=10,va="top")
    make_fig(name,fn,size=size); return img(name,w)

def scatter(name,xs,ys,w=40,size=(3.4,3.0)):
    def fn(ax):
        ax.set_xlim(min(xs)-1,max(xs)+1); ax.set_ylim(min(ys)-1,max(ys)+1); ax.axis("off")
        x0,y0=min(xs)-0.6,min(ys)-0.6
        ax.annotate("",xy=(max(xs)+1,y0),xytext=(x0,y0),arrowprops=dict(arrowstyle="->",lw=1.1,color="#333"))
        ax.annotate("",xy=(x0,max(ys)+1),xytext=(x0,y0),arrowprops=dict(arrowstyle="->",lw=1.1,color="#333"))
        ax.plot(xs,ys,"o",color=RED,ms=7); ax.text(max(xs)+1,y0-0.1,"x",fontsize=11,va="top",ha="right"); ax.text(x0+0.1,max(ys)+1,"y",fontsize=11,va="top")
    make_fig(name,fn,size=size); return img(name,w)
