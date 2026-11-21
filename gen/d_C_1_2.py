# -*- coding: utf-8 -*-
from bh import *
Z=U_(); CH=[]
R=sp.Rational
X,Y,Zv=sp.symbols('x y z')
def v3(a): return r"\left(%s,\ %s,\ %s\right)"%tuple(L(t) for t in a)
def sub(a,b): return tuple(p-q for p,q in zip(a,b))
def dot(a,b): return sum(p*q for p,q in zip(a,b))
def cross(a,b): return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def nrm(a): return sp.sqrt(dot(a,a))
ANG={R(1,2):60,R(-1,2):120,sp.sqrt(2)/2:45,sp.Integer(0):90}
def pl(n,d):
    return L(n[0]*X+n[1]*Y+n[2]*Zv)+"="+L(d)
def reduce(n,d):
    g=sp.gcd(sp.gcd(n[0],n[1]),sp.gcd(n[2],d)); n=tuple(t//g for t in n); d=d//g
    f=next((t for t in n if t!=0)); 
    if f<0: n=tuple(-t for t in n); d=-d
    return n,d
# 例題1 内積・なす角
def b1(a,b):
    ip=dot(a,b); na=nrm(a); nb=nrm(b); c=sp.radsimp(sp.nsimplify(sp.simplify(ip/(na*nb)))); key=[k for k in ANG if sp.simplify(k-c)==0]; assert key; deg=ANG[key[0]]
    st=[("内積","<p>"+I(r"\vec a\cdot\vec b=a_1b_1+a_2b_2+a_3b_3")+"。</p>"+D(r"\vec a\cdot\vec b=%s"%L(ip))),
        ("大きさ",D(r"|\vec a|=\sqrt{%s}=%s,\qquad |\vec b|=\sqrt{%s}=%s"%(L(dot(a,a)),L(na),L(dot(b,b)),L(nb)))),
        ("$\\cos\\theta$",D(r"\cos\theta=\dfrac{%s}{%s\times%s}=%s"%(L(ip),L(na),L(nb),L(c)))),
        ("なす角",D(r"\theta=%d^\circ"%deg))]
    return r"$\vec a=%s,\ \vec b=%s$ のとき、$\vec a\cdot\vec b$、$|\vec a|,\ |\vec b|$ と、なす角 $\theta$ を求めよ。"%(v3(a),v3(b)),st,r"\vec a\cdot\vec b=%s,\ |\vec a|=%s,\ |\vec b|=%s,\ \theta=%d^\circ"%(L(ip),L(na),L(nb),deg)
V=[((1,1,0),(0,1,1)),((1,0,1),(1,1,0)),((1,-1,0),(0,1,-1)),((1,1,1),(1,0,-1)),((0,1,1),(0,0,1))]
o=[b1(*x) for x in V]
build(Z,CH,"空間ベクトルの内積となす角",o,r"<p>成分は3つ：$\vec a\cdot\vec b=a_1b_1+a_2b_2+a_3b_3$、$|\vec a|=\sqrt{a_1^2+a_2^2+a_3^2}$。$\cos\theta=\dfrac{\vec a\cdot\vec b}{|\vec a||\vec b|}$ は平面と同じ。</p>","平面のベクトルに「高さ」の成分が1つ増えただけ。公式はそのまま3成分に拡張。",1)
# 例題2 平面の方程式
def b2(A,B,C,Q):
    AB=sub(B,A); AC=sub(C,A); n=cross(AB,AC); d=dot(n,A); n,d=reduce(n,d); assert dot(n,AB)==0 and dot(n,AC)==0 and dot(n,B)==d
    dist=sp.radsimp(sp.Abs(dot(n,Q)-d)/nrm(n)); lam=sp.Symbol('l')
    st=[("平面の法線ベクトル $\\vec n=(a,b,c)$","<p>"+I(r"\overrightarrow{AB}=%s,\ \overrightarrow{AC}=%s"%(v3(AB),v3(AC)))+"。</p>"+D(r"\begin{cases}\vec n\cdot\overrightarrow{AB}=0\\ \vec n\cdot\overrightarrow{AC}=0\end{cases}")+D(r"\begin{cases}%s=0\\ %s=0\end{cases}"%(L(AB[0]*sp.Symbol('a')+AB[1]*sp.Symbol('b')+AB[2]*sp.Symbol('c')),L(AC[0]*sp.Symbol('a')+AC[1]*sp.Symbol('b')+AC[2]*sp.Symbol('c'))))),
        ("$\\vec n$ を1つ求める","<p>2式を満たす比を選ぶ。</p>"+D(r"\vec n=%s"%v3(n))),
        ("平面の方程式","<p>点 "+I("A"+v3(A))+" を通るので</p>"+D(L(n[0]*(X-A[0])+n[1]*(Y-A[1])+n[2]*(Zv-A[2]))+"=0")+D(pl(n,d))),
        ("点 $Q$ との距離","<p>"+I(r"\dfrac{|ax_0+by_0+cz_0-d|}{\sqrt{a^2+b^2+c^2}}")+"。</p>"+D(r"\dfrac{|%s-%s|}{\sqrt{%s}}=\dfrac{%s}{%s}=%s"%(L(dot(n,Q)),L(d),L(dot(n,n)),L(abs(dot(n,Q)-d)),L(nrm(n)),L(dist))))]
    return r"3点 $A%s,\ B%s,\ C%s$ を通る平面の方程式と、点 $Q%s$ からこの平面までの距離を求めよ。"%(v3(A),v3(B),v3(C),v3(Q)),st,r"%s,\ \ \text{距離 }%s"%(pl(n,d),L(dist))
V=[((1,0,0),(0,2,0),(0,0,3),(1,1,1)),((2,0,0),(0,2,0),(0,0,2),(1,2,3)),((1,1,0),(2,0,1),(0,2,1),(0,0,0)),((0,1,2),(1,0,2),(1,1,0),(2,2,2)),((1,0,1),(2,1,1),(1,2,3),(0,0,0))]
o=[b2(*x) for x in V]
build(Z,CH,"3点を通る平面の方程式と距離",o,r"<p>平面 $ax+by+cz=d$ の<b>法線ベクトル $\vec n=(a,b,c)$</b> は平面上の2つのベクトルと垂直（内積 $0$）。$\vec n$ を求め、1点を通る条件から $d$ を決める。点と平面の距離は $\dfrac{|ax_0+by_0+cz_0-d|}{\sqrt{a^2+b^2+c^2}}$。</p>","床に垂直な棒（法線）が決まれば、床の位置は1点で決まる。",2)
# 例題3 平行四辺形
def b3(A,B,C):
    D_=tuple(a+c-b for a,b,c in zip(A,B,C)); AB=sub(B,A); AD=sub(D_,A); cr=cross(AB,AD); S=nrm(cr)
    ip=dot(AB,AD); S2=sp.sqrt(dot(AB,AB)*dot(AD,AD)-ip**2); assert sp.simplify(S-S2)==0
    st=[("第4の頂点 $D$","<p>平行四辺形 "+I("ABCD")+" では "+I(r"\overrightarrow{AD}=\overrightarrow{BC}")+"。</p>"+D(r"D=A+C-B=%s"%v3(D_))),
        ("2辺のベクトル",D(r"\overrightarrow{AB}=%s,\quad \overrightarrow{AD}=%s"%(v3(AB),v3(AD)))),
        ("面積","<p>"+I(r"S=\sqrt{|\overrightarrow{AB}|^2|\overrightarrow{AD}|^2-(\overrightarrow{AB}\cdot\overrightarrow{AD})^2}")+"。</p>"+D(r"|\overrightarrow{AB}|^2=%s,\ |\overrightarrow{AD}|^2=%s,\ \overrightarrow{AB}\cdot\overrightarrow{AD}=%s"%(L(dot(AB,AB)),L(dot(AD,AD)),L(ip)))+D(r"S=\sqrt{%s\times%s-%s^2}=\sqrt{%s}=%s"%(L(dot(AB,AB)),L(dot(AD,AD)),L(ip),L(S**2),L(S))))]
    return r"空間に3点 $A%s,\ B%s,\ C%s$ がある。四角形 $ABCD$ が平行四辺形となるように点 $D$ をとるとき、$D$ の座標と平行四辺形の面積を求めよ。"%(v3(A),v3(B),v3(C)),st,r"D%s,\ S=%s"%(v3(D_),L(S))
V=[((0,0,0),(2,1,0),(3,3,1)),((1,0,0),(2,2,0),(4,3,1)),((0,1,1),(1,3,1),(3,4,2)),((1,1,0),(3,1,1),(4,3,3)),((2,0,1),(3,1,3),(5,2,4))]
o=[b3(*x) for x in V]
build(Z,CH,"平行四辺形の頂点と面積",o,r"<p>平行四辺形 $ABCD$：$\overrightarrow{AD}=\overrightarrow{BC}$ より $D=A+C-B$。面積 $S=\sqrt{|\vec a|^2|\vec b|^2-(\vec a\cdot\vec b)^2}$（$\vec a=\overrightarrow{AB},\ \vec b=\overrightarrow{AD}$）。</p>","向かい合う辺は同じベクトル。面積は「底辺×高さ」を内積だけで表した形。",3)
# 例題4 球面
def b4(A,B,k):
    M=tuple(R(a+b,2) for a,b in zip(A,B)); r2=R(dot(sub(B,A),sub(B,A)),4); rr=sp.sqrt(r2); cr2=r2-(k-M[2])**2; assert cr2>0; cr=sp.sqrt(cr2)
    st=[("中心は中点","<p>直径の両端 $A,B$ の中点が球の中心。</p>"+D(r"M=%s"%v3(M))),
        ("半径は直径の半分",D(r"|AB|^2=%s\ \Rightarrow\ r^2=\dfrac{|AB|^2}{4}=%s"%(L(dot(sub(B,A),sub(B,A))),L(r2)))),
        ("球面の方程式",D(r"(x-%s)^2+(y-%s)^2+(z-%s)^2=%s"%(P(M[0]),P(M[1]),P(M[2]),L(r2)))),
        ("平面 $z=%s$ での切り口"%L(k),"<p>"+I("z=%s"%L(k))+" を代入する。</p>"+D(r"(x-%s)^2+(y-%s)^2=%s-(%s-%s)^2=%s"%(P(M[0]),P(M[1]),L(r2),L(k),P(M[2]),L(cr2)))+"<p>中心 "+I(v3((M[0],M[1],k)))+"、半径 "+I(L(cr))+" の円。</p>")]
    return r"2点 $A%s,\ B%s$ を直径の両端とする球面 $S$ の方程式を求めよ。また、$S$ を平面 $z=%s$ で切った切り口の円の半径を求めよ。"%(v3(A),v3(B),L(k)),st,r"(x-%s)^2+(y-%s)^2+(z-%s)^2=%s,\ \ \text{半径 }%s"%(P(M[0]),P(M[1]),P(M[2]),L(r2),L(cr))
V=[((1,-1,2),(5,3,6),5),((0,0,0),(4,0,0),1),((1,2,3),(5,2,3),4),((-1,0,1),(3,2,5),2),((2,1,0),(4,3,4),3)]
o=[b4(*x) for x in V]
build(Z,CH,"球面の方程式と切り口",o,r"<p>中心 $(a,b,c)$、半径 $r$ の球面：$(x-a)^2+(y-b)^2+(z-c)^2=r^2$。直径の両端が分かれば<b>中点が中心</b>。平面 $z=k$ で切ると円で、$z=k$ を代入すれば中心と半径が分かる。</p>","球をスパッと切った切り口は円。切る高さの分だけ、半径が縮む。",4)
# 例題5 垂線の足
def b5(n,d,Pt):
    nn=dot(n,n); t=R(dot(n,Pt)-d,nn); H=tuple(p-t*c for p,c in zip(Pt,n)); assert dot(n,H)==d
    dist=sp.radsimp(sp.Abs(dot(n,Pt)-d)/nrm(n)); dd=nrm(sub(Pt,H)); assert sp.simplify(dist-dd)==0
    st=[("垂線の足を $P$ から表す","<p>平面の法線ベクトルは "+I(r"\vec n=%s"%v3(n))+"。$H$ は $P$ から $\\vec n$ 方向に進んだ点。</p>"+D(r"\overrightarrow{PH}=-t\,\vec n,\quad H=%s"%v3(tuple(p-sp.Symbol('t')*c for p,c in zip(Pt,n))))),
        ("$H$ が平面上にある条件",D(pl(n,d).replace("x","(%s)"%L(Pt[0]-n[0]*sp.Symbol('t'))).replace("y","(%s)"%L(Pt[1]-n[1]*sp.Symbol('t'))).replace("z","(%s)"%L(Pt[2]-n[2]*sp.Symbol('t'))) if False else r"%s(%s)+%s(%s)+%s(%s)=%s"%(cf(n[0]),L(Pt[0]-n[0]*sp.Symbol('t')),cf(n[1]),L(Pt[1]-n[1]*sp.Symbol('t')),cf(n[2]),L(Pt[2]-n[2]*sp.Symbol('t')),L(d)))+D(r"%s-%s\,t=%s\ \Rightarrow\ t=%s"%(L(dot(n,Pt)),L(nn),L(d),L(t)))),
        ("$H$ の座標と距離",D(r"H=%s"%v3(H))+D(r"PH=|t|\,|\vec n|=%s\times\sqrt{%s}=%s"%(L(abs(t)),L(nn),L(dd))))]
    return r"平面 $\alpha:\ %s$ と点 $P%s$ がある。$P$ から $\alpha$ に下ろした垂線の足 $H$ の座標と、$P$ と $\alpha$ の距離を求めよ。"%(pl(n,d),v3(Pt)),st,r"H%s,\ \ \text{距離 }%s"%(v3(H),L(dd))
V=[((1,2,2),9,(0,0,0)),((1,1,1),6,(1,1,1)),((2,1,-2),6,(1,2,3)),((1,-1,2),4,(2,0,-1)),((3,0,4),10,(1,2,3))]
o=[b5(*x) for x in V]
build(Z,CH,"点から平面への垂線の足",o,r"<p>$P$ から平面 $\alpha$ への垂線は <b>$\alpha$ の法線ベクトル $\vec n$ に平行</b>。$H=P-t\vec n$ とおき、$H$ が $\alpha$ 上にある条件から $t$ を求める。距離は $|t||\vec n|$。</p>","床に向かって真っすぐ（法線方向）に下ろした糸が、床に刺さる点が垂線の足。",5)
UNIT=finish(Z,CH,0,1,"ベクトル","空間ベクトル","内積、平面の方程式、平行四辺形、球面、垂線の足まで、空間ベクトルの難問に挑みます。",subject="C")
