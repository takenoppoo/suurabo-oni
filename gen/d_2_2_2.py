# -*- coding: utf-8 -*-
# 円（数学II 図形と方程式）
from bh import *
Z=U_(); CH=[]
def xs(a_): return "x" if a_==0 else "(x%+d)"%(-a_)
def cir(a_,b_,r2):
    fx="x^2" if a_==0 else "(x%+d)^2"%(-a_); fy="y^2" if b_==0 else "(y%+d)^2"%(-b_)
    return fx+"+"+fy+"="+L(r2)
def gen(a_,b_,r2):
    return L(sp.expand((x-a_)**2+(y-b_)**2-r2))+"=0"
# ===== 例題1 3点を通る円 =====
def b1(Ps):
    l_,m_,n_=sp.symbols('l m n')
    eqs=[p[0]**2+p[1]**2+l_*p[0]+m_*p[1]+n_ for p in Ps]; sol=sp.solve(eqs,[l_,m_,n_],dict=True)[0]
    ca=-sol[l_]/2; cb=-sol[m_]/2; r2=sp.simplify(ca**2+cb**2-sol[n_]); assert r2>0 and all(sp.simplify((p[0]-ca)**2+(p[1]-cb)**2-r2)==0 for p in Ps)
    steps=[("円の方程式を一般形でおく","<p>"+I("x^2+y^2+lx+my+n=0")+" とおき、3点の座標を代入する。</p>"+D(r"\begin{cases}"+r"\\ ".join("%d+%d+%d\\,l+(%d)m+n=0"%(p[0]**2,p[1]**2,p[0],p[1]) if False else "%s=0"%L(sp.expand(p[0]**2+p[1]**2+l_*p[0]+m_*p[1]+n_)) for p in Ps)+r"\end{cases}")),
           ("連立方程式を解く","<p>上から順に引き算して文字を減らすと</p>"+D(r"l=%s,\quad m=%s,\quad n=%s"%(L(sol[l_]),L(sol[m_]),L(sol[n_])))),
           ("標準形に直す（平方完成）",D(L(sp.expand(x**2+y**2+sol[l_]*x+sol[m_]*y+sol[n_]))+"=0")+D(cir(ca,cb,r2)))]
    prob=r"3点 $A(%d,\ %d)$、$B(%d,\ %d)$、$C(%d,\ %d)$ を通る円の方程式を求めよ。また、その中心と半径を答えよ。"%(Ps[0]+Ps[1]+Ps[2])
    return prob,steps,r"%s\qquad \text{中心 }(%s,\ %s),\ \text{半径 }%s"%(cir(ca,cb,r2),L(ca),L(cb),L(sp.sqrt(r2)))
V=[[(1,2),(5,2),(2,5)],[(0,0),(6,0),(2,4)],[(-1,1),(3,-3),(5,3)],[(2,-1),(4,5),(-2,3)],[(0,1),(4,3),(-2,-1)]]
o=[b1(v) for v in V]
build(Z,CH,"3点を通る円の方程式",o,
 r"<p>3点を通る円は <b>$x^2+y^2+lx+my+n=0$</b> とおくと、3点を代入するだけで $l,m,n$ の連立方程式になる。最後に平方完成して<b>中心と半径</b>を読む。$$x^2+y^2+lx+my+n=0\ \Rightarrow\ \left(x+\dfrac l2\right)^2+\left(y+\dfrac m2\right)^2=\dfrac{l^2+m^2-4n}4$$</p>",
 "円は3点で決まる。文字が3つ（$l,m,n$）なら、式も3本。",1)
def f1(ax):
    Ps=V[0]; l_,m_,n_=sp.symbols('l m n'); sol=sp.solve([p[0]**2+p[1]**2+l_*p[0]+m_*p[1]+n_ for p in Ps],[l_,m_,n_],dict=True)[0]
    ca=float(-sol[l_]/2); cb=float(-sol[m_]/2); r_=float(sp.sqrt(ca**2+cb**2-sol[n_])); dcirc(ax,ca,cb,r_,"#b81f36"); dpt(ax,ca,cb,"",ms=3)
    for nm,pp,dx,dy in zip("ABC",Ps,(-.5,.5,0),(-.4,-.4,.55)): dpt(ax,pp[0],pp[1],nm,dx,dy)
addfig(Z.E[0],2,plane("i222_e1",(-2,8),(-3,8),f1,size=(3.8,3.6),w=48))
# ===== 例題2 円と直線の位置関係 =====
def b2(a_,b_,r2,m_):
    N=sp.sqrt(r2*(m_*m_+1)); assert N==int(N); N=int(N); k=sp.Symbol('k'); c0=m_*a_-b_
    lo,hi=-N-c0,N-c0
    steps=[("円と直線の距離を計算する","<p>円の中心 "+I("(%d,\\ %d)"%(a_,b_))+"、半径 "+I(r"\sqrt{%d}"%r2)+"。直線を "+I("%s=0"%L(m_*x-y+k))+" と書く。</p>"+D(r"d=\dfrac{|%d\cdot%d-(%d)+k|}{\sqrt{%d^2+(-1)^2}}=\dfrac{|k%+d|}{\sqrt{%d}}"%(m_,a_,b_,m_,c0,m_*m_+1))),
           ("(1) 異なる2点で交わる $\\iff d<r$","<p>"+I(r"\dfrac{|k%+d|}{\sqrt{%d}}<\sqrt{%d}"%(c0,m_*m_+1,r2))+" の両辺に "+I(r"\sqrt{%d}"%(m_*m_+1))+" を掛けて</p>"+D(r"|k%+d|<\sqrt{%d}=%d"%(c0,r2*(m_*m_+1),N))+D(r"%d<k%+d<%d\ \Rightarrow\ %d<k<%d"%(-N,c0,N,lo,hi))),
           ("(2) 接する $\\iff d=r$",D(r"|k%+d|=%d\ \Rightarrow\ k=%d,\ %d"%(c0,N,lo,hi))),
           ("(3) 共有点なし $\\iff d>r$",D(r"k<%d,\ %d<k"%(lo,hi)))]
    prob=r"円 $%s$ と直線 $y=%sx+k$ について、(1) 異なる2点で交わる (2) 接する (3) 共有点をもたない ような定数 $k$ の値の範囲（(2) は値）を求めよ。"%(cir(a_,b_,r2),L(m_))
    return prob,steps,r"\text{(1) }%d<k<%d\quad \text{(2) }k=%d,\ %d\quad \text{(3) }k<%d,\ %d<k"%(lo,hi,lo,hi,lo,hi)
V=[(0,0,20,2),(1,-1,8,1),(2,1,5,2),(0,0,45,2),(-1,2,18,1)]
o=[b2(*v) for v in V]
build(Z,CH,"円と直線の位置関係",o,
 r"<p>円の半径 $r$ と、中心から直線までの距離 $d$ を比べる。$$d<r:\text{異なる2点},\quad d=r:\text{接する},\quad d>r:\text{共有点なし}$$ 距離は $d=\dfrac{|ax_0+by_0+c|}{\sqrt{a^2+b^2}}$。連立して判別式を使う方法もあるが、計算は距離のほうが軽い。</p>",
 "中心から直線までの「近さ」と、半径の「長さ」の勝負。近ければ2点、ちょうどなら接する、遠ければ交わらない。",2)
def f2(ax):
    a_,b_,r2,m_=V[0]; N=10; xr,yr=(-8,8),(-8,8)
    dcirc(ax,a_,b_,float(sp.sqrt(r2)),"#333")
    for kk,col,ls in ((N,"#b81f36","-"),(-N,"#b81f36","-"),(0,"#1f6fb8","--"),(14,"#999","--")):
        dline(ax,m_,-1,kk,xr,yr,col=col,ls=ls,lw=1.5)
    ax.text(-3.3,6.0,"k=10",fontsize=9,color="#b81f36"); ax.text(1.5,-6.4,"k=-10",fontsize=9,color="#b81f36")
addfig(Z.E[1],0,plane("i222_e2",(-8,8),(-8,8),f2,size=(3.8,3.6),w=48,step=2))
# ===== 例題3 円の接線 =====
def b3(r2,Pc,Pe):
    assert Pc[0]**2+Pc[1]**2==r2
    p_,q_=Pe; A2=p_*p_-r2; B2=-2*p_*q_; C2=q_*q_-r2; disc=B2*B2-4*A2*C2; sq=sp.sqrt(disc); assert sq==int(sq)
    ms=sorted([sp.Rational(-B2+sq,2*A2),sp.Rational(-B2-sq,2*A2)]); lines=[]
    for mm in ms:
        lines.append(lineeq(mm,-1,q_-mm*p_))
        # 接する確認
        assert sp.simplify(abs(lines[-1][2])**2-r2*(lines[-1][0]**2+lines[-1][1]**2))==0
    steps=[("(1) 円周上の点での接線","<p>円 "+I("x^2+y^2=r^2")+" 上の点 "+I("(x_0,y_0)")+" での接線は "+I("x_0x+y_0y=r^2")+"。</p>"+D(r"%d x+%d y=%d"%(Pc[0],Pc[1],r2))+"<p>整理して</p>"+D(leq(Pc[0],Pc[1],-r2))),
           ("(2) 傾きを $m$ として距離の条件を使う","<p>点 "+I("(%d,\\ %d)"%Pe)+" を通る直線を "+I("y-(%d)=m(x-(%d))"%(q_,p_))+"、すなわち</p>"+D(r"mx-y%+d=0"%(q_-p_*sp.Symbol('m')).__class__(0) if False else r"mx-y+(%s)=0"%L(q_-sp.Symbol('m')*p_))+"<p>接する条件：中心 "+I("O")+" との距離が半径 "+I(r"\sqrt{%d}"%r2)+"。</p>"+D(r"\dfrac{|%s|}{\sqrt{m^2+1}}=\sqrt{%d}"%(L(q_-sp.Symbol('m')*p_),r2))),
           ("2乗して $m$ の2次方程式を解く","<p>両辺を2乗して分母を払う：</p>"+D(r"(%s)^2=%d(m^2+1)"%(L(q_-sp.Symbol('m')*p_),r2))+D(L(sp.expand(A2*sp.Symbol('m')**2+B2*sp.Symbol('m')+C2))+"=0")+D(r"m=%s,\ %s"%(L(ms[0]),L(ms[1])))),
           ("接線の方程式",D(r"y-(%d)=%s(x-(%d))\ \Rightarrow\ %s"%(q_,"("+L(ms[0])+")",p_,leq(*lines[0])))+D(r"y-(%d)=%s(x-(%d))\ \Rightarrow\ %s"%(q_,"("+L(ms[1])+")",p_,leq(*lines[1]))))]
    prob=r"円 $x^2+y^2=%d$ について、(1) 円周上の点 $(%d,\ %d)$ における接線の方程式 (2) 円の外部の点 $(%d,\ %d)$ から引いた2本の接線の方程式 を求めよ。"%(r2,Pc[0],Pc[1],Pe[0],Pe[1])
    return prob,steps,r"\text{(1) }%s\qquad \text{(2) }%s,\ \ %s"%(leq(Pc[0],Pc[1],-r2),leq(*lines[0]),leq(*lines[1]))
V=[(5,(1,2),(3,1)),(10,(1,3),(5,5)),(20,(2,4),(5,0)),(8,(2,2),(4,0)),(13,(2,3),(5,1))]
o=[b3(*v) for v in V]
build(Z,CH,"円の接線",o,
 r"<p>・円 $x^2+y^2=r^2$ 上の点 $(x_0,y_0)$ での接線：$x_0x+y_0y=r^2$<br>・円外の点から引く接線：傾き $m$ とおき、<b>中心と直線の距離 $=$ 半径</b> で $m$ を決める。</p>",
 "接線は「円にちょうど触れる直線」。触れる＝中心からの距離が半径に等しい。",3)
def f3(ax):
    r2,Pc,Pe=V[0]; dcirc(ax,0,0,float(sp.sqrt(r2)),"#333"); xr,yr=(-4,7),(-4,6)
    dline(ax,2,-1,-5,xr,yr); dline(ax,1,2,-5,xr,yr); dline(ax,Pc[0],Pc[1],-r2,xr,yr,col="#1f6fb8")
    dpt(ax,Pc[0],Pc[1],"",ms=4,col="#1f6fb8"); dpt(ax,Pe[0],Pe[1],"P",.4,.45)
addfig(Z.E[2],3,plane("i222_e3",(-4,7),(-4,6),f3,size=(3.8,3.4),w=48))
# ===== 例題4 弦の長さ =====
def b4(a_,b_,r2,l):
    p_,q_,c_=l; d2=sp.Rational((p_*a_+q_*b_+c_)**2,p_*p_+q_*q_); assert r2>d2
    d=sp.sqrt(d2); ch=2*sp.sqrt(r2-d2)
    steps=[("中心から直線までの距離 $d$","<p>円の中心 "+I("(%d,\\ %d)"%(a_,b_))+"、半径 "+I(r"\sqrt{%d}"%r2)+"。</p>"+D(r"d=\dfrac{|%d\cdot%d+(%d)\cdot(%d)+(%d)|}{\sqrt{%d^2+(%d)^2}}=\dfrac{%d}{\sqrt{%d}}=%s"%(p_,a_,q_,b_,c_,p_,q_,abs(p_*a_+q_*b_+c_),p_*p_+q_*q_,L(d)))),
           ("三平方の定理で弦の半分を求める","<p>弦の中点と中心を結ぶと垂直。半径 "+I("r")+"、距離 "+I("d")+"、弦の半分 "+I(r"\dfrac{l}2")+" が直角三角形をつくる。</p>"+D(r"\left(\dfrac l2\right)^2=r^2-d^2=%d-%s=%s"%(r2,L(d2),L(r2-d2)))),
           ("弦の長さ",D(r"l=2\sqrt{%s}=%s"%(L(r2-d2),L(ch))))]
    prob=r"円 $%s$ が直線 $%s=0$ から切り取る弦の長さを求めよ。"%(cir(a_,b_,r2),poly([(p_,"x"),(q_,"y"),(c_,"")]))
    return prob,steps,r"%s"%L(ch)
V=[(0,0,25,(3,4,-15)),(1,-2,20,(1,2,-3)),(0,0,25,(4,-3,10)),(2,1,16,(3,-4,2)),(-1,3,18,(1,1,-1))]
o=[b4(*v) for v in V]
build(Z,CH,"円が直線から切り取る弦の長さ",o,
 r"<p>弦の長さは<b>直角三角形</b>で求める。中心から弦に下ろした垂線の足は弦の中点。$$\left(\dfrac l2\right)^2+d^2=r^2\ \Rightarrow\ l=2\sqrt{r^2-d^2}$$ 連立して交点を求めなくてよい。</p>",
 "弦を半分にして、中心から垂線を引く。直角三角形の三平方の定理だけで終わる。",4)
def f4(ax):
    a_,b_,r2,l=V[0]; dcirc(ax,a_,b_,5,"#333"); xr,yr=(-7,7),(-7,7); dline(ax,*l,xr,yr)
    ax.plot([0,1.8*1],[0,1.8*4/3*1],color="#555",lw=0)
    ax.plot([0,1.8],[0,2.4],color="#1f6fb8",lw=1.4,ls="--"); dpt(ax,0,0,"O",-.4,-.4,ms=3)
    ax.text(.55,1.5,"d",fontsize=11,color="#1f6fb8")
addfig(Z.E[3],1,plane("i222_e4",(-7,7),(-7,7),f4,size=(3.8,3.6),w=48,step=2))
# ===== 例題5 2円の交点 =====
def b5(r1,a_,b_,R2):
    dist2=a_*a_+b_*b_; assert (sp.sqrt(r1)-sp.sqrt(R2))**2<dist2<(sp.sqrt(r1)+sp.sqrt(R2))**2
    C1=sp.expand(x**2+y**2-r1); C2=sp.expand((x-a_)**2+(y-b_)**2-R2); dif=sp.expand(C1-C2); ln=lineeq(dif.coeff(x,1),dif.coeff(y,1),dif.subs({x:0,y:0}))
    d2=sp.Rational((ln[2])**2,ln[0]**2+ln[1]**2); ch=2*sp.sqrt(r1-d2)
    steps=[("2つの円の方程式を展開する",D(r"C_1:\ %s=0,\qquad C_2:\ %s=0"%(L(C1),L(C2)))),
           ("共通弦の方程式（2式の差）","<p>2つの円の交点は両方の式を満たすので、2式の差も満たす。2次の項が消えて<b>直線</b>になる。</p>"+D("("+L(C1)+")-("+L(C2)+")=0\\ \\Rightarrow\\ "+L(dif)+"=0")+"<p>整理して</p>"+D(leq(*ln))),
           ("共通弦の長さ","<p>円 "+I("C_1")+"（中心 "+I("O")+"、半径 "+I(r"\sqrt{%d}"%r1)+"）と共通弦の距離：</p>"+D(r"d=\dfrac{|%d|}{\sqrt{%d^2+%d^2}}=%s"%(ln[2],ln[0],ln[1],L(sp.sqrt(d2))))+D(r"l=2\sqrt{r^2-d^2}=2\sqrt{%d-%s}=%s"%(r1,L(d2),L(ch))))]
    prob=r"2つの円 $C_1:\ x^2+y^2=%d$、$C_2:\ %s$ は2点で交わる。(1) 2つの交点を通る直線の方程式 (2) 2つの交点を結ぶ線分（共通弦）の長さ を求めよ。"%(r1,cir(a_,b_,R2))
    return prob,steps,r"\text{(1) }%s\qquad \text{(2) }%s"%(leq(*ln),L(ch))
V=[(10,2,1,5),(25,3,4,25),(13,2,-1,10),(20,4,2,10),(8,2,2,8)]
o=[b5(*v) for v in V]
build(Z,CH,"2つの円の共通弦",o,
 r"<p>2円 $f=0,\ g=0$ が2点で交わるとき、$$f-g=0$$ は<b>2交点を通る直線</b>（共通弦）。2次の項が消えるからである。共通弦の長さは、中心から共通弦までの距離を使って $2\sqrt{r^2-d^2}$。</p>",
 "交点は両方の円に乗っている点。だから「引き算」しても0のまま。残った1次式が交点を通る直線。",5)
def f5(ax):
    r1,a_,b_,R2=V[0]; dcirc(ax,0,0,float(sp.sqrt(r1)),"#333"); dcirc(ax,a_,b_,float(sp.sqrt(R2)),"#1f6fb8"); dline(ax,2,1,-5,(-4,6),(-4,6)); dpt(ax,0,0,"O",-.4,-.4,ms=3); dpt(ax,a_,b_,"",ms=3,col="#1f6fb8")
addfig(Z.E[4],1,plane("i222_e5",(-4,6),(-4,6),f5,size=(3.8,3.6),w=48))
UNIT=finish(Z,CH,1,1,"図形と方程式","円","円の方程式、直線との位置関係、接線、弦の長さ、2円の共通弦まで、図形と方程式の中心となる円を鍛える難問に挑みます。")
