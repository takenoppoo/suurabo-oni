# -*- coding: utf-8 -*-
# 2次不等式（数学I 2次関数）
from tools import *
from fractions import Fraction as Fr
import sympy as sp, numpy as np
x,a=sp.symbols('x a')
EXS=[]
def ex(**k): EXS.append(k)
def row(figs): return "".join(figs)
G=[Fr(k,16) for k in range(-16*14,16*14+1)]
def sol(*conds): return [t for t in G if all(c(t) for c in conds)]
def segs_ok(S,intervals):
    """S の各点が intervals のどれかに入るか＆逆（intervals: (lo,hi,lo_closed,hi_closed)）"""
    def inn(t):
        for lo,hi,lc,hc in intervals:
            if (t>lo or (lc and t==lo)) and (t<hi or (hc and t==hi)): return True
        return False
    return set(S)==set(t for t in G if inn(t))
INF=Fr(10**6)

# ===== 例題1 連立2次不等式 =====
l1=nl("i34_e1a",-4,7,[-2,5],["-2","5"],segs=[(-2,5)],pts=[(-2,"open"),(5,"open")],w=66,size=(6.2,1.3))
l2=nl("i34_e1b",-4,7,[-1,2],["-1","2"],segs=[(None,-1),(2,None)],pts=[(-1,"closed"),(2,"closed")],w=66,size=(6.2,1.3))
l3=nl("i34_e1c",-4,7,[-2,-1,2,5],["-2","-1","2","5"],segs=[(-2,-1),(2,5)],pts=[(-2,"open"),(-1,"closed"),(2,"closed"),(5,"open")],w=66,size=(6.2,1.3))
ex(title="連立2次不等式",
 problem="連立不等式"+D(r"\begin{cases}x^2-3x-10<0\\ x^2-x-2\geqq0\end{cases}")+"を解け。",
 approach="<p>それぞれの不等式を<b>別々に解いて数直線に描き</b>、<b>共通部分</b>を求める。2次不等式は、<b>因数分解して「グラフが "+I("x")+" 軸の下か上か」</b>で解く。</p>"+D(r"(x-\alpha)(x-\beta)<0\ (\alpha<\beta)\Rightarrow\alpha<x<\beta")+D(r"(x-\alpha)(x-\beta)>0\ (\alpha<\beta)\Rightarrow x<\alpha,\ \beta<x"),
 kotsu="2つの門を両方通れる場所だけが答え。数直線に2本の道を描いて、重なる所を探す。端の○と●に注意。",
 steps=[
  step(1,"①を解く",D(r"x^2-3x-10=(x-5)(x+2)<0\ \Rightarrow\ -2<x<5")+l1),
  step(2,"②を解く",D(r"x^2-x-2=(x-2)(x+1)\geqq0\ \Rightarrow\ x\leqq-1,\ \ 2\leqq x")+l2),
  step(3,"共通部分を求める","<p>①と②の重なりは下図の太線。</p>"+l3+"<p>"+I("-2<x\\leqq-1")+" と "+I("2\\leqq x<5")+"。</p>"),
  step(4,"端点を確かめる","<p>"+I("x=-1")+"：①"+I("1+3-10=-6<0")+"、②"+I("1+1-2=0\\geqq0")+" で両方成立。"+I("x=2")+"：①"+I("4-6-10=-12<0")+"、②"+I("4-2-2=0\\geqq0")+" で両方成立。</p>")],
 answer=r"-2<x\leqq-1,\quad 2\leqq x<5",
 practice=[r"\begin{cases}x^2-x-6<0\\ x^2-4x+3\geqq0\end{cases}",r"\begin{cases}x^2-2x-8\leqq0\\ x^2-x-2>0\end{cases}",r"\begin{cases}x^2-4<0\\ x^2-x-2\geqq0\end{cases}"],
 pans=[
  ("<p>①："+I("(x-3)(x+2)<0")+" より "+I("-2<x<3")+"。②："+I("(x-1)(x-3)\\geqq0")+" より "+I("x\\leqq1,\\ 3\\leqq x")+"。重なり：</p>"+D(r"-2<x\leqq1"),r"-2<x\leqq1"),
  ("<p>①："+I("(x-4)(x+2)\\leqq0")+" より "+I("-2\\leqq x\\leqq4")+"。②："+I("(x-2)(x+1)>0")+" より "+I("x<-1,\\ 2<x")+"。重なり：</p>"+D(r"-2\leqq x<-1,\quad 2<x\leqq4"),r"-2\leqq x<-1,\ \ 2<x\leqq4"),
  ("<p>①："+I("(x-2)(x+2)<0")+" より "+I("-2<x<2")+"。②："+I("(x-2)(x+1)\\geqq0")+" より "+I("x\\leqq-1,\\ 2\\leqq x")+"。重なり：</p>"+D(r"-2<x\leqq-1"),r"-2<x\leqq-1")])
assert segs_ok(sol(lambda t:t*t-3*t-10<0,lambda t:t*t-t-2>=0),[(-2,-1,False,True),(2,5,True,False)])
assert segs_ok(sol(lambda t:t*t-t-6<0,lambda t:t*t-4*t+3>=0),[(-2,1,False,True)])
assert segs_ok(sol(lambda t:t*t-2*t-8<=0,lambda t:t*t-t-2>0),[(-2,-1,True,False),(2,4,False,True)])
assert segs_ok(sol(lambda t:t*t-4<0,lambda t:t*t-t-2>=0),[(-2,-1,False,True)])

# ===== 例題2 すべての実数で成り立つ =====
f2=graph("i34_e2",[(lambda v:(v-1)**2+0.8,RED,"-")],(-2,4),(-1,5),xticks=[],w=44,size=(3.6,2.8))
ex(title="すべての実数 x で成り立つ条件",
 problem="すべての実数 "+I("x")+" について "+I("x^2-2ax+a+2>0")+" が成り立つような定数 "+I("a")+" の値の範囲を求めよ。",
 approach="<p>下に凸の放物線 "+I("y=x^2-2ax+a+2")+" が<b>全体で "+I("x")+" 軸より上</b>にあればよい（図）。つまり "+I("x")+" 軸と<b>共有点をもたない</b>。</p>"+D(r"\text{常に}\ x^2+bx+c>0\ \Leftrightarrow\ D<0")+"<p>（"+I("x^2")+" の係数が正のとき）。</p>",
 kotsu="谷底が地面（x軸）より上にある放物線は、地面に一度も触れない＝判別式がマイナス。",
 steps=[
  step(1,"条件をグラフで言いかえる","<p>"+I("x^2")+" の係数は1（正）。グラフが "+I("x")+" 軸と共有点をもたなければ、常に "+I("y>0")+"。</p>"+f2),
  step(2,"判別式を計算する",D(r"\dfrac D4=(-a)^2-1\cdot(a+2)=a^2-a-2")),
  step(3,r"\(D<0\) を解く",D(r"a^2-a-2<0\ \Rightarrow\ (a-2)(a+1)<0\ \Rightarrow\ -1<a<2")),
  step(4,"確かめる","<p>"+I("a=0")+"："+I("x^2+2>0")+" は常に成立。"+I("a=2")+"：+"+I("x^2-4x+4=(x-2)^2")+" は "+I("x=2")+" で "+I("0")+" になり "+I(">0")+" でない。不適。</p>")],
 answer=r"-1<a<2",
 practice=[r"x^2+2ax-a+2>0\ \text{がすべての実数}\ x\ \text{で成り立つ}\ a",r"x^2-(a+2)x+a+5>0\ \text{がすべての実数}\ x\ \text{で成り立つ}\ a",r"x^2+ax+a>0\ \text{がすべての実数}\ x\ \text{で成り立つ}\ a"],
 pans=[
  ("<p>"+I("\\dfrac D4=a^2-(-a+2)=a^2+a-2=(a+2)(a-1)<0")+" より</p>"+D(r"-2<a<1"),r"-2<a<1"),
  ("<p>"+I("D=(a+2)^2-4(a+5)=a^2-16<0")+" より</p>"+D(r"-4<a<4"),r"-4<a<4"),
  ("<p>"+I("D=a^2-4a=a(a-4)<0")+" より</p>"+D(r"0<a<4"),r"0<a<4")])
for av in np.arange(-6,6.01,0.25):
    assert (min(t*t-2*av*t+av+2 for t in np.linspace(-20,20,40001))>1e-9)==(-1<av<2) or abs(av-(-1))<1e-9 or abs(av-2)<1e-9
    assert (min(t*t+2*av*t-av+2 for t in np.linspace(-30,30,60001))>1e-9)==(-2<av<1) or av in(-2,1)
    assert (min(t*t-(av+2)*t+av+5 for t in np.linspace(-30,30,60001))>1e-9)==(-4<av<4) or av in(-4,4)
    assert (min(t*t+av*t+av for t in np.linspace(-30,30,60001))>1e-9)==(0<av<4) or av in(0,4)

# ===== 例題3 解から係数を決める =====
ex(title="解から2次不等式の係数を決める",
 problem="2次不等式 "+I("x^2+ax+b<0")+" の解が "+I("-2<x<5")+" であるとき、定数 "+I("a,\\ b")+" の値を求めよ。",
 approach="<p>解が "+I("-2<x<5")+" となる2次不等式は "+I("(x+2)(x-5)<0")+"。これを展開して "+I("x^2+ax+b<0")+" と比べる。<b>"+I("x^2")+" の係数が1で同じ</b>ことを確認して、係数を比較する。</p>",
 kotsu="答えの範囲（-2 と 5）は、グラフが x 軸を横切る2地点。その2地点から、もとの式を逆算する。",
 steps=[
  step(1,"解から不等式を作る","<p>"+I("x^2")+" の係数が1で解が "+I("-2<x<5")+" となるのは</p>"+D(r"(x+2)(x-5)<0")),
  step(2,"展開する",D(r"(x+2)(x-5)=x^2-5x+2x-10=x^2-3x-10")),
  step(3,"係数を比べる","<p>"+I("x^2+ax+b<0")+" と "+I("x^2-3x-10<0")+" を比べて</p>"+D(r"a=-3,\qquad b=-10")),
  step(4,"確かめる","<p>"+I("x^2-3x-10<0")+" を解くと "+I("(x-5)(x+2)<0")+" より "+I("-2<x<5")+"。</p>")],
 answer=r"a=-3,\quad b=-10",
 practice=[r"x^2+ax+b\leqq0\ \text{の解が}\ -3\leqq x\leqq1",r"x^2+ax+b>0\ \text{の解が}\ x<-1,\ 4<x",r"ax^2+bx+4>0\ \text{の解が}\ -1<x<2"],
 pans=[
  ("<p>"+I("(x+3)(x-1)\\leqq0")+"。展開："+I("x^2-x+3x-3=x^2+2x-3")+"。</p>"+D(r"a=2,\quad b=-3"),r"a=2,\ b=-3"),
  ("<p>"+I("(x+1)(x-4)>0")+"。展開："+I("x^2-4x+x-4=x^2-3x-4")+"。</p>"+D(r"a=-3,\quad b=-4"),r"a=-3,\ b=-4"),
  ("<p>解が "+I("-1<x<2")+"（2解の間）なので、グラフは上に凸（"+I("a<0")+"）。"+I("a(x+1)(x-2)>0")+"（"+I("a<0")+"）と書ける。展開：</p>"+D(r"a(x+1)(x-2)=a(x^2-x-2)=ax^2-ax-2a")+"<p>定数項を比べて "+I("-2a=4")+" より "+I("a=-2")+"（"+I("a<0")+" をみたす）。"+I("b=-a=2")+"。</p>"+D(r"a=-2,\quad b=2")+"<p>確かめ："+I("-2x^2+2x+4>0")+" → "+I("x^2-x-2<0")+" → "+I("-1<x<2")+"。</p>",r"a=-2,\ b=2")])
assert sp.expand((x+2)*(x-5))==x**2-3*x-10 and sp.expand((x+3)*(x-1))==x**2+2*x-3 and sp.expand((x+1)*(x-4))==x**2-3*x-4
assert segs_ok(sol(lambda t:-2*t*t+2*t+4>0),[(-1,2,False,False)])

# ===== 例題4 整数解の個数 =====
f4a=nl("i34_e4a",-1,8,[2,3,4,5,6],None,segs=[(2,5.6)],pts=[(2,"open"),(5.6,"open")],w=68,size=(6.2,1.3),extra=lambda ax:ax.text(5.6,0.55,"a",ha="center",fontsize=13,color=RED))
ex(title="2次不等式の整数解の個数",
 problem="2次不等式 "+I("x^2-(a+2)x+2a<0")+" をみたす整数 "+I("x")+" がちょうど3個であるとき、定数 "+I("a")+" の値の範囲を求めよ。",
 approach="<p>左辺を因数分解して "+I("(x-2)(x-a)<0")+"。解は2と "+I("a")+" の間で、<b>"+I("a")+" が2より大きいか小さいかで解の形が変わる</b>。場合分けして、数直線上の整数を数える。端点は含まれない（"+I("<")+"）ので等号の入り方に注意。</p>",
 kotsu="2つの端（2 と a）の間にある整数を数える。a が右にあるか左にあるかで2通り、a=2 は空っぽ。",
 steps=[
  step(1,"因数分解する",D(r"x^2-(a+2)x+2a=(x-2)(x-a)<0")),
  step(2,r"① \(a>2\) のとき","<p>解は "+I("2<x<a")+"（図）。整数が3個になるのは "+I("3,\\ 4,\\ 5")+"。</p>"+f4a+"<p>5 は入り、6 は入らない："+I("5<a")+"（等号なし）、"+I("a\\leqq6")+"（等号あり、"+I("a=6")+" のとき "+I("x<6")+"）。</p>"+D(r"5<a\leqq6")),
  step(3,r"② \(a<2\) のとき","<p>解は "+I("a<x<2")+"。整数が3個になるのは "+I("1,\\ 0,\\ -1")+"。</p><p>"+I("-1")+" は入り、"+I("-2")+" は入らない："+I("a<-1")+"（等号なし）、"+I("-2\\leqq a")+"（等号あり、"+I("a=-2")+" のとき "+I("x>-2")+"）。</p>"+D(r"-2\leqq a<-1")),
  step(4,r"③ \(a=2\) のとき","<p>"+I("(x-2)^2<0")+" となり解なし。整数解は0個で不適。</p>"),
  step(5,"まとめる","<p>①と②を合わせる。</p>")],
 answer=r"-2\leqq a<-1,\quad 5<a\leqq6",
 practice=[r"x^2-(a+1)x+a<0\ \text{をみたす整数}\ x\ \text{がちょうど2個}",r"x^2-(a-1)x-a<0\ \text{をみたす整数}\ x\ \text{がちょうど3個}",r"x^2-(a+3)x+3a\leqq0\ \text{をみたす整数}\ x\ \text{がちょうど2個}"],
 pans=[
  ("<p>"+I("(x-1)(x-a)<0")+"。</p><p>"+I("a>1")+"：解 "+I("1<x<a")+"、整数 2, 3 → "+I("3<a\\leqq4")+"。</p><p>"+I("a<1")+"：解 "+I("a<x<1")+"、整数 0, -1 → "+I("-2\\leqq a<-1")+"。</p>",r"-2\leqq a<-1,\ \ 3<a\leqq4"),
  ("<p>"+I("(x+1)(x-a)<0")+"。</p><p>"+I("a>-1")+"：解 "+I("-1<x<a")+"、整数 0, 1, 2 → "+I("2<a\\leqq3")+"。</p><p>"+I("a<-1")+"：解 "+I("a<x<-1")+"、整数 -2, -3, -4 → "+I("-5\\leqq a<-4")+"。</p>",r"-5\leqq a<-4,\ \ 2<a\leqq3"),
  ("<p>"+I("(x-3)(x-a)\\leqq0")+"。端点も含む。</p><p>"+I("a>3")+"：解 "+I("3\\leqq x\\leqq a")+"、整数 3, 4 → "+I("4\\leqq a<5")+"。</p><p>"+I("a<3")+"：解 "+I("a\\leqq x\\leqq3")+"、整数 2, 3 → "+I("2")+" は入り（"+I("a\\leqq2")+"、等号あり）、"+I("1")+" は入らない（"+I("1<a")+"、等号なし）："+I("1<a\\leqq2")+"。</p><p>"+I("a=3")+" は整数が3の1個だけで不適。</p>",r"1<a\leqq2,\ \ 4\leqq a<5")])
def cntint(f,av): return sum(1 for k in range(-40,41) if f(Fr(k),av))
def rngs(f,n,vals): 
    ok=[v for v in vals if cntint(f,v)==n]; return ok
V=[Fr(k,4) for k in range(-40,60)]
ok=rngs(lambda t,av:(t-2)*(t-av)<0,3,V); assert all((-2<=v<-1 or 5<v<=6) for v in ok) and all(((-2<=v<-1 or 5<v<=6)==(v in ok)) for v in V)
ok=rngs(lambda t,av:(t-1)*(t-av)<0,2,V); assert all((-2<=v<-1 or 3<v<=4)==(v in ok) for v in V)
ok=rngs(lambda t,av:(t+1)*(t-av)<0,3,V); assert all((-5<=v<-4 or 2<v<=3)==(v in ok) for v in V)
ok=rngs(lambda t,av:(t-3)*(t-av)<=0,2,V); assert all((1<v<=2 or 4<=v<5)==(v in ok) for v in V)

# ===== 例題5 x² の係数が文字 =====
ex(title="係数が文字のとき（a=0 の場合を忘れない）",
 problem="すべての実数 "+I("x")+" について "+I("ax^2-2ax+3>0")+" が成り立つような定数 "+I("a")+" の値の範囲を求めよ。",
 approach="<p>"+I("x^2")+" の係数 "+I("a")+" が文字のときは、<b>まず "+I("a=0")+"（2次式でなくなる場合）を別に調べる</b>。"+I("a\\neq0")+" のときは「"+I("a>0")+"（下に凸）かつ "+I("D<0")+"」で考える。</p>",
 kotsu="a が 0 になると放物線が消えて直線（や定数）になる。放物線のルールを使う前に、a＝0 の特別な場合を先にチェック。",
 steps=[
  step(1,r"\(a=0\) の場合","<p>不等式は "+I("3>0")+"。これは常に成り立つ。よって "+I("a=0")+" は適する。</p>"),
  step(2,r"\(a\neq0\) の場合の条件","<p>常に "+I("ax^2-2ax+3>0")+" となるには、グラフが下に凸（"+I("a>0")+"）で、"+I("x")+" 軸と共有点をもたない（"+I("D<0")+"）。</p>"),
  step(3,r"\(D<0\) を解く",D(r"\dfrac D4=(-a)^2-a\cdot3=a^2-3a=a(a-3)<0\ \Rightarrow\ 0<a<3")),
  step(4,"まとめる","<p>"+I("a>0")+" と合わせて "+I("0<a<3")+"。これに "+I("a=0")+" を加える。</p>"+D(r"0\leqq a<3")),
  step(5,"確かめる","<p>"+I("a=3")+"："+I("3x^2-6x+3=3(x-1)^2")+" は "+I("x=1")+" で0。不適。</p>")],
 answer=r"0\leqq a<3",
 practice=[r"ax^2+2ax+1>0\ \text{がすべての実数}\ x\ \text{で成り立つ}\ a",r"ax^2-4x+a>0\ \text{がすべての実数}\ x\ \text{で成り立つ}\ a",r"ax^2-2ax+4>0\ \text{がすべての実数}\ x\ \text{で成り立つ}\ a"],
 pans=[
  ("<p>"+I("a=0")+"：「"+I("1>0")+"」は常に成立。"+I("a\\neq0")+"："+I("a>0")+" かつ "+I("\\dfrac D4=a^2-a=a(a-1)<0")+" より "+I("0<a<1")+"。合わせて：</p>"+D(r"0\leqq a<1"),r"0\leqq a<1"),
  ("<p>"+I("a=0")+"：「"+I("-4x>0")+"」は常には成り立たない（"+I("x=1")+" で偽）。不適。"+I("a\\neq0")+"："+I("a>0")+" かつ "+I("\\dfrac D4=4-a^2<0")+" より "+I("a<-2,\\ 2<a")+"。"+I("a>0")+" と合わせて：</p>"+D(r"a>2"),r"a>2"),
  ("<p>"+I("a=0")+"：「"+I("4>0")+"」は常に成立。"+I("a\\neq0")+"："+I("a>0")+" かつ "+I("\\dfrac D4=a^2-4a=a(a-4)<0")+" より "+I("0<a<4")+"。合わせて：</p>"+D(r"0\leqq a<4"),r"0\leqq a<4")])
def allpos(c,av): return min(c(t,av) for t in np.linspace(-40,40,80001))>1e-9
for av in np.arange(-6,6.01,0.25):
    assert allpos(lambda t,a_:a_*t*t-2*a_*t+3,av)==(0<=av<3) or abs(av-3)<1e-9
    assert allpos(lambda t,a_:a_*t*t+2*a_*t+1,av)==(0<=av<1) or abs(av-1)<1e-9
    assert allpos(lambda t,a_:a_*t*t-4*t+a_,av)==(av>2) or abs(av-2)<1e-9
    assert allpos(lambda t,a_:a_*t*t-2*a_*t+4,av)==(0<=av<4) or abs(av-4)<1e-9

CHE=[
 (r"\begin{cases}x^2-x-12<0\\ x^2-2x-3\geqq0\end{cases}\ \text{を解け。}",
  "<p>①："+I("(x-4)(x+3)<0")+" より "+I("-3<x<4")+"。②："+I("(x-3)(x+1)\\geqq0")+" より "+I("x\\leqq-1,\\ 3\\leqq x")+"。重なり：</p>"+D(r"-3<x\leqq-1,\quad 3\leqq x<4"),
  r"-3<x\leqq-1,\ \ 3\leqq x<4",1),
 (r"x^2+2ax+2a+3>0\ \text{がすべての実数}\ x\ \text{で成り立つような}\ a\ \text{の範囲を求めよ。}",
  "<p>"+I("\\dfrac D4=a^2-(2a+3)=a^2-2a-3=(a-3)(a+1)<0")+" より</p>"+D(r"-1<a<3"),
  r"-1<a<3",2),
 (r"x^2+ax+b\geqq0\ \text{の解が}\ x\leqq-2,\ 3\leqq x\ \text{であるとき},\ a,\ b\ \text{の値を求めよ。}",
  "<p>"+I("(x+2)(x-3)\\geqq0")+"。展開："+I("x^2-3x+2x-6=x^2-x-6")+"。係数を比べて</p>"+D(r"a=-1,\quad b=-6"),
  r"a=-1,\ b=-6",3),
 (r"x^2-(a+4)x+4a<0\ \text{をみたす整数}\ x\ \text{がちょうど2個であるような}\ a\ \text{の範囲を求めよ。}",
  "<p>"+I("(x-4)(x-a)<0")+"。</p><p>"+I("a>4")+"：解 "+I("4<x<a")+"、整数 5, 6 → "+I("6<a\\leqq7")+"。</p><p>"+I("a<4")+"：解 "+I("a<x<4")+"、整数 3, 2 → "+I("1\\leqq a<2")+"。</p>",
  r"1\leqq a<2,\ \ 6<a\leqq7",4),
 (r"ax^2-2ax+2>0\ \text{がすべての実数}\ x\ \text{で成り立つような}\ a\ \text{の範囲を求めよ。}",
  "<p>"+I("a=0")+"：「"+I("2>0")+"」は常に成立。"+I("a\\neq0")+"："+I("a>0")+" かつ "+I("\\dfrac D4=a^2-2a=a(a-2)<0")+" より "+I("0<a<2")+"。合わせて：</p>"+D(r"0\leqq a<2"),
  r"0\leqq a<2",5)]
assert segs_ok(sol(lambda t:t*t-t-12<0,lambda t:t*t-2*t-3>=0),[(-3,-1,False,True),(3,4,True,False)])
ok=rngs(lambda t,av:(t-4)*(t-av)<0,2,V); assert all((1<=v<2 or 6<v<=7)==(v in ok) for v in V)
for av in np.arange(-6,6.01,0.25):
    assert allpos(lambda t,a_:a_*t*t-2*a_*t+2,av)==(0<=av<2) or abs(av-2)<1e-9
    assert (min(t*t+2*av*t+2*av+3 for t in np.linspace(-40,40,80001))>1e-9)==(-1<av<3) or av in (-1,3)


# ===== 追加の図 =====

_f=graph("i34_g1",[(lambda v:v*v-3*v-10,RED,"-"),(lambda v:v*v-v-2,"#3a6fb5","-")],(-3.5,6.5),(-12,14),pts=[(-2,0,"-2",-0.5,0.9),(5,0,"5",0.1,0.9),(-1,0,"-1",0.05,-1.2),(2,0,"2",-0.3,-1.2)],texts=[(3.6,11,"赤：①","#b81f36"),(-3.4,11,"青：②","#3a6fb5")],hl=[(-2,-1,"#2a9d6a"),(2,5,"#2a9d6a")],w=60,size=(4.8,3.4))
addfig(EXS[0],2,_f)
_f=graph("i34_g3",[(lambda v:v*v-3*v-10,RED,"-")],(-3.5,6.5),(-14,8),pts=[(-2,0,"-2",-0.5,0.9),(5,0,"5",0.1,0.9)],hl=[(-2,5,"#2a9d6a")],texts=[(-3.3,5.5,"y<0 となる範囲が解","#2a9d6a")],w=52,size=(4.4,3.2))
addfig(EXS[2],0,_f)
def _g4(name,a,t,lo,hi):
    return graph(name,[(lambda v:(v-2)*(v-a),RED,"-")],(min(a,2)-2.5,max(a,2)+2.5),(-6,6),pts=[(2,0,"2",0.05,0.8),(a,0,"a",0.05,0.8)],hl=[(min(a,2),max(a,2),"#2a9d6a")],texts=[(min(a,2)-2.3,4.8,t,"#444")],xticks=[(k,str(k)) for k in range(lo,hi+1)],w=100,size=(3.4,2.8))
_w=lambda f:'<div style="width:58%;margin:2px auto">'+f+'</div>'
_rw=lambda figs:'<div style="display:flex;gap:6px;margin:4px 0">'+"".join('<div style="flex:1">'+f+'</div>' for f in figs)+'</div>'
addfig(EXS[3],1,_w(_g4("i34_g4a",5.5,"a>2（例：a=5.5）整数 3,4,5",3,5)))
addfig(EXS[3],2,_w(_g4("i34_g4b",-1.5,"a<2（例：a=-1.5）整数 -1,0,1",-1,1)))
def _g5(name,a,t):
    return graph(name,[(lambda v:a*v*v-2*a*v+3,RED,"-")],(-1.5,3.5),(-3,8),vlines=[(1,"#aaa")],texts=[(-1.4,6.6,t,"#444")],w=100,size=(2.4,2.4))
addfig(EXS[4],1,_rw([_g5("i34_g5a",-1,"a<0：下に凸でない"),_g5("i34_g5b",1.5,"0<a<3：x軸の上"),_g5("i34_g5c",4,"a≧3：x軸と交わる")]))

UNIT=dict(subject="1",ci=2,ui=3,chapter="2次関数",name="2次不等式",
  intro="連立2次不等式・常に成り立つ条件・解から係数を決める・整数解の個数・係数が文字の場合など、2次不等式の難問に挑みます。",
  examples=EXS,chapter_end=CHE)
