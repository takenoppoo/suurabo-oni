# -*- coding: utf-8 -*-
# 軌跡と領域（数学II 図形と方程式）
from bh import *
import itertools
Z=U_(); CH=[]
def cir(a_,b_,r2):
    fx="x^2" if a_==0 else "(x%+d)^2"%(-a_); fy="y^2" if b_==0 else "(y%+d)^2"%(-b_)
    return fx+"+"+fy+"="+L(r2)
# ===== 例題1 アポロニウスの円 =====
def b1(A,B,m_,n_):
    Pp=x**2  # dummy
    AP2=(x-A[0])**2+(y-A[1])**2; BP2=(x-B[0])**2+(y-B[1])**2
    eq=sp.expand(n_**2*AP2-m_**2*BP2); co=sp.Poly(eq,x,y); c2=eq.coeff(x,2)
    eqn=sp.expand(eq/c2); ca=-eqn.coeff(x,1)/2; cb=-eqn.coeff(y,1)/2; const=eqn.subs({x:0,y:0}); r2=sp.simplify(ca**2+cb**2-const); assert r2>0
    for th in np.linspace(0,6.28,9):
        px=float(ca)+float(sp.sqrt(r2))*np.cos(th); py=float(cb)+float(sp.sqrt(r2))*np.sin(th)
        ap=np.hypot(px-A[0],py-A[1]); bp=np.hypot(px-B[0],py-B[1]); assert abs(ap*n_-bp*m_)<1e-6
    steps=[("条件を座標で表す","<p>求める点を "+I("P(x,y)")+" とおく。"+I("AP:BP=%d:%d"%(m_,n_))+" は "+I("%d\\,AP=%d\\,BP"%(n_,m_))+"。ルートを避けるため2乗する。</p>"+D(r"%d^2AP^2=%d^2BP^2"%(n_,m_))+D(r"%d\{(x%+d)^2+(y%+d)^2\}=%d\{(x%+d)^2+(y%+d)^2\}"%(n_**2,-A[0],-A[1],m_**2,-B[0],-B[1]))),
           ("展開して整理する",D(L(eq)+"=0")+"<p>"+I("x^2")+" の係数 "+I(str(c2))+" で割って</p>"+D(L(eqn)+"=0")),
           ("平方完成して円の形にする",D(cir(ca,cb,r2))+"<p>これは中心 "+I("(%s,\\ %s)"%(L(ca),L(cb)))+"、半径 "+I(L(sp.sqrt(r2)))+" の円。</p>"),
           ("答え","<p>求める軌跡は、この円全体（逆に、この円上の点は条件を満たす）。</p>")]
    prob=r"2点 $A(%d,\ %d)$、$B(%d,\ %d)$ からの距離の比が $AP:BP=%d:%d$ である点 $P$ の軌跡を求めよ。"%(A[0],A[1],B[0],B[1],m_,n_)
    return prob,steps,r"\text{中心 }(%s,\ %s),\ \text{半径 }%s\ \text{の円}:\ %s"%(L(ca),L(cb),L(sp.sqrt(r2)),cir(ca,cb,r2)),(ca,cb,r2)
V=[((-2,0),(4,0),2,1),((0,0),(6,0),1,2),((-1,0),(5,0),3,1),((0,2),(0,8),2,1),((1,1),(7,1),1,2)]
o=[b1(*v) for v in V]
build(Z,CH,"距離の比が一定の点の軌跡",[z[:3] for z in o],
 r"<p>軌跡の求め方：①求める点を $P(x,y)$ とおく ②条件を $x,y$ の式で表す ③整理して図形を判断する ④<b>逆</b>も確かめる（条件を満たす点がすべて含まれる）。距離の比が一定（$\ne1$）のとき、軌跡は<b>円</b>（アポロニウスの円）。</p>",
 "動く点の条件を、そのまま $x,y$ の式に翻訳する。式が円の形になったら、それが軌跡。",1)
ca,cb,r2=o[0][3]; A_,B_=V[0][0],V[0][1]
def f1(ax):
    dcirc(ax,float(ca),float(cb),float(sp.sqrt(r2)),"#b81f36"); dpt(ax,A_[0],A_[1],"A",0,-.55); dpt(ax,B_[0],B_[1],"B",0,-.55); dpt(ax,float(ca),float(cb),"",ms=3)
addfig(Z.E[0],2,plane("i223_e1",(-8,10),(-6,6),f1,size=(4.2,3.3),w=54,step=2))
# ===== 例題2 動点に連動する点の軌跡 =====
def b2(a_,b_,r2,m_,n_):
    # Q(s,t) は円 s^2+t^2=r2 上、P は AQ を m:n に内分
    s,t=sp.symbols('s t'); Px=(n_*a_+m_*s)/sp.Integer(m_+n_); Py=(n_*b_+m_*t)/sp.Integer(m_+n_)
    qx=((m_+n_)*x-n_*a_)/sp.Integer(m_); qy=((m_+n_)*y-n_*b_)/sp.Integer(m_)
    eq=sp.expand(qx**2+qy**2-r2); c2=eq.coeff(x,2); eqn=sp.expand(eq/c2); ca=-eqn.coeff(x,1)/2; cb=-eqn.coeff(y,1)/2; rr=sp.sqrt(sp.simplify(ca**2+cb**2-eqn.subs({x:0,y:0})))
    assert sp.simplify(rr-sp.sqrt(r2)*sp.Rational(m_,m_+n_))==0 and sp.simplify(ca-sp.Rational(n_*a_,m_+n_))==0
    steps=[("連動する2点を文字でおく","<p>"+I("P(x,y)")+"、円上の点を "+I("Q(s,t)")+" とおく。"+I("Q")+" は円上なので</p>"+D(r"s^2+t^2=%d\quad\cdots\text{①}"%r2)),
           ("$P$ を $Q$ で表す","<p>"+I("P")+" は線分 "+I("AQ")+" を "+I("%d:%d"%(m_,n_))+" に内分するから</p>"+D(r"x=\dfrac{%d\cdot%d+%d\,s}{%d},\quad y=\dfrac{%d\cdot%d+%d\,t}{%d}"%(n_,a_,m_,m_+n_,n_,b_,m_,m_+n_))+"<p>これを "+I("s,t")+" について解く：</p>"+D(r"s=\dfrac{%d x-%d}{%d},\quad t=\dfrac{%d y-%d}{%d}"%(m_+n_,n_*a_,m_,m_+n_,n_*b_,m_))),
           ("①に代入して $s,t$ を消す",D(r"\left(\dfrac{%d x-%d}{%d}\right)^2+\left(\dfrac{%d y-%d}{%d}\right)^2=%d"%(m_+n_,n_*a_,m_,m_+n_,n_*b_,m_,r2))+"<p>整理して</p>"+D(L(eqn)+"=0")+D(cir(ca,cb,rr**2))),
           ("答え","<p>中心 "+I("(%s,\\ %s)"%(L(ca),L(cb)))+"、半径 "+I(L(rr))+" の円。</p>")]
    prob=r"点 $Q$ が円 $x^2+y^2=%d$ 上を動くとき、定点 $A(%d,\ %d)$ と $Q$ を結ぶ線分 $AQ$ を $%d:%d$ に内分する点 $P$ の軌跡を求めよ。"%(r2,a_,b_,m_,n_)
    return prob,steps,r"\text{中心 }(%s,\ %s),\ \text{半径 }%s\ \text{の円}:\ %s"%(L(ca),L(cb),L(rr),cir(ca,cb,rr**2))
V=[(6,0,16,1,1),(0,6,36,1,2),(8,4,36,1,3),(-6,3,81,2,1),(9,-3,36,1,2)]
o=[b2(*v) for v in V]
build(Z,CH,"動点に連動する点の軌跡",o,
 r"<p>連動する点の軌跡は、<b>動く点 $Q(s,t)$ の条件</b>を使って<b>$s,t$ を消去</b>する。①$P(x,y)$ を $Q$ の座標で表す ②$s,t$ を $x,y$ で表す ③$Q$ の条件に代入。</p>",
 "$Q$ が円を描いて動けば、それに引っぱられて $P$ も円を描く。$P$ から逆算して $Q$ の位置を表す。",2)
def f2(ax):
    a_,b_,r2,m_,n_=V[0]; dcirc(ax,0,0,4,"#333"); dcirc(ax,3,0,2,"#b81f36"); dpt(ax,a_,b_,"A",0,-.55); dpt(ax,2,2*1.0**0 *1.7320508,"",ms=3); ax.plot([a_,0],[b_,4.0],color="#999",lw=1,ls=":")
    dpt(ax,0,4,"Q",-.4,.4); dpt(ax,3,2,"P",.45,.4)
addfig(Z.E[1],3,plane("i223_e2",(-6,9),(-6,6),f2,size=(4.0,3.3),w=52,step=2))
# ===== 例題3 領域の図示 =====
CASES=[
 dict(conds=[(lambda X,Y:X**2+Y**2-8,'<='),(lambda X,Y:Y-X,'>')],tex=[r"x^2+y^2\leqq 8",r"y>x"],
      expl=["円 $x^2+y^2=8$（中心 O、半径 $2\\sqrt2$）。原点 $(0,0)$ は $0\\leqq8$ を満たすので<b>円の内部</b>。周は含む。","直線 $y=x$。$y>x$ は<b>直線の上側</b>。直線上は含まない（破線）。"],
      ans="円 $x^2+y^2=8$ の内部と周のうち、直線 $y=x$ の上側（直線上の点は含まない）",xr=(-4,4),yr=(-4,4),bd=[('c',0,0,2*np.sqrt(2),'-'),('l',1,-1,0,'--')]),
 dict(conds=[(lambda X,Y:X**2+Y**2-9,'<'),(lambda X,Y:X**2+Y**2-1,'>=')],tex=[r"x^2+y^2<9",r"x^2+y^2\geqq 1"],
      expl=["円 $x^2+y^2=9$。原点は $0<9$ を満たすので<b>円の内部</b>。周は含まない（破線）。","円 $x^2+y^2=1$。原点は $0\\geqq1$ を満たさないので、<b>円の外部</b>と周が領域。"],
      ans="原点中心の半径3の円の内部（周を含まない）のうち、半径1の円の外部と周上の部分（ドーナツ形）",xr=(-4,4),yr=(-4,4),bd=[('c',0,0,3,'--'),('c',0,0,1,'-')]),
 dict(conds=[(lambda X,Y:Y-X**2,'>='),(lambda X,Y:Y-X-2,'<')],tex=[r"y\geqq x^2",r"y<x+2"],
      expl=["放物線 $y=x^2$。$y\\geqq x^2$ は<b>放物線の上側</b>と周上。","直線 $y=x+2$。$y<x+2$ は<b>直線の下側</b>。直線上は含まない（破線）。"],
      ans="放物線 $y=x^2$ の上側（放物線上を含む）と、直線 $y=x+2$ の下側（直線上を含まない）の共通部分",xr=(-3,4),yr=(-2,6),bd=[('p',),('l',1,-1,2,'--')]),
 dict(conds=[(lambda X,Y:(X-1)**2+(Y-1)**2-4,'<'),(lambda X,Y:X+Y-2,'>=')],tex=[r"(x-1)^2+(y-1)^2<4",r"x+y\geqq 2"],
      expl=["円 $(x-1)^2+(y-1)^2=4$（中心 $(1,1)$、半径2）の<b>内部</b>。周は含まない（破線）。","直線 $x+y=2$（円の中心を通る）。$x+y\\geqq2$ は<b>直線の上側</b>と直線上。"],
      ans="中心 $(1,1)$、半径2の円の内部（周を含まない）のうち、直線 $x+y=2$ の上側（直線上を含む）。半円板になる",xr=(-3,5),yr=(-3,5),bd=[('c',1,1,2,'--'),('l',1,1,-2,'-')]),
 dict(conds=[(lambda X,Y:(X-Y)*(X+Y-4),'>')],tex=[r"(x-y)(x+y-4)>0"],
      expl=["積が正になるのは<b>2つの因数が同符号</b>のとき。","(i) $x-y>0$ かつ $x+y-4>0$、または (ii) $x-y<0$ かつ $x+y-4<0$。直線 $y=x$、$x+y=4$ の2直線（破線）で平面が4つに分かれ、その向かい合う2つが領域。"],
      ans="2直線 $y=x$、$x+y=4$ で分けられた4つの部分のうち、右側と左側の向かい合う2つ（直線上は含まない）",xr=(-3,7),yr=(-3,7),bd=[('l',1,-1,0,'--'),('l',1,1,-4,'--')]),
]
def regfig(name,cs,w=46):
    def draw(ax):
        xr,yr=cs['xr'],cs['yr']; X,Y=np.meshgrid(np.linspace(xr[0],xr[1],500),np.linspace(yr[0],yr[1],500)); m=np.ones_like(X,dtype=bool)
        for f,op in cs['conds']:
            v=f(X,Y); m&=(v<=0) if op=='<=' else (v<0) if op=='<' else (v>=0) if op=='>=' else (v>0)
        ax.contourf(X,Y,m.astype(float),levels=[0.5,1.5],colors=["#f7c9d0"],zorder=1)
        for b in cs['bd']:
            if b[0]=='c': dcirc(ax,b[1],b[2],b[3],"#b81f36",b[4],1.6)
            elif b[0]=='l': dline(ax,b[1],b[2],b[3],xr,yr,"#b81f36",b[4],1.6)
            elif b[0]=='p':
                xs_=np.linspace(xr[0],xr[1],200); ax.plot(xs_,xs_**2,color="#b81f36",lw=1.6)
        ax.set_xlim(*xr); ax.set_ylim(*yr)
    return plane(name,cs['xr'],cs['yr'],draw,size=(3.8,3.4),w=w,step=2 if (cs['xr'][1]-cs['xr'][0])>8 else 1)
def b3(i):
    cs=CASES[i]; fig=regfig("i223_e3_%d"%i,cs)
    steps=[("各不等式の境界線を引く","<p>境界の式（等号にしたもの）をかく。不等号に「=」が"+("ある" if any(op in ('<=','>=') for _,op in cs['conds']) else "ない")+"ものは境界を含む（実線）、ないものは含まない（破線）。</p>"),
           ("各不等式の表す領域を調べる","<br>".join("("+str(j+1)+") "+I(cs['tex'][j] if j<len(cs['tex']) else "")+"：" +cs['expl'][j] if j<len(cs['expl']) and len(cs['tex'])>1 else "" for j in range(len(cs['tex']))) if len(cs['tex'])>1 else "<p>"+"</p><p>".join(cs['expl'])+"</p>"),
           ("共通部分を図示する","<p>求める領域は下の図の色をつけた部分。</p>"+fig),
           ("領域を言葉でまとめる","<p>"+cs['ans']+"。</p>")]
    prob=r"連立不等式（不等式）の表す領域を図示せよ。 $$"+(r"\begin{cases}"+r"\\ ".join(cs['tex'])+r"\end{cases}" if len(cs['tex'])>1 else cs['tex'][0])+"$$"
    return prob,steps,r"\text{図の色の部分（実線の境界は含み、破線の境界は含まない）}"
o=[b3(i) for i in range(5)]
build(Z,CH,"不等式の表す領域の図示",o,
 r"<p>領域の図示：①境界（等号の式）をかく ②各不等式の領域を<b>テスト点（原点など）</b>で調べる ③共通部分をとる ④境界を含むか（実線）含まないか（破線）を区別する。<br>$y>f(x)$ は境界の上側、$y<f(x)$ は下側。$(x-a)^2+(y-b)^2<r^2$ は円の内部。</p>",
 "不等式は「境界線で分けられた陣地」。原点がその陣地に入っているか、で判断する。",3)
# ===== 例題4 領域と最大・最小（線形計画） =====
CNT4=0
def b4(cons,f):
    a_,b_=f
    lines=[(p_,q_,r_) for p_,q_,r_ in cons]  # p x + q y <= r
    V_=set()
    for L1,L2 in itertools.combinations(lines,2):
        d=L1[0]*L2[1]-L1[1]*L2[0]
        if d==0: continue
        xx=sp.Rational(L1[2]*L2[1]-L1[1]*L2[2],d); yy=sp.Rational(L1[0]*L2[2]-L1[2]*L2[0],d)
        if all(c[0]*xx+c[1]*yy<=c[2] for c in lines): V_.add((xx,yy))
    V_=sorted(V_,key=lambda v:np.arctan2(float(v[1])-float(sum(u[1] for u in V_))/len(V_),float(v[0])-float(sum(u[0] for u in V_))/len(V_)))
    vals=[(a_*v[0]+b_*v[1],v) for v in V_]; mx=max(vals,key=lambda z:z[0]); mn=min(vals,key=lambda z:z[0]); assert sum(1 for z in vals if z[0]==mx[0])==1 and sum(1 for z in vals if z[0]==mn[0])==1
    def ineq(c): return poly([(c[0],"x"),(c[1],"y")])+r"\leqq %d"%c[2]
    def hum(c):
        if c==(-1,0,0): return r"x\geqq0"
        if c==(0,-1,0): return r"y\geqq0"
        if c[2]<0 and c[1]==0: return r"x\geqq %d"%(-c[2]) if c[0]==-1 else ineq(c)
        if c[2]<0 and c[0]==0: return r"y\geqq %d"%(-c[2]) if c[1]==-1 else ineq(c)
        return ineq(c)
    global CNT4
    CNT4+=1; nm="i223_e4_%d"%CNT4
    def draw(ax):
        xr_,yr_=(-1,10),(-1,10)
        xs_=[float(v[0]) for v in V_]+[float(V_[0][0])]; ys_=[float(v[1]) for v in V_]+[float(V_[0][1])]
        ax.fill(xs_,ys_,color="#f7c9d0",zorder=1); ax.plot(xs_,ys_,color="#b81f36",lw=1.8)
        for z,(vx,vy) in [(v,v) for v in V_]: pass
        for v in V_: dpt(ax,float(v[0]),float(v[1]),"",ms=4)
        for kk,col in ((mx[0],"#1f6fb8"),(mn[0],"#1f6fb8")):
            dline(ax,a_,b_,-kk,xr_,yr_,col=col,ls="--",lw=1.2)
        ax.set_xlim(*xr_); ax.set_ylim(*yr_)
    fig=plane(nm,(-1,10),(-1,10),draw,size=(3.8,3.6),w=48,step=2)
    vt=r",\quad ".join(r"(%s,\ %s):\ %s=%s"%(L(v[0]),L(v[1]),poly([(a_,"x"),(b_,"y")]).replace("x","\\cdot x").replace("y","\\cdot y") if False else "f",L(a_*v[0]+b_*v[1])) for v in V_)
    steps=[("領域を図示する","<p>連立不等式の表す領域は、下の図の多角形（境界を含む）。</p>"+fig),
           ("頂点の座標を求める","<p>隣り合う境界線の交点を連立方程式で求める。頂点は</p>"+D(r",\ ".join("("+L(v[0])+r",\ "+L(v[1])+")" for v in V_))),
           ("目的の式を $k$ とおく","<p>"+I("%s=k"%poly([(a_,"x"),(b_,"y")]))+" とおくと、これは傾き "+I(L(sp.Rational(-a_,b_)))+" の直線。"+I("k")+" は直線の"+("切片に比例" if b_>0 else "切片の符号が逆に比例")+"するので、この直線を平行移動して、領域と共有点をもつ範囲で "+I("k")+" の最大・最小を調べる。</p>"),
           ("最大・最小は頂点でおこる","<p>直線が領域を通る範囲の端は、必ず頂点を通るときである。各頂点での値を計算する。</p>"+D(r",\quad ".join(r"(%s,%s):\ %s"%(L(v[0]),L(v[1]),L(a_*v[0]+b_*v[1])) for v in V_))),
           ("答え","<p>最大値 "+I(L(mx[0]))+"（"+I("(%s,%s)"%(L(mx[1][0]),L(mx[1][1])))+"）、最小値 "+I(L(mn[0]))+"（"+I("(%s,%s)"%(L(mn[1][0]),L(mn[1][1])))+"）。</p>")]
    prob=r"実数 $x,\ y$ が $$"+r"\begin{cases}"+r"\\ ".join(hum(c) for c in cons)+r"\end{cases}$$ を満たすとき、$%s$ の最大値・最小値と、そのときの $(x,y)$ を求めよ。"%poly([(a_,"x"),(b_,"y")])
    return prob,steps,r"\text{最大値 }%s\ (%s,%s),\quad \text{最小値 }%s\ (%s,%s)"%(L(mx[0]),L(mx[1][0]),L(mx[1][1]),L(mn[0]),L(mn[1][0]),L(mn[1][1]))
C4=[([(-1,0,0),(0,-1,0),(1,2,8),(3,1,9)],(3,-1)),([(-1,0,-1),(0,-1,-1),(1,1,7),(2,1,10)],(1,2)),([(-1,0,0),(0,-1,0),(2,1,10),(1,3,15)],(1,-2)),([(-1,0,0),(0,-1,0),(-1,-1,-2),(1,0,4),(0,1,4)],(2,-3)),([(-1,0,0),(0,-1,0),(1,1,6),(-1,-2,-4)],(3,1))]
o=[b4(*v) for v in C4]
build(Z,CH,"領域における1次式の最大・最小",o,
 r"<p>領域内で $ax+by$ の最大・最小：<b>$ax+by=k$ とおいて直線を平行移動</b>し、領域と共有点をもつ範囲で $k$ を動かす。1次式の最大・最小は<b>領域の頂点</b>でおこる。頂点の座標を求めて、それぞれの値を比べればよい。</p>",
 "ものさしを平行にスライドさせて、領域に最後に触れる点（頂点）を探す。",4)
# ===== 例題5 円の内部での1次式の最大・最小 =====
def b5(a0,b0,R2,a_,b_):
    n2=a_*a_+b_*b_; N=sp.sqrt(R2*n2); assert N==int(N); N=int(N); c0=a_*a0+b_*b0; sc=sp.sqrt(sp.Rational(R2,n2)); assert sc==int(sc); sc=int(sc)
    kmax=c0+N; kmin=c0-N; pmax=(a0+sc*a_,b0+sc*b_); pmin=(a0-sc*a_,b0-sc*b_)
    assert (pmax[0]-a0)**2+(pmax[1]-b0)**2==R2 and a_*pmax[0]+b_*pmax[1]==kmax and a_*pmin[0]+b_*pmin[1]==kmin
    k=sp.Symbol('k'); lt=poly([(a_,"x"),(b_,"y")])
    steps=[("$%s=k$ とおく"%lt,"<p>これは直線。円の内部・周上の点が1つでも直線上にあるような "+I("k")+" の範囲を求める。</p>"+D(lt+"=k\\ \\iff\\ %s-k=0"%lt)),
           ("共有点をもつ条件（中心との距離 $\\leqq$ 半径）","<p>円の中心 "+I("(%d,\\ %d)"%(a0,b0))+"、半径 "+I(r"\sqrt{%d}"%R2)+"。</p>"+D(r"\dfrac{|%d\cdot%d+%d\cdot%d-k|}{\sqrt{%d^2+%d^2}}\leqq\sqrt{%d}"%(a_,a0,b_,b0,a_,b_,R2))+D(r"|%d-k|\leqq\sqrt{%d}\cdot\sqrt{%d}=%d"%(c0,R2,n2,N))+D(r"%d\leqq k\leqq %d"%(kmin,kmax))),
           ("最大値・最小値",D(r"\text{最大値 }%d,\quad \text{最小値 }%d"%(kmax,kmin))),
           ("そのときの $(x,y)$","<p>最大・最小になるのは直線が円に<b>接する</b>とき。接点は、中心から法線方向 "+I("(%d,\\ %d)"%(a_,b_))+" に半径だけ進んだ点。</p>"+D(r"(x,y)=(%d,\ %d)\pm\sqrt{\dfrac{%d}{%d}}\,(%d,\ %d)=(%d,\ %d)\pm%d(%d,\ %d)"%(a0,b0,R2,n2,a_,b_,a0,b0,sc,a_,b_))+D(r"\text{最大：}(%d,\ %d),\qquad \text{最小：}(%d,\ %d)"%(pmax+pmin)))]
    prob=r"実数 $x,\ y$ が $(x%+d)^2+(y%+d)^2\leqq %d$ を満たすとき、$%s$ の最大値・最小値と、そのときの $(x,y)$ を求めよ。"%(-a0,-b0,R2,lt)
    return prob,steps,r"\text{最大値 }%d\ (%d,%d),\quad \text{最小値 }%d\ (%d,%d)"%((kmax,)+pmax+(kmin,)+pmin)
V=[(1,2,5,2,1),(0,0,10,3,1),(2,-1,20,2,1),(-1,3,8,1,1),(3,1,13,3,2)]
o=[b5(*v) for v in V]
build(Z,CH,"円の内部での1次式の最大・最小",o,
 r"<p>$ax+by=k$ とおいて<b>直線と円（領域）が共有点をもつ条件</b>を考える。中心と直線の距離 $d\leqq$ 半径 から $k$ の範囲が出る。最大・最小は直線が円に<b>接する</b>とき。</p>",
 "直線をスライドさせて、円にちょうど触れる2つの位置が、最大と最小。触れるのは「距離＝半径」のとき。",5)
def f5(ax):
    a0,b0,R2,a_,b_=V[0]; dcirc(ax,a0,b0,float(np.sqrt(R2)),"#b81f36"); xr,yr=(-4,7),(-3,6)
    for kk in (9,-1): dline(ax,2,1,-kk,xr,yr,col="#1f6fb8",ls="--",lw=1.4)
    dpt(ax,a0,b0,"",ms=3); dpt(ax,3,3,"(3, 3)",.9,.45,col="#1f6fb8"); dpt(ax,-1,1,"(-1, 1)",-.9,-.45,col="#1f6fb8")
addfig(Z.E[4],3,plane("i223_e5",(-4,7),(-3,6),f5,size=(4.0,3.4),w=50))
UNIT=finish(Z,CH,1,2,"図形と方程式","軌跡と領域","距離の比が一定の軌跡、連動する点の軌跡、領域の図示、領域での最大・最小、円の内部での最大・最小まで、座標平面の総合力を問う難問に挑みます。")
