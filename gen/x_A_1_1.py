# -*- coding: utf-8 -*-
from bh import *
import math
Z=U_(); CH=[]; R=sp.Rational; _c=[0]
Bp=np.array([0.,0.]); Cp=np.array([6.,0.]); Ap=np.array([1.8,4.])
def pt(P,Q,m,n): return (n*np.array(P)+m*np.array(Q))/(m+n)   # P→Q を m:n
def tri(name,extra_segs=(),pts=(),polys=(),w=44,size=(3.8,3.2)):
    _c[0]+=1
    L_=[("A",Ap[0],Ap[1],0,.35),("B",0,0,-.3,-.3),("C",6,0,.3,-.3)]
    return geo(name+str(_c[0]),polys=[([tuple(Bp),tuple(Cp),tuple(Ap)],"#333")]+list(polys),segs=list(extra_segs),pts=L_+list(pts),w=w,size=size,lim=(-1,7,-1,5))
# 6 チェバ
def b6(a,b,c,d):
    # AF:FB=a:b, BD:DC=c:d, CE:EA=? = b*d/(a*c)
    r=R(b*d,a*c); n=r.p; m=r.q  # CE:EA=n:m
    Fp=pt(Ap,Bp,a,b); Dp=pt(Bp,Cp,c,d); Ep=pt(Cp,Ap,r.p,r.q)
    # concurrency check numerically
    def inter(P1,P2,P3,P4):
        M=np.array([P2-P1,-(P4-P3)]).T; t=np.linalg.solve(M,P3-P1); return P1+t[0]*(P2-P1)
    X=inter(Ap,Dp,Bp,Ep); Y=inter(Ap,Dp,Cp,Fp); assert np.allclose(X,Y)
    fig=tri("ax11c",[(Ap[0],Ap[1],Dp[0],Dp[1],"#b81f36","-"),(Bp[0],Bp[1],Ep[0],Ep[1],"#2a7fd0","-"),(Cp[0],Cp[1],Fp[0],Fp[1],"#2a9d6a","-")],[("F",Fp[0],Fp[1],-.3,.2),("D",Dp[0],Dp[1],0,-.35),("E",Ep[0],Ep[1],.3,.2)])
    st=[("チェバの定理","<p>3直線 $AD,BE,CF$ が1点で交わる $\\iff$</p>"+D(r"\dfrac{AF}{FB}\cdot\dfrac{BD}{DC}\cdot\dfrac{CE}{EA}=1")+fig),
        ("代入",D(r"\dfrac{%d}{%d}\cdot\dfrac{%d}{%d}\cdot\dfrac{CE}{EA}=1"%(a,b,c,d))),
        ("解く",D(r"\dfrac{CE}{EA}=\dfrac{%d}{%d}\cdot\dfrac{%d}{%d}=\dfrac{%d}{%d}\ \Rightarrow\ CE:EA=%d:%d"%(b,a,d,c,b*d,a*c,r.p,r.q)))]
    return r"$\triangle ABC$ の辺 $AB,\ BC,\ CA$ 上に点 $F,\ D,\ E$ をとり、$AD,\ BE,\ CF$ が1点で交わるようにする。$AF:FB=%d:%d$、$BD:DC=%d:%d$ のとき、$CE:EA$ を求めよ。"%(a,b,c,d),st,r"CE:EA=%d:%d"%(r.p,r.q)
o=[b6(*v) for v in [(2,3,3,1),(1,2,2,3),(3,1,1,2),(2,1,3,2),(1,3,4,1)]]
build(Z,CH,"チェバの定理（比を求める）",o,r"<p>頂点から出る3直線が1点で交わるとき $\dfrac{AF}{FB}\cdot\dfrac{BD}{DC}\cdot\dfrac{CE}{EA}=1$。<b>三角形を一周する</b>順（$A\to F\to B\to D\to C\to E\to A$）に比をかける。</p>","一周して元の頂点にもどると、比の積が1。",6)
# 7 内心
def b7(a,b,c):
    # triangle sides BC=a, CA=b, AB=c : AI:ID=(b+c):a
    r=R(b+c,a); 
    Cx=(c*c+a*a-b*b)/(2*c*a)  # cos B
    P=np.array([c*Cx*1.0,c*math.sqrt(1-Cx**2)]); B_=np.array([0,0.]); C_=np.array([a,0.])
    I_=(a*P+b*B_+c*C_)/(a+b+c); D_=pt(B_,C_,c,b)   # BD:DC=c:b
    assert abs(np.linalg.norm(P-I_)/np.linalg.norm(I_-D_)-float(r))<1e-9
    sc=5/max(a,b,c)
    def fn_name(): return "ax11i"+str(a)+str(b)+str(c)
    fig=geo(fn_name(),polys=[([tuple(B_*sc),tuple(C_*sc),tuple(P*sc)],"#333")],segs=[(P[0]*sc,P[1]*sc,D_[0]*sc,D_[1]*sc,"#b81f36","-"),(0,0,I_[0]*sc,I_[1]*sc,"#2a7fd0","--"),(a*sc,0,I_[0]*sc,I_[1]*sc,"#2a7fd0","--")],pts=[("A",P[0]*sc,P[1]*sc,0,.3),("B",0,0,-.3,-.3),("C",a*sc,0,.3,-.3),("D",D_[0]*sc,0,0,-.35),("I",I_[0]*sc,I_[1]*sc,.3,.2)],w=42,size=(3.6,3.0))
    st=[("$D$ は $BC$ を $c:b$ に内分","<p>"+I("AD")+" は "+I(r"\angle A")+" の二等分線。</p>"+D(r"BD:DC=AB:AC=%d:%d,\qquad BD=\dfrac{%d}{%d}\cdot%d=%s"%(c,b,c,b+c,a,L(R(a*c,b+c))))+fig),
        ("$BI$ は $\\angle B$ の二等分線","<p>"+I(r"\triangle ABD")+" で "+I("BI")+" は "+I(r"\angle B")+" の二等分線。</p>"+D(r"AI:ID=BA:BD=%d:%s=%d:%s"%(c,L(R(a*c,b+c)),b+c,L(a)))),
        ("答え",D(r"AI:ID=%d:%d"%(b+c,a)))]
    return r"$\triangle ABC$ で $BC=%d,\ CA=%d,\ AB=%d$ とする。$\angle A$ の二等分線と $BC$ の交点を $D$、内心を $I$ とするとき、$AI:ID$ を求めよ。"%(a,b,c),st,r"AI:ID=%d:%d"%(b+c,a)
o=[b7(*v) for v in [(6,5,7),(7,6,8),(5,6,7),(9,8,7),(6,7,8)]]
build(Z,CH,"内心と角の二等分線の比",o,r"<p>$AD$（角の二等分線）で $BD:DC=AB:AC$。次に $\triangle ABD$ で $BI$ が $\angle B$ の二等分線なので $AI:ID=BA:BD$。<b>二等分線の定理を2回</b>使う。</p>","二等分線の定理は、辺の比がそのまま分点の比になる。",7)
# 8 重心を通る平行線
def b8(a,S):
    # G を通り BC に平行な直線; PQ=2/3 BC, area APQ=4/9 S
    PQ=R(2*a,3); S2=R(4,9)*S; Gp=(Ap+Bp+Cp)/3
    P=Ap+(Bp-Ap)*(2/3); Q=Ap+(Cp-Ap)*(2/3)
    fig=tri("ax11g",[(P[0],P[1],Q[0],Q[1],"#b81f36","-")],[("G",Gp[0],Gp[1],0,-.35),("P",P[0],P[1],-.3,.1),("Q",Q[0],Q[1],.3,.1)],polys=[])
    st=[("重心は中線を $2:1$","<p>中線 "+I("AM")+" 上で "+I("AG:GM=2:1")+"。よって "+I("AG:AM=2:3")+"。"+I("PQ\\parallel BC")+" なので "+I(r"\triangle APQ\sim\triangle ABC")+"、相似比 "+I("2:3")+"。</p>"+fig),
        ("長さ",D(r"PQ=\dfrac23BC=\dfrac23\cdot%d=%s"%(a,L(PQ)))),
        ("面積","<p>面積比は相似比の2乗。</p>"+D(r"\triangle APQ=\dfrac49\triangle ABC=\dfrac49\cdot%d=%s"%(S,L(S2))))]
    return r"$\triangle ABC$ の重心 $G$ を通り $BC$ に平行な直線が $AB,\ AC$ と交わる点を $P,\ Q$ とする。$BC=%d$、$\triangle ABC$ の面積が $%d$ のとき、$PQ$ の長さと $\triangle APQ$ の面積を求めよ。"%(a,S),st,r"PQ=%s,\ \ \triangle APQ=%s"%(L(PQ),L(S2))
o=[b8(*v) for v in [(9,54),(12,72),(6,45),(15,81),(21,63)]]
build(Z,CH,"重心を通る平行線と相似",o,r"<p>重心は中線を $2:1$ に内分する。平行線で<b>相似な三角形</b>ができ、相似比 $2:3$、面積比は $4:9$。</p>","重心から頂点までが全体の $\\frac23$。この比が相似比になる。",8)
# 9 五心と角
def b9(Adeg):
    A=Adeg; B_=70; C_=180-A-B_
    assert C_>0
    BOC=2*A; BIC=90+A/2; BHC=180-A
    # numeric check
    ra=lambda d:math.radians(d)
    a_=math.sin(ra(A)); b_=math.sin(ra(B_)); c_=math.sin(ra(C_))
    Bq=np.array([0,0.]); Cq=np.array([a_,0.]); Aq=np.array([c_*math.cos(ra(B_)),c_*math.sin(ra(B_))])
    def ang(P,Q,Rr):
        u=P-Q; v=Rr-Q; return math.degrees(math.acos(u@v/np.linalg.norm(u)/np.linalg.norm(v)))
    I_=(a_*Aq+b_*Bq+c_*Cq)/(a_+b_+c_); H_=np.array([Aq[0],(Aq[0]*(Cq[0]-Aq[0])*-1)/Aq[1]*-1 if False else 0])
    # orthocenter
    Hy=-(Aq[0]-Bq[0])*(Aq[0]-Cq[0])/Aq[1]*-1
    H_=np.array([Aq[0],(Aq[0]-Bq[0])*(Cq[0]-Aq[0])/Aq[1]])
    assert abs(ang(Bq,I_,Cq)-BIC)<1e-6 and abs(ang(Bq,H_,Cq)-BHC)<1e-6
    st=[("内心","<p>"+I(r"\angle IBC+\angle ICB=\dfrac{\angle B+\angle C}{2}=\dfrac{180^\circ-%d^\circ}{2}"%A)+"。</p>"+D(r"\angle BIC=180^\circ-\dfrac{180^\circ-%d^\circ}{2}=90^\circ+\dfrac{%d^\circ}{2}=%s^\circ"%(A,A,L(R(BIC)))) ),
        ("外心","<p>"+I("\\angle BOC")+" は "+I("\\angle A")+" に対する中心角。</p>"+D(r"\angle BOC=2\angle A=%d^\circ"%BOC)),
        ("垂心","<p>四角形 "+I("AEHF")+" の対角が "+I("90^\\circ")+" ずつ。</p>"+D(r"\angle BHC=180^\circ-\angle A=%d^\circ"%BHC))]
    return r"$\angle A=%d^\circ$ の鋭角三角形 $ABC$ の内心を $I$、外心を $O$、垂心を $H$ とする。$\angle BIC,\ \angle BOC,\ \angle BHC$ を求めよ。"%A,st,r"\angle BIC=%s^\circ,\ \angle BOC=%d^\circ,\ \angle BHC=%d^\circ"%(L(R(BIC)),BOC,BHC)
o=[b9(v) for v in [50,60,40,45,55]]
build(Z,CH,"三角形の五心と角（内心・外心・垂心）",o,r"<p>$\angle BIC=90^\circ+\dfrac A2$（内心）、$\angle BOC=2A$（外心、中心角）、$\angle BHC=180^\circ-A$（垂心）。<b>鋭角三角形</b>のとき。</p>","同じ辺 $BC$ を見込む3つの角は、$A$ で決まる。",9)
# 10 三角形の成立と鈍角
def b10(d):
    # sides x, x+d, x+2d ; triangle: x+x+d > x+2d -> x>d ; obtuse: x^2+(x+d)^2 < (x+2d)^2 -> x^2-2dx-3d^2<0 -> x<3d ; so d<x<3d
    for xv in np.linspace(0.1,10*d,2000):
        tri_ok=xv+xv+d>xv+2*d; ob=xv**2+(xv+d)**2<(xv+2*d)**2
        assert (tri_ok and ob)==(d<xv<3*d) or abs(xv-d)<1e-2 or abs(xv-3*d)<1e-2
    st=[("成り立つ条件","<p>最大辺は "+I("x+%d"%(2*d))+"。三角形の成立条件：</p>"+D(r"x+(x+%d)>x+%d\ \Rightarrow\ x>%d"%(d,2*d,d))),
        ("鈍角三角形の条件","<p>最大角が鈍角 "+I(r"\iff")+" 最大辺の2乗が他の2辺の2乗の和より大。</p>"+D(r"(x+%d)^2>x^2+(x+%d)^2\ \Rightarrow\ x^2-%dx-%d<0\ \Rightarrow\ (x-%d)(x+%d)<0"%(2*d,d,2*d,3*d*d,3*d,d))),
        ("共通部分",D(r"%d<x<%d"%(d,3*d)))]
    return r"3辺の長さが $x,\ x+%d,\ x+%d$ の三角形が鈍角三角形になるような $x$ の値の範囲を求めよ。"%(d,2*d),st,r"%d<x<%d"%(d,3*d)
o=[b10(d) for d in [1,2,3,4,5]]
build(Z,CH,"鈍角三角形になる辺の長さの範囲",o,r"<p>(1) 三角形の成立 $a<b+c$（最大辺で確認）、(2) 鈍角 $\iff$ 最大辺の2乗 $>$ 他の2乗の和。<b>2つの条件の共通部分</b>。</p>","まず「三角形ができるか」、次に「どんな三角形か」。",10)
XU=finishx(Z,CH)
