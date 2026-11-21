# -*- coding: utf-8 -*-
from bh import *
Z=U_(); CH=[]
R=sp.Rational
_c=[0]
def vf(name,xr,yr,draw,size=(3.8,3.4),w=48): return plane(name,xr,yr,draw,size=size,w=w)
def arrow(ax,p,q,col="#b81f36",lab="",dx=.15,dy=.15):
    ax.annotate("",xy=q,xytext=p,arrowprops=dict(arrowstyle="-|>",lw=2,color=col,shrinkA=0,shrinkB=0))
    if lab: ax.text(q[0]+dx,q[1]+dy,lab,fontsize=11,color=col)
def v(a): return r"\left(%s,\ %s\right)"%(L(a[0]),L(a[1]))
ANG={R(1,2):(r"\dfrac{\pi}{3}",60),R(-1,2):(r"\dfrac{2\pi}{3}",120),sp.sqrt(2)/2:(r"\dfrac{\pi}{4}",45),-sp.sqrt(2)/2:(r"\dfrac{3\pi}{4}",135),sp.Integer(0):(r"\dfrac{\pi}{2}",90),sp.sqrt(3)/2:(r"\dfrac{\pi}{6}",30)}
# 例題1 内積・なす角
def b1(a,b):
    ip=a[0]*b[0]+a[1]*b[1]; na=sp.sqrt(a[0]**2+a[1]**2); nb=sp.sqrt(b[0]**2+b[1]**2); c=sp.nsimplify(sp.simplify(ip/(na*nb))); c=sp.radsimp(c)
    key=[k for k in ANG if sp.simplify(k-c)==0]; assert key,(a,b,c); th,deg=ANG[key[0]]
    _c[0]+=1; xs=[0,a[0],b[0]]; ys=[0,a[1],b[1]]; xr=(min(xs)-1,max(xs)+1.5); yr=(min(ys)-1,max(ys)+1.5)
    def dr(ax): arrow(ax,(0,0),a,"#b81f36",r"$\vec{a}$"); arrow(ax,(0,0),b,"#1f6fb8",r"$\vec{b}$")
    fig=vf("ic11_a%d"%_c[0],xr,yr,dr)
    st=[("内積","<p>"+I(r"\vec a\cdot\vec b=a_1b_1+a_2b_2")+"。</p>"+D(r"\vec a\cdot\vec b=%s\times%s+%s\times%s=%s"%(P(a[0]),P(b[0]),P(a[1]),P(b[1]),L(ip)))),
        ("大きさ",D(r"|\vec a|=\sqrt{%s^2+%s^2}=%s,\qquad |\vec b|=\sqrt{%s^2+%s^2}=%s"%(P(a[0]),P(a[1]),L(na),P(b[0]),P(b[1]),L(nb)))),
        ("$\\cos\\theta$ を求める","<p>"+I(r"\cos\theta=\dfrac{\vec a\cdot\vec b}{|\vec a||\vec b|}")+"。</p>"+D(r"\cos\theta=\dfrac{%s}{%s\times%s}=%s"%(L(ip),L(na),L(nb),L(c)))),
        ("なす角",D(r"0^\circ\leqq\theta\leqq180^\circ\ \text{より}\ \theta=%d^\circ"%deg)+fig)]
    return r"$\vec a=%s,\ \vec b=%s$ のとき、内積 $\vec a\cdot\vec b$、$|\vec a|,\ |\vec b|$、およびなす角 $\theta$ を求めよ。"%(v(a),v(b)),st,r"\vec a\cdot\vec b=%s,\ |\vec a|=%s,\ |\vec b|=%s,\ \theta=%d^\circ"%(L(ip),L(na),L(nb),deg)
V=[((1,2),(3,1)),((2,1),(1,3)),((1,2),(-3,-1)),((2,-1),(1,-3)),((3,2),(-2,3))]
o=[b1(*x) for x in V]
build(Z,CH,"内積となす角",o,r"<p>$\vec a\cdot\vec b=a_1b_1+a_2b_2=|\vec a||\vec b|\cos\theta$。よって $\cos\theta=\dfrac{\vec a\cdot\vec b}{|\vec a||\vec b|}$。内積が $0$ なら垂直。</p>","内積は「同じ向きにどれだけ重なっているか」。重なりが大きいほど角は小さい。",1)
# 例題2 大きさと内積の条件
def b2(A,B,m,k,l):
    n2=k**2*A**2+2*k*l*m+l**2*B**2; t=sp.Symbol('t'); eq=sp.expand((sp.Integer(1)*A**2+t*m)-(m+t*B**2)*0+ (A**2 - m + t*m - t*B**2)); sol=sp.solve(A**2-m+t*(m-B**2),t)
    sol=sol[0]; assert sp.simplify((A**2-m+sol*(m-B**2)))==0
    st=[("$|k\\vec a+l\\vec b|^2$ を展開","<p>"+I(r"|k\vec a+l\vec b|^2=k^2|\vec a|^2+2kl\,\vec a\cdot\vec b+l^2|\vec b|^2")+"。</p>"+D(r"|%s\vec a%s\vec b|^2=%d\cdot%d+%d\cdot%d+%d\cdot%d=%d"%(cf(k),("+" if l>0 else "")+cf(l),k**2,A**2,2*k*l,m,l**2,B**2,n2))),
        ("大きさを求める",D(r"|%s\vec a%s\vec b|=\sqrt{%d}=%s"%(cf(k),("+" if l>0 else "")+cf(l),n2,L(sp.sqrt(n2))))),
        ("垂直条件","<p>"+I(r"(\vec a+t\vec b)\cdot(\vec a-\vec b)=0")+" を展開する。</p>"+D(r"|\vec a|^2-\vec a\cdot\vec b+t\,\vec a\cdot\vec b-t|\vec b|^2=0")+D(r"%d-%d+%d\,t-%d\,t=0\ \Rightarrow\ %s\,t=%s"%(A**2,m,m,B**2,L(m-B**2),L(m-A**2)))+D(r"t=%s"%L(sol)))]
    return r"$|\vec a|=%d,\ |\vec b|=%d,\ \vec a\cdot\vec b=%d$ のとき、(1) $|%s\vec a%s\vec b|$ (2) $\vec a+t\vec b$ と $\vec a-\vec b$ が垂直になる $t$ の値を求めよ。"%(A,B,m,cf(k),("+" if l>0 else "")+cf(l)),st,r"\text{(1) }%s\quad\text{(2) }t=%s"%(L(sp.sqrt(n2)),L(sol))
V=[(2,3,1,2,-1),(3,2,2,1,2),(2,4,3,3,-1),(4,3,5,2,1),(3,5,4,1,-2)]
o=[b2(*x) for x in V]
build(Z,CH,"ベクトルの大きさと垂直条件",o,r"<p>大きさは<b>2乗して展開</b>：$|k\vec a+l\vec b|^2=k^2|\vec a|^2+2kl\,\vec a\cdot\vec b+l^2|\vec b|^2$。垂直は <b>内積 $=0$</b>。</p>","ベクトルの大きさは、2乗して「自分自身との内積」にして展開する。",2)
# 例題3 交点の位置ベクトル
def b3(c,d):
    c=R(c); d=R(d); u,vv=sp.symbols('u v'); s=sp.solve([sp.Eq(1-u,vv*c),sp.Eq(u*d,1-vv)],[u,vv]); uu=s[u]; va=s[vv]
    pa=1-uu; pb=uu*d; assert pa==va*c and pb==1-va
    a_=(4,0); b_=(1,3); Cp=(c*a_[0],c*a_[1]); Dp=(d*b_[0],d*b_[1]); Pp=(pa*a_[0]+pb*b_[0],pa*a_[1]+pb*b_[1])
    _c[0]+=1
    def dr(ax):
        pts=[(0,0),a_,b_]; ax.fill([p_[0] for p_ in pts],[p_[1] for p_ in pts],color="#fbe9ec",zorder=0)
        for p1,p2 in [((0,0),a_),((0,0),b_),(a_,b_)]: ax.plot([p1[0],p2[0]],[p1[1],p2[1]],color="#333",lw=1.4)
        ax.plot([a_[0],Dp[0]],[a_[1],Dp[1]],color="#b81f36",lw=1.8); ax.plot([b_[0],Cp[0]],[b_[1],Cp[1]],color="#1f6fb8",lw=1.8)
        for nm,p_,dx,dy in [("O",(0,0),-.3,-.3),("A",a_,.1,-.3),("B",b_,.0,.15),("C",Cp,0,-.3),("D",Dp,-.3,.0),("P",Pp,.1,.1)]: ax.plot(*p_,"o",color="#222",ms=4); ax.text(p_[0]+dx,p_[1]+dy,nm,fontsize=11)
    fig=plane("ic11_c%d"%_c[0],(-1,5),(-1,4),dr,size=(3.8,3.2),w=46,grid=False)
    st=[("点を位置ベクトルで表す","<p>"+I(r"\overrightarrow{OA}=\vec a,\ \overrightarrow{OB}=\vec b")+" とすると</p>"+D(r"\overrightarrow{OC}=%s\vec a,\qquad \overrightarrow{OD}=%s\vec b"%(L(c),L(d)))),
        ("直線 $AD$ 上の点として表す","<p>"+I(r"AP:PD=u:(1-u)")+" とおくと（$\\overrightarrow{OP}=(1-u)\\overrightarrow{OA}+u\\overrightarrow{OD}$）</p>"+D(r"\overrightarrow{OP}=(1-u)\vec a+%s\,u\,\vec b\quad\cdots①"%L(d))),
        ("直線 $BC$ 上の点として表す","<p>"+I(r"BP:PC=v:(1-v)")+" とおくと</p>"+D(r"\overrightarrow{OP}=%s\,v\,\vec a+(1-v)\vec b\quad\cdots②"%L(c))),
        ("係数を比較する","<p>$\\vec a,\\vec b$ は一次独立なので、①②の係数が等しい。</p>"+D(r"\begin{cases}1-u=%s\,v\\ %s\,u=1-v\end{cases}"%(L(c),L(d)))+D(r"u=%s,\quad v=%s"%(L(uu),L(va)))),
        ("答え",D(r"\overrightarrow{OP}=%s\vec a+%s\vec b"%(L(pa),L(pb)))+fig)]
    return r"△$OAB$ で、辺 $OA$ 上に $OC=%s\,OA$ となる点 $C$、辺 $OB$ 上に $OD=%s\,OB$ となる点 $D$ をとる。$AD$ と $BC$ の交点を $P$ とするとき、$\overrightarrow{OP}$ を $\vec a=\overrightarrow{OA}$、$\vec b=\overrightarrow{OB}$ で表せ。"%(L(c),L(d)),st,r"\overrightarrow{OP}=%s\vec a+%s\vec b"%(L(pa),L(pb))
V=[(R(1,2),R(1,3)),(R(2,3),R(1,2)),(R(1,3),R(3,4)),(R(3,4),R(2,3)),(R(1,2),R(1,2))]
o=[b3(*x) for x in V]
build(Z,CH,"2直線の交点の位置ベクトル",o,r"<p>交点 $P$ を<b>2通りに表す</b>：①$AD$ 上の点として $(1-u)\vec a+u\overrightarrow{OD}$、②$BC$ 上の点として $v\overrightarrow{OC}+(1-v)\vec b$。$\vec a,\vec b$ は一次独立なので<b>係数を比較</b>して $u,v$ を求める。</p>","同じ場所への行き方を2通り書いて、「$\\vec a$ の歩数」「$\\vec b$ の歩数」を比べる。",3)
# 例題4 法線ベクトルと直線
def b4(A,n):
    c=-(n[0]*A[0]+n[1]*A[1]); eq=n[0]*x+n[1]*sp.Symbol('y')+c; dist=sp.Abs(c)/sp.sqrt(n[0]**2+n[1]**2); dist=sp.radsimp(dist)
    Y=sp.Symbol('y')
    _c[0]+=1
    def dr(ax):
        xr=(-6,6); ys=[(-c-n[0]*t)/n[1] for t in xr]; ax.plot(list(xr),ys,color="#b81f36",lw=1.8)
        ax.plot(*A,"o",color="#222",ms=4); ax.text(A[0]+.15,A[1]+.15,"A",fontsize=11); arrow(ax,A,(A[0]+n[0]*.6,A[1]+n[1]*.6),"#1f6fb8",r"$\vec n$")
    fig=plane("ic11_d%d"%_c[0],(-5,5),(-5,5),dr,size=(3.6,3.4),w=44)
    st=[("法線ベクトルとの垂直条件","<p>直線上の点 "+I("P(x,y)")+" について "+I(r"\overrightarrow{AP}\perp\vec n")+"、つまり</p>"+D(r"\vec n\cdot\overrightarrow{AP}=0")),
        ("成分で書く",D(r"%s(x-%s)+%s(y-%s)=0"%(P(n[0]),P(A[0]),P(n[1]),P(A[1])))+D(L(eq)+"=0")),
        ("原点からの距離","<p>"+I(r"ax+by+c=0")+" と点 "+I(r"(x_0,y_0)")+" の距離は "+I(r"\dfrac{|ax_0+by_0+c|}{\sqrt{a^2+b^2}}")+"。</p>"+D(r"\dfrac{|%s|}{\sqrt{%s^2+%s^2}}=\dfrac{%s}{\sqrt{%d}}=%s"%(L(c),P(n[0]),P(n[1]),L(abs(c)),n[0]**2+n[1]**2,L(dist)))+fig)]
    return r"点 $A%s$ を通り、$\vec n=%s$ に垂直な直線の方程式を求めよ。また、原点とこの直線の距離を求めよ。"%(v(A),v(n)),st,r"%s=0,\ \ \text{距離 }%s"%(L(eq),L(dist))
V=[((1,2),(2,1)),((3,1),(1,-2)),((-1,2),(3,2)),((2,-3),(1,1)),((0,4),(2,-1))]
o=[b4(*x) for x in V]
build(Z,CH,"法線ベクトルと直線の方程式",o,r"<p>点 $A(x_1,y_1)$ を通り法線ベクトル $\vec n=(a,b)$ の直線は $\vec n\cdot\overrightarrow{AP}=0$ から <b>$a(x-x_1)+b(y-y_1)=0$</b>。点と直線の距離は $\dfrac{|ax_0+by_0+c|}{\sqrt{a^2+b^2}}$。</p>","法線ベクトルは直線に直角に立てた棒。棒と垂直な線がすべて直線上の動点。",4)
# 例題5 面積と垂線の足
def b5(a,b):
    area=R(abs(a[0]*b[1]-a[1]*b[0]),2); na2=a[0]**2+a[1]**2; ip=a[0]*b[0]+a[1]*b[1]; k=R(ip,na2); H=(k*a[0],k*a[1])
    assert (b[0]-H[0])*a[0]+(b[1]-H[1])*a[1]==0
    _c[0]+=1
    def dr(ax):
        ax.fill([0,a[0],b[0]],[0,a[1],b[1]],color="#fbe9ec",zorder=0); arrow(ax,(0,0),a,"#b81f36",r"$A$"); arrow(ax,(0,0),b,"#1f6fb8",r"$B$")
        ax.plot([a[0],b[0]],[a[1],b[1]],color="#333",lw=1.2); ax.plot([b[0],H[0]],[b[1],H[1]],color="#333",lw=1.2,ls="--"); ax.plot(float(H[0]),float(H[1]),"o",color="#222",ms=4); ax.text(float(H[0])+.15,float(H[1])-.45,"H",fontsize=11)
    xs=[0,a[0],b[0]]; ys=[0,a[1],b[1]]
    fig=plane("ic11_e%d"%_c[0],(min(xs)-1,max(xs)+1.5),(min(ys)-1,max(ys)+1.5),dr,size=(3.8,3.4),w=46)
    st=[("面積の公式","<p>"+I(r"\triangle OAB=\dfrac12\sqrt{|\vec a|^2|\vec b|^2-(\vec a\cdot\vec b)^2}=\dfrac12|a_1b_2-a_2b_1|")+"。</p>"+D(r"S=\dfrac12\left|%s\times%s-%s\times%s\right|=%s"%(P(a[0]),P(b[1]),P(a[1]),P(b[0]),L(area)))),
        ("垂線の足 $H$ の式","<p>"+I(r"H")+" は直線 $OA$ 上にあるので "+I(r"\overrightarrow{OH}=k\vec a")+"。</p>"+D(r"\overrightarrow{BH}\cdot\vec a=0\ \Rightarrow\ (k\vec a-\vec b)\cdot\vec a=0\ \Rightarrow\ k=\dfrac{\vec a\cdot\vec b}{|\vec a|^2}")),
        ("$k$ と $H$ の座標",D(r"k=\dfrac{%s}{%d}=%s"%(L(ip),na2,L(k)))+D(r"\overrightarrow{OH}=%s%s=%s"%(L(k),v(a),v(H)))+fig)]
    return r"座標平面上に $O(0,0),\ A%s,\ B%s$ がある。△$OAB$ の面積と、$B$ から直線 $OA$ に下ろした垂線の足 $H$ の座標を求めよ。"%(v(a),v(b)),st,r"S=%s,\ H%s"%(L(area),v(H))
V=[((4,0),(1,3)),((3,1),(1,4)),((2,2),(-1,3)),((4,2),(0,3)),((3,-1),(2,4))]
o=[b5(*x) for x in V]
build(Z,CH,"面積と垂線の足",o,r"<p>$\triangle OAB=\dfrac12|a_1b_2-a_2b_1|$。垂線の足 $H$ は $\overrightarrow{OH}=k\vec a$ とおき、$\overrightarrow{BH}\perp\vec a$ （内積 $=0$）から $k=\dfrac{\vec a\cdot\vec b}{|\vec a|^2}$。</p>","$B$ から $OA$ に影を落とした位置が $H$。影の長さは内積で決まる。",5)
UNIT=finish(Z,CH,0,0,"ベクトル","平面ベクトル","内積・なす角、大きさと垂直条件、交点の位置ベクトル、直線の方程式、面積と垂線の足まで、平面ベクトルの難問に挑みます。",subject="C")
