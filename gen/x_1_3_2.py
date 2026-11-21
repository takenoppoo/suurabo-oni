# -*- coding: utf-8 -*-
from bh import *
Z=U_(); CH=[]
R=sp.Rational
# 6 壁を使った囲い
def b6(l):
    f=x*(l-2*x); xm=R(l,4); v=f.subs(x,xm); xs=np.linspace(0,l/2,100001); assert abs(max(float(f.subs(x,0)) if False else v for _ in [0])-v)<1e-9
    fl=sp.lambdify(x,f,"numpy"); assert abs(fl(xs).max()-float(v))<1e-3
    st=[("文字を決める","<p>壁に垂直な辺を "+I("x")+" m とすると、壁に平行な辺は "+I("%d-2x"%l)+" m。長さが正なので "+I(r"0<x<%s"%L(R(l,2)))+"。</p>"),
        ("面積の式",D(r"S=x(%d-2x)=-2x^2+%dx=-2\left(x-%s\right)^2+%s"%(l,l,L(xm),L(v)))),
        ("最大値","<p>"+I(r"x=%s"%L(xm))+" は範囲 "+I(r"0<x<%s"%L(R(l,2)))+" に含まれるので、最大値は</p>"+D(r"%s\ \text{m}^2"%L(v)))]
    return r"長さ $%d$ m の柵を使い、壁を一辺として長方形の囲いをつくる。囲いの面積の最大値と、そのときの壁に垂直な辺の長さを求めよ。"%l,st,r"x=%s\ \text{のとき最大 }%s\ \text{m}^2"%(L(xm),L(v))
o=[b6(l) for l in [24,40,36,60,30]]
build(Z,CH,"壁を使った囲いの面積の最大",o,r"<p>文字 $x$ の<b>範囲を先に決める</b>（長さは正）。面積を $x$ の2次式で表し、平方完成。頂点の $x$ が範囲に入っているか確認する。</p>","現実の長さには、正という範囲がある。頂点が範囲外なら端が答え。",6)
# 7 最大・最小から係数
def b7(M,m):
    # f=a(x^2-4x)+b on [0,3], max M min m
    sols=[]
    a1=R(M-m,4); b1=M; f1=lambda t:a1*(t*t-4*t)+b1; assert max(f1(t) for t in np.linspace(0,3,3001))>=0
    a2=R(m-M,4); b2=m
    for a_,b_ in [(a1,b1),(a2,b2)]:
        fl=sp.lambdify(x,a_*(x**2-4*x)+b_,"numpy"); xs=np.linspace(0,3,30001); y_=fl(xs); assert abs(y_.max()-M)<1e-3 and abs(y_.min()-m)<1e-3
    st=[("平方完成","<p>"+I(r"f(x)=a(x-2)^2-4a+b")+"。軸 "+I("x=2")+" は定義域 "+I(r"0\leqq x\leqq3")+" の内部にある。</p>"+D(r"f(0)=b,\quad f(2)=b-4a,\quad f(3)=b-3a")),
        ("$a>0$ のとき","<p>最小は頂点、最大は軸から遠い "+I("x=0")+"。</p>"+D(r"b=%d,\ \ b-4a=%d\ \Rightarrow\ a=%s"%(M,m,L(a1)))),
        ("$a<0$ のとき","<p>最大は頂点、最小は軸から遠い "+I("x=0")+"。</p>"+D(r"b-4a=%d,\ \ b=%d\ \Rightarrow\ a=%s"%(M,m,L(a2)))),
        ("答え","<p>"+I(r"a\neq0")+" で、どちらも条件に合う。</p>")]
    return r"$f(x)=a(x^2-4x)+b$（$a\neq0$）の $0\leqq x\leqq3$ における最大値が $%d$、最小値が $%d$ であるとき、定数 $a,\ b$ の値を求めよ。"%(M,m),st,r"(a,b)=(%s,%d),\ (%s,%d)"%(L(a1),b1,L(a2),b2)
o=[b7(*v) for v in [(7,3),(5,-3),(9,1),(6,-2),(10,2)]]
build(Z,CH,"最大・最小から係数を決める（a の符号で場合分け）",o,r"<p>$a$ の符号が不明なら<b>$a>0$ と $a<0$ で場合分け</b>。$a>0$ は最小が頂点、$a<0$ は最大が頂点。軸が定義域に入っているかも確認する。</p>","谷型か山型か、2通り考える。答えが2組になることがある。",7)
# 8 最小値 m(a) の最大
def b8(c,t):
    assert c<2*t
    def m(a): 
        if a<0: return c*a
        if a<=t: return c*a-a*a
        return t*t-2*a*t+c*a
    aa=np.linspace(-3,t+4,70001); v=np.array([m(a) for a in aa]); assert abs(v.max()-c*c/4)<1e-3 and abs(aa[v.argmax()]-c/2)<1e-3
    st=[("軸の位置で場合分け","<p>"+I(r"f(x)=x^2-2ax+%da=(x-a)^2-a^2+%da"%(c,c))+"、"+I(r"0\leqq x\leqq%d"%t)+"。軸 "+I("x=a")+"。</p>"+D(r"m(a)=\begin{cases}%da&(a<0)\\%da-a^2&(0\leqq a\leqq %d)\\%d-%da+%da&(a>%d)\end{cases}"%(c,c,t,t*t,2*t,c,t))),
        ("各場合の最大","<p>"+I("a<0")+"：増加で "+I("m(a)<0")+"。"+I("a>%d"%t)+"：傾き "+I("%d"%(c-2*t))+"（負）で減少。</p>"+D(r"0\leqq a\leqq %d:\ m(a)=-\left(a-%s\right)^2+%s"%(t,L(R(c,2)),L(R(c*c,4))))),
        ("最大値","<p>"+I("a=%s"%L(R(c,2)))+" は "+I(r"0\leqq a\leqq%d"%t)+" に含まれるので、最大値は "+I(L(R(c*c,4)))+"。</p>")]
    return r"$0\leqq x\leqq %d$ における $f(x)=x^2-2ax+%da$ の最小値を $m(a)$ とする。$m(a)$ の最大値とそのときの $a$ の値を求めよ。"%(t,c),st,r"a=%s\ \text{のとき最大 }%s"%(L(R(c,2)),L(R(c*c,4)))
o=[b8(*v) for v in [(2,3),(3,4),(4,5),(1,2),(3,3)]]
build(Z,CH,"最小値 m(a) の最大値",o,r"<p>まず軸 $x=a$ の位置で<b>場合分けして $m(a)$ を式で表す</b>。次に各区間で $m(a)$ の最大を調べ、比べる。</p>","2段階の最大化：先に最小値を求め、その最小値を最大にする。",8)
# 9 置き換え x^2=t
def b9(b,c,u):
    # y=x^4+b x^2+c, -u<=x<=u'  b<0
    f=lambda t:t*t+b*t+c; tm=R(-b,2); assert 0<=tm<=u*u
    xs=np.linspace(-u,u,200001); yv=xs**4+b*xs**2+c; mx=max(f(0),f(u*u)); mn=f(tm)
    assert abs(yv.max()-mx)<1e-2 and abs(yv.min()-float(mn))<1e-3
    st=[("置き換え","<p>"+I("t=x^2")+" とおく。"+I(r"-%d\leqq x\leqq %d"%(u,u))+" より "+I(r"0\leqq t\leqq %d"%(u*u))+"。</p>"+D(r"y=t^2%+dt%+d=\left(t%+s\right)^2%+s"%(b,c,L(R(b,2)),L(c-R(b*b,4)) if False else L(c-R(b*b,4))))),
        ("頂点と端点","<p>頂点 "+I("t=%s"%L(tm))+" は範囲内。端点 "+I("t=0,\\ %d"%(u*u))+"。</p>"+D(r"y(0)=%d,\quad y(%d)=%d"%(f(0),u*u,f(u*u)))),
        ("最大・最小",D(r"\text{最大値 }%d\ (x=%s),\quad\text{最小値 }%s\ (x=\pm\sqrt{%s})"%(mx,("0" if f(0)>=f(u*u) else r"\pm%d"%u),L(mn),L(tm))))]
    return r"$-%d\leqq x\leqq %d$ における $y=x^4%+dx^2%+d$ の最大値・最小値を求めよ。"%(u,u,b,c),st,r"\text{最大 }%d,\ \text{最小 }%s"%(mx,L(mn))
o=[b9(*v) for v in [(-4,1,3),(-6,2,3),(-2,0,2),(-8,5,4),(-6,0,3)]]
build(Z,CH,"4次式の最大・最小（x² を置き換える）",o,r"<p>$t=x^2$ と置き換え、<b>$t$ の範囲（$t\geqq0$ と定義域から決まる上限）</b>を求める。$t$ の2次関数として最大・最小を調べ、最後に $x$ にもどす。</p>","置き換えたら、範囲も一緒に変換する。",9)
# 10 整数の最小
def b10(b,c):
    # f(n)=n^2-b n + c, b odd, n integer min
    n0=(b-1)//2; n1=n0+1; v=n0*n0-b*n0+c; assert v==n1*n1-b*n1+c==min(n*n-b*n+c for n in range(-20,60))
    st=[("平方完成","<p>"+I(r"f(n)=n^2-%dn+%d=\left(n-%s\right)^2+%s"%(b,c,L(R(b,2)),L(c-R(b*b,4))))+"。頂点は "+I("n=%s"%L(R(b,2)))+"。</p>"),
        ("頂点に近い整数",D(r"n=%d,\ %d\ \text{が頂点から等距離 }\left(\pm\dfrac12\right)"%(n0,n1))),
        ("最小値",D(r"f(%d)=f(%d)=%d"%(n0,n1,v)))]
    return r"整数 $n$ に対する $f(n)=n^2-%dn+%d$ の最小値と、そのときの $n$ を求めよ。"%(b,c),st,r"n=%d,\ %d\ \text{のとき最小 }%d"%(n0,n1,v)
o=[b10(*v) for v in [(7,3),(9,5),(5,1),(11,10),(13,2)]]
build(Z,CH,"整数変数の最小値",o,r"<p>$n$ が整数のとき、頂点が整数でなければ<b>頂点に最も近い整数</b>で最小。頂点が $\dfrac{奇数}{2}$ なら、両隣の2つの整数が同じ値で最小。</p>","整数しか立てない足場では、頂点にいちばん近い足場を選ぶ。",10)
XU=finishx(Z,CH)
