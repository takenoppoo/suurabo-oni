# -*- coding: utf-8 -*-
from bh import *
import math
Z=U_(); CH=[]
R=sp.Rational; s=sp.sqrt
def deg_note(c):
    return {R(-1,2):r",\ C=120^\circ",R(1,2):r",\ C=60^\circ",0:r",\ C=90^\circ"}.get(c,"")
# 6
def b6(p,q,r_):
    assert r_>=max(p,q) and p+q>r_
    cC=R(p*p+q*q-r_*r_,2*p*q); assert abs(math.acos(float(cC))-sum(0 for _ in [0]) )>=0
    st=[("辺の比にする","<p>正弦定理 "+I(r"a=2R\sin A")+" などより "+I(r"a:b:c=\sin A:\sin B:\sin C")+"。</p>"+D(r"a:b:c=%d:%d:%d"%(p,q,r_))+"<p>"+I("a=%dk,\\ b=%dk,\\ c=%dk"%(p,q,r_))+" とおく。</p>"),
        ("最大辺の対角に余弦定理",D(r"\cos C=\dfrac{(%dk)^2+(%dk)^2-(%dk)^2}{2\cdot%dk\cdot%dk}=\dfrac{%d}{%d}=%s"%(p,q,r_,p,q,p*p+q*q-r_*r_,2*p*q,L(cC)))),
        ("判断","<p>"+I(r"\cos C%s0"%("<" if cC<0 else (">" if cC>0 else "=")))+" なので "+("鈍角" if cC<0 else ("鋭角" if cC>0 else "直角"))+"。</p>")]
    return r"$\triangle ABC$ で $\sin A:\sin B:\sin C=%d:%d:%d$ のとき、$\cos C$ の値を求めよ。"%(p,q,r_),st,r"\cos C=%s%s"%(L(cC),deg_note(cC))
o=[b6(*v) for v in [(3,5,7),(5,7,8),(3,4,5),(4,7,9),(7,8,13)]]
build(Z,CH,"sinA:sinB:sinC の比から角を求める",o,r"<p>$a:b:c=\sin A:\sin B:\sin C$。<b>$k$ を使って辺を表し</b>、最大辺の対角に余弦定理。$k$ は約分で消える。</p>","角の比は辺の比と同じ。比のまま計算する。",6)
# 7 仰角
def b7(a1,a2,d):
    # tower height h: from A elevation a1, from B (d farther away on a line) elevation a2 ; cot a2 - cot a1 = d/h  with a2<a1
    cot=lambda t:1/sp.tan(sp.rad(t)) if False else sp.cot(t*sp.pi/180)
    h=sp.nsimplify(sp.simplify(d/(cot(a2)-cot(a1)))); h=sp.radsimp(h)
    assert abs(float(h)*(float(cot(a2))-float(cot(a1)))-d)<1e-9
    st=[("図の文字","<p>塔の高さを "+I("h")+"、塔の足から "+I("A")+" までを "+I("%s"%("h\\cot %d^\\circ"%a1))+"、"+I("B")+" までを "+I("h\\cot %d^\\circ"%a2)+" と表す。</p>"),
        ("距離の条件",D(r"h\cot%d^\circ-h\cot%d^\circ=%d"%(a2,a1,d))),
        ("$h$ を求める","<p>"+I(r"\cot30^\circ=\sqrt3,\ \cot45^\circ=1,\ \cot60^\circ=\dfrac1{\sqrt3}")+"。</p>"+D(r"h=\dfrac{%d}{\cot%d^\circ-\cot%d^\circ}=%s"%(d,a2,a1,L(h))))]
    return r"水平な地面に立つ塔の足と一直線上の2地点 $A,\ B$ から塔の先端を見上げると、仰角はそれぞれ $%d^\circ,\ %d^\circ$ であった。$AB=%d$ m のとき、塔の高さを求めよ。（$A$ のほうが塔に近い）"%(a1,a2,d),st,r"%s\ \text{m}"%L(h)
o=[b7(*v) for v in [(45,30,20),(60,30,40),(60,45,30),(45,30,50),(60,30,24)]]
build(Z,CH,"仰角から塔の高さを求める",o,r"<p>塔の足からの距離は $h\cot\theta$（$=h/\tan\theta$）。<b>2地点の距離の差</b>が $d$ になる式を立てて $h$ を求める。</p>","仰角が大きいほど塔に近い。近い方からの距離は短い。",7)
# 8 形状決定
def shape(i):
    forms=[
     (r"a\cos A=b\cos B",r"\sin A\cos A=\sin B\cos B\ \text{（正弦定理）}\Rightarrow\sin2A=\sin2B\Rightarrow 2A=2B\ \text{または}\ 2A=180^\circ-2B",r"\text{二等辺三角形（}A=B\text{）または}\ C=90^\circ\text{の直角三角形}"),
     (r"\sin A=2\sin B\cos C",r"\sin(B+C)=2\sin B\cos C\Rightarrow\sin B\cos C-\cos B\sin C=0\Rightarrow\sin(B-C)=0\Rightarrow B=C",r"B=C\text{の二等辺三角形}"),
     (r"\sin^2A+\sin^2B=\sin^2C",r"a^2+b^2=c^2\ \text{（正弦定理で辺に直す）}",r"C=90^\circ\text{の直角三角形}"),
     (r"\dfrac{a}{\cos A}=\dfrac{b}{\cos B}",r"\dfrac{\sin A}{\cos A}=\dfrac{\sin B}{\cos B}\Rightarrow\tan A=\tan B\Rightarrow A=B",r"A=B\text{の二等辺三角形}"),
     (r"a^2\tan B=b^2\tan A",r"\sin^2A\cdot\dfrac{\sin B}{\cos B}=\sin^2B\cdot\dfrac{\sin A}{\cos A}\Rightarrow\sin A\cos A=\sin B\cos B\Rightarrow\sin2A=\sin2B",r"A=B\text{の二等辺三角形または}\ C=90^\circ\text{の直角三角形}")]
    cond,der,res=forms[i]
    st=[("条件を $\\sin$ だけの式にする","<p>正弦定理 "+I(r"a=2R\sin A,\ b=2R\sin B,\ c=2R\sin C")+" を使い、辺を $\\sin$ に置きかえる（$2R$ は約分で消える）。</p>"),
        ("式を変形",D(der)),
        ("三角形の形",D(res))]
    return r"$\triangle ABC$ で $%s$ が成り立つとき、この三角形はどんな形か。"%cond,st,res
o=[shape(i) for i in [0,1,2,3,4]]
# o の例題を入れかえ: 例題は0
build(Z,CH,"三角形の形の決定",o,r"<p>正弦定理 $\sin A=\dfrac a{2R}$ や余弦定理で、<b>角か辺のどちらか一方にそろえる</b>。$\sin2A=\sin2B$ のときは $A=B$ のほか $2A=180^\circ-2B$ の場合も忘れない。</p>","三角形の素性を調べる、辺か角のどちらかに言葉をそろえる。",8)
# 9 四角形の面積
def b9(p,q,th):
    S=R(1,2)*p*q*sp.sin(th*sp.pi/180); S=sp.simplify(S)
    # numeric: build quadrilateral with diagonals intersecting at angle th
    a=np.radians(th); P=np.array([0,0]); d1=np.array([p,0]); 
    # place diagonals from intersection O at origin: A=(-p/3,..) use full
    A=np.array([-p*0.4,0]); C=np.array([p*0.6,0]); B=np.array([-q*0.3*np.cos(a),-q*0.3*np.sin(a)]); D_=np.array([q*0.7*np.cos(a),q*0.7*np.sin(a)])
    pts=[A,B,C,D_]; area=0.5*abs(sum(pts[i][0]*pts[(i+1)%4][1]-pts[(i+1)%4][0]*pts[i][1] for i in range(4)))
    assert abs(area-float(S))<1e-6
    st=[("四角形を4つの三角形に","<p>対角線の交点を "+I("O")+" とし、4つの三角形の面積を足す。"+I(r"AO=a_1,\ CO=a_2,\ BO=b_1,\ DO=b_2")+"（"+I("a_1+a_2=%d,\\ b_1+b_2=%d"%(p,q))+"）。</p>"),
        ("1つの三角形の面積","<p>"+I(r"\triangle AOB=\dfrac12a_1b_1\sin%d^\circ"%th)+"。他も同じ角（または補角）なので "+I(r"\sin")+" は同じ値。</p>"),
        ("まとめる","<p>4つの三角形の面積を足す。</p>"+D(r"S=\dfrac12a_1b_1\sin%d^\circ+\dfrac12b_1a_2\sin%d^\circ+\dfrac12a_2b_2\sin%d^\circ+\dfrac12b_2a_1\sin%d^\circ"%(th,th,th,th))+"<p>共通の "+I(r"\dfrac12\sin%d^\circ"%th)+" でくくる。</p>"+D(r"S=\dfrac12(a_1b_1+a_2b_1+a_2b_2+a_1b_2)\sin%d^\circ=\dfrac12(a_1+a_2)(b_1+b_2)\sin%d^\circ"%(th,th))+D(r"S=\dfrac12\cdot%d\cdot%d\cdot%s=%s"%(p,q,L(sp.sin(th*sp.pi/180)),L(S))))]
#\dfrac12\cdot%d\cdot%d\cdot%s=%s"%(th,p,q,L(sp.sin(th*sp.pi/180)),L(S))))]
    return r"四角形 $ABCD$ の対角線 $AC=%d,\ BD=%d$ が $%d^\circ$ の角で交わっている。この四角形の面積を求めよ。"%(p,q,th),st,L(S)
o=[b9(*v) for v in [(8,6,30),(10,7,45),(12,5,60),(9,8,30),(14,6,45)]]
build(Z,CH,"四角形の面積（対角線と交角）",o,r"<p>対角線 $p,q$ が角 $\theta$ で交わるとき $S=\dfrac12pq\sin\theta$。4つの三角形に分け、$\sin\theta=\sin(180^\circ-\theta)$ を使えば導ける。</p>","対角線2本さえ分かれば、四角形の面積が決まる。",9)
# 10 外接円一定で面積最大
def b10(Adeg,Rr):
    A=Adeg*math.pi/180; S=lambda B:2*Rr**2*np.sin(A)*np.sin(B)*np.sin(math.pi-A-B)
    Bs=np.linspace(0.001,math.pi-A-0.001,100001); v=S(Bs); mx=v.max()
    a_=2*Rr*sp.sin(Adeg*sp.pi/180); cA=sp.cos(Adeg*sp.pi/180); sA=sp.sin(Adeg*sp.pi/180)
    bcmax=sp.simplify(a_**2/(2*(1-cA))); Smax=sp.simplify(R(1,2)*bcmax*sA)
    assert abs(float(Smax)-mx)<1e-3
    st=[("$a$ は一定","<p>正弦定理より "+I(r"a=2R\sin A=%s"%L(sp.simplify(a_)))+"（一定）。</p>"),
        ("余弦定理と相加・相乗平均","<p>"+I(r"a^2=b^2+c^2-2bc\cos A\geqq 2bc-2bc\cos A=2bc(1-\cos A)")+"（等号は "+I("b=c")+"）。</p>"+D(r"bc\leqq\dfrac{a^2}{2(1-\cos A)}=%s"%L(bcmax))),
        ("面積の最大値","<p>"+I(r"S=\dfrac12bc\sin A")+" より</p>"+D(r"S_{\max}=\dfrac12\cdot%s\cdot%s=%s"%(L(bcmax),L(sA),L(Smax))))]
    return r"外接円の半径が $%d$、$\angle A=%d^\circ$ の $\triangle ABC$ の面積の最大値を求めよ。"%(Rr,Adeg),st,L(Smax)
o=[b10(*v) for v in [(60,2),(90,3),(60,4),(120,2),(90,5)]]
build(Z,CH,"外接円が一定のときの面積の最大",o,r"<p>$A$ と $R$ が一定なら $a$ も一定。余弦定理 $a^2=b^2+c^2-2bc\cos A$ と $b^2+c^2\geqq2bc$ から <b>$bc$ の最大値</b>を出し、$S=\dfrac12bc\sin A$ に入れる。等号は $b=c$。</p>","1辺が決まったら、残る2辺が等しいときに面積が最大になる。",10)
XU=finishx(Z,CH)
