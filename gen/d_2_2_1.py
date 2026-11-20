# -*- coding: utf-8 -*-
# 点と直線（数学II 図形と方程式）
from bh import *
Z=U_(); CH=[]
def Pt(P): return "("+L(P[0])+",\\ "+L(P[1])+")"
# ===== 例題1 内分・外分・重心 =====
def b1(A,B,mn,pq,C):
    m_,n_=mn; p2,q2=pq
    P=((n_*A[0]+m_*B[0])/sp.Integer(m_+n_),(n_*A[1]+m_*B[1])/sp.Integer(m_+n_))
    Q=((-q2*A[0]+p2*B[0])/sp.Integer(p2-q2),(-q2*A[1]+p2*B[1])/sp.Integer(p2-q2))
    G=((A[0]+B[0]+C[0])/sp.Integer(3),(A[1]+B[1]+C[1])/sp.Integer(3))
    steps=[("(1) 内分点の公式","<p>"+I("m:n")+" に内分する点は "+I(r"\left(\dfrac{nx_1+mx_2}{m+n},\ \dfrac{ny_1+my_2}{m+n}\right)")+"。</p>"+D(r"P\left(\dfrac{%d\cdot%d+%d\cdot%d}{%d+%d},\ \dfrac{%d\cdot(%d)+%d\cdot%d}{%d+%d}\right)=%s"%(n_,A[0],m_,B[0],m_,n_,n_,A[1],m_,B[1],m_,n_,Pt(P)))),
           ("(2) 外分点の公式","<p>"+I("m:n")+" に外分する点は "+I(r"\left(\dfrac{-nx_1+mx_2}{m-n},\ \dfrac{-ny_1+my_2}{m-n}\right)")+"。</p>"+D(r"Q\left(\dfrac{-%d\cdot%d+%d\cdot%d}{%d-%d},\ \dfrac{-%d\cdot(%d)+%d\cdot%d}{%d-%d}\right)=%s"%(q2,A[0],p2,B[0],p2,q2,q2,A[1],p2,B[1],p2,q2,Pt(Q)))),
           ("(3) 重心の公式","<p>重心は3頂点の座標の平均。</p>"+D(r"G\left(\dfrac{%d+%d+(%d)}{3},\ \dfrac{(%d)+%d+%d}{3}\right)=%s"%(A[0],B[0],C[0],A[1],B[1],C[1],Pt(G))))]
    prob=r"3点 $A(%d,\ %d)$、$B(%d,\ %d)$、$C(%d,\ %d)$ について、(1) 線分 $AB$ を $%d:%d$ に内分する点 $P$ (2) 線分 $AB$ を $%d:%d$ に外分する点 $Q$ (3) $\triangle ABC$ の重心 $G$ の座標をそれぞれ求めよ。"%(A[0],A[1],B[0],B[1],C[0],C[1],m_,n_,p2,q2)
    return prob,steps,r"P%s,\quad Q%s,\quad G%s"%(Pt(P),Pt(Q),Pt(G)),(A,B,C,P,Q,G)
V=[((1,-2),(7,4),(2,1),(3,1),(4,1)),((-3,2),(5,-6),(3,1),(5,3),(1,8)),((2,5),(-4,-1),(1,2),(2,1),(6,-3)),((-1,-4),(9,6),(3,2),(4,1),(2,5)),((0,7),(-6,-2),(2,3),(5,2),(3,4))]
o=[b1(*v) for v in V]
build(Z,CH,"内分点・外分点・重心",[z[:3] for z in o],
 r"<p>$A(x_1,y_1),\ B(x_2,y_2)$ のとき、<br>内分点：$\left(\dfrac{nx_1+mx_2}{m+n},\ \dfrac{ny_1+my_2}{m+n}\right)$、外分点：$\left(\dfrac{-nx_1+mx_2}{m-n},\ \dfrac{-ny_1+my_2}{m-n}\right)$、<br>重心：$\left(\dfrac{x_1+x_2+x_3}3,\ \dfrac{y_1+y_2+y_3}3\right)$。</p>",
 "内分は「たすき掛けで分ける」。外分は、分母の符号が変わる（$m-n$）だけで同じ形。",1)
A,B,C,P_,Q_,G_=o[0][3]
def f1(ax):
    xr,yr=(-1,11),(-4,9)
    ax.plot([A[0],Q_[0]],[A[1],Q_[1]],color="#555",lw=1.4); ax.plot([A[0],C[0]],[A[1],C[1]],color="#555",lw=1.4); ax.plot([B[0],C[0]],[B[1],C[1]],color="#555",lw=1.4)
    for nm,pp,dx,dy in (("A",A,-.4,-.5),("B",B,.45,-.1),("C",C,.1,.6),("P",P_,.2,.55),("Q",Q_,.2,.55),("G",G_,.55,.3)): dpt(ax,pp[0],pp[1],nm,dx,dy)
f1fig=plane("i221_e1",(-1,11),(-4,9),f1,size=(4.2,3.6),w=54)
addfig(Z.E[0],2,f1fig)
# ===== 例題2 平行・垂直な直線 =====
def b2(a,b,p_,q_,r_):
    ppar=lineeq(q_,-p_,0)  # placeholder
    par=lineeq(p_,q_,-(p_*a+q_*b)); per=lineeq(q_,-p_,-(q_*a-p_*b))
    assert par[0]*a+par[1]*b+par[2]==0 and per[0]*a+per[1]*b+per[2]==0
    assert par[0]*q_-par[1]*p_==0 and per[0]*p_+per[1]*q_==0
    m_=sp.Rational(-p_,q_)
    steps=[("傾きを読み取る","<p>"+I("%s"%(poly([(p_,"x"),(q_,"y"),(r_,"")])+"=0"))+" を "+I("y")+" について解くと "+I("y=%s"%L(m_*x+sp.Rational(-r_,q_)))+"。傾きは "+I("%s"%L(m_))+"。</p>"),
           ("(1) 平行な直線","<p>平行 "+I(r"\iff")+" 傾きが等しい。傾き "+I(L(m_))+"、点 "+I("A(%d,\\ %d)"%(a,b))+" を通る直線：</p>"+D("y-(%d)=%s(x-(%d))"%(b,"("+L(m_)+")",a))+"<p>整理して</p>"+D(leq(*par))),
           ("(2) 垂直な直線","<p>垂直 "+I(r"\iff")+" 傾きの積が "+I("-1")+"。傾きは "+I(r"-\dfrac1{%s}=%s"%("("+L(m_)+")",L(-1/m_)))+"。</p>"+D("y-(%d)=%s(x-(%d))"%(b,"("+L(-1/m_)+")",a))+"<p>整理して</p>"+D(leq(*per)))]
    prob=r"点 $A(%d,\ %d)$ を通り、直線 $l:\ %s=0$ に (1) 平行な直線 (2) 垂直な直線 の方程式を求めよ。"%(a,b,poly([(p_,"x"),(q_,"y"),(r_,"")]))
    return prob,steps,r"\text{(1) }%s\qquad \text{(2) }%s"%(leq(*par),leq(*per))
V=[(1,2,2,-3,6),(3,-1,3,2,-6),(-2,4,1,2,-4),(2,0,4,-1,3),(-1,-3,2,5,10)]
o=[b2(*v) for v in V]
build(Z,CH,"平行・垂直な直線の方程式",o,
 r"<p>2直線の傾きを $m_1,m_2$ とすると<br>平行 $\iff m_1=m_2$、垂直 $\iff m_1m_2=-1$。<br>点 $(x_0,y_0)$ を通り傾き $m$ の直線：$y-y_0=m(x-x_0)$。</p>",
 "平行は「同じ傾き」。垂直は「傾きをひっくり返して符号を変える」。",2)
def f2(ax):
    xr,yr=(-5,6),(-4,8); a,b,p_,q_,r_=V[0]
    dline(ax,p_,q_,r_,xr,yr,col="#555",ls="--"); par=lineeq(p_,q_,-(p_*a+q_*b)); per=lineeq(q_,-p_,-(q_*a-p_*b))
    dline(ax,*par,xr,yr); dline(ax,*per,xr,yr,col="#1f6fb8"); dpt(ax,a,b,"A",.35,.45)
    ax.text(5.3,2.6,"l",fontsize=12,color="#555"); 
addfig(Z.E[1],2,plane("i221_e2",(-5,6),(-4,8),f2,size=(4.0,3.6),w=50))
# ===== 例題3 点と直線の距離・三角形の面積 =====
def b3(A,B,C):
    a,b,c=lthru(A,B); AB=sp.sqrt((B[0]-A[0])**2+(B[1]-A[1])**2); num=abs(a*C[0]+b*C[1]+c); den=sp.sqrt(a*a+b*b); d=num/den
    S=sp.Rational(1,2)*AB*d; S2=sp.Rational(1,2)*abs((B[0]-A[0])*(C[1]-A[1])-(B[1]-A[1])*(C[0]-A[0])); assert sp.simplify(S-S2)==0
    steps=[("直線 $AB$ の方程式を求める","<p>"+I("A(%d,%d),\\ B(%d,%d)"%(A+B))+" を通る直線。傾き "+I(r"\dfrac{%d-(%d)}{%d-(%d)}"%(B[1],A[1],B[0],A[0]))+"。</p>"+D(leq(a,b,c))),
           ("線分 $AB$ の長さ",D(r"AB=\sqrt{(%d-(%d))^2+(%d-(%d))^2}=\sqrt{%d}=%s"%(B[0],A[0],B[1],A[1],(B[0]-A[0])**2+(B[1]-A[1])**2,L(AB)))),
           ("点 $C$ と直線 $AB$ の距離","<p>点と直線の距離の公式 "+I(r"d=\dfrac{|ax_0+by_0+c|}{\sqrt{a^2+b^2}}")+"。</p>"+D(r"d=\dfrac{|%d\cdot(%d)+(%d)\cdot(%d)+(%d)|}{\sqrt{%d^2+(%d)^2}}=\dfrac{%d}{\sqrt{%d}}=%s"%(a,C[0],b,C[1],c,a,b,num,a*a+b*b,L(d)))),
           ("面積を求める",D(r"S=\dfrac12\cdot AB\cdot d=\dfrac12\cdot%s\cdot%s=%s"%(L(AB),L(d),L(S))))]
    prob=r"3点 $A(%d,\ %d)$、$B(%d,\ %d)$、$C(%d,\ %d)$ を頂点とする $\triangle ABC$ の面積を求めよ。"%(A+B+C)
    return prob,steps,r"S=%s"%L(S)
V=[((1,1),(5,3),(2,6)),((-2,0),(4,2),(1,7)),((0,-3),(6,1),(-1,4)),((3,2),(-1,5),(6,7)),((-4,-1),(2,-3),(0,5))]
o=[b3(*v) for v in V]
build(Z,CH,"点と直線の距離と三角形の面積",o,
 r"<p>点 $(x_0,y_0)$ と直線 $ax+by+c=0$ の距離 $$d=\dfrac{|ax_0+by_0+c|}{\sqrt{a^2+b^2}}$$ 三角形の面積は 底辺 $AB$（長さ）と、頂点 $C$ から直線 $AB$ までの距離 $d$ で $S=\dfrac12\,AB\cdot d$。</p>",
 "面積は「底辺×高さ÷2」。高さは、点と直線の距離の公式がそのまま使える。",3)
def f3(ax):
    A,B,C=V[0]; ax.fill([A[0],B[0],C[0]],[A[1],B[1],C[1]],color="#fbe3e6",zorder=1)
    ax.plot([A[0],B[0],C[0],A[0]],[A[1],B[1],C[1],A[1]],color="#b81f36",lw=1.8)
    for nm,pp,dx,dy in (("A",A,-.4,-.4),("B",B,.4,-.4),("C",C,0,.55)): dpt(ax,pp[0],pp[1],nm,dx,dy)
addfig(Z.E[2],3,plane("i221_e3",(-1,7),(-1,8),f3,size=(3.8,3.4),w=48))
# ===== 例題4 対称点と最短距離 =====
def b4(A,B,l):
    p_,q_,r_=l; k_=sp.Rational(2*(p_*A[0]+q_*A[1]+r_),p_*p_+q_*q_); s=A[0]-k_*p_; t=A[1]-k_*q_; assert s==int(s) and t==int(t)
    assert (p_*A[0]+q_*A[1]+r_)*(p_*B[0]+q_*B[1]+r_)>0
    Ap=(int(s),int(t)); dd=sp.sqrt((B[0]-Ap[0])**2+(B[1]-Ap[1])**2)
    X=sp.Symbol('X'); ln=lthru(Ap,B); sol=sp.solve([ln[0]*x+ln[1]*y+ln[2],p_*x+q_*y+r_],[x,y],dict=True)[0]
    steps=[("対称点を $A'(s,t)$ とおいて条件を式にする","<p>①"+I("AA'")+" が "+I("l")+" に垂直 ②線分 "+I("AA'")+" の中点が "+I("l")+" 上。</p>"+D(r"\begin{cases}%d(s-(%d))-(%d)(t-(%d))=0\quad(\text{①：}AA'\parallel\text{法線 }(%d,%d))\\ %d\cdot\dfrac{%d+s}{2}+(%d)\cdot\dfrac{%d+t}{2}+(%d)=0\quad(\text{②})\end{cases}"%(q_,A[0],p_,A[1],p_,q_,p_,A[0],q_,A[1],r_))),
           ("連立方程式を解く","<p>①②を整理して解くと</p>"+D(r"s=%d,\quad t=%d"%Ap)+"<p>よって "+I("A'(%d,\\ %d)"%Ap)+"。</p>"),
           ("最短距離を考える","<p>"+I("l")+" 上の点 "+I("P")+" について "+I("AP=A'P")+" だから "+I("AP+PB=A'P+PB\\geqq A'B")+"。等号は "+I("P")+" が線分 "+I("A'B")+" 上にあるとき（"+I("A,B")+" は "+I("l")+" の同じ側なので "+I("A'B")+" は "+I("l")+" と交わる）。</p>"+D(r"A'B=\sqrt{(%d-(%d))^2+(%d-(%d))^2}=%s"%(B[0],Ap[0],B[1],Ap[1],L(dd))))
           ,("そのときの点 $P$","<p>直線 "+I("A'B")+"："+I(leq(*ln))+" と "+I(leq(p_,q_,r_))+" の交点。</p>"+D(r"P\left(%s,\ %s\right)"%(L(sol[x]),L(sol[y]))))]
    prob=r"直線 $l:\ %s=0$ について、(1) 点 $A(%d,\ %d)$ と対称な点 $A'$ の座標を求めよ。(2) $l$ 上に点 $P$ をとり $AP+PB$ を最小にしたい。$B(%d,\ %d)$ とするとき、最小値とそのときの $P$ の座標を求めよ。"%(poly([(p_,"x"),(q_,"y"),(r_,"")]),A[0],A[1],B[0],B[1])
    return prob,steps,r"A'(%d,\ %d),\quad \text{最小値 }%s,\quad P\left(%s,\ %s\right)"%(Ap+(L(dd),L(sol[x]),L(sol[y])))
V=[((0,1),(1,0),(1,1,-4)),((3,1),(4,2),(1,-1,1)),((0,0),(1,1),(2,1,-5)),((1,0),(2,1),(1,2,-6)),((0,4),(1,3),(1,-2,3))]
o=[b4(*v) for v in V]
build(Z,CH,"直線に関する対称点と最短距離",o,
 r"<p>点 $A$ と直線 $l$ に関して対称な点 $A'$ は、<b>①$AA'\perp l$</b>、<b>②$AA'$ の中点が $l$ 上</b>の2条件で決まる。$l$ 上の点 $P$ について $AP=A'P$ なので、$AP+PB$ の最小値は $A'B$（折れ線を直線に伸ばす）。</p>",
 "鏡に映した像 $A'$ を使うと、折れ線が「まっすぐ」になる。まっすぐが最短。",4)
def f4(ax):
    A,B,l=V[0]; xr,yr=(-2,7),(-2,7); dline(ax,*l,xr,yr,col="#555")
    p_,q_,r_=l; k_=sp.Rational(2*(p_*A[0]+q_*A[1]+r_),p_*p_+q_*q_); Ap=(A[0]-k_*p_,A[1]-k_*q_)
    ax.plot([Ap[0],B[0]],[Ap[1],B[1]],color="#b81f36",lw=1.6); ax.plot([A[0],2],[A[1],2],color="#1f6fb8",lw=1.6,ls="--"); ax.plot([A[0],Ap[0]],[A[1],Ap[1]],color="#888",lw=1,ls=":")
    for nm,pp,dx,dy in (("A",A,-.4,.1),("B",B,.4,-.1),("A'",Ap,.5,.1),("P",(2,2),.45,-.35)): dpt(ax,float(pp[0]),float(pp[1]),nm,dx,dy)
    ax.text(6.1,-.6,"l",fontsize=12,color="#555")
addfig(Z.E[3],2,plane("i221_e4",(-2,7),(-2,7),f4,size=(3.8,3.6),w=48))
# ===== 例題5 2直線の交点を通る直線 =====
def b5(l1,l2,Q):
    v1=l1[0]*Q[0]+l1[1]*Q[1]+l1[2]; v2=l2[0]*Q[0]+l2[1]*Q[1]+l2[2]; assert v2!=0 and v1!=0
    kk=sp.Rational(-v1,v2); fin=lineeq(l1[0]+kk*l2[0],l1[1]+kk*l2[1],l1[2]+kk*l2[2]); assert fin[0]*Q[0]+fin[1]*Q[1]+fin[2]==0
    T=lambda l:poly([(l[0],"x"),(l[1],"y"),(l[2],"")])
    steps=[("交点を通る直線を1つの式で表す","<p>2直線 "+I(T(l1)+"=0")+"、"+I(T(l2)+"=0")+" の交点を通る直線は、定数 "+I("k")+" を使って</p>"+D("("+T(l1)+")+k("+T(l2)+")=0")+"<p>と表せる。（"+I(T(l2)+"=0")+" そのものは表せない点に注意。）</p>"),
           ("点 $Q$ を通る条件で $k$ を決める","<p>"+I("x=%d,\\ y=%d"%Q)+" を代入：</p>"+D("("+L(v1)+")+k\\cdot("+L(v2)+")=0\\ \\Rightarrow\\ k=%s"%L(kk))),
           ("$k$ を戻して整理する",D("("+T(l1)+")+("+L(kk)+")("+T(l2)+")=0")+"<p>整数係数に直して</p>"+D(leq(*fin)))]
    prob=r"2直線 $%s=0$、$%s=0$ の交点と、点 $Q(%d,\ %d)$ を通る直線の方程式を求めよ。"%(T(l1),T(l2),Q[0],Q[1])
    return prob,steps,leq(*fin)
V=[((1,1,-3),(2,-1,0),(3,1)),((2,-1,1),(1,1,-5),(4,0)),((3,1,-5),(1,-1,-1),(2,3)),((1,-2,3),(3,1,-5),(1,-1)),((4,1,-2),(1,1,1),(0,1))]
o=[b5(*v) for v in V]
build(Z,CH,"2直線の交点を通る直線",o,
 r"<p>2直線 $f=0,\ g=0$ の交点を通る直線は $$f+kg=0\quad(k\text{ は定数})$$ と表せる。交点を計算せず、<b>もう1つの条件</b>（通る点など）で $k$ を決める。</p>",
 "交点をわざわざ求めない。「交点を通る直線のグループ」を1つの式にまとめて、1本に絞る。",5)
def f5(ax):
    l1,l2,Q=V[0]; xr,yr=(-2,6),(-3,6); dline(ax,*l1,xr,yr,col="#555"); dline(ax,*l2,xr,yr,col="#1f6fb8"); fin=lineeq(l1[0]+sp.Rational(-1,5)*l2[0],l1[1]+sp.Rational(-1,5)*l2[1],l1[2]+sp.Rational(-1,5)*l2[2]); dline(ax,*fin,xr,yr); dpt(ax,Q[0],Q[1],"Q",.4,.45)
addfig(Z.E[4],2,plane("i221_e5",(-2,6),(-3,6),f5,size=(3.8,3.4),w=48))
UNIT=finish(Z,CH,1,0,"図形と方程式","点と直線","内分・外分・重心、平行と垂直、点と直線の距離、対称点と最短距離、交点を通る直線まで、座標平面上の直線の総合力を問う難問に挑みます。")
