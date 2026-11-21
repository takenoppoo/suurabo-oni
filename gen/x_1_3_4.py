# -*- coding: utf-8 -*-
from bh import *
from gq import *
Z=U_(); CH=[]
R=sp.Rational
# 6 範囲つきの不等式 (定数分離)
def b6(c,t):
    # x^2 -2a x + c >= 0 for 0<=x<=t
    s=sp.sqrt(c)
    if s<=t: amax=s; why="x=\\sqrt{%d}"%c
    else: amax=R(t*t+c,2*t); why="x=%d"%t
    for a_ in np.linspace(float(amax)-1,float(amax)+1,81):
        xs=np.linspace(0,t,4001); ok=(xs**2-2*a_*xs+c>=-1e-9).all(); assert ok==(a_<=float(amax)+1e-9),(a_,amax)
    st=[("軸で場合分け","<p>"+I(r"f(x)=(x-a)^2+%d-a^2"%c)+"、"+I(r"0\leqq x\leqq %d"%t)+"。最小値を調べる。</p>"),
        ("3つの場合","<p>"+I(r"a<0")+"：最小は "+I("f(0)=%d>0"%c)+"（成立）。</p><p>"+I(r"0\leqq a\leqq%d"%t)+"：最小は "+I(r"f(a)=%d-a^2\geqq0"%c)+" より "+I(r"a\leqq\sqrt{%d}"%c)+"。</p><p>"+I(r"a>%d"%t)+"：最小は "+I(r"f(%d)=%d-%da\geqq0"%(t,t*t+c,2*t))+" より "+I(r"a\leqq %s"%L(R(t*t+c,2*t)))+"。</p>"),
        ("まとめる","<p>"+("%d"%c if False else "")+I(r"\sqrt{%d}%s%d"%(c,r"\leqq" if s<=t else ">",t))+" なので</p>"+D(r"a\leqq %s"%L(amax)))]
    return r"$0\leqq x\leqq%d$ のすべての $x$ について $x^2-2ax+%d\geqq0$ が成り立つような定数 $a$ の範囲を求めよ。"%(t,c),st,r"a\leqq %s"%L(amax)
o=[b6(*v) for v in [(3,2),(4,3),(9,2),(2,3),(16,3)]]
build(Z,CH,"範囲つきの不等式がつねに成り立つ条件",o,r"<p>「すべての $x$ で」のときは、<b>範囲内での最小値 $\geqq0$</b> を考える。軸が範囲の左・中・右のどこにあるかで<b>場合分け</b>。</p>","一番低い所でも0以上なら、全体が0以上。",6)
# 7 整数解がちょうど1つ
def b7(p,q):
    r_=R(2*p-3,2)
    intervals=[]
    def cnt(k):
        lo,hi=sorted([r_,k]); return sum(1 for n in range(-40,60) if lo<n<hi and (n<p or n>q))
    ks=[R(i,4) for i in range(-120,200)]
    good=[k for k in ks if cnt(k)==1]
    # expected
    exp=[k for k in ks if (p-3<=k<p-2) or (p-1<k<=q+1)]
    assert good==exp,(good[:3],exp[:3])
    st=[("$A$ の整数","<p>"+I(r"A:\ x<%d,\ x>%d"%(p,q))+"。</p>"),
        ("$B$ の解","<p>"+I(r"(2x-%d)(x-k)<0"%(2*p-3))+" の解は "+I(r"%s"%L(r_))+" と "+I("k")+" の間。</p>"),
        ("$k>%s$ のとき"%L(r_),"<p>"+I(r"B:\ %s<x<k"%L(r_))+"。"+I("A")+" に入る整数は、"+I("%d"%(p-1))+"（"+I("x<%d"%p)+"）と "+I("%d"%(q+1))+" 以上。ちょうど1つ：</p>"+D(r"%d<k\leqq %d"%(p-1,q+1))),
        ("$k<%s$ のとき"%L(r_),"<p>"+I(r"B:\ k<x<%s"%L(r_))+"。"+I("A")+" に入る整数は "+I("%d,\\ %d,\\ \\cdots"%(p-2,p-3))+"。ちょうど1つ：</p>"+D(r"%d\leqq k<%d"%(p-3,p-2))),
        ("答え",D(r"%d\leqq k<%d,\qquad %d<k\leqq %d"%(p-3,p-2,p-1,q+1)))]
    return r"連立不等式 $x^2-%dx+%d>0,\ \ (2x-%d)(x-k)<0$ を同時にみたす整数 $x$ がちょうど1つとなるような定数 $k$ の範囲を求めよ。"%(p+q,p*q,2*p-3),st,r"%d\leqq k<%d,\ \ %d<k\leqq %d"%(p-3,p-2,p-1,q+1)
o=[b7(*v) for v in [(-1,2),(0,3),(1,4),(-2,1),(2,5)]]
build(Z,CH,"連立不等式の整数解がちょうど1つ",o,r"<p>$A$ の範囲は固定、$B$ の範囲は $k$ で動く。<b>$k$ が大きいとき・小さいときで場合分け</b>し、共通部分に入る整数を数え上げる。端点の等号に注意。</p>","動く区間が、固定区間の穴に何個の整数を取り込むかを数える。",7)
# 8 解から別の不等式
def b8(al,be,a):
    assert al*be!=0 and a<0
    bb=-a*(al+be); cc=a*al*be
    r1,r2=sorted([R(1,al),R(1,be)])
    xs=np.linspace(-3,3,24001)
    f=lambda t: cc*t**2+bb*t+a
    if al*be>0: ans=r"x<%s,\ \ x>%s"%(L(r1),L(r2)); chk=lambda t:(t<float(r1)-1e-9)|(t>float(r2)+1e-9)
    else: ans=r"%s<x<%s"%(L(r1),L(r2)); chk=lambda t:(t>float(r1)+1e-9)&(t<float(r2)-1e-9)
    v=f(xs); m=np.abs(xs-float(r1))>1e-3; m&=np.abs(xs-float(r2))>1e-3
    assert ((v[m]<0)==chk(xs[m])).all()
    q=sp.expand(al*be*x**2-(al+be)*x+1)
    st=[("$b,\\ c$ を $a$ で表す","<p>解が "+I(r"%s<x<%s"%(L(al),L(be)) if al<be else r"%s<x<%s"%(L(be),L(al)))+" なので "+I("a<0")+"、2解は "+I(r"%s,\ %s"%(L(al),L(be)))+"。</p>"+D(r"b=-a(%s+%s)=%s\,a,\qquad c=a\cdot%s\cdot%s=%s\,a"%(L(al),P(be),L(-(al+be)),L(al),P(be),L(al*be)))),
        ("新しい不等式に代入","<p>"+I(r"cx^2+bx+a<0")+" を "+I("a")+" でわる。"+I("a<0")+" なので<b>不等号の向きが逆</b>になる。</p>"+D(r"%sx^2%sx+1>0"%(L(al*be),("+"+L(-(al+be)) if -(al+be)>0 else L(-(al+be)))))),
        ("因数分解して解く","<p>"+I(r"%s=(%sx-1)(%sx-1)"%(L(q),L(al),L(be)))+"。2解は "+I(r"x=%s,\ %s"%(L(R(1,al)),L(R(1,be))))+"。"+I("x^2")+" の係数 "+I(L(al*be))+" が"+("正" if al*be>0 else "負")+"なので</p>"+D(ans))]
    f0=a*x**2+bb*x+cc; lo_,hi_=sorted([al,be]); xv=R(-bb,2*a)
    fg=quadfig("x134_8_%d_%d_%d"%(al+9,be+9,a+9),[(f0,"#b81f36")],[(lo_,0,"(%d, 0)"%lo_),(hi_,0,"(%d, 0)"%hi_)],axis=xv,hl=[(lo_,hi_)],xr=(min(lo_,hi_)-3,max(lo_,hi_)+3))
    st[0]=(st[0][0],st[0][1]+"<p>"+I(r"ax^2+bx+c>0")+" の解（放物線が "+I("x")+" 軸より上の部分）が太線。上に凸なので "+I("a<0")+"。</p>"+fg)
    return r"$ax^2+bx+c>0$ の解が $%s<x<%s$ であるとき、$cx^2+bx+a<0$ の解を求めよ。"%((L(al),L(be)) if al<be else (L(be),L(al))),st,ans
o=[b8(*v) for v in [(1,3,-1),(2,5,-1),(-3,-1,-2),(-1,2,-1),(-2,3,-2)]]
build(Z,CH,"解から別の2次不等式の解を求める",o,r"<p>解の形から $a<0$、$b,c$ を $a$ で表す。新しい不等式に代入し<b>$a$ でわる（$a<0$ で向きが逆）</b>。因数分解して解く。</p>","負の数でわるときは不等号が逆向きになる。",8)
# 9 つねに正でない（f(x)>0 の解が存在しない）
def b9(p,q):
    # a x^2 + 2p x + q <= 0 が すべての実数 x で成り立つ条件 a<0 ,D<=0: p^2 - a q <=0
    # a x^2 +2p x + q <=0 for all x : a<0, p^2 - a q <= 0 → a <= -p^2/q (q<0?) choose q negative: a<0 and p^2 <= a q → a <= p^2/q ... q<0: a q >=p^2 → a <= p^2/q
    amax=R(p*p,q); assert q<0
    for a_ in [float(amax)-1,float(amax),float(amax)+0.5,-0.5,0,1]:
        xs=np.linspace(-50,50,200001); ok=(a_*xs**2+2*p*xs+q<=1e-6).all(); exp=(a_<0 and a_<=float(amax)+1e-9)
        assert ok==exp,(a_,amax,ok,exp)
    st=[("次数で場合分け","<p>"+I("a=0")+" のとき "+I(r"%dx%+d\leqq0"%(2*p,q))+" は "+I("x")+" が大きいと成り立たない。よって "+I(r"a\neq0")+"。</p>"),
        ("2次不等式の条件","<p>すべての "+I("x")+" で "+I(r"\leqq0")+" となるには、上に凸 "+I("a<0")+" かつ 判別式 "+I(r"D\leqq0")+"。</p>"+D(r"\dfrac D4=%d-%sa\leqq0"%(p*p,L(q)) if q!=-1 else r"\dfrac D4=%d+a\leqq0"%(p*p))),
        ("解く","<p>"+I(r"a\leqq %s"%L(amax))+"（"+I("%s<0"%L(amax))+" より "+I("a<0")+" も満たす）。</p>"+D(r"a\leqq %s"%L(amax)))]
    a_ex=R(sp.floor(amax)-1)
    f_ex=a_ex*x**2+2*p*x+q; xv=R(-p,1)/a_ex
    fg=quadfig("x134_9_%d_%d"%(p+9,-q),[(f_ex,"#b81f36")],[(xv,f_ex.subs(x,xv),"頂点")],axis=xv)
    st[0]=(st[0][0],st[0][1]+"<p>例として "+I("a=%s"%L(a_ex))+" のグラフ。上に凸で頂点が "+I("x")+" 軸より下にあれば、すべての "+I("x")+" で "+I(r"\leqq0")+"。</p>"+fg)
    return r"すべての実数 $x$ について $ax^2+%dx%+d\leqq0$ が成り立つような定数 $a$ の範囲を求めよ。"%(2*p,q),st,r"a\leqq %s"%L(amax)
o=[b9(*v) for v in [(2,-1),(3,-2),(1,-3),(2,-5),(4,-4)]]
build(Z,CH,"すべての実数で不等式が成り立つ条件（a の場合分け）",o,r"<p>$x^2$ の係数が文字のときは<b>まず $a=0$ の場合</b>を調べる。$a\neq0$ なら、$\leqq0$ がつねに成り立つ条件は「上に凸 かつ $D\leqq0$」。</p>","最高次の係数が0になる場合を、かならず別に確認する。",9)
# 10 ボールの高さ
def b10(v0,H):
    # h = v0 t - 5 t^2 >= H : 5t^2 - v0 t + H <= 0
    D_=v0*v0-20*H; assert D_>0
    t1=(v0-sp.sqrt(D_))/10; t2=(v0+sp.sqrt(D_))/10; dur=sp.simplify(t2-t1)
    st=[("高さの式","<p>"+I(r"h=%dt-5t^2"%v0)+"（地面から投げ上げ）。</p>"),
        ("不等式",D(r"%dt-5t^2\geqq %d\ \Rightarrow\ 5t^2-%dt+%d\leqq0\ \Rightarrow\ t^2-%st+%s\leqq0"%(v0,H,v0,H,L(R(v0,5)),L(R(H,5))))),
        ("解く",D(r"%s\leqq t\leqq %s"%(L(sp.simplify(t1)),L(sp.simplify(t2))))+"<p>高さ "+I("%d"%H)+" m 以上にいる時間は</p>"+D(r"t_2-t_1=%s\ \text{秒}"%L(dur)))]
    return r"地面から真上に初速度 $%d$ m/s でボールを投げ上げると、$t$ 秒後の高さは $%dt-5t^2$ m である。高さが $%d$ m 以上である時間は何秒間か。"%(v0,v0,H),st,r"%s\ \text{秒間}"%L(dur)
o=[b10(*v) for v in [(20,15),(30,40),(20,10),(40,60),(30,25)]]
build(Z,CH,"2次不等式の文章題（投げ上げ）",o,r"<p>高さの式から<b>不等式を作り、2次不等式を解く</b>。「以上にいる時間」は2つの解の<b>差</b>。時間は正という条件も忘れない。</p>","山なりの軌道で、ある高さより上にいる間は、2つの交点の間。",10)
XU=finishx(Z,CH)
