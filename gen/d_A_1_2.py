# -*- coding: utf-8 -*-
# 円の性質（数学A 図形の性質）
from ah import *
import math
from fractions import Fraction as Fr
Z=U_()
def dist(p,q): return math.hypot(p[0]-q[0],p[1]-q[1])
def tp(a,b,c):
    cb=(c*c+a*a-b*b)/(2*c*a); return (c*cb,c*math.sqrt(1-cb*cb))
def ang(P,Q,R):
    v=np.array(P)-np.array(Q); w=np.array(R)-np.array(Q); return math.degrees(math.acos(v@w/np.linalg.norm(v)/np.linalg.norm(w)))
def onc(deg,r=1,c=(0,0)): return (c[0]+r*math.cos(math.radians(deg)),c[1]+r*math.sin(math.radians(deg)))

# ===== 例題1 方べきの定理 =====
def power_fig():
    # P=(0,0), 割線1: x軸上 A=3,B=8, 中心(5.5,k)
    k=2.5; O=(5.5,k); r=math.sqrt(2.5**2+k**2)
    # 割線2: 角θ で t=4,6
    from math import cos,sin
    th=None
    for i in range(1,1800):
        t_=math.radians(i/10)
        if abs(5.5*cos(t_)+k*sin(t_)-5)<1e-3 and 0<i/10<90: th=t_
    assert th
    return O,r,th
O,r,th=power_fig()
C=(4*math.cos(th),4*math.sin(th)); Dd=(6*math.cos(th),6*math.sin(th))
close(dist(C,O),r,2e-2); close(dist(Dd,O),r,2e-2)
pw=dist((0,0),O)**2-r*r; close(pw,24,1e-6)
# 接点
d=dist((0,0),O); tl=math.sqrt(d*d-r*r); close(tl,2*math.sqrt(6))
f1=geo("a12_e1",circles=[(O[0],O[1],r,"#333","-")],segs=[(0,0,8.8,0,"#b81f36","-"),(0,0,6.6*math.cos(th),6.6*math.sin(th),"#2a7fd0","-")],
 pts=[("P",0,0,-0.4,-0.3),("A",3,0,0,-0.5),("B",8,0,0.4,-0.4),("C",C[0],C[1],-0.45,0.1),("D",Dd[0],Dd[1],-0.45,0.35)],w=48,size=(4.6,3.2),lim=(-1,9.6,-1.3,6.6))
for (pa,ab,pc),(pd,cd,pt2) in (((3,5,4),(6,2,24)),((2,7,3),(6,3,18)),((4,5,3),(12,9,36)),((2,4,3),(4,1,12)),((5,3,4),(10,6,40))):
    pb=pa+ab; assert pa*pb==pc*pd and pd-pc==cd and pa*pb==pt2
Z.ex("方べきの定理",
 r"円の外部の点 P から、この円に2本の割線を引く。1本は円と A、B で交わり（A が P に近い側）$PA=3,\ AB=5$、もう1本は C、D で交わる（C が P に近い側）。$PC=4$ のとき、PD、CD の長さと、P から円に引いた接線の長さ PT を求めよ。",
 r"<p><b>方べきの定理</b>：円外の点 P を通る直線が円と X、Y で交わるとき、$PX\cdot PY$ は直線によらず一定。接線なら $PT^2$ に等しい。</p>$$PA\cdot PB=PC\cdot PD=PT^2$$<p>「近い方×遠い方」を、どの交点も <b>P からの距離</b>で測るのがポイント。</p>",
 "P から見て『手前の交点までの長さ×奥の交点までの長さ』は、どの直線でも同じ値。接線は手前と奥が一致した場合。",
 [("PB を求める",r"$PB=PA+AB=3+5=8$。"),
  ("方べきの定理で PD を求める",r"$$PA\cdot PB=PC\cdot PD\ \Rightarrow\ 3\times8=4\times PD\ \Rightarrow\ PD=6$$"),
  ("CD を求める",r"$CD=PD-PC=6-4=2$。"),
  ("接線の長さ PT を求める",r"$$PT^2=PA\cdot PB=24\ \Rightarrow\ PT=\sqrt{24}=2\sqrt6$$")],
 r"PD=6,\quad CD=2,\quad PT=2\sqrt6",
 [r"$PA=2,\ AB=7,\ PC=3$ のときの PD、CD、PT",r"$PA=4,\ AB=5,\ PC=3$ のときの PD、CD、PT",r"$PA=2,\ AB=4,\ PC=3$ のときの PD、CD、PT"],
 [(r"$PB=9$。$2\cdot9=3\cdot PD\Rightarrow PD=6$。$CD=3$。$PT^2=18\Rightarrow PT=3\sqrt2$。",r"PD=6,\ CD=3,\ PT=3\sqrt2"),
  (r"$PB=9$。$4\cdot9=3\cdot PD\Rightarrow PD=12$。$CD=9$。$PT^2=36\Rightarrow PT=6$。",r"PD=12,\ CD=9,\ PT=6"),
  (r"$PB=6$。$2\cdot6=3\cdot PD\Rightarrow PD=4$。$CD=1$。$PT^2=12\Rightarrow PT=2\sqrt3$。",r"PD=4,\ CD=1,\ PT=2\sqrt3")],fig=f1)

# ===== 例題2 円周角・内接四角形 =====
def cyc4(adb,bac):
    # 弧AB=2*adb, 弧BC=2*bac, 残り(360-2adb-2bac)を C→D→A に分ける(CD:DA=5:6)
    a0=0; B_=2*adb; C_=B_+2*bac; rest=360-C_; D_=C_+rest*5/11
    return [onc(a0),onc(B_),onc(C_),onc(D_)]
for adb,bac in ((40,30),(35,45),(28,62),(48,33),(38,47)):
    A,B,C,D=cyc4(adb,bac)
    close(ang(A,D,B),adb,1e-7); close(ang(B,A,C),bac,1e-7); close(ang(A,C,B),adb,1e-7); close(ang(A,B,C),180-adb-bac,1e-7); close(ang(A,D,C),adb+bac,1e-7)
A,B,C,D=cyc4(40,30)
f2=geo("a12_e2",circles=[(0,0,1,"#333","-")],polys=[([A,B,C,D],"#333")],segs=[(A[0],A[1],C[0],C[1],"#b81f36","-"),(B[0],B[1],D[0],D[1],"#2a7fd0","-")],
 pts=[("A",A[0],A[1],0.18,0),("B",B[0],B[1],0.06,0.16),("C",C[0],C[1],-0.18,0.05),("D",D[0],D[1],0.0,-0.18)],w=38,size=(3.4,3.4),lim=(-1.4,1.4,-1.4,1.4))
Z.ex("円周角の定理と円に内接する四角形",
 r"円周上に4点 A、B、C、D がこの順にあり、$\angle ADB=40^\circ,\ \angle BAC=30^\circ$ である。$\angle ACB,\ \angle ABC,\ \angle ADC$ を求めよ。",
 r"<ul><li><b>円周角の定理</b>：同じ弧に対する円周角は等しい。</li><li><b>円に内接する四角形</b>：向かい合う角の和は $180^\circ$（外角は内対角に等しい）。</li></ul>",
 "『同じ弧を見ている角は同じ大きさ』。まず弧AB を見ている2つの角を結びつける。",
 [(r"$\angle ACB$",r"$\angle ADB$ と $\angle ACB$ はどちらも弧 AB に対する円周角なので $$\angle ACB=\angle ADB=40^\circ$$"),
  (r"$\angle ABC$",r"△ABC の内角の和より $$\angle ABC=180^\circ-30^\circ-40^\circ=110^\circ$$"),
  (r"$\angle ADC$",r"四角形 ABCD は円に内接するので、対角の和は $180^\circ$。 $$\angle ADC=180^\circ-\angle ABC=180^\circ-110^\circ=70^\circ$$ （確かめ：$\angle ADC=\angle ADB+\angle BDC=40^\circ+30^\circ=70^\circ$。$\angle BDC=\angle BAC$）")],
 r"\angle ACB=40^\circ,\quad \angle ABC=110^\circ,\quad \angle ADC=70^\circ",
 [r"$\angle ADB=35^\circ,\ \angle BAC=45^\circ$ のときの $\angle ACB,\ \angle ABC,\ \angle ADC$",r"$\angle ADB=28^\circ,\ \angle BAC=62^\circ$ のときの $\angle ACB,\ \angle ABC,\ \angle ADC$",r"$\angle ADB=48^\circ,\ \angle BAC=33^\circ$ のときの $\angle ACB,\ \angle ABC,\ \angle ADC$"],
 [(r"$\angle ACB=35^\circ$。$\angle ABC=180^\circ-45^\circ-35^\circ=100^\circ$。$\angle ADC=180^\circ-100^\circ=80^\circ$。",r"35^\circ,\ 100^\circ,\ 80^\circ"),
  (r"$\angle ACB=28^\circ$。$\angle ABC=180^\circ-62^\circ-28^\circ=90^\circ$。$\angle ADC=90^\circ$（AC は直径）。",r"28^\circ,\ 90^\circ,\ 90^\circ"),
  (r"$\angle ACB=48^\circ$。$\angle ABC=180^\circ-33^\circ-48^\circ=99^\circ$。$\angle ADC=180^\circ-99^\circ=81^\circ$。",r"48^\circ,\ 99^\circ,\ 81^\circ")],fig=f2)

# ===== 例題3 接弦定理 =====
def tang(tab,sac):
    arcAB=2*tab; arcAC=2*sac; arcBC=360-arcAB-arcAC
    A=onc(-90); B=onc(-90+arcAB); C=onc(-90+arcAB+arcBC)
    return A,B,C
for tab,sac in ((70,50),(65,45),(80,35),(55,75),(58,64)):
    A,B,C=tang(tab,sac)
    close(ang((1.5,-1),A,B),tab,1e-7) if False else None
    close(ang(B,A,C),180-tab-sac,1e-7); close(ang(A,C,B),tab,1e-7); close(ang(A,B,C),sac,1e-7)
    # 接弦: 接線方向 T=(A.x+1,A.y) と AB のなす角
    T=(A[0]+1,A[1]); S=(A[0]-1,A[1]); close(ang(T,A,B),tab,1e-7); close(ang(S,A,C),sac,1e-7)
A,B,C=tang(70,50)
f3=geo("a12_e3",circles=[(0,0,1,"#333","-")],polys=[([A,B,C],"#333")],segs=[(-1.7,-1,1.7,-1,"#b81f36","-")],
 pts=[("A",A[0],A[1],0,-0.2),("B",B[0],B[1],0.18,0.05),("C",C[0],C[1],-0.18,0.08),("T",1.7,-1,0,0.18,False),("S",-1.7,-1,0,0.18,False)],w=42,size=(3.8,3.2),lim=(-2,2,-1.4,1.4))
Z.ex("接弦定理",
 r"円周上の点 A における接線上に、A をはさんで2点 T、S をとる。円周上に2点 B、C があって、B は T の側、C は S の側にある。$\angle TAB=70^\circ,\ \angle SAC=50^\circ$ のとき、$\angle ACB,\ \angle ABC,\ \angle BAC$ を求めよ。",
 r"<p><b>接弦定理</b>：接線と弦のつくる角は、その角の内部にある弧に対する円周角に等しい。$\angle TAB$ の内部の弧は弧 AB なので、$\angle TAB=\angle ACB$。</p>",
 "接線は『円周角を接点に押しつぶしたもの』。接線と弦の角は、反対側の円周角と同じ。",
 [(r"$\angle ACB$",r"接弦定理：$\angle ACB=\angle TAB=70^\circ$。"),
  (r"$\angle ABC$",r"接線と弦 AC のつくる角 $\angle SAC$ について、内部の弧は弧 AC。よって $\angle ABC=\angle SAC=50^\circ$。"),
  (r"$\angle BAC$",r"一直線 TS 上で $\angle TAB+\angle BAC+\angle SAC=180^\circ$ より $$\angle BAC=180^\circ-70^\circ-50^\circ=60^\circ$$ 確かめ：△ABC の内角の和 $60^\circ+70^\circ+50^\circ=180^\circ$。")],
 r"\angle ACB=70^\circ,\quad \angle ABC=50^\circ,\quad \angle BAC=60^\circ",
 [r"$\angle TAB=65^\circ,\ \angle SAC=45^\circ$ のときの $\angle ACB,\ \angle ABC,\ \angle BAC$",r"$\angle TAB=80^\circ,\ \angle SAC=35^\circ$ のときの $\angle ACB,\ \angle ABC,\ \angle BAC$",r"$\angle TAB=55^\circ,\ \angle SAC=75^\circ$ のときの $\angle ACB,\ \angle ABC,\ \angle BAC$"],
 [(r"$\angle ACB=65^\circ$、$\angle ABC=45^\circ$、$\angle BAC=180^\circ-65^\circ-45^\circ=70^\circ$。",r"65^\circ,\ 45^\circ,\ 70^\circ"),
  (r"$\angle ACB=80^\circ$、$\angle ABC=35^\circ$、$\angle BAC=180^\circ-80^\circ-35^\circ=65^\circ$。",r"80^\circ,\ 35^\circ,\ 65^\circ"),
  (r"$\angle ACB=55^\circ$、$\angle ABC=75^\circ$、$\angle BAC=180^\circ-55^\circ-75^\circ=50^\circ$。",r"55^\circ,\ 75^\circ,\ 50^\circ")],fig=f3)

# ===== 例題4 共通接線 =====
def tl(r1,r2,d): return math.sqrt(d*d-(r1-r2)**2),math.sqrt(d*d-(r1+r2)**2)
for (r1,r2,d),(e,i) in (((4,1,13),(4*math.sqrt(10),12)),((5,2,10),(math.sqrt(91),math.sqrt(51))),((3,3,10),(10,8)),((6,2,10),(2*math.sqrt(21),6)),((7,3,12),(8*math.sqrt(2),2*math.sqrt(11)))):
    a,b=tl(r1,r2,d); close(a,e); close(b,i)
# 図: O=(0,0) r=4, O'=(13,0) r=1 ; 外接線
d=13; r1,r2=4,1; s=(r1-r2)/d; c=math.sqrt(1-s*s)
P=(r1*s,r1*c); Q=(d+r2*s,r2*c)   # 外接線の接点(上側)
close(dist(P,Q),4*math.sqrt(10),1e-7)
H=(Q[0]-(Q[0]-P[0])*0+0,0)
f4=geo("a12_e4",circles=[(0,0,4,"#333","-"),(13,0,1,"#333","-")],segs=[(0,0,13,0,"#999","--"),(P[0],P[1],Q[0],Q[1],"#b81f36","-"),(0,0,P[0],P[1],"#999","--"),(13,0,Q[0],Q[1],"#999","--"),(Q[0],Q[1],0+Q[0]-(Q[0]-P[0]),Q[1]-(Q[0]-P[0])*0,"#fff","-")],
 pts=[("O",0,0,-0.4,-0.4),("O'",13,0,0.5,-0.45),("P",P[0],P[1],-0.3,0.4),("Q",Q[0],Q[1],0.3,0.4)],w=60,size=(5.6,2.6),lim=(-5,15,-5,5.3))
Z.ex("2円の共通接線の長さ",
 r"半径 4 の円 O と半径 1 の円 O' があり、中心間の距離 $OO'=13$ で、2円は離れている。2円の共通外接線の接点間の長さ（共通外接線の長さ）と、共通内接線の接点間の長さ（共通内接線の長さ）を求めよ。",
 r"<p>接点と中心を結ぶ半径は接線に垂直。<b>直角三角形を作って三平方の定理</b>を使う。</p><ul><li>外接線：O' から OP（P は円 O 上の接点）に垂線 O'H を引く。長方形ができて $PQ=O'H$、$OH=r-r'$（半径の<b>差</b>）。</li><li>内接線：同じく補助線を引くと $OH=r+r'$（半径の<b>和</b>）。</li></ul>",
 "接線の長さ＝√（中心間の距離² －（半径の差 or 和）²）。外側は差、内側（交差）は和。",
 [("共通外接線の長さ",r"外接線の接点を P、Q とする。O' から OP に垂線 O'H を引くと、$PQ=O'H$、$OH=4-1=3$。△OO'H で三平方の定理 $$PQ^2=13^2-3^2=169-9=160\ \Rightarrow\ PQ=4\sqrt{10}$$"),
  ("共通内接線の長さ",r"内接線の接点を P'、Q' とする。O' から OP' の延長上に垂線 O'H' を引くと、$P'Q'=O'H'$、$OH'=4+1=5$。 $$P'Q'^2=13^2-5^2=169-25=144\ \Rightarrow\ P'Q'=12$$")],
 r"\text{外接線の長さ}\ 4\sqrt{10},\quad \text{内接線の長さ}\ 12",
 [r"半径 5 と半径 2 の2円（離れている）、中心間距離 10 のときの共通外接線・共通内接線の長さ",r"半径 3 と半径 3 の2円（離れている）、中心間距離 10 のときの共通外接線・共通内接線の長さ",r"半径 6 と半径 2 の2円（離れている）、中心間距離 10 のときの共通外接線・共通内接線の長さ"],
 [(r"外接線：$100-(5-2)^2=91$ → $\sqrt{91}$。内接線：$100-(5+2)^2=51$ → $\sqrt{51}$。",r"\text{外接}\ \sqrt{91},\ \text{内接}\ \sqrt{51}"),
  (r"外接線：$100-(3-3)^2=100$ → $10$。内接線：$100-(3+3)^2=64$ → $8$。",r"\text{外接}\ 10,\ \text{内接}\ 8"),
  (r"外接線：$100-(6-2)^2=84$ → $2\sqrt{21}$。内接線：$100-(6+2)^2=36$ → $6$。",r"\text{外接}\ 2\sqrt{21},\ \text{内接}\ 6")],fig=f4)

# ===== 例題5 内接円と接線の長さ =====
def inc(ab,bc,ca):
    xa=Fr(ab+ca-bc,2); xb=Fr(ab+bc-ca,2); xc=Fr(bc+ca-ab,2)
    s=Fr(ab+bc+ca,2); S2=s*(s-ab)*(s-bc)*(s-ca); r2=S2/s**2   # r^2=S^2/s^2
    return xa,xb,xc,r2
for (ab,bc,ca),(xa,xb,xc,r2,ai2) in (((7,8,9),(4,3,5,Fr(5),Fr(21))),((5,6,5),(2,3,3,Fr(9,4),Fr(25,4))),((13,14,15),(7,6,8,Fr(16),Fr(65))),((6,7,5),(2,4,3,Fr(8,3),Fr(20,3))),((8,10,12),(5,3,7,Fr(7),Fr(32)))):
    got=inc(ab,bc,ca); assert got[:3]==(xa,xb,xc) and got[3]==r2, (ab,bc,ca,got)
    assert xa**2+r2==ai2
Ap=tp(8,9,7); Bp=(0,0); Cp=(8,0); la,lb,lc=8,9,7
I_=((la*Ap[0]+lb*Bp[0]+lc*Cp[0])/24,(la*Ap[1]+lb*Bp[1]+lc*Cp[1])/24); rr=math.sqrt(5); close(I_[1],rr,1e-9)
f5=geo("a12_e5",circles=[(I_[0],I_[1],rr,"#b81f36","-")],polys=[([Bp,Cp,Ap],"#333")],
 pts=[("A",Ap[0],Ap[1],0,0.3),("B",0,0,-0.3,-0.2),("C",8,0,0.3,-0.2),("I",I_[0],I_[1],0.18,0.18)],texts=[(0.9,1.8,"3","#555"),(4,-0.5,"8","#555")],w=42,size=(3.8,3.2),lim=(-1,9,-1,4.5))
Z.ex("内接円と接線の長さ",
 r"△ABC で $AB=7,\ BC=8,\ CA=9$ とし、内接円 I が各辺に接する点を考える。頂点 A、B、C から接点までの長さ、内接円の半径 $r$、AI の長さを求めよ。",
 r"<p>円外の1点から引いた2本の接線の長さは等しい。頂点 A、B、C から接点までの長さを $x,y,z$ とすると $x+y=AB,\ y+z=BC,\ z+x=CA$。半径は面積 $S$ と $s=\dfrac{a+b+c}2$ から $S=rs$ で出す。</p>",
 "1つの点から円に引いた接線の長さは同じ。3辺を、頂点ごとの『接線の長さ』の和で表して連立。",
 [("連立方程式を立てる",r"A、B、C から接点までの長さを $x,\ y,\ z$ とする。 $$x+y=7,\quad y+z=8,\quad z+x=9$$"),
  ("解く",r"3式を足して $2(x+y+z)=24$、$x+y+z=12$。よって $$z=12-7=5,\quad x=12-8=4,\quad y=12-9=3$$"),
  ("面積と半径",r"$s=\dfrac{7+8+9}2=12$。ヘロンの公式 $$S=\sqrt{12(12-7)(12-8)(12-9)}=\sqrt{12\cdot5\cdot4\cdot3}=\sqrt{720}=12\sqrt5$$ $S=rs$ より $r=\dfrac{12\sqrt5}{12}=\sqrt5$。"),
  ("AI を求める",r"I から A 側の接点への半径は接線に垂直なので、△（A、接点、I）は直角三角形。 $$AI^2=x^2+r^2=16+5=21\ \Rightarrow\ AI=\sqrt{21}$$")],
 r"x=4,\ y=3,\ z=5,\quad r=\sqrt5,\quad AI=\sqrt{21}",
 [r"$AB=5,\ BC=6,\ CA=5$ のときの接線の長さ $x,y,z$、$r$、AI",r"$AB=13,\ BC=14,\ CA=15$ のときの接線の長さ $x,y,z$、$r$、AI",r"$AB=6,\ BC=7,\ CA=5$ のときの接線の長さ $x,y,z$、$r$、AI"],
 [(r"$x+y+z=8$：$z=3,\ x=2,\ y=3$。$s=8$、$S=\sqrt{8\cdot3\cdot2\cdot3}=12$、$r=\dfrac{12}8=\dfrac32$。$AI^2=4+\dfrac94=\dfrac{25}4$、$AI=\dfrac52$。",r"x=2,y=3,z=3,\ r=\dfrac32,\ AI=\dfrac52"),
  (r"$x+y+z=21$：$z=8,\ x=7,\ y=6$。$S=\sqrt{21\cdot8\cdot7\cdot6}=84$、$r=\dfrac{84}{21}=4$。$AI^2=49+16=65$、$AI=\sqrt{65}$。",r"x=7,y=6,z=8,\ r=4,\ AI=\sqrt{65}"),
  (r"$x+y+z=9$：$z=3,\ x=2,\ y=4$。$S=\sqrt{9\cdot3\cdot2\cdot4}=\sqrt{216}=6\sqrt6$、$r=\dfrac{6\sqrt6}9=\dfrac{2\sqrt6}3$。$AI^2=4+\dfrac{24}9=\dfrac{20}3$、$AI=\dfrac{2\sqrt{15}}3$。",r"x=2,y=4,z=3,\ r=\dfrac{2\sqrt6}3,\ AI=\dfrac{2\sqrt{15}}3")],fig=f5)

# ===== 章末 =====
for pa,ab,pc in ((5,3,4),): assert pa*(pa+ab)==pc*10
Z.ch(r"円外の点 P から引いた2本の割線が円と A、B（$PA=5,\ AB=3$）と C、D で交わる。$PC=4$ のとき CD と、P から引いた接線の長さを求めよ。",
 r"$PB=8$、$5\cdot8=4\cdot PD\Rightarrow PD=10$、$CD=6$。$PT^2=40\Rightarrow PT=2\sqrt{10}$。",r"CD=6,\ PT=2\sqrt{10}",1)
A,B,C,D=cyc4(38,47)
Z.ch(r"円周上の4点 A、B、C、D がこの順にあり $\angle ADB=38^\circ,\ \angle BAC=47^\circ$。$\angle ACB,\ \angle ABC,\ \angle ADC$ を求めよ。",
 r"$\angle ACB=38^\circ$、$\angle ABC=180^\circ-47^\circ-38^\circ=95^\circ$、$\angle ADC=180^\circ-95^\circ=85^\circ$。",r"38^\circ,\ 95^\circ,\ 85^\circ",2)
Z.ch(r"点 A での接線上に T、S をとり、$\angle TAB=58^\circ,\ \angle SAC=64^\circ$（B は T 側、C は S 側）。$\angle ACB,\ \angle ABC,\ \angle BAC$ を求めよ。",
 r"$\angle ACB=58^\circ$、$\angle ABC=64^\circ$、$\angle BAC=180^\circ-58^\circ-64^\circ=58^\circ$。",r"58^\circ,\ 64^\circ,\ 58^\circ",3)
Z.ch(r"半径 7 と半径 3 の2円（離れている）、中心間距離 12 のとき、共通外接線と共通内接線の長さを求めよ。",
 r"外接線：$12^2-(7-3)^2=144-16=128$ → $8\sqrt2$。内接線：$12^2-(7+3)^2=144-100=44$ → $2\sqrt{11}$。",r"8\sqrt2,\ 2\sqrt{11}",4)
Z.ch(r"$AB=8,\ BC=10,\ CA=12$ の △ABC の内接円について、各頂点から接点までの長さ $x,y,z$（A、B、C の順）と半径 $r$ を求めよ。",
 r"$x+y+z=15$：$z=15-8=7,\ x=15-10=5,\ y=15-12=3$。$s=15$、$S=\sqrt{15\cdot5\cdot3\cdot7}=\sqrt{1575}=15\sqrt7$、$r=\dfrac{15\sqrt7}{15}=\sqrt7$。",r"x=5,y=3,z=7,\ r=\sqrt7",5)
UNIT=Z.unit(0,1,"図形の性質","円の性質","方べきの定理、円周角と内接四角形、接弦定理、共通接線の長さ、内接円と接線の長さなど、円の性質の難問に挑みます。")
