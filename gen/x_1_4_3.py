# -*- coding: utf-8 -*-
from bh import *
import math
Z=U_(); CH=[]
R=sp.Rational; s=sp.sqrt
# 6 立方体の垂線
def b6(a):
    S=s(3)/2*a**2; V=R(1,6)*a**3; h=sp.simplify(3*V/S); assert abs(float(h)-a/math.sqrt(3))<1e-9
    st=[("三角すい $A\\text{-}BDE$ の体積","<p>立方体の1辺を "+I(str(a))+"。"+I("\\triangle ABD")+" は直角二等辺三角形、高さ "+I("AE=%d"%a)+"。</p>"+D(r"V=\dfrac13\cdot\dfrac12\cdot%d\cdot%d\cdot%d=%s"%(a,a,a,L(V)))),
        ("$\\triangle BDE$ の面積","<p>"+I(r"BD=DE=EB=%s"%L(a*s(2)))+"（面の対角線）の正三角形。</p>"+D(r"S=\dfrac{\sqrt3}{4}\cdot(%s)^2=%s"%(L(a*s(2)),L(S)))),
        ("垂線の長さ","<p>"+I("A")+" から平面 "+I("BDE")+" への距離を "+I("h")+" とする。底面を "+I("\\triangle BDE")+" とみると "+I(r"V=\dfrac13Sh")+"。</p>"+D(r"h=\dfrac{3V}{S}=\dfrac{%s}{%s}=%s"%(L(3*V),L(S),L(h))))]
    return r"1辺の長さが $%d$ の立方体 $ABCD\text{-}EFGH$ で、頂点 $A$ から平面 $BDE$ に下ろした垂線の長さを求めよ。"%a,st,L(h)
o=[b6(a) for a in [3,6,4,9,12]]
build(Z,CH,"立方体の頂点から平面への距離（体積で求める）",o,r"<p>三角すいの<b>体積を2通りに表す</b>（底面をかえる）。$V=\dfrac13Sh$ から $h=\dfrac{3V}S$。直角の頂点を頂点にとると体積が簡単に出る。</p>","底面を取りかえれば、同じ体積から高さが出る。",6)
# 7 円錐の最短経路
def b7(l,r_):
    th=2*math.pi*r_/l; assert th<math.pi
    d=2*l*math.sin(th/2); 
    ang=sp.Rational(360*r_,l)
    chord=sp.simplify(2*l*sp.sin(sp.pi*r_/l))
    assert abs(float(chord)-d)<1e-9
    st=[("展開図の中心角","<p>側面の展開図はおうぎ形。弧の長さ "+I(r"2\pi\cdot%d"%r_)+"、半径 "+I(str(l))+"。</p>"+D(r"\theta=\dfrac{2\pi\cdot%d}{%d}=%s^\circ"%(r_,l,L(ang)))),
        ("最短経路","<p>母線上の点 "+I("A")+" から1周して "+I("A")+" にもどる最短経路は、展開図上で <b>"+I("A")+" と "+I("A'")+" を結ぶ線分</b>。</p>"),
        ("余弦定理（または二等辺三角形）","<p>"+I(r"\angle AOA'=%s^\circ"%L(ang))+"、"+I("OA=OA'=%d"%l)+"。</p>"+D(r"AA'=2\cdot%d\sin\dfrac{%s^\circ}{2}=%s"%(l,L(ang),L(chord))))]
    return r"底面の半径 $%d$、母線の長さ $%d$ の円錐がある。母線の端 $A$ から側面を1周して $A$ にもどる最短の長さを求めよ。"%(r_,l),st,L(chord)
o=[b7(*v) for v in [(12,4),(12,2),(10,5) if False else (18,3),(12,1),(8,2)]]
build(Z,CH,"円錐の側面を1周する最短経路",o,r"<p>側面を<b>展開図（おうぎ形）</b>にして、最短は2点を結ぶ線分。中心角 $\theta=\dfrac{2\pi r}{l}$ を求め、二等辺三角形として弦の長さを出す。</p>","曲がった面は、広げて平らにすれば直線が最短。",7)
# 8 直角の三角すい
def b8(a,b,c):
    Sq=a*a*b*b+b*b*c*c+c*c*a*a; S=R(1,2)*s(Sq); V=R(a*b*c,6); h=sp.simplify(3*V/S); assert abs(float(h)-a*b*c/math.sqrt(Sq))<1e-9
    st=[("体積","<p>"+I(r"OA=%d,\ OB=%d,\ OC=%d"%(a,b,c))+"（互いに垂直）。"+I(r"\triangle OAB")+" を底面、"+I("OC")+" を高さとして</p>"+D(r"V=\dfrac13\cdot\dfrac12\cdot%d\cdot%d\cdot%d=%s"%(a,b,c,L(V)))),
        ("$\\triangle ABC$ の面積","<p>3辺 "+I(r"AB=\sqrt{%d},\ BC=\sqrt{%d},\ CA=\sqrt{%d}"%(a*a+b*b,b*b+c*c,c*c+a*a))+"。余弦定理で "+I(r"\cos A")+" を求め、面積を計算すると</p>"+D(r"S=\dfrac12\sqrt{%d\cdot%d+%d\cdot%d+%d\cdot%d}=%s"%(a*a,b*b,b*b,c*c,c*c,a*a,L(S)))),
        ("垂線の長さ",D(r"h=\dfrac{3V}{S}=%s"%L(h)))]
    return r"四面体 $OABC$ で、$OA=%d,\ OB=%d,\ OC=%d$ かつ $OA,\ OB,\ OC$ は互いに垂直である。$O$ から平面 $ABC$ に下ろした垂線の長さを求めよ。"%(a,b,c),st,L(h)
o=[b8(*v) for v in [(2,3,6),(3,4,12),(1,2,2),(2,3,4),(6,3,2)]]
build(Z,CH,"互いに垂直な3辺をもつ四面体の高さ",o,r"<p>$OA,OB,OC$ が互いに垂直なら、体積は $\dfrac16abc$。底面 $\triangle ABC$ の面積を3辺から出し、<b>$V=\dfrac13Sh$</b> で $h$ を求める。</p>","同じ立体を2つの見方で数えて、等しいとおく。",8)
# 9 正八面体
def b9(a):
    V=R(1,3)*a**2*(a/s(2)); V=sp.simplify(2*V); r_=sp.simplify(3*V/(8*(s(3)/4*a**2))); assert abs(float(r_)-a*math.sqrt(6)/6)<1e-9
    st=[("正四角すい2つに分ける","<p>正八面体は、底面が1辺 "+I(str(a))+" の正方形の正四角すい2個。高さは対角線の半分。</p>"+D(r"h=\dfrac{%s}{2}=%s"%(L(a*s(2)),L(a*s(2)/2)))),
        ("体積",D(r"V=2\times\dfrac13\cdot%d^2\cdot%s=%s"%(a,L(a*s(2)/2),L(V)))),
        ("内接球の半径","<p>表面積は正三角形8個。内接球の中心から各面までの距離が "+I("r")+"。</p>"+D(r"V=\dfrac13\cdot S_{\text{表}}\cdot r,\quad S_{\text{表}}=8\cdot\dfrac{\sqrt3}{4}%d^2=%s"%(a,L(8*s(3)/4*a**2)))+D(r"r=\dfrac{3V}{S_{\text{表}}}=%s"%L(r_)))]
    return r"1辺の長さが $%d$ の正八面体の体積と、内接球の半径を求めよ。"%a,st,r"V=%s,\ \ r=%s"%(L(V),L(r_))
o=[b9(a) for a in [2,4,6,3,12]]
build(Z,CH,"正八面体の体積と内接球",o,r"<p>正八面体は<b>正四角すい2個</b>。高さは正方形の対角線の半分。内接球の半径は、体積を<b>表面積を使って</b> $V=\dfrac13Sr$ で求める。</p>","複雑な立体は、知っている立体に切り分ける。",9)
# 10 直方体の外接球
def b10(a,b,c):
    R2=R(a*a+b*b+c*c,4); r_=sp.sqrt(R2); Vs=R(4,3)*sp.pi*r_**3
    st=[("球の直径","<p>直方体の8つの頂点を通る球の直径は、<b>空間対角線</b>。</p>"+D(r"\sqrt{%d^2+%d^2+%d^2}=\sqrt{%d}"%(a,b,c,a*a+b*b+c*c))),
        ("半径",D(r"R=\dfrac12\sqrt{%d}=%s"%(a*a+b*b+c*c,L(r_)))),
        ("体積",D(r"V=\dfrac43\pi R^3=%s"%L(sp.simplify(Vs))))]
    return r"縦・横・高さが $%d,\ %d,\ %d$ の直方体の8つの頂点をすべて通る球の半径と体積を求めよ。"%(a,b,c),st,r"R=%s,\ V=%s"%(L(r_),L(sp.simplify(Vs)))
o=[b10(*v) for v in [(2,3,6),(1,2,2),(4,4,2),(2,6,9),(3,4,12)]]
build(Z,CH,"直方体の外接球",o,r"<p>外接球の中心は直方体の中心。<b>直径＝空間対角線</b> $\sqrt{a^2+b^2+c^2}$。半径を出して体積 $\dfrac43\pi R^3$。</p>","球は、いちばん遠い頂点同士の対角線がちょうど直径。",10)
XU=finishx(Z,CH)
