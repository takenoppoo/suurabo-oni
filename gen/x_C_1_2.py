# -*- coding: utf-8 -*-
from bh import *
import numpy as np, math
Z=U_(); CH=[]; R=sp.Rational; x,y,z,t=sp.symbols("x y z t")
def vec(v): return r"\begin{pmatrix}%s\\%s\\%s\end{pmatrix}"%tuple(L(c) for c in v)
def pt(P): return "(%s,\\ %s,\\ %s)"%tuple(L(c) for c in P)
# 6 直線と平面の交点
def b6(P,d,n,c):
    # line P + t d ; plane n·X=c
    Pv=sp.Matrix(P); dv=sp.Matrix(d); nv=sp.Matrix(n)
    tv=sp.solve(nv.dot(Pv+t*dv)-c,t)[0]; X=Pv+tv*dv
    assert nv.dot(X)==c
    a=sp.symbols("a")
    p1="<p>直線上の点：</p>"+D(r"(x,y,z)=%s"%("(%s,\\ %s,\\ %s)"%tuple(L(P[i]+t*d[i]) for i in range(3))))
    p2="<p>平面 "+I("%s=%s"%(L(n[0]*x+n[1]*y+n[2]*z),L(c)))+" に代入：</p>"+D(r"%s=%s\ \Rightarrow\ t=%s"%(L(sp.expand(nv.dot(Pv+t*dv))),L(c),L(tv)))
    st=[("直線のパラメータ表示",p1),("平面に代入",p2),("交点","<p>"+D(r"%s"%pt(list(X))))]
    return r"点 $%s$ を通り、方向ベクトル $%s$ の直線と、平面 $%s=%s$ の交点の座標を求めよ。"%(pt(P),"(%s,\\ %s,\\ %s)"%tuple(d),L(n[0]*x+n[1]*y+n[2]*z),L(c)),st,r"%s"%pt(list(X))
o=[b6(*v) for v in [((1,2,3),(1,1,2),(1,2,-1),4),((0,1,2),(2,-1,1),(1,1,1),9),((3,0,1),(1,2,-1),(2,-1,1),5),((1,1,1),(1,-2,3),(3,1,-1),2),((2,-1,0),(1,2,2),(1,-2,2),7)]]
build(Z,CH,"直線と平面の交点",o,"<p>直線を $t$ のパラメータで表し、平面の式に代入して $t$ を決め、座標を戻す。</p>","直線を歩いて、平面に当たる歩数 t を探す。",6)
# 7 四面体の体積
def b7(A,B,C,Dp):
    Av=sp.Matrix(A);u=sp.Matrix(B)-Av;v=sp.Matrix(C)-Av;w=sp.Matrix(Dp)-Av
    cr=u.cross(v); S=sp.sqrt(cr.dot(cr))/2; vol=abs(cr.dot(w))/6
    h=abs(cr.dot(w))/sp.sqrt(cr.dot(cr))
    assert sp.simplify(S*h/3-vol)==0
    st=[("辺のベクトル","<p>"+D(r"\overrightarrow{AB}=%s,\quad \overrightarrow{AC}=%s,\quad \overrightarrow{AD}=%s"%(vec(list(u)),vec(list(v)),vec(list(w))))),
        ("外積","<p>"+D(r"\overrightarrow{AB}\times\overrightarrow{AC}=%s"%vec(list(cr)))),
        ("体積","<p>"+D(r"V=\dfrac16\left|(\overrightarrow{AB}\times\overrightarrow{AC})\cdot\overrightarrow{AD}\right|=\dfrac16\cdot%s=%s"%(L(abs(cr.dot(w))),L(vol))))]
    return r"4点 $A%s,\ B%s,\ C%s,\ D%s$ を頂点とする四面体 $ABCD$ の体積を求めよ。"%(pt(A),pt(B),pt(C),pt(Dp)),st,L(vol)
o=[b7(*v) for v in [((0,0,0),(2,0,0),(0,3,0),(1,1,4)),((1,0,0),(0,2,0),(0,0,3),(1,1,1)),((1,1,0),(3,1,1),(2,4,1),(0,0,5)),((0,0,0),(1,2,0),(3,1,0),(2,2,6)),((2,1,1),(4,2,0),(1,5,2),(3,3,5))]]
build(Z,CH,"四面体の体積（外積とスカラー三重積）",o,"<p>$V=\\dfrac16\\left|(\\overrightarrow{AB}\\times\\overrightarrow{AC})\\cdot\\overrightarrow{AD}\\right|$。外積で底面の面積ベクトルを作り、$\\overrightarrow{AD}$ との内積で高さをかける。</p>","底面の面積×高さ÷3 を、ベクトルで一気に計算。",7)
# 8 2点を直径の球
def b8(A,B):
    Av=sp.Matrix(A);Bv=sp.Matrix(B); M=(Av+Bv)/2; r2=sp.simplify((Bv-Av).dot(Bv-Av)/4)
    st=[("中心と半径","<p>"+I("AB")+" の中点が中心 "+I("M%s"%pt(list(M)))+"。</p>"+D(r"r^2=\left(\dfrac{AB}{2}\right)^2=%s"%L(r2))),
        ("球面の方程式",D(r"(x-%s)^2+(y-%s)^2+(z-%s)^2=%s"%(L(M[0]),L(M[1]),L(M[2]),L(r2)))),
        ("別解","<p>"+I(r"\overrightarrow{PA}\cdot\overrightarrow{PB}=0")+" を成分で書いても同じ式になる。</p>")]
    return r"2点 $A%s,\ B%s$ を直径の両端とする球面の方程式を求めよ。"%(pt(A),pt(B)),st,r"(x-%s)^2+(y-%s)^2+(z-%s)^2=%s"%(L(M[0]),L(M[1]),L(M[2]),L(r2))
o=[b8(*v) for v in [((1,2,3),(3,4,5)),((0,0,0),(2,4,4)),((1,-1,2),(5,3,0)),((2,0,1),(4,2,-3)),((-1,3,2),(3,1,0))]]
build(Z,CH,"2点を直径の両端とする球面",o,"<p>中心は<b>中点</b>、半径は $\\dfrac{AB}2$。または球面上の点 $P$ で $\\overrightarrow{PA}\\cdot\\overrightarrow{PB}=0$（直径に対する円周角が直角）。</p>","直径がわかれば、中点と半径が決まる。",8)
# 9 平面の方程式（3点）と原点との距離
def b9(A,B,C):
    Av=sp.Matrix(A);u=sp.Matrix(B)-Av;v=sp.Matrix(C)-Av; n=u.cross(v); g=sp.gcd(sp.gcd(int(n[0]),int(n[1])),int(n[2])); n=n/g
    c=n.dot(Av); dist=abs(c)/sp.sqrt(n.dot(n))
    assert n.dot(sp.Matrix(B))==c and n.dot(sp.Matrix(C))==c
    st=[("法線ベクトル","<p>"+D(r"\overrightarrow{AB}\times\overrightarrow{AC}=%s\ \parallel\ %s"%(vec(list(u.cross(v))),vec(list(n))))),
        ("平面の方程式","<p>"+D(r"%s=%s"%(L(n[0]*x+n[1]*y+n[2]*z),L(c)))),
        ("原点との距離","<p>"+D(r"\dfrac{|%s|}{\sqrt{%s}}=%s"%(L(c),L(n.dot(n)),L(dist))))]
    return r"3点 $A%s,\ B%s,\ C%s$ を通る平面の方程式と、原点からこの平面までの距離を求めよ。"%(pt(A),pt(B),pt(C)),st,r"%s=%s,\ \ \text{距離 }%s"%(L(n[0]*x+n[1]*y+n[2]*z),L(c),L(dist))
o=[b9(*v) for v in [((1,0,0),(0,2,0),(0,0,3)),((1,1,0),(0,1,2),(2,0,1)),((2,0,0),(0,3,0),(0,0,6)),((1,2,0),(3,0,1),(0,1,2)),((1,1,1),(2,3,1),(0,2,4))]]
build(Z,CH,"3点を通る平面と原点からの距離",o,"<p>法線ベクトル $=\\overrightarrow{AB}\\times\\overrightarrow{AC}$。点 $A$ を通ることから右辺を決める。距離は $\\dfrac{|d|}{|\\vec n|}$。</p>","面に垂直な向きが分かれば、面の式が決まる。",9)
# 10 球と直線
def b10(c,r,P,d):
    # sphere center c radius r ; line P+t d ; intersections
    cv=sp.Matrix(c);Pv=sp.Matrix(P);dv=sp.Matrix(d)
    eq=sp.expand((Pv+t*dv-cv).dot(Pv+t*dv-cv)-r*r); ts=sp.solve(eq,t)
    pts=[tuple(Pv+tt*dv) for tt in ts]; chord=sp.sqrt((sp.Matrix(pts[0])-sp.Matrix(pts[1])).dot(sp.Matrix(pts[0])-sp.Matrix(pts[1])))
    st=[("直線上の点","<p>"+D(r"(x,y,z)=(%s,\ %s,\ %s)"%tuple(L(P[i]+t*d[i]) for i in range(3)))),
        ("球面の式に代入","<p>"+D(r"%s=0\ \Rightarrow\ t=%s"%(L(eq),r",\ ".join(L(tt) for tt in ts)))),
        ("交点と弦の長さ","<p>"+D(r"%s,\quad %s"%(pt(pts[0]),pt(pts[1])))+D(r"\text{弦の長さ }%s"%L(chord)))]
    return r"球面 $(x-%d)^2+(y-%d)^2+(z-%d)^2=%d$ と、点 $%s$ を通り方向ベクトル $%s$ の直線との交点を求め、この直線が球面から切り取る弦の長さを求めよ。"%(c[0],c[1],c[2],r*r,pt(P),"(%s,\\ %s,\\ %s)"%tuple(d)),st,r"%s,\ %s,\ \text{弦 }%s"%(pt(pts[0]),pt(pts[1]),L(chord))
o=[b10(*v) for v in [((0,0,0),3,(0,0,1),(1,2,2)) if False else ((0,0,0),3,(0,0,-3),(1,2,2)),((1,0,0),3,(1,0,-3),(0,0,1)) if False else ((1,0,0),5,(1,0,0),(2,3,6)),((0,0,0),3,(0,0,0),(2,1,2)),((1,1,1),3,(1,1,1),(1,2,2)),((2,0,0),7,(2,0,0),(2,3,6))]]
build(Z,CH,"球面と直線の交点・弦の長さ",o,"<p>直線のパラメータ表示を球面の式に代入し、$t$ の2次方程式を解く。2解の差と方向ベクトルの長さの積が弦の長さ。</p>","直線を歩いて、球の表面をまたぐ2か所を探す。",10)
XU=finishx(Z,CH)
