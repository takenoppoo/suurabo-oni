# -*- coding: utf-8 -*-
from bh import *
import math
Z=U_(); CH=[]; R=sp.Rational; s=sp.sqrt; _c=[0]
def nm(p): _c[0]+=1; return "ax12%s%d"%(p,_c[0])
# 6 接線長と接点を結ぶ弦
def b6(r_,d):
    t=sp.sqrt(d*d-r_*r_); ch=sp.simplify(2*r_*t/d); 
    P=(d,0); th=math.acos(r_/d); T1=(r_*math.cos(th),r_*math.sin(th)); T2=(T1[0],-T1[1])
    assert abs(2*T1[1]-float(ch))<1e-9
    fig=geo(nm("t"),circles=[(0,0,r_,"#333","-")],segs=[(0,0,P[0],P[1],"#888","--"),(P[0],P[1],T1[0],T1[1],"#b81f36","-"),(P[0],P[1],T2[0],T2[1],"#b81f36","-"),(T1[0],T1[1],T2[0],T2[1],"#2a7fd0","-"),(0,0,T1[0],T1[1],"#888","--")],pts=[("O",0,0,-.3,-.3),("P",P[0],P[1],.3,-.3),("A",T1[0],T1[1],0,.4),("B",T2[0],T2[1],0,-.4)],w=44,size=(3.8,3.2))
    st=[("接線長（三平方の定理）","<p>"+I(r"OA\perp PA")+"。</p>"+D(r"PA=\sqrt{OP^2-OA^2}=\sqrt{%d^2-%d^2}=%s"%(d,r_,L(t)))+fig),
        ("弦 $AB$ と $OP$ の交点 $M$","<p>"+I("OP")+" は "+I("AB")+" を垂直に2等分。"+I(r"\triangle OAP")+" の面積を2通りに表す。</p>"+D(r"\dfrac12\cdot OP\cdot AM=\dfrac12\cdot OA\cdot PA\ \Rightarrow\ AM=\dfrac{%d\cdot%s}{%d}"%(r_,L(t),d))),
        ("$AB=2AM$",D(r"AB=%s"%L(ch)))]
    return r"半径 $%d$ の円の中心 $O$ から距離 $%d$ の点 $P$ から円に2本の接線を引き、接点を $A,\ B$ とする。接線の長さ $PA$ と、弦 $AB$ の長さを求めよ。"%(r_,d),st,r"PA=%s,\ AB=%s"%(L(t),L(ch))
o=[b6(*v) for v in [(3,5),(5,13),(4,8),(6,10),(2,6)]]
build(Z,CH,"接線の長さと接点を結ぶ弦",o,r"<p>接線は半径に垂直。$PA=\sqrt{OP^2-r^2}$。弦 $AB$ は $OP$ に垂直で $OP$ に2等分される。$\triangle OAP$ の<b>面積を2通りに</b>表すと $AM$ が出る。</p>","直角三角形の面積は、底辺×高さと斜辺×垂線の2通りで書ける。",6)
# 7 共通弦
def b7(r1,r2,d):
    # centers O1(0,0) O2(d,0); x = (d^2+r1^2-r2^2)/(2d); h=sqrt(r1^2-x^2)
    xx=R(d*d+r1*r1-r2*r2,2*d); h2=r1*r1-xx**2; assert h2>0; ch=2*sp.sqrt(h2)
    hh=float(sp.sqrt(h2))
    fig=geo(nm("c"),circles=[(0,0,r1,"#333","-"),(d,0,r2,"#2a7fd0","-")],segs=[(float(xx),hh,float(xx),-hh,"#b81f36","-"),(0,0,d,0,"#888","--")],pts=[("A",float(xx),hh,0,.4),("B",float(xx),-hh,0,-.4),("O₁",0,0,-.3,-.3),("O₂",d,0,.3,-.3)],w=50,size=(4.4,3.2))
    st=[("交点の座標","<p>"+I("O_1(0,0),\\ O_2(%d,0)"%d)+"。共通弦 "+I("AB")+" は "+I("O_1O_2")+" に垂直。交点 "+I("M")+" の位置を "+I("O_1M=x")+" とおく。</p>"+fig),
        ("2つの三平方",D(r"AM^2=%d^2-x^2=%d^2-(%d-x)^2"%(r1,r2,d))+D(r"x=\dfrac{%d^2+%d^2-%d^2}{2\cdot%d}=%s"%(d,r1,r2,d,L(xx)))),
        ("弦の長さ",D(r"AM=\sqrt{%d-%s}=%s,\qquad AB=%s"%(r1*r1,L(xx**2),L(sp.sqrt(h2)),L(ch))))]
    return r"半径 $%d$ と $%d$ の2円があり、中心間の距離が $%d$ で2点 $A,\ B$ で交わっている。共通弦 $AB$ の長さを求めよ。"%(r1,r2,d),st,L(ch)
o=[b7(*v) for v in [(5,4,6),(7,5,8),(5,5,6),(10,8,12),(13,5,12)]]
build(Z,CH,"2円の共通弦の長さ",o,r"<p>共通弦は中心線に<b>垂直</b>。交点 $M$ までの距離を $x$ とおいて、<b>2つの直角三角形で $AM^2$ を2通りに</b>表し、$x$ を求める。</p>","同じ長さ $AM$ を、2つの円からそれぞれ表して等しいとおく。",7)
# 8 トレミー
def b8(a_,b_,c_,d_):
    # cyclic quadrilateral sides AB=a,BC=b,CD=c,DA=d; diagonal AC = sqrt((ac+bd)(ad+bc)/(ab+cd))
    AC2=R((a_*c_+b_*d_)*(a_*d_+b_*c_),(a_*b_+c_*d_)); BD2=R((a_*c_+b_*d_)*(a_*b_+c_*d_),(a_*d_+b_*c_))
    # check via 余弦定理: cosB=(a²+b²-AC²)/(2ab) ; cosD=(c²+d²-AC²)/(2cd) ; cosB=-cosD
    cB=(a_*a_+b_*b_-AC2)/(2*a_*b_); cD=(c_*c_+d_*d_-AC2)/(2*c_*d_); assert cB+cD==0
    prod=sp.sqrt(AC2)*sp.sqrt(BD2); assert sp.simplify(prod-(a_*c_+b_*d_))==0
    st=[("余弦定理を2回","<p>円に内接する四角形で "+I(r"\angle B+\angle D=180^\circ")+"。"+I("AC")+" を2通りに表す。</p>"+D(r"AC^2=%d^2+%d^2-2\cdot%d\cdot%d\cos B=%d^2+%d^2+2\cdot%d\cdot%d\cos B"%(a_,b_,a_,b_,c_,d_,c_,d_))),
        ("$\\cos B$ を求める",D(r"%d+%d-%d\cos B=%d+%d+%d\cos B\ \Rightarrow\ \cos B=%s"%(a_*a_,b_*b_,2*a_*b_,c_*c_,d_*d_,2*c_*d_,L(cB)) ) if False else D(r"\cos B=%s"%L(cB))),
        ("$AC$",D(r"AC^2=%s\ \Rightarrow\ AC=%s"%(L(AC2),L(sp.sqrt(AC2))))+"<p>（トレミーの定理 "+I(r"AC\cdot BD=AB\cdot CD+BC\cdot DA=%d"%(a_*c_+b_*d_))+" で検算。）</p>")]
    return r"円に内接する四角形 $ABCD$ で、$AB=%d,\ BC=%d,\ CD=%d,\ DA=%d$ のとき、対角線 $AC$ の長さを求めよ。"%(a_,b_,c_,d_),st,L(sp.sqrt(AC2))
o=[b8(*v) for v in [(3,4,5,6),(2,3,4,5),(5,5,5,5) if False else (4,5,6,7),(3,5,7,8),(2,4,6,3)]]
build(Z,CH,"円に内接する四角形の対角線",o,r"<p>内接四角形では対角の和が $180^\circ$ なので $\cos D=-\cos B$。<b>余弦定理を2つの三角形で</b>使って $\cos B$ を出し、$AC$ を求める。</p>","同じ対角線 $AC$ を、$B$ 側と $D$ 側の両方から測る。",8)
# 9 弧の比と角
def b9(p,q,r_):
    tot=p+q+r_; A=R(360*p,tot)/2*1; 
    arcs=[R(360*p,tot),R(360*q,tot),R(360*r_,tot)]; ang=[a/2 for a in arcs]
    th=[math.radians(float(a)) for a in [0,arcs[0],arcs[0]+arcs[1]]]
    pts=[(math.cos(t),math.sin(t)) for t in th]
    fig=geo(nm("a"),circles=[(0,0,1,"#333","-")],polys=[(pts,"#b81f36")],pts=[("A",pts[0][0],pts[0][1],.2,.15),("B",pts[1][0],pts[1][1],-.2,.15),("C",pts[2][0],pts[2][1],0,-.2)],w=38,size=(3.2,3.2))
    st=[("弧の中心角","<p>円周全体が "+I("360^\\circ")+"、弧 "+I("\\overset{\\frown}{AB}:\\overset{\\frown}{BC}:\\overset{\\frown}{CA}=%d:%d:%d"%(p,q,r_))+"。</p>"+D(r"\overset{\frown}{AB}=%s^\circ,\ \ \overset{\frown}{BC}=%s^\circ,\ \ \overset{\frown}{CA}=%s^\circ"%tuple(L(a) for a in arcs))+fig),
        ("円周角は中心角の半分","<p>各角は、<b>その角が向かい合う弧</b>の中心角の半分。</p>"+D(r"\angle C=%s^\circ,\ \ \angle A=%s^\circ,\ \ \angle B=%s^\circ"%(L(ang[0]),L(ang[1]),L(ang[2])))),
        ("確認","<p>"+I(r"%s+%s+%s=180"%tuple(L(a) for a in ang))+"。</p>")]
    return r"円周上の3点 $A,\ B,\ C$ が円周を $\overset{\frown}{AB}:\overset{\frown}{BC}:\overset{\frown}{CA}=%d:%d:%d$ に分けるとき、$\triangle ABC$ の3つの内角を求めよ。"%(p,q,r_),st,r"\angle A=%s^\circ,\ \angle B=%s^\circ,\ \angle C=%s^\circ"%(L(ang[1]),L(ang[2]),L(ang[0]))
o=[b9(*v) for v in [(2,3,4),(1,2,3),(3,4,5),(2,3,7),(1,1,2)]]
build(Z,CH,"弧の比から三角形の角を求める",o,r"<p>弧の比 $\to$ <b>中心角</b>（$360^\circ$ を比で分ける）$\to$ 円周角は中心角の半分。角 $A$ は<b>向かい合う弧 $BC$</b> に対する円周角。</p>","弧の長さは角度の比。向かい合う弧を間違えない。",9)
# 10 外接四角形
def b10(a_,b_,c_,r_):
    d_=a_+c_-b_; S=R(1,2)*(a_+b_+c_+d_)*r_  # S = r*s, s=(a+b+c+d)/2
    s_=a_+c_
    fig=geo(nm("e"),circles=[(0,0,1,"#333","-")],polys=[([(1.2,-1),(1.2,1),(-1,1),(-1.0,-1)],"#b81f36")],w=34,size=(3,3)) if False else ""
    st=[("外接四角形の性質","<p>円に外接する四角形では、<b>向かい合う辺の和が等しい</b>。</p>"+D(r"AB+CD=BC+DA")),
        ("$DA$ を求める",D(r"%d+%d=%d+DA\ \Rightarrow\ DA=%d"%(a_,c_,b_,d_))),
        ("面積","<p>内接円の半径を "+I("r")+" とすると、中心から各頂点へ結んで4つの三角形に分け、"+I(r"S=\dfrac12r(AB+BC+CD+DA)")+"。</p>"+D(r"S=\dfrac12\cdot%d\cdot(%d+%d+%d+%d)=%s"%(r_,a_,b_,c_,d_,L(S))))]
    return r"円に外接する四角形 $ABCD$ で、$AB=%d,\ BC=%d,\ CD=%d$、内接円の半径が $%d$ のとき、$DA$ の長さと四角形の面積を求めよ。"%(a_,b_,c_,r_),st,r"DA=%d,\ \ S=%s"%(d_,L(S))
o=[b10(*v) for v in [(5,7,9,3),(4,6,8,2),(6,5,7,4),(8,9,6,3),(7,8,10,5)]]
build(Z,CH,"円に外接する四角形の辺と面積",o,r"<p>円に外接する四角形は<b>向かい合う辺の和が等しい</b>。面積は、内心から4頂点へ結んだ4つの三角形（高さ $r$）の合計 $S=\dfrac12r\times(\text{周の長さ})$。</p>","接線の長さが等しいので、辺の和が対辺どうしで一致する。",10)
XU=finishx(Z,CH)
