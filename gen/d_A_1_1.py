# -*- coding: utf-8 -*-
# 三角形の性質（数学A 図形の性質）
from ah import *
import math, itertools
from fractions import Fraction as Fr
Z=U_()
def tp(a,b,c):  # B=(0,0),C=(a,0), AB=c, AC=b
    cb=(c*c+a*a-b*b)/(2*c*a); return (c*cb,c*math.sqrt(1-cb*cb)),cb
def dist(p,q): return math.hypot(p[0]-q[0],p[1]-q[1])

# ===== 例題1 角の二等分線の長さ =====
A_,cb=tp(5,4,6); D_=(3,0)
f1=geo("a11_e1",polys=[([(0,0),(5,0),A_],"#333")],segs=[(A_[0],A_[1],3,0,"#b81f36","-")],
 pts=[("B",0,0,-0.25,-0.2),("C",5,0,0.25,-0.2),("A",A_[0],A_[1],0.1,0.3),("D",3,0,0,-0.35)],texts=[(1.5,-0.9,"BD=3，DC=2","#b81f36"),(1.5,1.4,"6","#555"),(4.9,2.0,"4","#555")],w=42,size=(3.8,3.0),lim=(-0.8,5.8,-1.2,4.6))
for (a,b,c),exp in (((5,4,6),(3,2,math.sqrt(18))),((7,6,8),(4,3,6)),((10,6,9),(6,4,math.sqrt(30))),((8,6,10),(5,3,math.sqrt(45)))):
    Ap,_=tp(a,b,c); bd=a*c/(b+c); Dp=(bd,0); close(dist(Dp,(a,0))*c,bd*b); close(dist(Ap,Dp),exp[2]); close(bd,exp[0])
Z.ex("角の二等分線の長さ",
 r"△ABC で $AB=6,\ AC=4,\ BC=5$ とする。$\angle A$ の二等分線が辺 BC と交わる点を D とするとき、BD、DC、線分 AD の長さを求めよ。",
 r"<p>まず<b>角の二等分線の定理</b>「$BD:DC=AB:AC$」で BD、DC を求める。AD は、<b>余弦定理を2回</b>使う（△ABC で $\cos B$、次に △ABD で AD）。</p>",
 "二等分線は、向かい合う辺を「となりの2辺の比」に分ける。長さは、角 B を共通にもつ2つの三角形で余弦定理。",
 [("BD、DC を求める",r"$BD:DC=AB:AC=6:4=3:2$。$BC=5$ より $$BD=5\times\dfrac35=3,\qquad DC=5\times\dfrac25=2$$"),
  (r"$\cos B$ を求める（△ABC）",r"$$\cos B=\dfrac{AB^2+BC^2-AC^2}{2\cdot AB\cdot BC}=\dfrac{36+25-16}{2\cdot6\cdot5}=\dfrac{45}{60}=\dfrac34$$"),
  ("AD を求める（△ABD）",r"$$\begin{aligned}AD^2&=AB^2+BD^2-2\cdot AB\cdot BD\cos B\\ &=36+9-2\cdot6\cdot3\cdot\dfrac34\\ &=45-27=18\end{aligned}$$ よって $AD=\sqrt{18}=3\sqrt2$。"),
  ("確かめる",r"公式 $AD^2=AB\cdot AC-BD\cdot DC$ に入れると $6\cdot4-3\cdot2=18$ で一致。")],
 r"BD=3,\quad DC=2,\quad AD=3\sqrt2",
 [r"$AB=8,\ AC=6,\ BC=7$ のときの BD、DC、AD",r"$AB=9,\ AC=6,\ BC=10$ のときの BD、DC、AD",r"$AB=10,\ AC=6,\ BC=8$ のときの BD、DC、AD"],
 [(r"$BD=7\cdot\dfrac{8}{14}=4$、$DC=3$。$\cos B=\dfrac{64+49-36}{2\cdot8\cdot7}=\dfrac{77}{112}=\dfrac{11}{16}$。$$AD^2=64+16-2\cdot8\cdot4\cdot\dfrac{11}{16}=80-44=36\ \Rightarrow\ AD=6$$",r"BD=4,\ DC=3,\ AD=6"),
  (r"$BD=10\cdot\dfrac{9}{15}=6$、$DC=4$。$\cos B=\dfrac{81+100-36}{2\cdot9\cdot10}=\dfrac{145}{180}=\dfrac{29}{36}$。$$AD^2=81+36-2\cdot9\cdot6\cdot\dfrac{29}{36}=117-87=30\ \Rightarrow\ AD=\sqrt{30}$$",r"BD=6,\ DC=4,\ AD=\sqrt{30}"),
  (r"$BD=8\cdot\dfrac{10}{16}=5$、$DC=3$。$\cos B=\dfrac{100+64-36}{2\cdot10\cdot8}=\dfrac{128}{160}=\dfrac45$。$$AD^2=100+25-2\cdot10\cdot5\cdot\dfrac45=125-80=45\ \Rightarrow\ AD=3\sqrt5$$",r"BD=5,\ DC=3,\ AD=3\sqrt5")],fig=f1)

# ===== 例題2 メネラウスの定理 =====
def pts_P(adb,aec):
    A=np.array([1.0,5.0]);B=np.array([0.0,0.0]);C=np.array([6.0,0.0])
    D=A+(adb[0]/(adb[0]+adb[1]))*(B-A); E=A+(aec[0]/(aec[0]+aec[1]))*(C-A)
    # P = B+t(E-B) = C+s(D-C)
    M=np.array([E-B,-(D-C)]).T; t,s=np.linalg.solve(M,C-B)
    P=B+t*(E-B); cr=lambda u,v:u[0]*v[1]-u[1]*v[0]; areaPBC=abs(cr(B-P,C-P))/2; areaABC=abs(cr(B-A,C-A))/2
    return t/(1-t),areaPBC/areaABC,(A,B,C,D,E,P)
for adb,aec,bp,ar in (((2,3),(3,1),Fr(6),Fr(3,14)),((1,2),(2,1),Fr(6),Fr(2,7)),((3,1),(1,1),Fr(2,3),Fr(1,5)),((1,3),(3,2),Fr(15,2),Fr(6,17))):
    r,a,_=pts_P(adb,aec); close(r,float(bp)); close(a,float(ar))
(_,_,(A,B,C,D,E,P))=pts_P((2,3),(3,1))
f2=geo("a11_e2",polys=[([tuple(B),tuple(C),tuple(A)],"#333")],segs=[(B[0],B[1],E[0],E[1],"#b81f36","-"),(C[0],C[1],D[0],D[1],"#b81f36","-")],
 pts=[("A",A[0],A[1],0,0.35),("B",B[0],B[1],-0.3,-0.25),("C",C[0],C[1],0.3,-0.25),("D",D[0],D[1],-0.3,0),("E",E[0],E[1],0.3,0.1),("P",P[0],P[1],0.05,-0.4)],w=42,size=(3.8,3.2),lim=(-0.8,6.8,-0.8,5.8))
Z.ex("メネラウスの定理で比と面積比を求める",
 r"△ABC で、辺 AB 上に点 D を $AD:DB=2:3$、辺 AC 上に点 E を $AE:EC=3:1$ となるようにとる。BE と CD の交点を P とするとき、$BP:PE$ と、$\triangle PBC:\triangle ABC$ を求めよ。",
 r"<p>図に<b>1本の直線が三角形の辺（またはその延長）を3か所で切っている</b>形を見つけて、<b>メネラウスの定理</b>を使う。</p>$$\dfrac{(\text{頂点→交点})}{(\text{交点→頂点})}\times\cdots=1\quad(\text{三角形のまわりを1周する形で})$$<p>ここでは △ABE を直線 DPC が切っている。面積比は、底辺または高さの比に直す。</p>",
 "メネラウスは「三角形を1周しながら、比を順に掛けると1」。1周のコースを決めてから掛ける。",
 [("メネラウスを使う三角形と直線を決める",r"△ABE と直線 D-P-C。直線は AB 上の D、BE 上の P、EA の延長上の C を通る。"),
  ("比を1周掛ける",r"A→D→B→P→E→C→A の順に $$\dfrac{AD}{DB}\cdot\dfrac{BP}{PE}\cdot\dfrac{EC}{CA}=1$$ $AE:EC=3:1$ より $EC:CA=1:4$。よって $$\dfrac23\cdot\dfrac{BP}{PE}\cdot\dfrac14=1\ \Rightarrow\ \dfrac{BP}{PE}=1\times\dfrac32\times4=6$$ すなわち $BP:PE=6:1$。"),
  ("面積比を出す（△EBC）",r"高さが同じ辺の比で面積比が決まる。$\triangle EBC:\triangle ABC=EC:AC=1:4$ なので $\triangle EBC=\dfrac14\triangle ABC$。"),
  ("面積比を出す（△PBC）",r"$\triangle PBC:\triangle EBC=BP:BE=6:7$。 $$\triangle PBC=\dfrac67\times\dfrac14\triangle ABC=\dfrac{3}{14}\triangle ABC$$")],
 r"BP:PE=6:1,\quad \triangle PBC:\triangle ABC=3:14",
 [r"$AD:DB=1:2,\ AE:EC=2:1$ のときの $BP:PE$ と $\triangle PBC:\triangle ABC$",r"$AD:DB=3:1,\ AE:EC=1:1$ のときの $BP:PE$ と $\triangle PBC:\triangle ABC$",r"$AD:DB=1:3,\ AE:EC=3:2$ のときの $BP:PE$ と $\triangle PBC:\triangle ABC$"],
 [(r"$EC:CA=1:3$。$$\dfrac12\cdot\dfrac{BP}{PE}\cdot\dfrac13=1\Rightarrow\dfrac{BP}{PE}=6$$ $\triangle EBC=\dfrac13\triangle ABC$、$\triangle PBC=\dfrac67\cdot\dfrac13=\dfrac27$。",r"BP:PE=6:1,\ 2:7"),
  (r"$EC:CA=1:2$。$$3\cdot\dfrac{BP}{PE}\cdot\dfrac12=1\Rightarrow\dfrac{BP}{PE}=\dfrac23$$ $BP:PE=2:3$、$\triangle EBC=\dfrac12\triangle ABC$、$\triangle PBC=\dfrac25\cdot\dfrac12=\dfrac15$。",r"BP:PE=2:3,\ 1:5"),
  (r"$EC:CA=2:5$。$$\dfrac13\cdot\dfrac{BP}{PE}\cdot\dfrac25=1\Rightarrow\dfrac{BP}{PE}=\dfrac{15}2$$ $BP:PE=15:2$、$\triangle EBC=\dfrac25\triangle ABC$、$\triangle PBC=\dfrac{15}{17}\cdot\dfrac25=\dfrac6{17}$。",r"BP:PE=15:2,\ 6:17")],fig=f2)

# ===== 例題3 内心・外心・垂心 =====
def ang(P,Q,R):
    v=np.array(P)-np.array(Q); w=np.array(R)-np.array(Q); return math.degrees(math.acos(v@w/np.linalg.norm(v)/np.linalg.norm(w)))
def centers(A_,B_,C_):  # 角度(度)から三角形を作り内心・外心・垂心を求める
    a,b,c=[math.radians(x) for x in (A_,B_,C_)]
    B=np.array([0.0,0.0]); C=np.array([math.sin(a),0.0])*1; 
    R=0.5; # 外接円半径=0.5→a=sinA
    Cc=np.array([math.sin(a),0.0]); Ap=np.array([math.sin(c)*math.cos(b),math.sin(c)*math.sin(b)])
    Bp=np.array([0.0,0.0])
    la,lb,lc=dist(Bp,Cc),dist(Cc,Ap),dist(Ap,Bp)
    I=(la*Ap+lb*Bp+lc*Cc)/(la+lb+lc)
    # 外心
    def circ(p,q,r):
        ax,ay=p;bx,by=q;cx,cy=r;d=2*(ax*(by-cy)+bx*(cy-ay)+cx*(ay-by))
        ux=((ax*ax+ay*ay)*(by-cy)+(bx*bx+by*by)*(cy-ay)+(cx*cx+cy*cy)*(ay-by))/d
        uy=((ax*ax+ay*ay)*(cx-bx)+(bx*bx+by*by)*(ax-cx)+(cx*cx+cy*cy)*(bx-ax))/d
        return np.array([ux,uy])
    O=circ(Ap,Bp,Cc); H=Ap+Bp+Cc-2*O
    return Ap,Bp,Cc,I,O,H
for A_,B_,C_,bi,bo,bh in ((50,60,70,115,100,130),(40,70,70,110,80,140),(64,58,58,122,128,116),(80,50,50,130,160,100)):
    Ap,Bp,Cc,I_,O_,H_=centers(A_,B_,C_); close(ang(Bp,I_,Cc),bi,1e-7); close(ang(Bp,O_,Cc),bo,1e-7); close(ang(Bp,H_,Cc),bh,1e-7)
Ap,Bp,Cc,I_,O_,H_=centers(50,60,70)
f3=geo("a11_e3",polys=[([tuple(Bp),tuple(Cc),tuple(Ap)],"#333")],segs=[(Bp[0],Bp[1],I_[0],I_[1],"#2a7fd0","-"),(Cc[0],Cc[1],I_[0],I_[1],"#2a7fd0","-"),(Bp[0],Bp[1],O_[0],O_[1],"#2a9d6a","-"),(Cc[0],Cc[1],O_[0],O_[1],"#2a9d6a","-"),(Bp[0],Bp[1],H_[0],H_[1],"#b81f36","-"),(Cc[0],Cc[1],H_[0],H_[1],"#b81f36","-")],
 pts=[("A",Ap[0],Ap[1],0,0.06),("B",Bp[0],Bp[1],-0.06,-0.05),("C",Cc[0],Cc[1],0.06,-0.05),("I",I_[0],I_[1],0.05,-0.06),("O",O_[0],O_[1],0.06,0.04),("H",H_[0],H_[1],-0.06,0.04)],w=40,size=(3.6,3.2),lim=(-0.2,1.0,-0.2,0.8))
Z.ex("内心・外心・垂心のつくる角",
 r"鋭角三角形 ABC で $\angle A=50^\circ,\ \angle B=60^\circ,\ \angle C=70^\circ$ とする。内心を I、外心を O、垂心を H とするとき、$\angle BIC,\ \angle BOC,\ \angle BHC$ を求めよ。",
 r"<ul><li><b>内心</b>：角の二等分線の交点 → $\angle IBC=\dfrac B2,\ \angle ICB=\dfrac C2$。</li><li><b>外心</b>：垂直二等分線の交点 → <b>円周角の定理</b>（中心角は円周角の2倍）。</li><li><b>垂心</b>：頂点から対辺への垂線の交点 → 直角2つを使った四角形の内角和。</li></ul>",
 "3つの「中心」はそれぞれ使う道具が違う。二等分・円周角・垂直（直角）の3つ。",
 [(r"$\angle BIC$（内心）",r"I は内心なので $\angle IBC=\dfrac{60^\circ}2=30^\circ,\ \angle ICB=\dfrac{70^\circ}2=35^\circ$。 $$\angle BIC=180^\circ-30^\circ-35^\circ=115^\circ$$"),
  (r"$\angle BOC$（外心）",r"O は外接円の中心。弧 BC に対する中心角は円周角 $\angle A$ の2倍（鋭角三角形）。 $$\angle BOC=2\angle A=100^\circ$$"),
  (r"$\angle BHC$（垂心）",r"B から AC への垂線の足を E、C から AB への垂線の足を F とすると、H は BE と CF の交点。四角形 AFHE で $\angle AFH=\angle AEH=90^\circ$ なので $$\angle FHE=360^\circ-90^\circ-90^\circ-50^\circ=130^\circ$$ $\angle BHC$ は $\angle FHE$ と対頂角なので $130^\circ$。")],
 r"\angle BIC=115^\circ,\quad \angle BOC=100^\circ,\quad \angle BHC=130^\circ",
 [r"鋭角三角形 ABC で $\angle A=40^\circ,\ \angle B=70^\circ,\ \angle C=70^\circ$ のときの $\angle BIC,\ \angle BOC,\ \angle BHC$",r"鋭角三角形 ABC で $\angle A=64^\circ,\ \angle B=58^\circ,\ \angle C=58^\circ$ のときの $\angle BIC,\ \angle BOC,\ \angle BHC$",r"鋭角三角形 ABC で $\angle A=80^\circ,\ \angle B=50^\circ,\ \angle C=50^\circ$ のときの $\angle BIC,\ \angle BOC,\ \angle BHC$"],
 [(r"$\angle BIC=180^\circ-35^\circ-35^\circ=110^\circ$。$\angle BOC=2\cdot40^\circ=80^\circ$。$\angle BHC=360^\circ-90^\circ-90^\circ-40^\circ=140^\circ$。",r"110^\circ,\ 80^\circ,\ 140^\circ"),
  (r"$\angle BIC=180^\circ-29^\circ-29^\circ=122^\circ$。$\angle BOC=2\cdot64^\circ=128^\circ$。$\angle BHC=360^\circ-180^\circ-64^\circ=116^\circ$。",r"122^\circ,\ 128^\circ,\ 116^\circ"),
  (r"$\angle BIC=180^\circ-25^\circ-25^\circ=130^\circ$。$\angle BOC=2\cdot80^\circ=160^\circ$。$\angle BHC=360^\circ-180^\circ-80^\circ=100^\circ$。",r"130^\circ,\ 160^\circ,\ 100^\circ")],fig=f3)

# ===== 例題4 中線定理と重心 =====
def med2(a,b,c): return (2*b*b+2*c*c-a*a)/4  # 中線^2 (a=対辺)
for (AB,AC,BC),(am,ag,sg) in (((7,9,8),(7,Fr(14,3),Fr(194,3))),((6,8,10),(5,Fr(10,3),Fr(200,3))),((5,5,6),(4,Fr(8,3),Fr(86,3))),((10,10,12),(8,Fr(16,3),Fr(344,3)))):
    close(math.sqrt(med2(BC,AC,AB)),am)
    GA2=Fr(4,9)*Fr(med2(BC,AC,AB)).limit_denominator(100); GB2=Fr(4,9)*Fr(med2(AC,AB,BC)).limit_denominator(100); GC2=Fr(4,9)*Fr(med2(AB,AC,BC)).limit_denominator(100)
    assert GA2+GB2+GC2==sg==Fr(AB**2+AC**2+BC**2,3)
    close(float(Fr(2,3)*am),float(ag))
Z.ex("中線定理と重心",
 r"△ABC で $AB=7,\ AC=9,\ BC=8$ とし、辺 BC の中点を M、重心を G とする。中線 AM、線分 AG の長さと、$GA^2+GB^2+GC^2$ の値を求めよ。",
 r"<p><b>中線定理</b>：$AB^2+AC^2=2(AM^2+BM^2)$（M は BC の中点）。<b>重心 G は中線を頂点側から $2:1$ に分ける</b>ので $AG=\dfrac23AM$。他の2本の中線も同じ定理で求める。</p>",
 "中線定理は、余弦定理を2回使って出る公式。「2辺の2乗の和＝2×（中線の2乗＋半辺の2乗）」。",
 [("AM を求める（中線定理）",r"$BM=4$ なので $$49+81=2(AM^2+16)\ \Rightarrow\ AM^2=65-16=49\ \Rightarrow\ AM=7$$"),
  ("AG を求める（重心は 2:1）",r"$$AG=\dfrac23AM=\dfrac{14}3$$ よって $GA^2=\dfrac{196}9$。"),
  ("他の中線を求める",r"AC の中点への中線 $BN$：$AB^2+BC^2=2(BN^2+(\tfrac92)^2)$ より $$49+64=2BN^2+\dfrac{81}2\ \Rightarrow\ BN^2=\dfrac{145}4$$ $GB=\dfrac23BN$ なので $GB^2=\dfrac49\cdot\dfrac{145}4=\dfrac{145}9$。<br>AB の中点への中線 $CL$：$AC^2+BC^2=2(CL^2+(\tfrac72)^2)$ より $$81+64=2CL^2+\dfrac{49}2\ \Rightarrow\ CL^2=\dfrac{241}4$$ $GC^2=\dfrac49\cdot\dfrac{241}4=\dfrac{241}9$。"),
  ("和を求める",r"$$GA^2+GB^2+GC^2=\dfrac{196+145+241}9=\dfrac{582}9=\dfrac{194}3$$ これは $\dfrac{AB^2+BC^2+CA^2}3=\dfrac{49+64+81}3$ と一致する。")],
 r"AM=7,\quad AG=\dfrac{14}3,\quad GA^2+GB^2+GC^2=\dfrac{194}3",
 [r"$AB=6,\ AC=8,\ BC=10$ のときの AM、AG、$GA^2+GB^2+GC^2$",r"$AB=5,\ AC=5,\ BC=6$ のときの AM、AG、$GA^2+GB^2+GC^2$",r"$AB=10,\ AC=10,\ BC=12$ のときの AM、AG、$GA^2+GB^2+GC^2$"],
 [(r"$BM=5$：$36+64=2(AM^2+25)\Rightarrow AM^2=25,\ AM=5$。$AG=\dfrac{10}3$。$$GA^2+GB^2+GC^2=\dfrac{36+100+64}3=\dfrac{200}3$$",r"AM=5,\ AG=\dfrac{10}3,\ \dfrac{200}3"),
  (r"$BM=3$：$25+25=2(AM^2+9)\Rightarrow AM^2=16,\ AM=4$。$AG=\dfrac83$。$$GA^2+GB^2+GC^2=\dfrac{25+36+25}3=\dfrac{86}3$$",r"AM=4,\ AG=\dfrac83,\ \dfrac{86}3"),
  (r"$BM=6$：$100+100=2(AM^2+36)\Rightarrow AM^2=64,\ AM=8$。$AG=\dfrac{16}3$。$$GA^2+GB^2+GC^2=\dfrac{100+144+100}3=\dfrac{344}3$$",r"AM=8,\ AG=\dfrac{16}3,\ \dfrac{344}3")])

# ===== 例題5 外角の二等分線 =====
for (a,b,c),(ce,ae2,de) in (((5,4,6),(10,126,12)),((6,4,8),(6,40,8)),((5,6,9),(10,96,12)),((7,6,8),(21,540,24))):
    Ap,_=tp(a,b,c); k=c/b  # BE:EC=c:b
    ce_=a*b/(c-b) if c>b else None
    close(ce_,ce); E_=(a+ce_,0); close(dist(Ap,E_)**2,ae2,1e-7); bd=a*c/(b+c); close(E_[0]-bd,de)
    close(dist(Ap,(bd,0))**2+ae2,de*de,1e-7)
A_,_=tp(5,4,6)
f5=geo("a11_e5",polys=[([(0,0),(5,0),A_],"#333")],segs=[(5,0,15,0,"#333","-"),(A_[0],A_[1],3,0,"#b81f36","-"),(A_[0],A_[1],15,0,"#2a7fd0","-")],
 pts=[("B",0,0,-0.4,-0.3),("C",5,0,0,-0.45),("D",3,0,0,-0.45),("E",15,0,0.4,-0.3),("A",A_[0],A_[1],0,0.5)],w=60,size=(5.4,2.6),lim=(-1,16.5,-1.2,5))
Z.ex("外角の二等分線と線分の長さ",
 r"△ABC で $AB=6,\ AC=4,\ BC=5$ とする。$\angle A$ の外角の二等分線が直線 BC と交わる点を E とするとき、CE、AE の長さを求めよ。さらに、$\angle A$ の内角の二等分線と BC の交点 D について DE を求めよ。",
 r"<p><b>外角の二等分線の定理</b>：$BE:EC=AB:AC$（外分）。AB＞AC なので E は C の側の延長上にある。AE は △ABE で余弦定理。D、E ともに二等分線なので $\angle DAE=90^\circ$ になることも使える。</p>",
 "内角の二等分線は辺を内側で、外角の二等分線は外側で、同じ比 AB:AC に分ける。この2本は直角に交わる。",
 [("CE を求める",r"$BE:EC=6:4=3:2$。E は C の延長上なので $BE=BC+CE=5+CE$。 $$(5+CE):CE=3:2\ \Rightarrow\ 2(5+CE)=3\,CE\ \Rightarrow\ CE=10$$ よって $BE=15$。"),
  (r"$\cos B$ を求める",r"$$\cos B=\dfrac{36+25-16}{2\cdot6\cdot5}=\dfrac{45}{60}=\dfrac34$$"),
  ("AE を求める（△ABE）",r"$$\begin{aligned}AE^2&=AB^2+BE^2-2\cdot AB\cdot BE\cos B\\ &=36+225-2\cdot6\cdot15\cdot\dfrac34\\ &=261-135=126\end{aligned}$$ $AE=\sqrt{126}=3\sqrt{14}$。"),
  ("DE を求める",r"$BD=3$（例題1）。$DE=BE-BD=15-3=12$。確かめ：$\angle DAE=90^\circ$ なので $AD^2+AE^2=18+126=144=12^2$ で一致。")],
 r"CE=10,\quad AE=3\sqrt{14},\quad DE=12",
 [r"$AB=8,\ AC=4,\ BC=6$ のときの CE、AE、DE",r"$AB=9,\ AC=6,\ BC=5$ のときの CE、AE、DE",r"$AB=8,\ AC=6,\ BC=7$ のときの CE、AE、DE"],
 [(r"$BE:EC=2:1$：$(6+CE):CE=2:1\Rightarrow CE=6$、$BE=12$。$\cos B=\dfrac{64+36-16}{2\cdot8\cdot6}=\dfrac78$。$$AE^2=64+144-2\cdot8\cdot12\cdot\dfrac78=208-168=40$$ $BD=4$、$DE=12-4=8$。",r"CE=6,\ AE=2\sqrt{10},\ DE=8"),
  (r"$BE:EC=3:2$：$(5+CE):CE=3:2\Rightarrow CE=10$、$BE=15$。$\cos B=\dfrac{81+25-36}{2\cdot9\cdot5}=\dfrac79$。$$AE^2=81+225-2\cdot9\cdot15\cdot\dfrac79=306-210=96$$ $BD=\dfrac{9}{15}\cdot5=3$、$DE=15-3=12$。",r"CE=10,\ AE=4\sqrt6,\ DE=12"),
  (r"$BE:EC=4:3$：$(7+CE):CE=4:3\Rightarrow CE=21$、$BE=28$。$\cos B=\dfrac{64+49-36}{2\cdot8\cdot7}=\dfrac{11}{16}$。$$AE^2=64+784-2\cdot8\cdot28\cdot\dfrac{11}{16}=848-308=540$$ $BD=\dfrac{8}{14}\cdot7=4$、$DE=28-4=24$。",r"CE=21,\ AE=6\sqrt{15},\ DE=24")],fig=f5)

# ===== 章末 =====
Z.ch(r"△ABC で $AB=12,\ AC=8,\ BC=10$。$\angle A$ の二等分線が BC と交わる点 D について BD と AD を求めよ。",
 r"$BD=10\cdot\dfrac{12}{20}=6$、$DC=4$。$\cos B=\dfrac{144+100-64}{2\cdot12\cdot10}=\dfrac{180}{240}=\dfrac34$。$$AD^2=144+36-2\cdot12\cdot6\cdot\dfrac34=180-108=72\ \Rightarrow\ AD=6\sqrt2$$",r"BD=6,\ AD=6\sqrt2",1)
Z.ch(r"△ABC で $AD:DB=3:2$、$AE:EC=1:2$（D は AB 上、E は AC 上）。BE と CD の交点を P とするとき、$BP:PE$ を求めよ。",
 r"△ABE と直線 D-P-C：$\dfrac{AD}{DB}\cdot\dfrac{BP}{PE}\cdot\dfrac{EC}{CA}=1$。$EC:CA=2:3$。$$\dfrac32\cdot\dfrac{BP}{PE}\cdot\dfrac23=1\ \Rightarrow\ \dfrac{BP}{PE}=1$$",r"BP:PE=1:1",2)
Z.ch(r"鋭角三角形 ABC で $\angle A=72^\circ,\ \angle B=54^\circ,\ \angle C=54^\circ$。内心 I、外心 O、垂心 H について $\angle BIC,\ \angle BOC,\ \angle BHC$ を求めよ。",
 r"$\angle BIC=180^\circ-27^\circ-27^\circ=126^\circ$。$\angle BOC=2\cdot72^\circ=144^\circ$。$\angle BHC=360^\circ-180^\circ-72^\circ=108^\circ$。",r"126^\circ,\ 144^\circ,\ 108^\circ",3)
Z.ch(r"△ABC で $AB=9,\ AC=11,\ BC=8$ とする。BC の中点を M、重心を G とするとき、AM と AG を求めよ。",
 r"$BM=4$：$81+121=2(AM^2+16)\Rightarrow AM^2=101-16=85$。$AM=\sqrt{85}$、$AG=\dfrac23\sqrt{85}$。",r"AM=\sqrt{85},\ AG=\dfrac{2\sqrt{85}}3",4)
Z.ch(r"△ABC で $AB=10,\ AC=5,\ BC=6$。$\angle A$ の外角の二等分線が直線 BC と交わる点を E とするとき、CE と AE を求めよ。",
 r"$BE:EC=2:1$：$(6+CE):CE=2:1\Rightarrow CE=6$、$BE=12$。$\cos B=\dfrac{100+36-25}{2\cdot10\cdot6}=\dfrac{111}{120}=\dfrac{37}{40}$。$$AE^2=100+144-2\cdot10\cdot12\cdot\dfrac{37}{40}=244-222=22\ \Rightarrow\ AE=\sqrt{22}$$",r"CE=6,\ AE=\sqrt{22}",5)
tt=tp(6,5,10); close(dist(tt[0],(12,0)),math.sqrt(22),1e-7)
a,b,c=6,5,10; bd=a*c/(b+c)
UNIT=Z.unit(0,0,"図形の性質","三角形の性質","角の二等分線、メネラウスの定理、内心・外心・垂心、中線定理と重心、外角の二等分線など、三角形の性質の難問に挑みます。")
