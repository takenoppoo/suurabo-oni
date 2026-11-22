# -*- coding: utf-8 -*-
from bh import *
import numpy as np, math
Z=U_(); CH=[]; R=sp.Rational; x,y,z,t=sp.symbols("x y z t")
def vec(v): return r"\begin{pmatrix}%s\\%s\\%s\end{pmatrix}"%tuple(L(c) for c in v)
import hashlib as _h
def hn(*a): return _h.md5(repr(a).encode()).hexdigest()[:8]
def pp(c): return L(c) if c>=0 else "(%s)"%L(c)
def SQ(var,v): return var+"^2" if v==0 else "(%s%s%s)^2"%(var,"-" if v>0 else "+",L(abs(v)))
def term(c,e): return ("" if c==1 else "-" if c==-1 else pp(c))+r"\left(%s\right)"%e
def patch(H,n,s=1.6):
    n_=sp.Matrix(n); u=n_.cross(sp.Matrix([0,0,1])) if (n[0] or n[1]) else n_.cross(sp.Matrix([1,0,0])); u=u/sp.sqrt(u.dot(u)); v=n_.cross(u); v=v/sp.sqrt(v.dot(v))
    Hm=sp.Matrix(H); return [tuple(Hm+s*(i*u+j*v)) for i,j in [(-1,-1),(1,-1),(1,1),(-1,1)]]
def pt(P): return "(%s,\\ %s,\\ %s)"%tuple(L(c) for c in P)
# 6 直線と平面の交点
def b6(P,d,n,c):
    # line P + t d ; plane n·X=c
    Pv=sp.Matrix(P); dv=sp.Matrix(d); nv=sp.Matrix(n)
    tv=sp.solve(nv.dot(Pv+t*dv)-c,t)[0]; X=Pv+tv*dv
    assert nv.dot(X)==c
    a=sp.symbols("a")
    p1="<p>直線上の点：</p>"+D(r"(x,y,z)=%s"%("(%s,\\ %s,\\ %s)"%tuple(L(P[i]+t*d[i]) for i in range(3))))
    p2="<p>平面 "+I("%s=%s"%(L(n[0]*x+n[1]*y+n[2]*z),L(c)))+" の "+I("x,y,z")+" に直線上の点を代入：</p>"+D(r"%s=%s"%("+".join(term(n[i],L(P[i]+t*d[i])) for i in range(3)),L(c)))+"<p>展開して "+I("t")+" の1次方程式にする。</p>"+D(r"%s=%s"%(L(sp.expand(nv.dot(Pv+t*dv))),L(c)))+D(r"t=%s"%L(tv))
    fig6=sp3("c12_6_"+hn(P,d,n,c),polys=[(patch(list(X),n),"#1f6fb8")],pts=[(P,"P",None),(tuple(X),"X",None)],segs=[(tuple(Pv-dv),tuple(X+dv),"-","#b81f36")],vecs=[(tuple(Pv),tuple(Pv+dv),r"\vec d","#2a8a4a")])
    st=[("直線のパラメータ表示",p1),("平面に代入",p2),("交点","<p>"+I("t=%s"%L(tv))+" を "+I("(x,y,z)")+" に戻す。</p>"+D(r"(x,y,z)=(%s,\ %s,\ %s)=%s"%(tuple(L(P[i]+t*d[i]) for i in range(3))+(pt(list(X)),)))+"<p>図：直線（赤）が平面（青）と1点で交わる。</p>"+fig6)]
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
        ("外積","<p>"+I(r"\vec u\times\vec v=(u_2v_3-u_3v_2,\ u_3v_1-u_1v_3,\ u_1v_2-u_2v_1)")+"。</p>"+D(r"\overrightarrow{AB}\times\overrightarrow{AC}=\left(%s\cdot%s-%s\cdot%s,\ %s\cdot%s-%s\cdot%s,\ %s\cdot%s-%s\cdot%s\right)"%(pp(u[1]),pp(v[2]),pp(u[2]),pp(v[1]),pp(u[2]),pp(v[0]),pp(u[0]),pp(v[2]),pp(u[0]),pp(v[1]),pp(u[1]),pp(v[0])))+D(r"=%s"%vec(list(cr)))),
        ("体積","<p>図：四面体 "+I("ABCD")+"（底面 "+I("ABC")+"、頂点 "+I("D")+"）。</p>"+sp3("c12_7_"+hn(A,B,C,Dp),polys=[([A,B,C],"#1f6fb8")],pts=[(A,"A",None),(B,"B",None),(C,"C",None),(Dp,"D",None)],segs=[(Dp,A,"--","#333"),(Dp,B,"-","#333"),(Dp,C,"-","#333")])+D(r"(\overrightarrow{AB}\times\overrightarrow{AC})\cdot\overrightarrow{AD}=%s\cdot%s+%s\cdot%s+%s\cdot%s=%s"%(pp(cr[0]),pp(w[0]),pp(cr[1]),pp(w[1]),pp(cr[2]),pp(w[2]),L(cr.dot(w))))+D(r"V=\dfrac16\left|%s\right|=%s"%(L(cr.dot(w)),L(vol))))]
    return r"4点 $A%s,\ B%s,\ C%s,\ D%s$ を頂点とする四面体 $ABCD$ の体積を求めよ。"%(pt(A),pt(B),pt(C),pt(Dp)),st,L(vol)
o=[b7(*v) for v in [((0,0,0),(2,0,0),(0,3,0),(1,1,4)),((1,0,0),(0,2,0),(0,0,3),(1,1,1)),((1,1,0),(3,1,1),(2,4,1),(0,0,5)),((0,0,0),(1,2,0),(3,1,0),(2,2,6)),((2,1,1),(4,2,0),(1,5,2),(3,3,5))]]
build(Z,CH,"四面体の体積（外積とスカラー三重積）",o,"<p>$V=\\dfrac16\\left|(\\overrightarrow{AB}\\times\\overrightarrow{AC})\\cdot\\overrightarrow{AD}\\right|$。外積で底面の面積ベクトルを作り、$\\overrightarrow{AD}$ との内積で高さをかける。</p>","底面の面積×高さ÷3 を、ベクトルで一気に計算。",7)
# 8 2点を直径の球
def b8(A,B):
    Av=sp.Matrix(A);Bv=sp.Matrix(B); M=(Av+Bv)/2; r2=sp.simplify((Bv-Av).dot(Bv-Av)/4)
    st=[("中心と半径","<p>"+I("AB")+" の中点が中心。</p>"+D(r"M=\left(\dfrac{%s+%s}{2},\ \dfrac{%s+%s}{2},\ \dfrac{%s+%s}{2}\right)=%s"%(pp(A[0]),pp(B[0]),pp(A[1]),pp(B[1]),pp(A[2]),pp(B[2]),pt(list(M))))+D(r"AB^2=%s^2+%s^2+%s^2=%s"%(pp(B[0]-A[0]),pp(B[1]-A[1]),pp(B[2]-A[2]),L(4*r2)))+D(r"r^2=\left(\dfrac{AB}{2}\right)^2=\dfrac{%s}{4}=%s"%(L(4*r2),L(r2)))+sp3("c12_8_"+hn(A,B),spheres=[(tuple(M),sp.sqrt(r2))],pts=[(A,"A",None),(B,"B",None),(tuple(M),"M",None)],segs=[(A,B,"-","#333")])),
        ("球面の方程式","<p>中心 "+I("M")+"、半径 "+I("r")+" の球面 "+I("(x-a)^2+(y-b)^2+(z-c)^2=r^2")+" に代入する。</p>"+D(r"%s+%s+%s=%s"%(SQ("x",M[0]),SQ("y",M[1]),SQ("z",M[2]),L(r2)))),
        ("別解","<p>"+I(r"\overrightarrow{PA}\cdot\overrightarrow{PB}=0")+" を成分で書いても同じ式になる。</p>")]
    return r"2点 $A%s,\ B%s$ を直径の両端とする球面の方程式を求めよ。"%(pt(A),pt(B)),st,r"%s+%s+%s=%s"%(SQ("x",M[0]),SQ("y",M[1]),SQ("z",M[2]),L(r2))
o=[b8(*v) for v in [((1,2,3),(3,4,5)),((0,0,0),(2,4,4)),((1,-1,2),(5,3,0)),((2,0,1),(4,2,-3)),((-1,3,2),(3,1,0))]]
build(Z,CH,"2点を直径の両端とする球面",o,"<p>中心は<b>中点</b>、半径は $\\dfrac{AB}2$。または球面上の点 $P$ で $\\overrightarrow{PA}\\cdot\\overrightarrow{PB}=0$（直径に対する円周角が直角）。</p>","直径がわかれば、中点と半径が決まる。",8)
# 9 平面の方程式（3点）と原点との距離
def b9(A,B,C):
    Av=sp.Matrix(A);u=sp.Matrix(B)-Av;v=sp.Matrix(C)-Av; n=u.cross(v); g=sp.gcd(sp.gcd(int(n[0]),int(n[1])),int(n[2])); n=n/g
    c=n.dot(Av); dist=abs(c)/sp.sqrt(n.dot(n))
    assert n.dot(sp.Matrix(B))==c and n.dot(sp.Matrix(C))==c
    cr_=u.cross(v)
    Hn=sp.Matrix([0,0,0])+n*c/n.dot(n); fig9=sp3("c12_9_"+hn(A,B,C),polys=[([A,B,C],"#1f6fb8")],pts=[(A,"A",None),(B,"B",None),(C,"C",None),(tuple(Hn),"H",None)],segs=[((0,0,0),tuple(Hn),"-","#b81f36")],vecs=[(tuple(Hn),tuple(Hn+n/sp.sqrt(n.dot(n))*1.2),r"\vec n","#2a8a4a")])
    st=[("法線ベクトル","<p>"+D(r"\overrightarrow{AB}=%s,\quad \overrightarrow{AC}=%s"%(vec(list(u)),vec(list(v))))+D(r"\overrightarrow{AB}\times\overrightarrow{AC}=\left(%s\cdot%s-%s\cdot%s,\ %s\cdot%s-%s\cdot%s,\ %s\cdot%s-%s\cdot%s\right)=%s"%(pp(u[1]),pp(v[2]),pp(u[2]),pp(v[1]),pp(u[2]),pp(v[0]),pp(u[0]),pp(v[2]),pp(u[0]),pp(v[1]),pp(u[1]),pp(v[0]),vec(list(cr_))))+("<p>各成分を "+I(str(g))+" でわって、向きが同じ短いベクトルにする。</p>" if g!=1 else "")+D(r"\vec n=%s"%vec(list(n)))),
        ("平面の方程式","<p>"+I(r"\vec n=(a,b,c)")+" のとき平面は "+I("ax+by+cz=d")+"。点 "+I("A%s"%pt(A))+" を通るので "+I("d")+" を決める。</p>"+D(r"d=%s\cdot%s+%s\cdot%s+%s\cdot%s=%s"%(pp(n[0]),pp(A[0]),pp(n[1]),pp(A[1]),pp(n[2]),pp(A[2]),L(c)))+D(r"%s=%s"%(L(n[0]*x+n[1]*y+n[2]*z),L(c)))),
        ("原点との距離","<p>"+I(r"\dfrac{|a x_0+b y_0+c z_0-d|}{\sqrt{a^2+b^2+c^2}}")+" に "+I(r"(x_0,y_0,z_0)=(0,0,0)")+" を代入する。</p>"+D(r"\dfrac{|%s\cdot0+%s\cdot0+%s\cdot0-%s|}{\sqrt{%s^2+%s^2+%s^2}}=\dfrac{%s}{\sqrt{%s}}%s"%(pp(n[0]),pp(n[1]),pp(n[2]),pp(c),pp(n[0]),pp(n[1]),pp(n[2]),L(abs(c)),L(n.dot(n)),("" if L(dist)==r"\dfrac{%s}{\sqrt{%s}}"%(L(abs(c)),L(n.dot(n))) else "="+L(dist))))+"<p>図：原点 "+I("O")+" から平面に下ろした垂線の足 "+I("H")+" までの長さが距離。</p>"+fig9)]
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
        ("球面の式に代入","<p>"+I("(x-a)^2+(y-b)^2+(z-c)^2=r^2")+" の "+I("x,y,z")+" を "+I("t")+" の式にする。</p>"+D(r"%s+%s+%s=%d"%(SQ("(%s)"%L(P[0]+t*d[0]),c[0]).replace("(("+L(P[0]+t*d[0])+")","(").replace("^2^2","^2") if False else r"\left(%s\right)^2"%L(P[0]+t*d[0]-c[0]),r"\left(%s\right)^2"%L(P[1]+t*d[1]-c[1]),r"\left(%s\right)^2"%L(P[2]+t*d[2]-c[2]),r*r))+"<p>展開して整理する。</p>"+D(r"%s=0"%L(eq))+D(r"%s=0\ \Rightarrow\ t=%s"%(L(sp.factor(eq)),r",\ ".join(L(tt) for tt in ts)))),
        ("交点と弦の長さ","<p>各 "+I("t")+" の値を "+I("(x,y,z)")+" に戻す。</p>"+D(r"t=%s:\ %s,\qquad t=%s:\ %s"%(L(ts[0]),pt(pts[0]),L(ts[1]),pt(pts[1])))+"<p>図：直線と球面の2つの交点。弦の長さは2点間の距離。</p>"+sp3("c12_10_"+hn(c,r,P,d),spheres=[(tuple(cv),r)],pts=[(tuple(pts[0]),"S",None),(tuple(pts[1]),"T",None)],segs=[(tuple(Pv+(min(ts)-sp.Rational(1,2))*dv),tuple(Pv+(max(ts)+sp.Rational(1,2))*dv),"-","#b81f36")])+D(r"ST=|t_1-t_2|\,|\vec d|=%s\times%s=%s"%(L(abs(ts[0]-ts[1])),L(sp.sqrt(dv.dot(dv))),L(chord))))]
    return r"球面 $%s+%s+%s=%d$ と、点 $%s$ を通り方向ベクトル $%s$ の直線との交点を求め、この直線が球面から切り取る弦の長さを求めよ。"%(SQ("x",c[0]),SQ("y",c[1]),SQ("z",c[2]),r*r,pt(P),"(%s,\\ %s,\\ %s)"%tuple(d)),st,r"%s,\ %s,\ \text{弦 }%s"%(pt(pts[0]),pt(pts[1]),L(chord))
o=[b10(*v) for v in [((0,0,0),3,(0,0,1),(1,2,2)) if False else ((0,0,0),3,(0,0,-3),(1,2,2)),((1,0,0),3,(1,0,-3),(0,0,1)) if False else ((1,0,0),5,(1,0,0),(2,3,6)),((0,0,0),3,(0,0,0),(2,1,2)),((1,1,1),3,(1,1,1),(1,2,2)),((2,0,0),7,(2,0,0),(2,3,6))]]
build(Z,CH,"球面と直線の交点・弦の長さ",o,"<p>直線のパラメータ表示を球面の式に代入し、$t$ の2次方程式を解く。2解の差と方向ベクトルの長さの積が弦の長さ。</p>","直線を歩いて、球の表面をまたぐ2か所を探す。",10)
XU=finishx(Z,CH)
