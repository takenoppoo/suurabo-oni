# -*- coding: utf-8 -*-
from bh import *
import math
Z=U_(); CH=[]
R=sp.Rational
s=sp.sqrt
# 6 sin cos 値から 3乗
def b6(sn,cs,den):
    # sinθ=sn/den, cosθ=cs/den (pythagorean triple)
    sn_=R(sn,den); cs_=R(cs,den); assert sn_**2+cs_**2==1
    v=sn_**3+cs_**3; w=sp.simplify(sn_*cs_); s_=sn_+cs_
    assert sp.simplify(s_**3-3*sn_*cs_*s_-v)==0
    st=[("$\\sin\\theta+\\cos\\theta$ と $\\sin\\theta\\cos\\theta$","<p>"+I(r"\sin\theta+\cos\theta=%s"%L(s_))+"。両辺を2乗：</p>"+D(r"1+2\sin\theta\cos\theta=%s\ \Rightarrow\ \sin\theta\cos\theta=%s"%(L(s_**2),L(w)))),
        ("3乗の和の公式","<p>"+I(r"a^3+b^3=(a+b)^3-3ab(a+b)")+"。</p>"+D(r"\sin^3\theta+\cos^3\theta=\left(%s\right)^3-3\cdot%s\cdot%s"%(L(s_),L(w),L(s_)))+D(r"=%s-%s=%s"%(L(s_**3),L(3*w*s_),L(s_**3-3*w*s_)))),
        ("計算",D(r"=%s"%L(v)))]
    return r"$\sin\theta+\cos\theta=%s$ のとき、$\sin^3\theta+\cos^3\theta$ の値を求めよ。"%L(s_),st,L(v)
o=[b6(*v) for v in [(3,4,5),(5,12,13),(8,15,17),(7,24,25),(20,21,29)]]
build(Z,CH,"sinθ+cosθ から3乗の和を求める",o,r"<p>$\sin\theta+\cos\theta$ を2乗して $\sin\theta\cos\theta$ を出し、$a^3+b^3=(a+b)^3-3ab(a+b)$ を使う。$\sin^2\theta+\cos^2\theta=1$ が出発点。</p>","和と積の2情報にまとめれば、どんな対称式も計算できる。",6)
# 7 tanθ→ 分数式
def b7(t,a_,b_,c_,d_):
    expr=(a_*sp.sin(x)+b_*sp.cos(x))/(c_*sp.sin(x)+d_*sp.cos(x)); th=sp.atan(t)
    v=sp.nsimplify(expr.subs(x,th)); w=R(a_*t+b_,c_*t+d_); assert sp.simplify(v-w)==0
    st=[("分母・分子を $\\cos\\theta$ でわる","<p>"+I(r"\cos\theta\neq0")+" として</p>"+D(r"\dfrac{%s\sin\theta%+d\cos\theta}{%s\sin\theta%+d\cos\theta}=\dfrac{%s\tan\theta%+d}{%s\tan\theta%+d}"%(L(a_),b_,L(c_),d_,L(a_),b_,L(c_),d_))),
        ("$\\tan\\theta=%d$ を代入"%t,D(r"\dfrac{%d\cdot%d%+d}{%d\cdot%d%+d}=\dfrac{%d}{%d}=%s"%(a_,t,b_,c_,t,d_,a_*t+b_,c_*t+d_,L(w))))]
    return r"$\tan\theta=%d$ のとき、$\dfrac{%d\sin\theta%+d\cos\theta}{%d\sin\theta%+d\cos\theta}$ の値を求めよ。"%(t,a_,b_,c_,d_),st,L(w)
o=[b7(*v) for v in [(2,3,1,1,-1),(3,2,-1,1,2),(4,1,3,2,-1),(-2,3,2,1,1),(5,4,-3,2,1)]]
build(Z,CH,"tanθ から1次式の分数の値",o,r"<p>$\sin$ と $\cos$ の1次式の分数は、<b>分母・分子を $\cos\theta$ でわって $\tan\theta$ の式</b>に直す。値を直接求める必要はない。</p>","単位をそろえてから比べるように、$\\cos\\theta$ でそろえる。",7)
# 8 2次式 tan
def b8(t):
    # sin^2 + 2 sin cos 
    th=sp.atan(t); e=sp.sin(x)**2+2*sp.sin(x)*sp.cos(x)-3*sp.cos(x)**2; v=sp.nsimplify(e.subs(x,th)); w=R(t*t+2*t-3,1+t*t)
    assert sp.simplify(v-w)==0
    st=[("分母を $1$ とみて分数にする","<p>"+I("1=\\sin^2\\theta+\\cos^2\\theta")+" とみる。</p>"+D(r"\dfrac{\sin^2\theta+2\sin\theta\cos\theta-3\cos^2\theta}{\sin^2\theta+\cos^2\theta}")),
        ("$\\cos^2\\theta$ でわる",D(r"=\dfrac{\tan^2\theta+2\tan\theta-3}{\tan^2\theta+1}")),
        ("代入",D(r"=\dfrac{%d+%d-3}{%d+1}=%s"%(t*t,2*t,t*t,L(w))))]
    return r"$\tan\theta=%d$ のとき、$\sin^2\theta+2\sin\theta\cos\theta-3\cos^2\theta$ の値を求めよ。"%t,st,L(w)
o=[b8(t) for t in [2,3,4,-2,5]]
build(Z,CH,"tanθ から2次式の値（1 を分母に）",o,r"<p>2次の同次式は、$1=\sin^2\theta+\cos^2\theta$ を分母にして、<b>分母・分子を $\cos^2\theta$ でわる</b>と $\tan\theta$ の式になる。</p>","「1」を分数の分母に変身させて、$\\tan$ だけの式にする。",8)
# 9 方程式 2次
def b9(a,b):
    # 2 sin^2 - a... choose 2cos^2θ + (a)sinθ - b = 0 ... param: 2sin^2θ - sinθ -1 type: solve with roots
    # (sinθ - r1)(2 sinθ - ... ) simple: 2sin²θ + a sinθ - b =0 with roots r in [-1,1] 
    pass
def b9(r1,r2):
    # (2 sinθ - r1)(sinθ + r2)=0  → 2sin²+ (2 r2 - r1) sin - r1 r2  with 0<=θ<=180 sin∈[0,1]
    # use cos: 2cos²θ-... Use r2 outside range
    bb=2*r2-r1; cc=-r1*r2
    sols=[]
    for th in range(0,181):
        v=2*math.sin(math.radians(th))**2+bb*math.sin(math.radians(th))+cc
        if abs(v)<1e-9: sols.append(th)
    # roots sinθ=r1/2 (if in range) & sinθ=-r2 (out of range for 0<=θ<=180 since negative)
    th0=round(math.degrees(math.asin(r1/2)))
    exp=sorted({th0,180-th0}); assert sols==exp,(sols,exp)
    st=[("$\\sin\\theta$ で整理","<p>"+I("s=\\sin\\theta")+" とおく。</p>"+D(r"2s^2%+ds%+d=0"%(bb,cc))+"<p>たすき掛けで因数分解する（展開して確かめる）。</p>"+D(r"(2s-%d)(s+%d)=2s^2+%ds-%ds-%d=2s^2%+ds%+d"%(r1,r2,2*r2,r1,r1*r2,bb,cc))+D(r"(2s-%d)(s+%d)=0"%(r1,r2))),
        ("範囲を確認","<p>"+I(r"0^\circ\leqq\theta\leqq180^\circ")+" より "+I(r"0\leqq s\leqq1")+"。</p>"+D(r"s=\dfrac{%d}{2}\ \text{または}\ s=-%d"%(r1,r2))+"<p>"+I("s=-%d"%r2)+" は範囲外。</p>"),
        ("角を求める","<p>単位円で、"+I(r"y=\dfrac{%d}{2}"%r1)+" の高さの直線と円の交点を探す。"+I(r"0^\circ\leqq\theta\leqq180^\circ")+" は上半分。</p>"+uceq("u141_9_%d_%d"%(r1,r2),"sin",r1/2,pts=[(math.radians(v),"%d^\\circ"%v) for v in exp])+D(r"\sin\theta=\dfrac{%d}{2}\ \Rightarrow\ \theta=%s"%(r1,r",\ ".join("%d^\\circ"%v for v in exp))))]
    return r"$0^\circ\leqq\theta\leqq180^\circ$ のとき、方程式 $2\sin^2\theta%+d\sin\theta%+d=0$ を解け。"%(bb,cc),st,r"\theta=%s^\circ"%(r",\ ".join(str(v) for v in exp))
o=[b9(*v) for v in [(1,2),(1,3),(2,2),(1,1) if False else (1,4),(1,5)]]
build(Z,CH,"三角比の2次方程式（範囲に注意）",o,r"<p>$\sin\theta=s$ と置き換えて因数分解。<b>$0^\circ\leqq\theta\leqq180^\circ$ では $0\leqq\sin\theta\leqq1$</b>、これを外れる解は捨てる。$\sin$ は $\theta$ と $180^\circ-\theta$ で同じ値。</p>","置き換えたら、$s$ の範囲もチェック。",9)
# 10 加法 sin 35 etc 和
def b10(n):
    # sin^2 1°+ ... + sin^2 89° = 44.5 ; param: sin^2 a + sin^2 (a+...)? general: sum_{k=1}^{n-1} sin^2(k*90/n)? use 1..89 only: vary (1,89),(1,45)...
    # use sin^2 5°+ sin^2 10°+...+ sin^2 85° : pairs 5k and 90-5k
    step=n; angs=list(range(step,90,step)); v=sum(math.sin(math.radians(a))**2 for a in angs)
    m=len(angs)
    # if 45 is included it is 1/2 alone; sum = (m-1)/2*1 + 1/2
    if 45 in angs: exp=R(m-1,2)+R(1,2)
    else: exp=R(m,2)
    assert abs(v-float(exp))<1e-9
    st=[("$90^\\circ-\\theta$ の関係","<p>"+I(r"\sin(90^\circ-\theta)=\cos\theta")+"、よって</p>"+D(r"\sin^2\theta+\sin^2(90^\circ-\theta)=\sin^2\theta+\cos^2\theta=1")),
        ("ペアをつくる","<p>"+I(r"%s^\circ\sim%s^\circ"%(step,angs[-1]))+" は "+I(str(m))+" 個。和が "+I("90^\\circ")+" になる2つずつをペアにする。</p>"+("<p>"+I("45^\\circ")+" は1つだけ余り、"+I(r"\sin^245^\circ=\dfrac12")+"。</p>" if 45 in angs else "")),
        ("合計",D(r"%s"%(r"\dfrac{%d}{2}\times1%s=%s"%(m-1,r"+\dfrac12" if 45 in angs else "",L(exp)) if 45 in angs else r"\dfrac{%d}{2}\times1=%s"%(m,L(exp)))))]
    return r"$\sin^2%d^\circ+\sin^2%d^\circ+\sin^2%d^\circ+\cdots+\sin^2%d^\circ$ の値を求めよ。（$%d^\circ$ ずつ増えて $%d^\circ$ まで）"%(step,2*step,3*step,angs[-1],step,angs[-1]),st,L(exp)
o=[b10(n) for n in [5,10,9,15,6]]
build(Z,CH,"sin²θ の和（90°−θ のペア）",o,r"<p>$\sin(90^\circ-\theta)=\cos\theta$ から、和が $90^\circ$ になるペアは $\sin^2\theta+\cos^2\theta=1$。<b>ペアの数</b>を数え、$45^\circ$ が余る場合は $\dfrac12$ を足す。</p>","両端から手をつなぐように2つずつペアにして、全体を数える。",10)
XU=finishx(Z,CH)
