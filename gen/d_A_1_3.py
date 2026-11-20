# -*- coding: utf-8 -*-
# 作図・空間図形（数学A 図形の性質）
from ah import *
import math, itertools
from fractions import Fraction as Fr
Z=U_()
V3={"A":(0,0,0),"B":(1,0,0),"C":(1,1,0),"D":(0,1,0),"E":(0,0,1),"F":(1,0,1),"G":(1,1,1),"H":(0,1,1)}
def cub(name,a,b,c,hl=(),w=40,size=(3.6,3.0)):
    def fn(ax):
        s=1.0
        def P(v): return (v[0]*a+0.55*v[1]*b,v[2]*c+0.35*v[1]*b)
        hid=[("A","D"),("D","C"),("D","H")]
        for u,v in [("A","B"),("B","C"),("C","D"),("D","A"),("E","F"),("F","G"),("G","H"),("H","E"),("A","E"),("B","F"),("C","G"),("D","H")]:
            p,q=P(V3[u]),P(V3[v]); ax.plot([p[0],q[0]],[p[1],q[1]],color="#555",lw=1.2,ls="--" if (u,v) in hid else "-")
        for u,v,col in hl:
            p,q=P(V3[u]),P(V3[v]); ax.plot([p[0],q[0]],[p[1],q[1]],color=col,lw=2.4)
        for k,v in V3.items():
            p=P(v); ax.text(p[0]+(-0.18 if k in "AEDH" else 0.18)*max(a,b,c)*0.25,p[1]+(-0.2 if k in "ABCD" else 0.15)*max(a,b,c)*0.25,k,fontsize=12,ha="center",va="center")
        ax.set_aspect("equal"); ax.axis("off")
    make_fig(name,fn,size=size); return img(name,w)
def vec(u,v,a,b,c): 
    k=lambda p:(V3[p][0]*a,V3[p][1]*b,V3[p][2]*c)
    return np.array(k(v))-np.array(k(u))
def cosang(u,v): return abs(u@v)/np.linalg.norm(u)/np.linalg.norm(v)

# ===== 例題1 オイラーの多面体定理 =====
def euler(m,k):   # 面は正m角形、各頂点にk面
    E=sp.symbols('E'); 
    # V=2E/k, F=2E/m, V-E+F=2
    Ev=Fr(2)/(Fr(2,k)-1+Fr(2,m)); return Ev,2*Ev/k,2*Ev/m
import sympy as sp
for (m,k),(Ev,V,F) in (((3,5),(30,12,20)),((5,3),(30,20,12)),((3,4),(12,6,8)),((3,3),(6,4,4)),((4,3),(12,8,6))):
    assert euler(m,k)==(Ev,V,F) and V-Ev+F==2
assert 3*8+4*6==48 and Fr(48,2)==24 and Fr(2*24,4)==12 and 12-24+14==2
Z.ex("オイラーの多面体定理で頂点・辺・面の数を求める",
 r"凸多面体で、すべての面が正三角形であり、どの頂点にも5つの面が集まっている。この多面体の頂点の数 $V$、辺の数 $E$、面の数 $F$ を求めよ。また、すべての面が正五角形で、どの頂点にも3つの面が集まっている場合も求めよ。",
 r"<p><b>オイラーの多面体定理</b>：凸多面体では $V-E+F=2$。</p><p>数え上げの関係を2つ作る。<br>・各面は $m$ 角形：辺は2つの面に共有されるので $mF=2E$。<br>・各頂点に $k$ 面（辺も $k$ 本）：$kV=2E$。<br>これを $V-E+F=2$ に代入して $E$ を出す。</p>",
 "辺は『面と面の境目』なので、面ごとに辺を数えると、同じ辺を2回数える。だから『面の辺の数の合計＝2E』。",
 [("関係式を作る（正三角形・各頂点に5面）",r"各面は正三角形なので $3F=2E$。各頂点に5面（5本の辺）なので $5V=2E$。 $$F=\dfrac{2E}3,\qquad V=\dfrac{2E}5$$"),
  ("オイラーの定理に代入",r"$$V-E+F=2\ \Rightarrow\ \dfrac{2E}5-E+\dfrac{2E}3=2$$ 通分して（分母15） $$\dfrac{6E-15E+10E}{15}=\dfrac E{15}=2\ \Rightarrow\ E=30$$ よって $V=\dfrac{2\cdot30}5=12,\ F=\dfrac{2\cdot30}3=20$（正二十面体）。"),
  ("関係式を作る（正五角形・各頂点に3面）",r"$5F=2E,\ 3V=2E$ より $F=\dfrac{2E}5,\ V=\dfrac{2E}3$。"),
  ("オイラーの定理に代入",r"$$\dfrac{2E}3-E+\dfrac{2E}5=2\ \Rightarrow\ \dfrac{10E-15E+6E}{15}=\dfrac E{15}=2\ \Rightarrow\ E=30$$ よって $V=20,\ F=12$（正十二面体）。")],
 r"\begin{aligned}&\text{正三角形・5面：}V=12,\ E=30,\ F=20\\ &\text{正五角形・3面：}V=20,\ E=30,\ F=12\end{aligned}",
 [r"すべての面が正三角形で、どの頂点にも4つの面が集まる凸多面体の $V,E,F$",r"すべての面が正三角形で、どの頂点にも3つの面が集まる凸多面体の $V,E,F$",r"すべての面が正方形で、どの頂点にも3つの面が集まる凸多面体の $V,E,F$"],
 [(r"$3F=2E,\ 4V=2E$：$F=\dfrac{2E}3,\ V=\dfrac E2$。$$\dfrac E2-E+\dfrac{2E}3=\dfrac{3E-6E+4E}6=\dfrac E6=2\Rightarrow E=12$$ $V=6,\ F=8$（正八面体）。",r"V=6,\ E=12,\ F=8"),
  (r"$3F=2E,\ 3V=2E$：$F=V=\dfrac{2E}3$。$$\dfrac{4E}3-E=\dfrac E3=2\Rightarrow E=6$$ $V=4,\ F=4$（正四面体）。",r"V=4,\ E=6,\ F=4"),
  (r"$4F=2E,\ 3V=2E$：$F=\dfrac E2,\ V=\dfrac{2E}3$。$$\dfrac{2E}3-E+\dfrac E2=\dfrac{4E-6E+3E}6=\dfrac E6=2\Rightarrow E=12$$ $V=8,\ F=6$（立方体）。",r"V=8,\ E=12,\ F=6")])

# ===== 例題2 直方体の対角線と面のなす角 =====
for (a,b,c),(ag,ac,sn,cs,tn,cab) in (((3,4,12),(13,5,Fr(12,13),Fr(5,13),Fr(12,5),Fr(3,13))),((2,3,6),(7,math.sqrt(13),Fr(6,7),None,None,Fr(2,7))),((1,4,8),(9,math.sqrt(17),Fr(8,9),None,None,Fr(1,9))),((2,6,9),(11,math.sqrt(40),Fr(9,11),None,None,Fr(2,11))),((6,8,24),(26,10,Fr(12,13),Fr(5,13),Fr(12,5),Fr(3,13)))):
    v=vec("A","G",a,b,c); close(np.linalg.norm(v),ag); close(math.hypot(a,b),ac)
    close(c/ag,float(sn)); close(cosang(v,np.array([1.0,0,0])),float(cab))
    th=math.atan2(c,math.hypot(a,b)); close(math.sin(th),float(sn))
f2=cub("a13_e2",3,4,12,hl=[("A","G","#b81f36"),("A","C","#2a7fd0"),("C","G","#2a9d6a")],w=26,size=(3.2,3.6))
Z.ex("直方体の対角線と平面・辺のなす角",
 r"直方体 ABCD-EFGH で $AB=3,\ AD=4,\ AE=12$ とする。対角線 AG と平面 ABCD のなす角を $\theta$ とするとき、$\sin\theta,\ \cos\theta,\ \tan\theta$ を求めよ。また、AG と辺 AB のなす角を $\varphi$ とするとき $\cos\varphi$ を求めよ。",
 r"<p><b>直線と平面のなす角</b>は、直線上の点から平面に下ろした垂線の足を結んで、<b>直角三角形</b>を作って求める。G から平面 ABCD に下ろした垂線の足は C なので、$\theta=\angle GAC$（△AGC は $\angle ACG=90^\circ$ の直角三角形）。</p>",
 "『平面とのなす角』は、真上から影をつくって影との角を見る。影は GからCへの垂線で作る。",
 [("AC、AG を求める",r"底面 ABCD は長方形なので $$AC=\sqrt{AB^2+AD^2}=\sqrt{9+16}=5$$ △ACG は $\angle ACG=90^\circ$、$CG=12$。 $$AG=\sqrt{AC^2+CG^2}=\sqrt{25+144}=13$$"),
  ("三角比を求める",r"$\theta=\angle GAC$ なので $$\sin\theta=\dfrac{CG}{AG}=\dfrac{12}{13},\quad \cos\theta=\dfrac{AC}{AG}=\dfrac5{13},\quad \tan\theta=\dfrac{CG}{AC}=\dfrac{12}5$$"),
  ("AG と AB のなす角",r"$AB\perp$ 平面 BCGF なので $AB\perp BG$。△ABG は $\angle ABG=90^\circ$ の直角三角形で $AB=3,\ AG=13$。 $$\cos\varphi=\dfrac{AB}{AG}=\dfrac3{13}$$")],
 r"\sin\theta=\dfrac{12}{13},\ \cos\theta=\dfrac5{13},\ \tan\theta=\dfrac{12}5;\quad \cos\varphi=\dfrac3{13}",
 [r"$AB=2,\ AD=3,\ AE=6$ のときの $\sin\theta,\ \cos\theta,\ \tan\theta$ と $\cos\varphi$",r"$AB=1,\ AD=4,\ AE=8$ のときの $\sin\theta,\ \cos\theta,\ \tan\theta$ と $\cos\varphi$",r"$AB=2,\ AD=6,\ AE=9$ のときの $\sin\theta,\ \cos\theta,\ \tan\theta$ と $\cos\varphi$"],
 [(r"$AC=\sqrt{13}$、$AG=\sqrt{13+36}=7$。$\sin\theta=\dfrac67,\ \cos\theta=\dfrac{\sqrt{13}}7,\ \tan\theta=\dfrac6{\sqrt{13}}=\dfrac{6\sqrt{13}}{13}$。$\cos\varphi=\dfrac27$。",r"\dfrac67,\ \dfrac{\sqrt{13}}7,\ \dfrac{6\sqrt{13}}{13};\ \dfrac27"),
  (r"$AC=\sqrt{17}$、$AG=\sqrt{17+64}=9$。$\sin\theta=\dfrac89,\ \cos\theta=\dfrac{\sqrt{17}}9,\ \tan\theta=\dfrac8{\sqrt{17}}=\dfrac{8\sqrt{17}}{17}$。$\cos\varphi=\dfrac19$。",r"\dfrac89,\ \dfrac{\sqrt{17}}9,\ \dfrac{8\sqrt{17}}{17};\ \dfrac19"),
  (r"$AC=\sqrt{40}=2\sqrt{10}$、$AG=\sqrt{40+81}=11$。$\sin\theta=\dfrac9{11},\ \cos\theta=\dfrac{2\sqrt{10}}{11},\ \tan\theta=\dfrac9{2\sqrt{10}}=\dfrac{9\sqrt{10}}{20}$。$\cos\varphi=\dfrac2{11}$。",r"\dfrac9{11},\ \dfrac{2\sqrt{10}}{11},\ \dfrac{9\sqrt{10}}{20};\ \dfrac2{11}")],fig=f2)

# ===== 例題3 ねじれの位置のなす角 =====
def cube_ang(l1,l2): return math.degrees(math.acos(cosang(vec(l1[0],l1[1],1,1,1),vec(l2[0],l2[1],1,1,1))))
for (l1,l2),exp in ((("AC","BG"),60),(("AC","DG"),60),(("AF","CH"),90),(("AC","EF"),45),(("AH","BE"),60)):
    close(cube_ang(l1,l2),exp,1e-7)
f3=cub("a13_e3",1,1,1,hl=[("A","C","#b81f36"),("B","G","#2a7fd0"),("A","H","#2a9d6a"),("C","H","#2a9d6a")],w=34,size=(3.2,3.0))
Z.ex("ねじれの位置にある2直線のなす角",
 r"立方体 ABCD-EFGH で、対角線 AC と辺でない線分 BG（面 BCGF の対角線）のなす角を求めよ。",
 r"<p>交わらない（ねじれの位置にある）2直線のなす角は、<b>一方を平行移動して、交わる2直線にして</b>求める。</p><p>立方体では、面の対角線どうしの平行を探す。</p>",
 "ねじれた2本は、片方を平行にずらして、同じ点で交わるようにしてから角を測る。",
 [("平行な線分を探す",r"四角形 ABGH は長方形（$AB\parallel HG$、$AB=HG$）なので $BG\parallel AH$。"),
  ("角を作りかえる",r"AC と BG のなす角は、AC と AH のなす角（$\angle CAH$）に等しい。"),
  ("三角形の形を調べる",r"$AC,\ CH,\ HA$ はどれも立方体の面の対角線で、辺を1とすると $$AC=CH=HA=\sqrt2$$ △ACH は正三角形。"),
  ("角を求める",r"$\angle CAH=60^\circ$。")],
 r"60^\circ",
 [r"立方体 ABCD-EFGH で、AC と DG のなす角",r"立方体 ABCD-EFGH で、AF と CH のなす角",r"立方体 ABCD-EFGH で、AC と EF のなす角"],
 [(r"$DG\parallel AF$（ADGF は長方形）。AC と AF のなす角 $\angle CAF$。$AC=CF=FA=\sqrt2$ の正三角形なので $60^\circ$。",r"60^\circ"),
  (r"$CH\parallel BE$（BCHE は長方形）。AF と BE は正方形 ABFE の対角線で垂直に交わる。よって $90^\circ$。",r"90^\circ"),
  (r"$EF\parallel AB$。AC と AB のなす角 $\angle CAB$。△ABC は直角二等辺三角形なので $45^\circ$。",r"45^\circ")],fig=f3)

# ===== 例題4 作図 =====
C4=(2.0,math.sqrt(6)); close(math.hypot(C4[0]-2.5,C4[1]),2.5)
th=np.linspace(0,math.pi,200)
f4=geo("a13_e4",circles=[],segs=[(0,0,5,0,"#333","-"),(2,0,2,math.sqrt(6),"#b81f36","-"),(0,0,2,math.sqrt(6),"#999","--"),(5,0,2,math.sqrt(6),"#999","--")],
 pts=[("A",0,0,-0.3,-0.3),("H",2,0,0,-0.35),("B",5,0,0.3,-0.3),("C",2,math.sqrt(6),0,0.3),("M",2.5,0,0.25,-0.35)],texts=[(2.3,1.2,"√6","#b81f36"),(1.0,-0.8,"2","#555"),(3.5,-0.8,"3","#555")],w=48,size=(4.6,3.0),lim=(-1,6,-1.2,3.4))
f4=geo("a13_e4",circles=[(2.5,0,2.5,"#333","-")],segs=[(0,0,5,0,"#333","-"),(2,0,2,math.sqrt(6),"#b81f36","-"),(0,0,2,math.sqrt(6),"#999","--"),(5,0,2,math.sqrt(6),"#999","--")],
 pts=[("A",0,0,-0.3,-0.3),("H",2,0,0,-0.35),("B",5,0,0.3,-0.3),("C",2,math.sqrt(6),0,0.3),("M",2.5,0,0.3,-0.35)],texts=[(2.4,1.2,"√6","#b81f36")],w=48,size=(4.6,3.2),lim=(-1,6,-1.2,3.4))
for ah_,hb in ((2,3),(2,5),(3,5),(1,7),(3,7)):
    r=(ah_+hb)/2; hx=ah_-r; ch=math.sqrt(r*r-hx*hx); close(ch*ch,ah_*hb)
Z.ex("長さ √6 の線分の作図",
 r"長さ1の線分が与えられているとき、コンパスと定規だけで長さ $\sqrt6$ の線分を作図する方法を述べ、その長さが $\sqrt6$ になることを示せ。",
 r"<p>$\sqrt{ab}$ の作図は、<b>直径の上に長さ $a$、$b$ をつなぎ、直径上の点で垂線を立てて半円と交わらせる</b>。このとき垂線の長さが $\sqrt{ab}$。理由は、直径に対する円周角が直角であることと、直角三角形の相似。</p>",
 "半円の中に作った直角三角形は、高さの2乗＝（分けた2つの長さの積）。これが√ab を作る道具。",
 [("線分 AB を作る",r"直線上に A をとり、長さ1の線分を2回、さらに3回つなげて $AH=2,\ HB=3$ となる点 H をとる。$AB=5$。"),
  ("半円を描く",r"AB の垂直二等分線を作図して中点 M を求め、M を中心に A、B を通る半円を描く。"),
  ("垂線を立てる",r"H を通り AB に垂直な直線を引き、半円との交点を C とする。"),
  (r"$CH=\sqrt6$ を示す",r"AB は直径なので $\angle ACB=90^\circ$。△ACH と △CBH は、$\angle CHA=\angle BHC=90^\circ$ で、$\angle ACH=90^\circ-\angle BCH=\angle CBH$ なので相似。 $$AH:CH=CH:HB\ \Rightarrow\ CH^2=AH\cdot HB=2\times3=6$$ よって $CH=\sqrt6$。")],
 r"AH=2,\ HB=3,\ CH^2=AH\cdot HB=6\ \Rightarrow\ CH=\sqrt6",
 [r"長さ1の線分から、長さ $\sqrt{10}$ の線分を作るときの AH、HB の長さと、$CH^2$ の計算",r"長さ1の線分から、長さ $\sqrt{15}$ の線分を作るときの AH、HB の長さと、$CH^2$ の計算",r"長さ1の線分から、長さ $\sqrt{21}$ の線分を作るときの AH、HB の長さと、$CH^2$ の計算"],
 [(r"$AH=2,\ HB=5$（$AB=7$）。$CH^2=AH\cdot HB=2\times5=10$、$CH=\sqrt{10}$。",r"AH=2,\ HB=5,\ CH^2=10"),
  (r"$AH=3,\ HB=5$（$AB=8$）。$CH^2=3\times5=15$、$CH=\sqrt{15}$。",r"AH=3,\ HB=5,\ CH^2=15"),
  (r"$AH=3,\ HB=7$（$AB=10$）。$CH^2=3\times7=21$、$CH=\sqrt{21}$。",r"AH=3,\ HB=7,\ CH^2=21")],fig=f4)

# ===== 例題5 展開図と最短経路 =====
def shortest(a,b,c): return min((a+b)**2+c*c,(a+c)**2+b*b,(b+c)**2+a*a)
for (a,b,c),exp in (((3,4,5),74),((2,3,6),61),((1,2,3),18),((4,5,6),117),((2,5,7),98)): assert shortest(a,b,c)==exp
# 表面上の最短経路を独立に検算：展開した2面(底辺a, 高さ…)のすべての組合せ
def brute(a,b,c):
    best=1e18
    # 経路が通る2面の選び方：A→Gの途中の面は3方向 × 2通り
    for (p,q,r) in itertools.permutations((a,b,c)):
        best=min(best,(p+q)**2+r*r)
    return best
for abc in ((3,4,5),(2,3,6),(1,2,3),(4,5,6),(2,5,7)): assert brute(*abc)==shortest(*abc)
f5=geo("a13_e5",segs=[(0,0,7,0,"#333","-"),(7,0,7,5,"#333","-"),(7,5,0,5,"#333","-"),(0,5,0,0,"#333","-"),(3,0,3,5,"#333","--"),(0,0,7,5,"#b81f36","-")],
 pts=[("A",0,0,-0.4,-0.35),("B",3,0,0,-0.45),("C",7,0,0.4,-0.35),("G",7,5,0.4,0.35),("F",3,5,0,0.4),("E",0,5,-0.4,0.35)],texts=[(1.5,-0.9,"3","#555"),(5,-0.9,"4","#555"),(7.7,2.5,"5","#555")],w=48,size=(4.4,2.8),lim=(-1.2,8.6,-1.5,6))
Z.ex("直方体の表面を通る最短経路",
 r"直方体 ABCD-EFGH で $AB=3,\ AD=4,\ AE=5$ とする。頂点 A から、表面を通って頂点 G に至る最短の経路の長さを求めよ。",
 r"<p>表面を通る最短経路は、<b>通る面を平面に広げた展開図で、2点を結んだ直線</b>になる。A から G へ通る2つの面の選び方は3通りあるので、3通りの展開図で長さを比べる。</p>",
 "立体の表面は、広げれば平面。広げた平面の上では、最短は直線。広げ方が複数あるので、全部試して最小を選ぶ。",
 [("展開図の長さを3通り求める",r"A から G へ通る2つの面を続けて広げた長方形で考える。<br>①面 ABFE と面 BCGF を広げる：横 $3+4=7$、縦 $5$ → $$\sqrt{7^2+5^2}=\sqrt{74}$$ ②面 ABFE と面 EFGH を広げる：横 $3$、縦 $5+4=9$ → $$\sqrt{3^2+9^2}=\sqrt{90}$$ ③面 ABCD と面 BCGF を広げる：横 $3+5=8$、縦 $4$ → $$\sqrt{8^2+4^2}=\sqrt{80}$$"),
  ("最小を選ぶ",r"$74<80<90$ なので最短は $\sqrt{74}$。")],
 r"\sqrt{74}",
 [r"$AB=2,\ AD=3,\ AE=6$ のときの A から G への表面上の最短距離",r"$AB=1,\ AD=2,\ AE=3$ のときの A から G への表面上の最短距離",r"$AB=4,\ AD=5,\ AE=6$ のときの A から G への表面上の最短距離"],
 [(r"3通り：$(2+3)^2+6^2=61$、$(2+6)^2+3^2=73$、$(3+6)^2+2^2=85$。最小は $61$。",r"\sqrt{61}"),
  (r"3通り：$(1+2)^2+3^2=18$、$(1+3)^2+2^2=20$、$(2+3)^2+1^2=26$。最小は $18$ で $\sqrt{18}=3\sqrt2$。",r"3\sqrt2"),
  (r"3通り：$(4+5)^2+6^2=117$、$(4+6)^2+5^2=125$、$(5+6)^2+4^2=137$。最小は $117$ で $\sqrt{117}=3\sqrt{13}$。",r"3\sqrt{13}")],fig=f5)

# ===== 章末 =====
Z.ch(r"凸多面体で、三角形の面が8個、正方形の面が6個あり、どの頂点にも4つの面が集まっている。辺の数 $E$ と頂点の数 $V$ を求めよ。",
 r"面の辺の数の合計は $3\times8+4\times6=48$。これは $2E$ なので $E=24$。各頂点に4本の辺：$4V=2E=48$ より $V=12$。確かめ：$V-E+F=12-24+14=2$。",r"E=24,\ V=12",1)
Z.ch(r"直方体 ABCD-EFGH で $AB=6,\ AD=8,\ AE=24$。対角線 AG と平面 ABCD のなす角 $\theta$ の $\sin\theta,\ \cos\theta,\ \tan\theta$ と、AG と AB のなす角 $\varphi$ の $\cos\varphi$ を求めよ。",
 r"$AC=\sqrt{36+64}=10$、$AG=\sqrt{100+576}=26$。$\sin\theta=\dfrac{24}{26}=\dfrac{12}{13}$、$\cos\theta=\dfrac{10}{26}=\dfrac5{13}$、$\tan\theta=\dfrac{24}{10}=\dfrac{12}5$。$\cos\varphi=\dfrac{6}{26}=\dfrac3{13}$。",r"\dfrac{12}{13},\ \dfrac5{13},\ \dfrac{12}5;\ \dfrac3{13}",2)
Z.ch(r"立方体 ABCD-EFGH で、AH と BE のなす角を求めよ。",
 r"$BE\parallel CH$（BCHE は長方形）。AH と CH のなす角 $\angle AHC$。$AH=HC=CA=\sqrt2$ の正三角形なので $60^\circ$。",r"60^\circ",3)
Z.ch(r"長さ1の線分から長さ $\sqrt7$ の線分を作図する方法を、$AH$、$HB$ の長さと $CH^2$ の計算で示せ。",
 r"$AH=1,\ HB=7$（$AB=8$）とし、AB を直径とする半円を描く。H で AB に垂線を立てて半円との交点を C とする。$CH^2=AH\cdot HB=1\times7=7$、$CH=\sqrt7$。",r"AH=1,\ HB=7,\ CH^2=7",4)
Z.ch(r"直方体 ABCD-EFGH で $AB=2,\ AD=5,\ AE=7$。A から表面を通って G に至る最短経路の長さを求めよ。",
 r"3通り：$(2+5)^2+7^2=98$、$(2+7)^2+5^2=106$、$(5+7)^2+2^2=148$。最小は $98$ で $\sqrt{98}=7\sqrt2$。",r"7\sqrt2",5)
UNIT=Z.unit(0,2,"図形の性質","作図・空間図形","オイラーの多面体定理、直線と平面のなす角、ねじれの位置の2直線のなす角、√ab の作図、表面を通る最短経路などに挑みます。")
