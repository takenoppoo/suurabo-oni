# -*- coding: utf-8 -*-
from bh import *
import math
Z=U_(); CH=[]
R=sp.Rational; I_=sp.I; PI=sp.pi
X,Y=sp.symbols('x y',real=True); _c=[0]
def cz(z): return L(sp.nsimplify(sp.simplify(sp.expand_complex(sp.sympify(z)))))
def polar(r,t): return sp.simplify(sp.expand_complex(r*(sp.cos(t)+I_*sp.sin(t))))
def ptx(z): z=sp.sympify(z); return (float(sp.re(z)),float(sp.im(z)))
def pj(r,t): return r"%s\left(\cos%s+i\sin%s\right)"%(L(r),L(t),L(t))
# 例題1 積と商
V1=[(sp.sqrt(2),PI/4,sp.sqrt(2),-PI/4),(2,PI/6,2,PI/3),(3,PI/3,2,PI/6),(2,2*PI/3,1,PI/3),(4,PI/4,2,3*PI/4)]
def b1(i):
    r1,t1,r2,t2=V1[i]; z1=polar(r1,t1); z2=polar(r2,t2); pr=polar(r1*r2,t1+t2); qu=polar(r1/r2,t1-t2)
    assert sp.simplify(z1*z2-pr)==0 and sp.simplify(z1/z2-qu)==0
    st=[("極形式にする","<p>"+I(r"z=r(\cos\theta+i\sin\theta)")+"。</p>"+D(r"z_1=%s,\qquad z_2=%s"%(pj(r1,t1),pj(r2,t2)))),
        ("積","<p>"+I(r"z_1z_2=r_1r_2\{\cos(\theta_1+\theta_2)+i\sin(\theta_1+\theta_2)\}")+"。</p>"+D(r"z_1z_2=%s=%s"%(pj(sp.simplify(r1*r2),sp.simplify(t1+t2)),cz(pr)))),
        ("商","<p>"+I(r"\dfrac{z_1}{z_2}=\dfrac{r_1}{r_2}\{\cos(\theta_1-\theta_2)+i\sin(\theta_1-\theta_2)\}")+"。</p>"+D(r"\dfrac{z_1}{z_2}=%s=%s"%(pj(sp.simplify(r1/r2),sp.simplify(t1-t2)),cz(qu))))]
    return r"$z_1=%s,\ z_2=%s$ のとき、$z_1z_2$ と $\dfrac{z_1}{z_2}$ を、極形式を用いて計算せよ。"%(cz(z1),cz(z2)),st,r"z_1z_2=%s,\ \dfrac{z_1}{z_2}=%s"%(cz(pr),cz(qu))
o=[b1(i) for i in range(5)]
build(Z,CH,"極形式での積と商",o,r"<p>$z=r(\cos\theta+i\sin\theta)$。積は<b>絶対値をかけ偏角をたす</b>、商は<b>絶対値をわり偏角をひく</b>。複素数のかけ算は「拡大と回転」。</p>","かけ算＝拡大＋回転。わり算＝縮小＋逆回転。",1)
# 例題2 ド・モアブル
V2=[(1+I_,8),(sp.sqrt(3)+I_,6),(1-I_,10),(-1+sp.sqrt(3)*I_,5),(sp.sqrt(3)-I_,9)]
def b2(i):
    z,n=V2[i]; r=sp.simplify(sp.Abs(z)); th=sp.simplify(sp.arg(z)); res=sp.simplify(sp.expand_complex(z**n)); 
    res2=polar(r**n,n*th); assert sp.simplify(res-res2)==0
    st=[("極形式にする",D(r"|z|=%s,\quad \arg z=%s"%(L(r),L(th)))+D(r"z=%s"%pj(r,th))),
        ("ド・モアブルの定理","<p>"+I(r"z^n=r^n(\cos n\theta+i\sin n\theta)")+"。</p>"+D(r"z^{%d}=\left(%s\right)^{%d}\left\{\cos\left(%d\cdot%s\right)+i\sin\left(%d\cdot%s\right)\right\}"%(n,L(r),n,n,L(th),n,L(th)))),
        ("値を求める",D(r"z^{%d}=%s=%s"%(n,pj(sp.simplify(r**n),sp.simplify(n*th)),cz(res))))]
    return r"$\left(%s\right)^{%d}$ を計算せよ。"%(cz(z),n),st,cz(res)
o=[b2(i) for i in range(5)]
build(Z,CH,"ド・モアブルの定理",o,r"<p>$\{r(\cos\theta+i\sin\theta)\}^n=r^n(\cos n\theta+i\sin n\theta)$。大きい累乗は、<b>極形式にして</b>絶対値を $n$ 乗、偏角を $n$ 倍。</p>","累乗は「同じ回転を $n$ 回くり返す」。偏角が $n$ 倍になる。",2)
# 例題3 n乗根
V3=[(3,8),(4,-4),(3,-8*I_),(4,16),(3,-1)]
def b3(i):
    n,w=V3[i]; r=sp.simplify(sp.Abs(w)); th=sp.arg(w); th=th+2*PI if th<0 else th; rr=sp.simplify(r**R(1,n))
    ang=[sp.simplify((th+2*PI*k)/n) for k in range(n)]; rts=[polar(rr,a) for a in ang]
    for z in rts: assert sp.simplify(sp.expand_complex(z**n)-w)==0
    _c[0]+=1
    def dr(ax):
        t=np.linspace(0,2*np.pi,300); ax.plot(float(rr)*np.cos(t),float(rr)*np.sin(t),color="#bbb",lw=1,ls="--")
        pts=[ptx(z) for z in rts]; ax.fill([p_[0] for p_ in pts],[p_[1] for p_ in pts],color="#fbe9ec",zorder=0)
        for p_ in pts: ax.plot(*p_,"o",color="#b81f36",ms=6)
    M=float(rr)+1
    fig=plane("ic23_c%d"%_c[0],(-M,M),(-M,M),dr,size=(3.6,3.4),w=44,step=max(1,int(M)//4))
    st=[("右辺を極形式にする",D(r"%s=%s"%(cz(w),pj(r,th)))),
        ("解を極形式で書く","<p>"+I(r"z=%s(\cos\phi+i\sin\phi)"%L(rr))+" とおくと、ド・モアブルより "+I(r"z^{%d}=%s(\cos%d\phi+i\sin%d\phi)"%(n,L(r),n,n))+"。</p>"+D(r"%d\phi=%s+2k\pi\ \Rightarrow\ \phi=\dfrac{%s+2k\pi}{%d}\quad(k=0,1,\cdots,%d)"%(n,L(th),L(th),n,n-1))),
        ("$k$ に値を代入する",D(r"\\ ".join(r"k=%d:\ z=%s=%s"%(k,pj(rr,ang[k]),cz(rts[k])) for k in range(n)))+"<p>解は複素数平面上で、原点中心・半径 "+I(L(rr))+" の円に内接する正 "+I(str(n))+" 角形の頂点。</p>"+fig)]
    return r"方程式 $z^{%d}=%s$ を解け。"%(n,cz(w)),st,r"z=%s"%r",\ ".join(cz(z) for z in rts)
o=[b3(i) for i in range(5)]
build(Z,CH,"複素数のn乗根（z^n=w）",o,r"<p>$w=r(\cos\theta+i\sin\theta)$ のとき $z^n=w$ の解は <b>$z=r^{1/n}\left\{\cos\dfrac{\theta+2k\pi}{n}+i\sin\dfrac{\theta+2k\pi}{n}\right\}$ $(k=0,\cdots,n-1)$</b>。解は円周上に等間隔（正 $n$ 角形）に並ぶ。</p>","$n$ 個の解は、円周を $n$ 等分した位置に並ぶ。",3)
# 例題4 三角形の形状
S3=sp.sqrt(3)
V4=[(0,2,1+S3*I_),(1+I_,3+I_,1+3*I_),(0,1,2*I_),(0,1,1+S3*I_),(0,2,2*sp.Rational(-1,2)*0+(-1+S3*I_))]
def b4(i):
    a,b,c=V4[i]; w=sp.simplify(sp.expand_complex((c-a)/(b-a))); r=sp.simplify(sp.Abs(w)); th=sp.simplify(sp.arg(w))
    AB=sp.simplify(sp.Abs(b-a)); AC=sp.simplify(sp.Abs(c-a)); BC=sp.simplify(sp.Abs(c-b))
    kind=None
    if r==1 and th in (PI/3,-PI/3): kind="正三角形"
    elif r==1 and th in (PI/2,-PI/2): kind=r"\angle A=90^\circ\text{ の直角二等辺三角形}"
    elif r==1 and th in (2*PI/3,-2*PI/3): kind=r"AB=AC,\ \angle A=120^\circ\text{ の二等辺三角形}"
    elif th in (PI/2,-PI/2): kind=r"\angle A=90^\circ\text{ の直角三角形}\ (AC=%s\,AB)"%L(r)
    else: kind=r"\angle A=60^\circ,\ AC=2AB\text{ より }\angle B=90^\circ\text{ の直角三角形}"
    assert (r!=2 or th!=PI/3) or abs(float(BC)**2+float(AB)**2-float(AC)**2)<1e-9
    _c[0]+=1; ps=[ptx(a),ptx(b),ptx(c)]
    def dr(ax):
        ax.fill([p_[0] for p_ in ps],[p_[1] for p_ in ps],color="#fbe9ec",zorder=0); ax.plot([p_[0] for p_ in ps+[ps[0]]],[p_[1] for p_ in ps+[ps[0]]],color="#b81f36",lw=2)
        for nm,p_ in zip("ABC",ps): ax.plot(*p_,"o",color="#222",ms=4.5); ax.text(p_[0]+.1,p_[1]+.12,nm,fontsize=11)
    xs=[p_[0] for p_ in ps]; ys=[p_[1] for p_ in ps]
    fig=plane("ic23_d%d"%_c[0],(min(xs)-1.2,max(xs)+1.5),(min(ys)-1.2,max(ys)+1.5),dr,size=(3.6,3.3),w=44)
    st=[("比 $\\dfrac{\\gamma-\\alpha}{\\beta-\\alpha}$ を計算する",D(r"w=\dfrac{\gamma-\alpha}{\beta-\alpha}=\dfrac{%s}{%s}=%s"%(cz(c-a),cz(b-a),cz(w)))),
        ("絶対値と偏角","<p>"+I(r"|w|=\dfrac{AC}{AB},\quad \arg w=\angle BAC")+"（$A$ を中心に $B$ から $C$ へ回す角）。</p>"+D(r"|w|=%s,\quad \arg w=%s"%(L(r),L(th)))),
        ("三角形の形",D(kind if kind=="正三角形" else kind)+fig)]
    return r"複素数平面上の3点 $A(%s),\ B(%s),\ C(%s)$ について、$\dfrac{\gamma-\alpha}{\beta-\alpha}$ を計算し、△$ABC$ がどんな三角形か答えよ。"%(cz(a),cz(b),cz(c)),st,kind if kind=="正三角形" else kind
o=[b4(i) for i in range(5)]
build(Z,CH,"3点がつくる三角形の形",o,r"<p>$w=\dfrac{\gamma-\alpha}{\beta-\alpha}$ の<b>絶対値</b>は $\dfrac{AC}{AB}$、<b>偏角</b>は $\angle BAC$。$|w|=1$ なら $AB=AC$、$\arg w=\pm\dfrac\pi3$ なら正三角形、$\pm\dfrac\pi2$ なら $\angle A$ が直角。</p>","$A$ から見て $B$ を何倍にして何度回すと $C$ に重なるか。それが $w$。",4)
# 例題5 アポロニウスの円
V5=[(0,3,2),(0,6,2),(1,-I_,1),(0,3*I_,2),(2,-1,2)]
def b5(i):
    a,b,k=V5[i]; k=sp.Integer(k); a=sp.sympify(a); b=sp.sympify(b); a1,a2=float(sp.re(a)),float(sp.im(a)); b1_,b2_=float(sp.re(b)),float(sp.im(b))
    lhs=(X-sp.re(a))**2+(Y-sp.im(a))**2; rhs=k**2*((X-sp.re(b))**2+(Y-sp.im(b))**2); eq=sp.expand(lhs-rhs)
    if k==1:
        line=sp.simplify(sp.solve(eq,Y)[0]); res=r"\text{直線 }y=%s"%L(line)
        mid=sp.expand(eq)
        _c[0]+=1
        def dr(ax):
            xs=np.array([-5,5]); ax.plot(xs,[float(line.subs(X,v)) for v in xs],color="#b81f36",lw=2)
            for nm,p_ in (("A",(a1,a2)),("B",(b1_,b2_))): ax.plot(*p_,"o",color="#222",ms=4.5); ax.text(p_[0]+.15,p_[1]+.15,nm,fontsize=11)
        fig=plane("ic23_e%d"%_c[0],(-5,5),(-5,5),dr,size=(3.6,3.4),w=44)
        steps=[("$z=x+yi$ とおいて2乗する",D(r"|z-%s|^2=|z-%s|^2"%(L(a) if a!=0 else "0",L(b)))+D(r"(x-%s)^2+(y-%s)^2=(x-%s)^2+(y-%s)^2"%(P(sp.re(a)),P(sp.im(a)),P(sp.re(b)),P(sp.im(b))))),
               ("整理する",D(L(eq)+"=0")+D(r"y=%s"%L(line))),("図形",D(res)+"<p>線分 $AB$ の<b>垂直二等分線</b>。</p>"+fig)]
        ans=res
    else:
        cen=sp.simplify((a-k**2*b)/(1-k**2)); rad=sp.simplify(k*sp.Abs(a-b)/sp.Abs(1-k**2)); cx,cy=float(sp.re(cen)),float(sp.im(cen))
        for th in np.linspace(0,6.28,9):
            z=complex(cx+float(rad)*math.cos(th),cy+float(rad)*math.sin(th)); assert abs(abs(z-complex(a1,a2))-float(k)*abs(z-complex(b1_,b2_)))<1e-9
        _c[0]+=1
        def dr(ax):
            t=np.linspace(0,2*np.pi,300); ax.plot(cx+float(rad)*np.cos(t),cy+float(rad)*np.sin(t),color="#b81f36",lw=2)
            for nm,p_ in (("A",(a1,a2)),("B",(b1_,b2_))): ax.plot(*p_,"o",color="#222",ms=4.5); ax.text(p_[0]+.15,p_[1]+.15,nm,fontsize=11)
        M=max(abs(cx),abs(cy),abs(a1),abs(b1_),abs(a2),abs(b2_))+float(rad)+1
        fig=plane("ic23_e%d"%_c[0],(-M,M),(-M,M),dr,size=(3.6,3.4),w=44,step=max(1,int(M)//5))
        sq=sp.expand(eq/(1-k**2)); circ=sp.expand((X-sp.re(cen))**2+(Y-sp.im(cen))**2-rad**2)
        steps=[("$|z-\\alpha|=k|z-\\beta|$ の2乗","<p>"+I("z=x+yi")+" とおいて両辺を2乗する。</p>"+D(r"(x-%s)^2+(y-%s)^2=%s\left\{(x-%s)^2+(y-%s)^2\right\}"%(P(sp.re(a)),P(sp.im(a)),L(k**2),P(sp.re(b)),P(sp.im(b))))),
               ("展開して整理する",D(L(eq)+"=0")+D(L(circ)+"=0")),
               ("円の方程式にする",D(r"(x-%s)^2+(y-%s)^2=%s"%(P(sp.re(cen)),P(sp.im(cen)),L(rad**2)))+"<p>中心 "+I(cz(cen))+"、半径 "+I(L(rad))+" の円（アポロニウスの円）。</p>"+fig)]
        ans=r"\text{中心 }%s\text{、半径 }%s\text{ の円}"%(cz(cen),L(rad))
    return r"方程式 $|z-%s|=%s|z-%s|$ を満たす点 $z$ 全体はどんな図形か。"%("("+cz(a)+")" if a!=0 else "0",(L(k)+"\\," if k!=1 else ""),"("+cz(b)+")"),steps,ans
o=[b5(i) for i in range(5)]
build(Z,CH,"複素数平面上の軌跡（アポロニウスの円）",o,r"<p>$|z-\alpha|=|z-\beta|$ は<b>垂直二等分線</b>。$|z-\alpha|=k|z-\beta|\ (k\neq1)$ は<b>円</b>（アポロニウスの円）。$z=x+yi$ とおいて<b>2乗</b>し、展開して整理する。</p>","2点までの距離の比が一定の点の集まり。比が1なら直線、1でなければ円。",5)
UNIT=finish(Z,CH,1,2,"平面上の曲線と複素数平面","複素数平面","極形式、ド・モアブル、n乗根、三角形の形、アポロニウスの円まで、複素数平面の難問に挑みます。",subject="C")
