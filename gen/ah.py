# -*- coding: utf-8 -*-
# 数学A 用の記述ヘルパー：$...$ でインライン数式、$$...$$ で別行数式
import re, math
from tools import *
def T(s):
    s=re.sub(r'\$\$(.+?)\$\$',lambda m:D(m.group(1)),s,flags=re.S)
    return re.sub(r'\$(.+?)\$',lambda m:I(m.group(1)),s)
class U_:
    def __init__(s): s.E=[]; s.C=[]
    def ex(s,title,problem,approach,kotsu,steps,answer,practice,pans,fig=""):
        s.E.append(dict(title=title,problem=T(problem)+fig,approach=T(approach),kotsu=T(kotsu),
          steps=[step(i,T(t),T(b)) for i,(t,b) in enumerate(steps,1)],answer=answer,
          practice=[T(p) for p in practice],pans=[(T(b),a) for b,a in pans]))
    def ch(s,problem,body,ans,k): s.C.append((T(problem),T(body),ans,k))
    def unit(s,ci,ui,chapter,name,intro,subject="A"):
        assert len(s.E)==5 and len(s.C)==5,(len(s.E),len(s.C))
        return dict(subject=subject,ci=ci,ui=ui,chapter=chapter,name=name,intro=intro,examples=s.E,chapter_end=s.C)
def close(a,b,e=1e-9): assert abs(a-b)<e,(a,b)
def geo(name,circles=(),segs=(),pts=(),polys=(),texts=(),w=44,size=(3.6,3.2),lim=None):
    """circles:(cx,cy,r,col,ls) segs:(x1,y1,x2,y2,col,ls) pts:(label,x,y,dx,dy[,dot]) polys:([(x,y)..],col)"""
    def fn(ax):
        for cx,cy,r,col,ls in circles:
            th=np.linspace(0,2*np.pi,400); ax.plot(cx+r*np.cos(th),cy+r*np.sin(th),color=col,lw=1.6,ls=ls)
        for pl,col in polys:
            q=list(pl)+[pl[0]]; ax.plot([p[0] for p in q],[p[1] for p in q],color=col,lw=1.8)
        for x1,y1,x2,y2,col,ls in segs: ax.plot([x1,x2],[y1,y2],color=col,lw=1.6,ls=ls)
        for p in pts:
            lab,x,y,dx,dy=p[:5]; dot=p[5] if len(p)>5 else True
            if dot: ax.plot([x],[y],"o",ms=3.5,color="#333")
            ax.text(x+dx,y+dy,lab,fontsize=12,ha="center",va="center")
        for x,y,t,col in texts: ax.text(x,y,t,fontsize=11,color=col,ha="center")
        ax.set_aspect("equal"); ax.axis("off")
        if lim: ax.set_xlim(lim[0],lim[1]); ax.set_ylim(lim[2],lim[3])
    make_fig(name,fn,size=size); return img(name,w)
import numpy as np
