# -*- coding: utf-8 -*-
from bh import *
Z=U_(); CH=[]
R=sp.Rational
Y=sp.Symbol('y'); _c=[0]
def ell(ax,cx,cy,a,b,col="#b81f36"):
    t=np.linspace(0,2*np.pi,400); ax.plot(cx+float(a)*np.cos(t),cy+float(b)*np.sin(t),color=col,lw=2)
def fpt(ax,p,lab="",dx=.15,dy=.15,col="#222"):
    ax.plot(float(p[0]),float(p[1]),"o",color=col,ms=4.5)
    if lab: ax.text(float(p[0])+dx,float(p[1])+dy,lab,fontsize=10,color=col)
def rng(v,m=1.5): return (-(float(v)+m),float(v)+m)
# 例題1 楕円
def b1(p,q,r):
    A=R(r,p); B=R(r,q); horiz=A>B; a2,b2=(A,B) if horiz else (B,A); c2=a2-b2; c=sp.sqrt(c2); a=sp.sqrt(a2); b=sp.sqrt(b2)
    F=[(c,0),(-c,0)] if horiz else [(0,c),(0,-c)]; V=[(a,0),(-a,0),(0,b),(0,-b)] if horiz else [(0,a),(0,-a),(b,0),(-b,0)]
    _c[0]+=1; M=float(max(a,b))
    def dr(ax):
        ell(ax,0,0,a if horiz else b,b if horiz else a)
        for f in F: fpt(ax,f,"F",.1,.15,"#1f6fb8")
    fig=plane("ic21_a%d"%_c[0],rng(M),rng(M*0.8 if False else M),dr,size=(3.6,3.4),w=44,step=max(1,int(M)//4))
    st=[("標準形に直す","<p>両辺を "+I(str(r))+" でわる。</p>"+D(r"\dfrac{x^2}{%s}+\dfrac{y^2}{%s}=1"%(L(A),L(B)))),
        ("長軸の向きと $a,\\ b$","<p>分母の大きい方が長軸。"+("$x$ 軸方向が長軸。" if horiz else "$y$ 軸方向が長軸。")+"</p>"+D(r"a^2=%s,\ b^2=%s\ \Rightarrow\ a=%s,\ b=%s"%(L(a2),L(b2),L(a),L(b)))),
        ("焦点",D(r"c=\sqrt{a^2-b^2}=\sqrt{%s-%s}=%s"%(L(a2),L(b2),L(c)))+D(r"F\,%s,\quad F'\,%s"%(pt(*F[0]),pt(*F[1])))),
        ("長軸・短軸の長さ",D(r"\text{長軸 }2a=%s,\qquad \text{短軸 }2b=%s"%(L(2*a),L(2*b)))+fig)]
    return r"楕円 $%dx^2+%dy^2=%d$ の焦点の座標と、長軸・短軸の長さを求めよ。"%(p,q,r),st,r"\text{焦点 }%s,\ %s;\ \text{長軸 }%s,\ \text{短軸 }%s"%(pt(*F[0]),pt(*F[1]),L(2*a),L(2*b))
V=[(4,9,36),(25,9,225),(9,25,225),(1,4,16),(3,2,6)]
o=[b1(*x) for x in V]
build(Z,CH,"楕円の焦点と軸",o,r"<p>$\dfrac{x^2}{a^2}+\dfrac{y^2}{b^2}=1$ で $a>b>0$ のとき、焦点 $(\pm c,0)$、$c=\sqrt{a^2-b^2}$、長軸 $2a$、短軸 $2b$。<b>分母の大きい方が長軸の向き</b>（$y^2$ の方が大きければ焦点は $y$ 軸上）。</p>","楕円は丸をつぶした形。長く伸びた方向に焦点が2つ並ぶ。",1)
# 例題2 双曲線
def b2(A,B,orient):
    A=sp.Integer(A); B=sp.Integer(B); a=sp.sqrt(A); b=sp.sqrt(B); c=sp.sqrt(A+B)
    F=[(c,0),(-c,0)] if orient=='x' else [(0,c),(0,-c)]
    sl=(b/a if orient=='x' else a/b)
    eq=(B*X_**2-A*Y**2==A*B) if False else None
    X_=sp.Symbol('x')
    lhs=(B*X_**2-A*Y**2) if orient=='x' else (A*Y**2-B*X_**2)
    _c[0]+=1; M=float(c)+1
    def dr(ax):
        t=np.linspace(-2.2,2.2,400)
        if orient=='x':
            for sg in (1,-1): ax.plot(sg*float(a)*np.cosh(t),float(b)*np.sinh(t),color="#b81f36",lw=2)
        else:
            for sg in (1,-1): ax.plot(float(b)*np.sinh(t),sg*float(a)*np.cosh(t),color="#b81f36",lw=2)
        xs=np.array([-M,M]); ax.plot(xs,float(sl)*xs,color="#1f6fb8",ls="--",lw=1.2); ax.plot(xs,-float(sl)*xs,color="#1f6fb8",ls="--",lw=1.2)
        for f in F: fpt(ax,f,"F",.1,.15,"#1f6fb8")
    fig=plane("ic21_b%d"%_c[0],rng(M),rng(M),dr,size=(3.6,3.4),w=44)
    st=[("標準形に直す","<p>両辺を "+I(str(A*B))+" でわる。</p>"+D((r"\dfrac{x^2}{%s}-\dfrac{y^2}{%s}=1" if orient=='x' else r"-\dfrac{x^2}{%s}+\dfrac{y^2}{%s}=1")%((L(A),L(B)) if orient=='x' else (L(B),L(A))))),
        ("$a,\\ b$ と焦点","<p>"+("$x^2$ が正の項なので焦点は $x$ 軸上。" if orient=='x' else "$y^2$ が正の項なので焦点は $y$ 軸上。")+"</p>"+D(r"a^2=%s,\ b^2=%s,\quad c=\sqrt{a^2+b^2}=\sqrt{%s}=%s"%(L(A),L(B),L(A+B),L(c)))+D(r"F\,%s,\quad F'\,%s"%(pt(*F[0]),pt(*F[1])))),
        ("漸近線","<p>右辺の $1$ を $0$ にして因数分解する。</p>"+D(r"y=\pm%sx"%cf(sl) if False else r"y=\pm%s\,x"%L(sl))+fig)]
    return r"双曲線 $%s=%s$ の焦点の座標と漸近線の方程式を求めよ。"%(L(lhs),L(A*B)),st,r"\text{焦点 }%s,\ %s;\ \text{漸近線 }y=\pm%s\,x"%(pt(*F[0]),pt(*F[1]),L(sl))
X=sp.Symbol('x')
V=[(9,4,'x'),(16,9,'x'),(9,16,'y'),(1,3,'x'),(4,5,'x')]
o=[b2(*x_) for x_ in V]
build(Z,CH,"双曲線の焦点と漸近線",o,r"<p>$\dfrac{x^2}{a^2}-\dfrac{y^2}{b^2}=1$：焦点 $(\pm c,0)$、$c=\sqrt{a^2+b^2}$（<b>楕円と違い和</b>）、漸近線 $y=\pm\dfrac bax$。$y^2$ が正の項なら焦点は $y$ 軸上、漸近線は $y=\pm\dfrac abx$。</p>","双曲線は2つに割れた曲線。遠くでは漸近線にどんどん近づく。",2)
# 例題3 放物線の軌跡
def b3(F,m,orient):
    if orient=='x':
        h=R(F[0]+m,2); p=R(F[0]-m,2); eq=(Y-F[1])**2-4*p*(X-h); form=r"(y-%s)^2=%s(x-%s)"%(P(F[1]),L(4*p),P(h))
        d_=lambda P_: abs(P_[0]-m)
    else:
        h=R(F[1]+m,2); p=R(F[1]-m,2); eq=(X-F[0])**2-4*p*(Y-h); form=r"(x-%s)^2=%s(y-%s)"%(P(F[0]),L(4*p),P(h))
        d_=lambda P_: abs(P_[1]-m)
    for tt in (-2,-1,0,1,2,3):
        if orient=='x': xx=sp.Rational(tt,1)*0+(h+ R(tt**2,4*p)*0); 
    # 数値検証
    import math
    for tt in np.linspace(-4,4,9):
        if orient=='x': yy=float(F[1])+tt; xx=float(h)+tt**2/(4*float(p)); Pp=(xx,yy)
        else: xx=float(F[0])+tt; yy=float(h)+tt**2/(4*float(p)); Pp=(xx,yy)
        assert abs(math.hypot(Pp[0]-F[0],Pp[1]-F[1])-d_(Pp))<1e-9
    _c[0]+=1
    def dr(ax):
        t=np.linspace(-4,4,300)
        if orient=='x': ax.plot(float(h)+t**2/(4*float(p)),float(F[1])+t,color="#b81f36",lw=2); ax.plot([m,m],[-6,6],color="#1f6fb8",ls="--",lw=1.4)
        else: ax.plot(float(F[0])+t,float(h)+t**2/(4*float(p)),color="#b81f36",lw=2); ax.plot([-6,6],[m,m],color="#1f6fb8",ls="--",lw=1.4)
        fpt(ax,F,"F",.15,.15,"#1f6fb8")
    fig=plane("ic21_c%d"%_c[0],(-5,6),(-4,5),dr,size=(3.8,3.2),w=46)
    dl=("x=%s"%L(m)) if orient=='x' else ("y=%s"%L(m))
    dist=r"\sqrt{(x-%s)^2+(y-%s)^2}"%(P(F[0]),P(F[1]))
    rhs=(r"|x-%s|"%P(m)) if orient=='x' else (r"|y-%s|"%P(m))
    st=[("条件を式にする","<p>動点 "+I("P(x,y)")+" について、焦点 $F$ までの距離 $=$ 準線までの距離。</p>"+D(dist+"="+rhs)),
        ("両辺を2乗する",D(r"(x-%s)^2+(y-%s)^2=(%s)^2"%(P(F[0]),P(F[1]),L(X-m) if orient=='x' else L(Y-m)))),
        ("整理する","<p>共通の2乗の項が消える。</p>"+D(form)+"<p>頂点 "+I(pt(h,F[1]) if orient=='x' else pt(F[0],h))+"、"+I("p=%s"%L(p))+"。</p>"+fig)]
    return r"点 $F%s$ からの距離と、直線 $%s$ からの距離が等しい点 $P$ の軌跡の方程式を求めよ。"%(pt(*F),dl),st,form
V=[((1,0),-1,'x'),((2,1),0,'x'),((0,2),-2,'y'),((1,3),1,'y'),((-1,0),-3,'x')]
o=[b3(*x_) for x_ in V]
build(Z,CH,"放物線（焦点と準線）",o,r"<p>放物線は<b>焦点 $F$ までの距離 $=$ 準線までの距離</b>の点の軌跡。$P(x,y)$ として式を作り<b>両辺を2乗</b>。標準形は $y^2=4px$（焦点 $(p,0)$、準線 $x=-p$）。</p>","焦点という「点」と準線という「線」から等距離を保って動く点が放物線を描く。",3)
# 例題4 楕円の定義
def b4(c,a,orient):
    c=sp.Integer(c); a=sp.Integer(a); b2=a**2-c**2; b=sp.sqrt(b2)
    F=[(c,0),(-c,0)] if orient=='x' else [(0,c),(0,-c)]
    import math
    for th in np.linspace(0,6.28,9):
        px=float(a)*math.cos(th) if orient=='x' else float(b)*math.cos(th); py=float(b)*math.sin(th) if orient=='x' else float(a)*math.sin(th)
        assert abs(math.hypot(px-F[0][0],py-F[0][1])+math.hypot(px-F[1][0],py-F[1][1])-2*float(a))<1e-9
    eqs=(r"\dfrac{x^2}{%s}+\dfrac{y^2}{%s}=1"%(L(a**2),L(b2))) if orient=='x' else (r"\dfrac{x^2}{%s}+\dfrac{y^2}{%s}=1"%(L(b2),L(a**2)))
    _c[0]+=1; M=float(a)+1
    def dr(ax):
        ell(ax,0,0,a if orient=='x' else b,b if orient=='x' else a)
        for f in F: fpt(ax,f,"F",.1,.15,"#1f6fb8")
    fig=plane("ic21_d%d"%_c[0],rng(M),rng(M),dr,size=(3.6,3.4),w=44,step=max(1,int(M)//4))
    st=[("楕円の定義から $a$","<p>2定点 $F,F'$ からの距離の和が一定 "+I("2a")+" の点の軌跡が楕円。</p>"+D(r"2a=%s\ \Rightarrow\ a=%s"%(L(2*a),L(a)))),
        ("$b$ を求める","<p>焦点が "+I(r"(%s)"%("\\pm%s,\\ 0"%L(c) if orient=='x' else "0,\\ \\pm%s"%L(c)))+"。"+I("c=%s"%L(c))+" とおくと</p>"+D(r"b^2=a^2-c^2=%s-%s=%s"%(L(a**2),L(c**2),L(b2)))),
        ("方程式",D(eqs)+fig)]
    return r"2点 $F%s,\ F'%s$ からの距離の和が $%s$ である点 $P$ の軌跡の方程式を求めよ。"%(pt(*F[0]),pt(*F[1]),L(2*a)),st,eqs
V=[(3,5,'x'),(4,5,'x'),(5,13,'x'),(3,5,'y'),(6,10,'y')]
o=[b4(*x_) for x_ in V]
build(Z,CH,"楕円の定義と軌跡",o,r"<p>2焦点 $(\pm c,0)$ からの距離の和が $2a$（$a>c>0$）の軌跡は <b>$\dfrac{x^2}{a^2}+\dfrac{y^2}{a^2-c^2}=1$</b>。焦点が $y$ 軸上なら $x^2$ と $y^2$ の分母が入れかわる。</p>","2本のひもを焦点に結んでピンと張りながら描くと楕円。ひもの長さが $2a$。",4)
# 例題5 接線
def b5(a2,b2,x0,y0):
    a2=sp.Integer(a2); b2=sp.Integer(b2); x0=sp.nsimplify(x0); y0=sp.nsimplify(y0); assert x0**2/a2+y0**2/b2==1
    cx=x0/a2; cy=y0/b2; lhs=cx*X+cy*Y; k=sp.lcm(sp.denom(cx),sp.denom(cy)); ln=sp.expand(lhs*k); 
    yy=sp.solve(sp.Eq(lhs,1),Y)[0]
    _c[0]+=1; M=float(sp.sqrt(a2))+1.5; Mb=float(sp.sqrt(b2))+1.5
    def dr(ax):
        ell(ax,0,0,sp.sqrt(a2),sp.sqrt(b2)); xs=np.array([-M,M]); f_=sp.lambdify(X,yy,"numpy"); ax.plot(xs,f_(xs)*np.ones(2),color="#1f6fb8",lw=1.6); fpt(ax,(x0,y0),"P",.15,.15)
    fig=plane("ic21_e%d"%_c[0],(-M,M),(-Mb,Mb),dr,size=(3.8,3.2),w=46,step=max(1,int(M)//4))
    st=[("接線の公式","<p>楕円 "+I(r"\dfrac{x^2}{a^2}+\dfrac{y^2}{b^2}=1")+" 上の点 "+I("(x_0,y_0)")+" での接線は</p>"+D(r"\dfrac{x_0x}{a^2}+\dfrac{y_0y}{b^2}=1")),
        ("代入する",D(r"\dfrac{%s\cdot x}{%s}+\dfrac{%s\cdot y}{%s}=1"%(P(x0),L(a2),P(y0),L(b2)))+D(L(lhs)+"=1")),
        ("整理する","<p>分母をはらう（両辺に "+I(str(k))+" をかける）。</p>"+D(L(ln)+"=%s"%L(k))+D(r"y=%s"%L(sp.expand(yy)))+fig)]
    return r"楕円 $\dfrac{x^2}{%d}+\dfrac{y^2}{%d}=1$ 上の点 $P%s$ における接線の方程式を求めよ。"%(a2,b2,pt(x0,y0)),st,r"%s=%s"%(L(ln),L(k))
V=[(9,4,R(9,5),R(8,5)),(25,9,4,R(9,5)),(25,16,3,R(16,5)),(100,36,8,R(18,5)),(169,25,12,R(25,13))]
o=[b5(*x_) for x_ in V]
build(Z,CH,"楕円上の点での接線",o,r"<p>楕円 $\dfrac{x^2}{a^2}+\dfrac{y^2}{b^2}=1$ 上の点 $(x_0,y_0)$ における接線は <b>$\dfrac{x_0x}{a^2}+\dfrac{y_0y}{b^2}=1$</b>（$x^2\to x_0x,\ y^2\to y_0y$ と置き換えた形）。</p>","$x^2$ の1つを $x_0$ に、もう1つを $x$ に置き換える。これで接線の式になる。",5)
UNIT=finish(Z,CH,1,0,"平面上の曲線と複素数平面","2次曲線","楕円・双曲線・放物線の性質、定義による軌跡、接線まで、2次曲線の難問に挑みます。",subject="C")
