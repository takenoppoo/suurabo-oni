# -*- coding: utf-8 -*-
"""2次関数などのグラフを手早く描く共通部品（数学I 2次関数の追加例題用）"""
import numpy as np, sympy as sp
from d_2_5_1 import gplane,curve,mark
x=sp.Symbol('x')
def _step(span):
    for s in (1,2,5,10,20):
        if span/s<=10: return s
    return 50
def quadfig(name,fs,pts=(),axis=None,xr=None,yr=None,w=52,hl=(),size=(4.2,3.0)):
    """fs=[(式,色)]、pts=[(x,y,ラベル)]、axis=対称軸のx（破線）、hl=[(a,b)] はx軸上の太線（不等式の解）"""
    pts=list(pts)
    xs_=[float(p[0]) for p in pts]+([float(axis)] if axis is not None else [])
    if xr is None:
        lo=min(xs_)-2 if xs_ else -4; hi=max(xs_)+2 if xs_ else 5
        xr=(np.floor(lo),np.ceil(hi))
    X=np.linspace(xr[0],xr[1],400)
    ys=[0.0]+[float(p[1]) for p in pts]
    for f,_ in fs: ys+=list(np.clip(sp.lambdify(x,f,"numpy")(X)*np.ones_like(X),-1e3,1e3))
    if yr is None:
        lo,hi=min(ys),max(ys); pad=(hi-lo)*.12+.5
        yr=(np.floor(max(lo-pad,-60)),np.ceil(min(hi+pad,60)))
    xs=_step(xr[1]-xr[0]); yst=_step(yr[1]-yr[0])
    def draw(ax):
        if axis is not None: ax.plot([float(axis)]*2,[yr[0],yr[1]],color="#1f6fb8",lw=1.2,ls="--")
        for a,b in hl: ax.plot([float(a),float(b)],[0,0],color="#1f6fb8",lw=5,solid_capstyle="butt",zorder=4)
        for f,col in fs: curve(ax,f,xr,col)
        for px,py,lab in pts: mark(ax,px,py,lab,0,((yr[1]-yr[0])*.05 if float(py)>=0 else -(yr[1]-yr[0])*.10))
    return gplane(name,xr,yr,draw,size=size,w=w,xs=xs,ys=yst)
def vtx(a,b,c): return (sp.Rational(-b,2*a), sp.Rational(4*a*c-b*b,4*a))
def pt(px,py): return "(%s, %s)"%(sp.latex(px).replace("\\frac","").replace("{","").replace("}","") if False else px,py)
