# -*- coding: utf-8 -*-
# 2次関数の最大・最小（数学I 2次関数）
from tools import *
from fractions import Fraction as Fr
import sympy as sp
x=sp.symbols('x')
EXS=[]
def ex(**k): EXS.append(k)
def mm(f,lo,hi,n=4000):
    vs=[float(f(lo+(hi-lo)*Fr(k,n))) for k in range(n+1)]
    return min(vs),max(vs)
def row(figs): return '<div style="display:flex;gap:6px;margin:4px 0">'+"".join('<div style="flex:1">'+f+'</div>' for f in figs)+'</div>'

# ===== 例題1 定義域つき =====
f1=graph("i32_e1",[(lambda v:2*v*v-8*v+3,RED,"-")],(-1.2,6),(-8,16),pts=[(2,-5,"頂点 (2, -5)",0.2,-1.2),(5,13,"(5, 13)",-2.2,0.2),(0,3,"(0, 3)",0.25,0.3)],xticks=[(2,"2"),(5,"5")],vlines=[(0,"#aaa"),(5,"#aaa")],w=54,size=(4.4,3.4))
ex(title="定義域のある2次関数の最大・最小",
 problem="2次関数 "+I("y=2x^2-8x+3")+"（"+I("0\\leqq x\\leqq5")+"）の最大値と最小値を求めよ。また、そのときの "+I("x")+" の値も答えよ。",
 approach="<p>平方完成して<b>頂点と軸</b>を求め、グラフを描く。<b>定義域の両端と頂点</b>の3か所の "+I("y")+" の値を比べる。下に凸なら、頂点が定義域内にあれば頂点が最小、<b>最大は軸から遠い方の端</b>で起こる。</p>",
 kotsu="山の底（頂点）は1か所、でも道の端は2か所。端のうち軸から遠い方が高い。",
 steps=[
  step(1,"平方完成する",D(r"y=2x^2-8x+3=2(x^2-4x)+3=2\{(x-2)^2-4\}+3=2(x-2)^2-5")+"<p>下に凸、頂点 "+I("(2,-5)")+"、軸 "+I("x=2")+"。</p>"),
  step(2,"定義域とグラフを見る","<p>軸 "+I("x=2")+" は定義域 "+I("0\\leqq x\\leqq5")+" の中にある（図）。</p>"+f1),
  step(3,"両端の値を計算する",D(r"x=0:\ y=3")+D(r"x=5:\ y=2(5-2)^2-5=18-5=13")),
  step(4,"比べる","<p>最小は頂点 "+I("x=2")+" のとき "+I("-5")+"。最大は軸から遠い "+I("x=5")+"（軸との距離3）のとき "+I("13")+"（"+I("x=0")+" は距離2で "+I("3")+"）。</p>")],
 answer=r"x=5\ \text{で最大値}\ 13,\quad x=2\ \text{で最小値}\ -5",
 practice=[r"y=-x^2+2x+3\ \ (-2\leqq x\leqq3)",r"y=x^2+4x+1\ \ (-1\leqq x\leqq2)",r"y=-2x^2+4x\ \ (1\leqq x\leqq3)"],
 pans=[
  ("<p>"+I("y=-(x-1)^2+4")+"。上に凸、軸 "+I("x=1")+" は定義域内。最大は頂点 "+I("x=1")+" で "+I("4")+"。</p><p>両端："+I("x=-2:\\ y=-(-3)^2+4=-5")+"、"+I("x=3:\\ y=-4+4=0")+"。軸から遠い "+I("x=-2")+"（距離3）で最小 "+I("-5")+"。</p>",r"x=1\ \text{で最大}\ 4,\ \ x=-2\ \text{で最小}\ -5"),
  ("<p>"+I("y=(x+2)^2-3")+"。下に凸、軸 "+I("x=-2")+" は定義域 "+I("-1\\leqq x\\leqq2")+" の<b>外</b>（左）。定義域内では単調に増加する。</p><p>"+I("x=-1:\\ y=1-3=-2")+"、"+I("x=2:\\ y=16-3=13")+"。</p>",r"x=2\ \text{で最大}\ 13,\ \ x=-1\ \text{で最小}\ -2"),
  ("<p>"+I("y=-2(x-1)^2+2")+"。上に凸、軸 "+I("x=1")+" は定義域 "+I("1\\leqq x\\leqq3")+" の左端。定義域内では単調に減少する。</p><p>"+I("x=1:\\ y=2")+"、"+I("x=3:\\ y=-2\\cdot4+2=-6")+"。</p>",r"x=1\ \text{で最大}\ 2,\ \ x=3\ \text{で最小}\ -6")])
def chk(f,lo,hi,mn,mx):
    a,b=mm(f,Fr(lo),Fr(hi)); assert abs(a-mn)<1e-6 and abs(b-mx)<1e-6,(a,b,mn,mx)
chk(lambda v:2*v*v-8*v+3,0,5,-5,13); chk(lambda v:-v*v+2*v+3,-2,3,-5,4); chk(lambda v:v*v+4*v+1,-1,2,-2,13); chk(lambda v:-2*v*v+4*v,1,3,-6,2)

# ===== 例題2 軸が動く（最小値） =====
def axfig(name,a):
    return graph(name,[(lambda v:(v-a)**2+0.4,RED,"-")],(-1.5,3.5),(-0.5,5),xticks=[(0,"0"),(2,"2")],vlines=[(0,"#aaa"),(2,"#aaa"),(a,"#c88")],w=100,size=(2.6,2.2))
fig2=row([axfig("i32_e2a",-0.7),axfig("i32_e2b",1.0),axfig("i32_e2c",2.7)])
ex(title="軸が動く場合の最小値（場合分け）",
 problem=I("a")+" は定数とする。2次関数 "+I("f(x)=x^2-2ax+1")+"（"+I("0\\leqq x\\leqq2")+"）の最小値 "+I("m(a)")+" を求めよ。",
 approach="<p>平方完成すると "+I("f(x)=(x-a)^2-a^2+1")+"。<b>軸 "+I("x=a")+" が定義域 "+I("0\\leqq x\\leqq2")+" に対してどの位置にあるか</b>で最小値が変わる。下に凸なので、軸が定義域の<b>左・中・右</b>の3通りに場合分けする。</p>",
 kotsu="谷底（軸）がコースの外にあるときは、谷底に近い端が最低点。コースの中にあるときは谷底そのものが最低点。",
 steps=[
  step(1,"平方完成する",D(r"f(x)=x^2-2ax+1=(x-a)^2-a^2+1")+"<p>軸は "+I("x=a")+"、下に凸。</p>"),
  step(2,"軸の位置で3つに場合分けする","<p>左：軸が定義域の左（"+I("a<0")+"）。中：軸が定義域内（"+I("0\\leqq a\\leqq2")+"）。右：軸が定義域の右（"+I("a>2")+"）。（図は左・中・右の順）</p>"+fig2),
  step(3,r"① \(a<0\) のとき","<p>定義域内で単調に増加するので、最小は "+I("x=0")+" のとき。</p>"+D(r"m(a)=f(0)=1")),
  step(4,r"② \(0\leqq a\leqq2\) のとき","<p>頂点で最小。</p>"+D(r"m(a)=f(a)=-a^2+1")),
  step(5,r"③ \(a>2\) のとき","<p>定義域内で単調に減少するので、最小は "+I("x=2")+" のとき。</p>"+D(r"m(a)=f(2)=4-4a+1=5-4a"))],
 answer=r"m(a)=\begin{cases}1&(a<0)\\ -a^2+1&(0\leqq a\leqq2)\\ 5-4a&(a>2)\end{cases}",
 practice=[r"f(x)=x^2-2ax+3\ \ (0\leqq x\leqq4)\ \text{の最小値}\ m(a)",r"f(x)=x^2+2ax-1\ \ (-1\leqq x\leqq1)\ \text{の最小値}\ m(a)",r"f(x)=x^2-6ax+1\ \ (0\leqq x\leqq3)\ \text{の最小値}\ m(a)"],
 pans=[
  ("<p>"+I("f(x)=(x-a)^2-a^2+3")+"。軸 "+I("x=a")+"。</p><p>"+I("a<0")+"："+I("m=f(0)=3")+"。"+I("0\\leqq a\\leqq4")+"："+I("m=f(a)=-a^2+3")+"。"+I("a>4")+"："+I("m=f(4)=16-8a+3=19-8a")+"。</p>",r"m(a)=\begin{cases}3&(a<0)\\ -a^2+3&(0\leqq a\leqq4)\\ 19-8a&(a>4)\end{cases}"),
  ("<p>"+I("f(x)=(x+a)^2-a^2-1")+"。軸 "+I("x=-a")+"。</p><p>軸が左（"+I("-a<-1")+"、"+I("a>1")+"）："+I("m=f(-1)=1-2a-1=-2a")+"。軸が中（"+I("-1\\leqq-a\\leqq1")+"、"+I("-1\\leqq a\\leqq1")+"）："+I("m=f(-a)=-a^2-1")+"。軸が右（"+I("-a>1")+"、"+I("a<-1")+"）："+I("m=f(1)=1+2a-1=2a")+"。</p>",r"m(a)=\begin{cases}2a&(a<-1)\\ -a^2-1&(-1\leqq a\leqq1)\\ -2a&(a>1)\end{cases}"),
  ("<p>"+I("f(x)=(x-3a)^2-9a^2+1")+"。軸 "+I("x=3a")+"。</p><p>"+I("3a<0")+"（"+I("a<0")+"）："+I("m=f(0)=1")+"。"+I("0\\leqq3a\\leqq3")+"（"+I("0\\leqq a\\leqq1")+"）："+I("m=f(3a)=-9a^2+1")+"。"+I("3a>3")+"（"+I("a>1")+"）："+I("m=f(3)=9-18a+1=10-18a")+"。</p>",r"m(a)=\begin{cases}1&(a<0)\\ -9a^2+1&(0\leqq a\leqq1)\\ 10-18a&(a>1)\end{cases}")])
def mina(F,lo,hi,a): return min(float(F(lo+(hi-lo)*Fr(k,2000),a)) for k in range(2001))
def M1(a): return 1 if a<0 else (-a*a+1 if a<=2 else 5-4*a)
for av in (-2,-.5,0,.7,2,3.3): assert abs(mina(lambda v,a:v*v-2*a*v+1,Fr(0),Fr(2),Fr(av).limit_denominator(100))-M1(av))<1e-5
def M2(a): return 3 if a<0 else (-a*a+3 if a<=4 else 19-8*a)
def M3(a): return 2*a if a<-1 else (-a*a-1 if a<=1 else -2*a)
def M4(a): return 1 if a<0 else (-9*a*a+1 if a<=1 else 10-18*a)
for av in (-3,-1,0,2,4,5.5): assert abs(mina(lambda v,a:v*v-2*a*v+3,Fr(0),Fr(4),Fr(av).limit_denominator(100))-M2(av))<1e-5
for av in (-3,-1,0,.5,1,2): assert abs(mina(lambda v,a:v*v+2*a*v-1,Fr(-1),Fr(1),Fr(av).limit_denominator(100))-M3(av))<1e-5
for av in (-1,0,.5,1,1.7,3): assert abs(mina(lambda v,a:v*v-6*a*v+1,Fr(0),Fr(3),Fr(av).limit_denominator(100))-M4(av))<1e-5

# ===== 例題3 軸が動く（最大値） =====
ex(title="軸が動く場合の最大値（定義域の中央で場合分け）",
 problem=I("a")+" は定数とする。2次関数 "+I("f(x)=x^2-2ax+1")+"（"+I("0\\leqq x\\leqq2")+"）の最大値 "+I("M(a)")+" を求めよ。",
 approach="<p>下に凸のグラフの最大値は、<b>軸から遠い方の端</b>で起こる。定義域 "+I("0\\leqq x\\leqq2")+" の<b>中央（"+I("x=1")+"）</b>と軸 "+I("x=a")+" の位置関係で、左端と右端のどちらが遠いかが変わる。</p>",
 kotsu="最小は「谷底に近い方」、最大は「谷底から遠い方」。谷底が中央より右なら左端、左なら右端が高い。",
 steps=[
  step(1,"軸と中央の位置で場合分けする","<p>軸 "+I("x=a")+"、定義域の中央 "+I("x=1")+"。</p><p>"+I("a<1")+"：軸は中央より左 → 右端 "+I("x=2")+" の方が遠い。</p><p>"+I("a>1")+"：軸は中央より右 → 左端 "+I("x=0")+" の方が遠い。</p><p>"+I("a=1")+"：両端が等距離で、値は等しい。</p>"),
  step(2,r"\(a<1\) のとき",D(r"M(a)=f(2)=4-4a+1=5-4a")),
  step(3,r"\(a\geqq1\) のとき","<p>"+I("a=1")+" のとき "+I("f(0)=f(2)=1")+"（"+I("5-4a=1")+" とも一致）なので、"+I("a=1")+" はどちらに入れてもよい。</p>"+D(r"M(a)=f(0)=1")),
  step(4,"確かめる","<p>"+I("a=0")+"："+I("f(x)=x^2+1")+"、"+I("0\\leqq x\\leqq2")+" の最大は "+I("f(2)=5")+"。"+I("5-4\\cdot0=5")+"。</p><p>"+I("a=3")+"：右端 "+I("f(2)=5-12=-7")+"、左端 "+I("f(0)=1")+"。最大は "+I("1")+"。</p>")],
 answer=r"M(a)=\begin{cases}5-4a&(a<1)\\ 1&(a\geqq1)\end{cases}",
 practice=[r"f(x)=x^2-2ax+3\ \ (0\leqq x\leqq4)\ \text{の最大値}\ M(a)",r"f(x)=x^2+2ax\ \ (-1\leqq x\leqq3)\ \text{の最大値}\ M(a)",r"f(x)=x^2-4ax\ \ (0\leqq x\leqq2)\ \text{の最大値}\ M(a)"],
 pans=[
  ("<p>中央 "+I("x=2")+"、軸 "+I("x=a")+"。"+I("a<2")+"：右端が遠い "+I("M=f(4)=16-8a+3=19-8a")+"。"+I("a\\geqq2")+"：左端が遠い "+I("M=f(0)=3")+"（"+I("a=2")+" で両端とも "+I("3")+"）。</p>",r"M(a)=\begin{cases}19-8a&(a<2)\\ 3&(a\geqq2)\end{cases}"),
  ("<p>"+I("f(x)=(x+a)^2-a^2")+"、軸 "+I("x=-a")+"、中央 "+I("x=1")+"。"+I("-a<1")+"（"+I("a>-1")+"）：右端が遠い "+I("M=f(3)=9+6a")+"。"+I("-a\\geqq1")+"（"+I("a\\leqq-1")+"）：左端が遠い "+I("M=f(-1)=1-2a")+"（"+I("a=-1")+" で両端とも "+I("3")+"）。</p>",r"M(a)=\begin{cases}9+6a&(a>-1)\\ 1-2a&(a\leqq-1)\end{cases}"),
  ("<p>"+I("f(x)=(x-2a)^2-4a^2")+"、軸 "+I("x=2a")+"、中央 "+I("x=1")+"。"+I("2a<1")+"（"+I("a<\\dfrac12")+"）：右端が遠い "+I("M=f(2)=4-8a")+"。"+I("2a\\geqq1")+"（"+I("a\\geqq\\dfrac12")+"）：左端が遠い "+I("M=f(0)=0")+"（"+I("a=\\dfrac12")+" で両端とも "+I("0")+"）。</p>",r"M(a)=\begin{cases}4-8a&(a<\frac12)\\ 0&(a\geqq\frac12)\end{cases}")])
def maxa(F,lo,hi,a): return max(float(F(lo+(hi-lo)*Fr(k,2000),a)) for k in range(2001))
for av in (-1,0,.5,1,1.5,3): assert abs(maxa(lambda v,a:v*v-2*a*v+1,Fr(0),Fr(2),Fr(av))-(5-4*av if av<1 else 1))<1e-5
for av in (-1,0,1,2,3,5): assert abs(maxa(lambda v,a:v*v-2*a*v+3,Fr(0),Fr(4),Fr(av))-(19-8*av if av<2 else 3))<1e-5
for av in (-3,-1,-.5,0,1,2): assert abs(maxa(lambda v,a:v*v+2*a*v,Fr(-1),Fr(3),Fr(av))-(9+6*av if av>-1 else 1-2*av))<1e-5
for av in (-1,0,.25,.5,1,2): assert abs(maxa(lambda v,a:v*v-4*a*v,Fr(0),Fr(2),Fr(av))-(4-8*av if av<.5 else 0))<1e-5

# ===== 例題4 置き換え =====
ex(title="置き換えを使う最大・最小（範囲に注意）",
 problem="関数 "+I("y=(x^2-2x)^2+4(x^2-2x)+3")+" の最小値と、そのときの "+I("x")+" の値を求めよ。",
 approach="<p>"+I("t=x^2-2x")+" とおくと "+I("y")+" は "+I("t")+" の2次関数になる。ただし<b>"+I("t")+" の取りうる値の範囲</b>を必ず先に調べる。"+I("t")+" は "+I("x")+" が実数全体を動いて "+I("t=(x-1)^2-1\\geqq-1")+" となる。2次関数の頂点が "+I("t")+" の範囲外のとき、最小値は頂点ではない。</p>",
 kotsu="かたまりを t に置き換えたら、t が走れる道（範囲）を確認する。谷底が道の外なら、道の端が最低点。",
 steps=[
  step(1,r"\(t\) の範囲を調べる",D(r"t=x^2-2x=(x-1)^2-1\geqq-1")+"<p>よって "+I("t\\geqq-1")+"。</p>"),
  step(2,r"\(y\) を \(t\) で表す",D(r"y=t^2+4t+3=(t+2)^2-1")),
  step(3,"頂点と範囲を比べる","<p>頂点は "+I("t=-2")+"。しかし "+I("t\\geqq-1")+" なので頂点は範囲の<b>外</b>（左）。</p><p>"+I("t\\geqq-1")+" では "+I("y")+" は単調に増加するから、最小は "+I("t=-1")+" のとき。</p>"+D(r"y=(-1)^2+4\cdot(-1)+3=1-4+3=0")),
  step(4,r"\(t=-1\) となる \(x\) を求める",D(r"x^2-2x=-1\ \Rightarrow\ x^2-2x+1=0\ \Rightarrow\ (x-1)^2=0\ \Rightarrow\ x=1"))],
 answer=r"x=1\ \text{のとき最小値}\ 0",
 practice=[r"y=(x^2+4x)^2+6(x^2+4x)+5",r"y=(x^2-2x)^2-2(x^2-2x)+2",r"y=-(x^2+2x)^2-2(x^2+2x)+5\ \text{の最大値}"],
 pans=[
  ("<p>"+I("t=x^2+4x=(x+2)^2-4\\geqq-4")+"。"+I("y=t^2+6t+5=(t+3)^2-4")+"。頂点 "+I("t=-3")+" は "+I("t\\geqq-4")+" の<b>内</b>にある。最小は "+I("t=-3")+" のとき "+I("-4")+"。</p><p>"+I("x^2+4x=-3")+" → "+I("x^2+4x+3=0")+" → "+I("(x+1)(x+3)=0")+" → "+I("x=-1,\\ -3")+"。</p>",r"x=-1,\ -3\ \text{のとき最小値}\ -4"),
  ("<p>"+I("t=x^2-2x\\geqq-1")+"。"+I("y=t^2-2t+2=(t-1)^2+1")+"。頂点 "+I("t=1")+" は "+I("t\\geqq-1")+" の内にある。最小は "+I("t=1")+" のとき "+I("1")+"。</p><p>"+I("x^2-2x=1")+" → "+I("x^2-2x-1=0")+" → "+I("x=1\\pm\\sqrt2")+"。</p>",r"x=1\pm\sqrt2\ \text{のとき最小値}\ 1"),
  ("<p>"+I("t=x^2+2x=(x+1)^2-1\\geqq-1")+"。"+I("y=-t^2-2t+5=-(t+1)^2+6")+"。頂点 "+I("t=-1")+" は範囲の端。最大は "+I("t=-1")+" のとき "+I("6")+"。</p><p>"+I("x^2+2x=-1")+" → "+I("(x+1)^2=0")+" → "+I("x=-1")+"。</p>",r"x=-1\ \text{のとき最大値}\ 6")])
import numpy as np
def num(F,lo=-8,hi=8):
    xs=np.linspace(lo,hi,160001); v=F(xs); return v.min(),v.max()
assert abs(num(lambda v:(v*v-2*v)**2+4*(v*v-2*v)+3)[0])<1e-6
assert abs(num(lambda v:(v*v+4*v)**2+6*(v*v+4*v)+5)[0]+4)<1e-6
assert abs(num(lambda v:(v*v-2*v)**2-2*(v*v-2*v)+2)[0]-1)<1e-6
assert abs(num(lambda v:-(v*v+2*v)**2-2*(v*v+2*v)+5)[1]-6)<1e-6

# ===== 例題5 条件つき（隠れた定義域） =====
ex(title="条件式のある最大・最小（変数の範囲に注意）",
 problem=I("x\\geqq0,\\ y\\geqq0")+" で "+I("2x+y=6")+" のとき、"+I("x^2+y")+" の最大値と最小値を求めよ。",
 approach="<p>条件式で "+I("y")+" を "+I("x")+" で表して<b>1変数にする</b>。そのとき、"+I("y\\geqq0")+" から "+I("x")+" の<b>定義域が決まる</b>ことを見落とさない。あとは定義域つきの2次関数の最大・最小。</p>",
 kotsu="文字を1つ消したら、消えた文字がマイナスにならない条件が、残った文字の「隠れた道の長さ」になる。",
 steps=[
  step(1,r"\(y\) を消去する","<p>"+I("y=6-2x")+"。</p>"),
  step(2,r"\(x\) の範囲を求める","<p>"+I("x\\geqq0")+" かつ "+I("y=6-2x\\geqq0")+" より "+I("x\\leqq3")+"。</p>"+D(r"0\leqq x\leqq3")),
  step(3,"式を1変数で表す",D(r"x^2+y=x^2+(6-2x)=x^2-2x+6=(x-1)^2+5")),
  step(4,"定義域で最大・最小を調べる","<p>軸 "+I("x=1")+" は "+I("0\\leqq x\\leqq3")+" の内。最小は "+I("x=1")+" のとき "+I("5")+"（このとき "+I("y=4")+"）。</p><p>両端："+I("x=0:\\ 6")+"、"+I("x=3:\\ (3-1)^2+5=9")+"。軸から遠い "+I("x=3")+" で最大 "+I("9")+"（"+I("y=0")+"）。</p>")],
 answer=r"(x,y)=(3,0)\ \text{で最大値}\ 9,\quad (x,y)=(1,4)\ \text{で最小値}\ 5",
 practice=[r"x\geqq0,\ y\geqq0,\ x+2y=8\ \text{のとき},\ xy\ \text{の最大値と最小値}",r"x\geqq0,\ y\geqq0,\ x+y=5\ \text{のとき},\ x^2+y^2\ \text{の最大値と最小値}",r"x\geqq0,\ y\geqq0,\ 3x+y=6\ \text{のとき},\ x^2+xy\ \text{の最大値と最小値}"],
 pans=[
  ("<p>"+I("x=8-2y\\geqq0")+" より "+I("0\\leqq y\\leqq4")+"。"+I("xy=(8-2y)y=-2y^2+8y=-2(y-2)^2+8")+"。軸 "+I("y=2")+" は範囲内で最大 "+I("8")+"（"+I("x=4")+"）。両端 "+I("y=0,\\ 4")+" で "+I("0")+"（最小）。</p>",r"\text{最大 }8\ (x,y)=(4,2),\ \ \text{最小 }0\ (x,y)=(8,0),(0,4)"),
  ("<p>"+I("y=5-x\\geqq0")+" より "+I("0\\leqq x\\leqq5")+"。"+I("x^2+y^2=x^2+(5-x)^2=2x^2-10x+25=2\\left(x-\\dfrac52\\right)^2+\\dfrac{25}2")+"。軸 "+I("x=\\dfrac52")+" は範囲内で最小 "+I("\\dfrac{25}2")+"。両端 "+I("x=0,\\ 5")+" で "+I("25")+"（最大）。</p>",r"\text{最大 }25\ (x,y)=(0,5),(5,0),\ \ \text{最小 }\dfrac{25}2\ (x,y)=\left(\dfrac52,\dfrac52\right)"),
  ("<p>"+I("y=6-3x\\geqq0")+" より "+I("0\\leqq x\\leqq2")+"。"+I("x^2+xy=x^2+x(6-3x)=-2x^2+6x=-2\\left(x-\\dfrac32\\right)^2+\\dfrac92")+"。軸 "+I("x=\\dfrac32")+" は範囲内で最大 "+I("\\dfrac92")+"。両端："+I("x=0:\\ 0")+"、"+I("x=2:\\ -8+12=4")+"。軸から遠い "+I("x=0")+" で最小 "+I("0")+"。</p>",r"\text{最大 }\dfrac92\ (x,y)=\left(\dfrac32,\dfrac32\right),\ \ \text{最小 }0\ (x,y)=(0,6)")])
assert [round(max(float(xx*yy) for xx,yy in ((8-2*Fr(k,1000)*1,Fr(k,1000)) for k in range(0,4001))),6)][0]==8
assert min(float((8-2*Fr(k,1000))*Fr(k,1000)) for k in range(0,4001))==0
assert abs(min(float(Fr(k,1000)**2+(5-Fr(k,1000))**2) for k in range(0,5001))-12.5)<1e-6 and max(float(Fr(k,1000)**2+(5-Fr(k,1000))**2) for k in range(0,5001))==25
assert abs(max(float(-2*Fr(k,1000)**2+6*Fr(k,1000)) for k in range(0,2001))-4.5)<1e-6 and min(float(-2*Fr(k,1000)**2+6*Fr(k,1000)) for k in range(0,2001))==0

CHE=[
 (r"y=-2x^2+8x-3\ \ (0\leqq x\leqq5)\ \text{の最大値と最小値を求めよ。}",
  "<p>"+I("y=-2(x^2-4x)-3=-2\\{(x-2)^2-4\\}-3=-2(x-2)^2+5")+"。上に凸、軸 "+I("x=2")+" は範囲内。最大は "+I("x=2")+" のとき "+I("5")+"。</p><p>両端："+I("x=0:\\ -3")+"、"+I("x=5:\\ -2\\cdot9+5=-13")+"。軸から遠い "+I("x=5")+" で最小 "+I("-13")+"。</p>",
  r"x=2\ \text{で最大}\ 5,\ \ x=5\ \text{で最小}\ -13",1),
 (r"a\ \text{は定数とする。}f(x)=x^2-4ax\ \ (0\leqq x\leqq2)\ \text{の最小値}\ m(a)\ \text{を求めよ。}",
  "<p>"+I("f(x)=(x-2a)^2-4a^2")+"。軸 "+I("x=2a")+"。</p><p>"+I("2a<0")+"（"+I("a<0")+"）："+I("m=f(0)=0")+"。"+I("0\\leqq2a\\leqq2")+"（"+I("0\\leqq a\\leqq1")+"）："+I("m=f(2a)=-4a^2")+"。"+I("2a>2")+"（"+I("a>1")+"）："+I("m=f(2)=4-8a")+"。</p>",
  r"m(a)=\begin{cases}0&(a<0)\\ -4a^2&(0\leqq a\leqq1)\\ 4-8a&(a>1)\end{cases}",2),
 (r"a\ \text{は定数とする。}f(x)=x^2-2ax+2\ \ (0\leqq x\leqq2)\ \text{の最大値}\ M(a)\ \text{を求めよ。}",
  "<p>軸 "+I("x=a")+"、中央 "+I("x=1")+"。"+I("a<1")+"：右端が遠い "+I("M=f(2)=4-4a+2=6-4a")+"。"+I("a\\geqq1")+"：左端が遠い "+I("M=f(0)=2")+"（"+I("a=1")+" で両端とも "+I("2")+"）。</p>",
  r"M(a)=\begin{cases}6-4a&(a<1)\\ 2&(a\geqq1)\end{cases}",3),
 (r"y=(x^2-4x)^2+2(x^2-4x)\ \text{の最小値を求めよ。}",
  "<p>"+I("t=x^2-4x=(x-2)^2-4\\geqq-4")+"。"+I("y=t^2+2t=(t+1)^2-1")+"。頂点 "+I("t=-1")+" は "+I("t\\geqq-4")+" の内。最小は "+I("t=-1")+" のとき "+I("-1")+"。</p><p>"+I("x^2-4x=-1")+" → "+I("x=2\\pm\\sqrt3")+"。</p>",
  r"x=2\pm\sqrt3\ \text{のとき最小値}\ -1",4),
 (r"x\geqq0,\ y\geqq0,\ x+3y=6\ \text{のとき},\ xy\ \text{の最大値と最小値を求めよ。}",
  "<p>"+I("x=6-3y\\geqq0")+" より "+I("0\\leqq y\\leqq2")+"。"+I("xy=(6-3y)y=-3y^2+6y=-3(y-1)^2+3")+"。軸 "+I("y=1")+" は範囲内で最大 "+I("3")+"（"+I("x=3")+"）。両端 "+I("y=0")+"：0、"+I("y=2")+"：0。最小 "+I("0")+"。</p>",
  r"\text{最大 }3\ (x,y)=(3,1),\ \ \text{最小 }0",5)]
chk(lambda v:-2*v*v+8*v-3,0,5,-13,5)
for av in (-1,0,.5,1,2,3): assert abs(mina(lambda v,a:v*v-4*a*v,Fr(0),Fr(2),Fr(av))-(0 if av<0 else (-4*av*av if av<=1 else 4-8*av)))<1e-5
for av in (-1,0,.5,1,2,3): assert abs(maxa(lambda v,a:v*v-2*a*v+2,Fr(0),Fr(2),Fr(av))-(6-4*av if av<1 else 2))<1e-5
assert abs(num(lambda v:(v*v-4*v)**2+2*(v*v-4*v))[0]+1)<1e-6

UNIT=dict(subject="1",ci=2,ui=1,chapter="2次関数",name="2次関数の最大・最小",
  intro="定義域つきの最大最小、軸が動く場合分け、置き換え、条件式つきの最大最小など、2次関数の最大・最小の難問に挑みます。",
  examples=EXS,chapter_end=CHE)
