# -*- coding: utf-8 -*-
# 2次方程式（数学I 2次関数）
from tools import *
import sympy as sp
x,a=sp.symbols('x a')
EXS=[]
def ex(**k): EXS.append(k)

# ===== 例題1 重解 =====
f1=graph("i33_e1",[(lambda v:(v-3)**2,RED,"-")],(-1,7),(-1.5,9),pts=[(3,0,"重解 x=3",0.25,0.9)],xticks=[(3,"3")],w=46,size=(4,3))
ex(title="重解をもつ条件",
 problem="2次方程式 "+I("x^2-2ax+a+6=0")+" が重解をもつような定数 "+I("a")+" の値と、そのときの重解を求めよ。",
 approach="<p>2次方程式 "+I("ax^2+bx+c=0")+" の判別式 "+I("D=b^2-4ac")+" について、<b>重解 ⇔ "+I("D=0")+"</b>。"+I("x")+" の係数が偶数のときは "+I("\\dfrac D4=b'^2-ac")+"（"+I("b=2b'")+"）が使えて計算が楽。重解は "+I("x=-\\dfrac b{2a}")+"。</p>",
 kotsu="放物線が x 軸にちょうど触れる（接する）瞬間が D=0。接点の x が重解。",
 steps=[
  step(1,"判別式を計算する","<p>"+I("x")+" の係数 "+I("-2a")+" は偶数なので "+I("b'=-a")+"。</p>"+D(r"\dfrac D4=(-a)^2-1\cdot(a+6)=a^2-a-6")),
  step(2,r"\(D=0\) を解く",D(r"a^2-a-6=0\ \Rightarrow\ (a-3)(a+2)=0\ \Rightarrow\ a=3,\ -2")),
  step(3,"重解を求める","<p>重解 "+I("x=-\\dfrac{-2a}{2}=a")+"。</p><p>"+I("a=3")+" のとき "+I("x^2-6x+9=(x-3)^2=0")+" より "+I("x=3")+"（図）。</p>"+f1+"<p>"+I("a=-2")+" のとき "+I("x^2+4x+4=(x+2)^2=0")+" より "+I("x=-2")+"。</p>")],
 answer=r"a=3\ \text{のとき重解}\ x=3,\quad a=-2\ \text{のとき重解}\ x=-2",
 practice=[r"x^2+2ax+3a+4=0\ \text{が重解をもつ}\ a\ \text{の値と重解}",r"x^2-(a+2)x+a+5=0\ \text{が重解をもつ}\ a\ \text{の値と重解}",r"x^2+ax+2a-3=0\ \text{が重解をもつ}\ a\ \text{の値と重解}"],
 pans=[
  ("<p>"+I("\\dfrac D4=a^2-(3a+4)=a^2-3a-4=(a-4)(a+1)=0")+" より "+I("a=4,\\ -1")+"。重解 "+I("x=-a")+"。</p><p>"+I("a=4")+"：重解 "+I("x=-4")+"（"+I("x^2+8x+16=(x+4)^2")+"）。"+I("a=-1")+"：重解 "+I("x=1")+"（"+I("x^2-2x+1=(x-1)^2")+"）。</p>",r"a=4:\ x=-4,\quad a=-1:\ x=1"),
  ("<p>"+I("D=(a+2)^2-4(a+5)=a^2+4a+4-4a-20=a^2-16=0")+" より "+I("a=\\pm4")+"。重解 "+I("x=\\dfrac{a+2}2")+"。</p><p>"+I("a=4")+"：重解 "+I("x=3")+"（"+I("x^2-6x+9")+"）。"+I("a=-4")+"：重解 "+I("x=-1")+"（"+I("x^2+2x+1")+"）。</p>",r"a=4:\ x=3,\quad a=-4:\ x=-1"),
  ("<p>"+I("D=a^2-4(2a-3)=a^2-8a+12=(a-2)(a-6)=0")+" より "+I("a=2,\\ 6")+"。重解 "+I("x=-\\dfrac a2")+"。</p><p>"+I("a=2")+"：重解 "+I("x=-1")+"（"+I("x^2+2x+1")+"）。"+I("a=6")+"：重解 "+I("x=-3")+"（"+I("x^2+6x+9")+"）。</p>",r"a=2:\ x=-1,\quad a=6:\ x=-3")])
def dd(eq): return sp.factor(sp.discriminant(eq,x))
assert sp.solve(sp.discriminant(x**2-2*a*x+a+6,x),a)==[-2,3]
assert sorted(sp.solve(sp.discriminant(x**2+2*a*x+3*a+4,x),a))==[-1,4]
assert sorted(sp.solve(sp.discriminant(x**2-(a+2)*x+a+5,x),a))==[-4,4]
assert sorted(sp.solve(sp.discriminant(x**2+a*x+2*a-3,x),a))==[2,6]

# ===== 例題2 解と係数の関係（対称式） =====
ex(title="解と係数の関係と対称式",
 problem="2次方程式 "+I("x^2-5x+3=0")+" の2つの解を "+I("\\alpha,\\ \\beta")+" とするとき、"+I("\\alpha^2+\\beta^2")+" と "+I("\\alpha^3+\\beta^3")+" の値を求めよ。",
 approach="<p>解を具体的に求めず、<b>解と係数の関係</b>を使う。"+I("x^2+px+q=0")+" の2解 "+I("\\alpha,\\beta")+" について</p>"+D(r"\alpha+\beta=-p,\qquad \alpha\beta=q")+"<p>次に、対称式を「和」と「積」で表す。</p>"+D(r"\alpha^2+\beta^2=(\alpha+\beta)^2-2\alpha\beta")+D(r"\alpha^3+\beta^3=(\alpha+\beta)^3-3\alpha\beta(\alpha+\beta)"),
 kotsu="2人の名前（解）はいらない。「合計」と「積」の2つの数字だけで、対称な式は全部作れる。",
 steps=[
  step(1,"和と積を求める","<p>"+I("x^2-5x+3=0")+" は "+I("p=-5,\\ q=3")+"。</p>"+D(r"\alpha+\beta=5,\qquad \alpha\beta=3")),
  step(2,r"\(\alpha^2+\beta^2\)",D(r"\alpha^2+\beta^2=(\alpha+\beta)^2-2\alpha\beta=5^2-2\cdot3=25-6=19")),
  step(3,r"\(\alpha^3+\beta^3\)",D(r"\alpha^3+\beta^3=(\alpha+\beta)^3-3\alpha\beta(\alpha+\beta)=5^3-3\cdot3\cdot5=125-45=80"))],
 answer=r"\alpha^2+\beta^2=19,\quad \alpha^3+\beta^3=80",
 practice=[r"x^2-4x+2=0\ \text{の2解を}\ \alpha,\beta\ \text{とするとき},\ \alpha^2+\beta^2,\ \alpha^3+\beta^3",r"x^2-6x+4=0\ \text{の2解を}\ \alpha,\beta\ \text{とするとき},\ \alpha^2+\beta^2,\ \alpha^3+\beta^3",r"x^2+3x+1=0\ \text{の2解を}\ \alpha,\beta\ \text{とするとき},\ \alpha^2+\beta^2,\ \alpha^3+\beta^3"],
 pans=[
  ("<p>"+I("\\alpha+\\beta=4,\\ \\alpha\\beta=2")+"。</p>"+D(r"\alpha^2+\beta^2=4^2-2\cdot2=12")+D(r"\alpha^3+\beta^3=4^3-3\cdot2\cdot4=64-24=40"),r"\alpha^2+\beta^2=12,\ \ \alpha^3+\beta^3=40"),
  ("<p>"+I("\\alpha+\\beta=6,\\ \\alpha\\beta=4")+"。</p>"+D(r"\alpha^2+\beta^2=6^2-2\cdot4=28")+D(r"\alpha^3+\beta^3=6^3-3\cdot4\cdot6=216-72=144"),r"\alpha^2+\beta^2=28,\ \ \alpha^3+\beta^3=144"),
  ("<p>"+I("\\alpha+\\beta=-3,\\ \\alpha\\beta=1")+"（和は "+I("-p=-3")+"）。</p>"+D(r"\alpha^2+\beta^2=(-3)^2-2\cdot1=7")+D(r"\alpha^3+\beta^3=(-3)^3-3\cdot1\cdot(-3)=-27+9=-18"),r"\alpha^2+\beta^2=7,\ \ \alpha^3+\beta^3=-18")]
 )
def sym(eq):
    r=sp.solve(eq,x); s=sp.simplify(sum(v**2 for v in r)); t=sp.simplify(sum(v**3 for v in r)); return s,t
assert sym(x**2-5*x+3)==(19,80) and sym(x**2-4*x+2)==(12,40) and sym(x**2-6*x+4)==(28,144) and sym(x**2+3*x+1)==(7,-18)

# ===== 例題3 解の条件から定数を決める =====
ex(title="解の条件から定数を決める（実数解の確認つき）",
 problem="2次方程式 "+I("x^2-6x+a=0")+" の2つの解の差が4であるとき、定数 "+I("a")+" の値を求めよ。",
 approach="<p>2解を "+I("\\alpha,\\ \\beta")+" とおく。"+I("(\\alpha-\\beta)^2")+" も対称式なので、和と積で表せる。</p>"+D(r"(\alpha-\beta)^2=(\alpha+\beta)^2-4\alpha\beta")+"<p>求めた "+I("a")+" が<b>実数の解をもつ</b>（"+I("D\\geqq0")+"）かを最後に確かめる。</p>",
 kotsu="「差」の2乗は、和の2乗から積の4倍を引くだけ。答えが出たら、本当にその方程式に解があるかを確認する。",
 steps=[
  step(1,"和と積",D(r"\alpha+\beta=6,\qquad\alpha\beta=a")),
  step(2,"差の2乗を作る","<p>差が4なので "+I("(\\alpha-\\beta)^2=16")+"。</p>"+D(r"(\alpha+\beta)^2-4\alpha\beta=16\ \Rightarrow\ 36-4a=16")),
  step(3,r"\(a\) を求める",D(r"4a=20\ \Rightarrow\ a=5")),
  step(4,"確かめる","<p>"+I("x^2-6x+5=(x-1)(x-5)=0")+" より "+I("x=1,\\ 5")+"。差は "+I("5-1=4")+" で条件をみたす。</p>")],
 answer=r"a=5",
 practice=[r"x^2-8x+a=0\ \text{の2つの解の差が}\ 2",r"x^2-4x+a=0\ \text{の2つの解の2乗の和が}\ 20",r"x^2+6x+a=0\ \text{の2つの解の差が}\ 4"],
 pans=[
  ("<p>"+I("\\alpha+\\beta=8,\\ \\alpha\\beta=a")+"。"+I("64-4a=4")+" より "+I("a=15")+"。確かめ："+I("x^2-8x+15=(x-3)(x-5)")+"、差 "+I("2")+"。</p>",r"a=15"),
  ("<p>"+I("\\alpha+\\beta=4,\\ \\alpha\\beta=a")+"。"+I("\\alpha^2+\\beta^2=16-2a=20")+" より "+I("a=-2")+"。確かめ："+I("x^2-4x-2=0")+" の判別式 "+I("D/4=4+2=6>0")+"（実数解あり）。</p>",r"a=-2"),
  ("<p>"+I("\\alpha+\\beta=-6,\\ \\alpha\\beta=a")+"。"+I("(\\alpha-\\beta)^2=36-4a=16")+" より "+I("a=5")+"。確かめ："+I("x^2+6x+5=(x+1)(x+5)")+"、解 "+I("-1,-5")+"、差 "+I("4")+"。</p>",r"a=5")])
assert sorted(sp.solve(x**2-6*x+5,x))==[1,5] and sorted(sp.solve(x**2-8*x+15,x))==[3,5] and sorted(sp.solve(x**2+6*x+5,x))==[-5,-1]
assert sum(v**2 for v in sp.solve(x**2-4*x-2,x)).simplify()==20

# ===== 例題4 解の符号 =====
f4=nl("i33_e4",-3,5,[-1,2],["-1","2"],segs=[(2,None)],pts=[(2,"open")],w=70,size=(6.2,1.5))
ex(title="2つの正の解をもつ条件",
 problem="2次方程式 "+I("x^2-2ax+a+2=0")+" が異なる2つの正の解をもつような定数 "+I("a")+" の値の範囲を求めよ。",
 approach="<p>2解を "+I("\\alpha,\\beta")+" とする。<b>異なる2つの正の解</b> ⇔ 次の3つが<b>すべて</b>成り立つ。</p><ol><li>異なる2つの実数解："+I("D>0")+"</li><li>和が正："+I("\\alpha+\\beta>0")+"</li><li>積が正："+I("\\alpha\\beta>0")+"</li></ol><p>（和も積も正 ⇒ 2つとも正）。</p>",
 kotsu="「2人とも正」を見張る条件は3つ。実数であること、合計がプラス、積がプラス。3つの共通部分が答え。",
 steps=[
  step(1,"判別式の条件",D(r"\dfrac D4=a^2-(a+2)=a^2-a-2=(a-2)(a+1)>0")+"<p>よって "+I("a<-1")+" または "+I("a>2")+"。</p>"),
  step(2,"和の条件",D(r"\alpha+\beta=2a>0\ \Rightarrow\ a>0")),
  step(3,"積の条件",D(r"\alpha\beta=a+2>0\ \Rightarrow\ a>-2")),
  step(4,"3つの共通部分を求める","<p>数直線で重ねると（図）、3つすべてをみたすのは "+I("a>2")+"。</p>"+f4),
  step(5,"確かめる","<p>"+I("a=3")+"：方程式 "+I("x^2-6x+5=0")+"、解 "+I("x=1,\\ 5")+"（ともに正）。</p>")],
 answer=r"a>2",
 practice=[r"x^2+2ax+a+6=0\ \text{が異なる2つの負の解をもつ}\ a\ \text{の範囲}",r"x^2-2ax+3a+4=0\ \text{が異なる2つの正の解をもつ}\ a\ \text{の範囲}",r"x^2-3x+a-2=0\ \text{が正の解と負の解を1つずつもつ}\ a\ \text{の範囲}"],
 pans=[
  ("<p>"+I("\\dfrac D4=a^2-(a+6)=(a-3)(a+2)>0")+" より "+I("a<-2,\\ a>3")+"。和 "+I("-2a<0")+" より "+I("a>0")+"。積 "+I("a+6>0")+" より "+I("a>-6")+"。共通部分：</p>"+D(r"a>3"),r"a>3"),
  ("<p>"+I("\\dfrac D4=a^2-(3a+4)=(a-4)(a+1)>0")+" より "+I("a<-1,\\ a>4")+"。和 "+I("2a>0")+" より "+I("a>0")+"。積 "+I("3a+4>0")+" より "+I("a>-\\dfrac43")+"。共通部分：</p>"+D(r"a>4"),r"a>4"),
  ("<p>正と負の解を1つずつ ⇔ <b>積が負</b>："+I("\\alpha\\beta=a-2<0")+" より "+I("a<2")+"。このとき "+I("D=9-4(a-2)=17-4a>0")+" は自動的に成り立つ（"+I("a<2")+" なら "+I("17-4a>9")+"）。</p>",r"a<2")])
def pos2(eq_a):  # 検証：端点を含め広い範囲で数値的に確認
    import numpy as np
    out=[]
    for av in np.arange(-8,8.01,0.25):
        r=np.roots(eq_a(av)); out.append((av,r))
    return out
import numpy as np
def ok_pos(av,c):
    r=np.roots(c(av))
    return np.all(np.isreal(r)) and abs(r[0]-r[1])>1e-9 and np.all(r.real>0)
def ok_neg(av,c):
    r=np.roots(c(av)); return np.all(np.isreal(r)) and abs(r[0]-r[1])>1e-9 and np.all(r.real<0)
for av in np.arange(-8,8.01,0.25):
    assert ok_pos(av,lambda t:[1,-2*t,t+2])==(av>2)
    assert ok_neg(av,lambda t:[1,2*t,t+6])==(av>3)
    assert ok_pos(av,lambda t:[1,-2*t,3*t+4])==(av>4)
    r=np.roots([1,-3,av-2]); assert (np.all(np.isreal(r)) and r.real.min()<0<r.real.max())==(av<2)

# ===== 例題5 共通解 =====
ex(title="2つの方程式が共通解をもつ条件",
 problem="2つの2次方程式 "+I("x^2+ax+2=0")+"、"+I("x^2+2x+a=0")+" が共通な実数解をもつような定数 "+I("a")+" の値を求めよ。",
 approach="<p>共通解を "+I("x=k")+" とおくと、両方に代入できる。<b>2式を引いて "+I("k^2")+" を消す</b>と "+I("k")+" の1次式（または積の形）になる。ただし、求めた "+I("a")+" で<b>共通解が実数になるか</b>を最後に確かめる。</p>",
 kotsu="2つの式に共通の人 k がいる。2式を引き算すると、2乗の人が消えて話が簡単になる。",
 steps=[
  step(1,"共通解を "+I("k")+" とおく","<p>"+I("k^2+ak+2=0\\ \\cdots①")+"、"+I("k^2+2k+a=0\\ \\cdots②")+"。</p>"),
  step(2,"引き算して因数分解する","<p>① − ②：</p>"+D(r"(a-2)k+2-a=0\ \Rightarrow\ (a-2)k-(a-2)=0\ \Rightarrow\ (a-2)(k-1)=0")+"<p>よって "+I("a=2")+" または "+I("k=1")+"。</p>"),
  step(3,r"\(k=1\) のとき","<p>①に代入：</p>"+D(r"1+a+2=0\ \Rightarrow\ a=-3")+"<p>確かめ：②は "+I("1+2-3=0")+" で成り立つ。</p>"),
  step(4,r"\(a=2\) のとき","<p>2つの方程式は両方とも "+I("x^2+2x+2=0")+"（同じ式）。判別式 "+I("\\dfrac D4=1-2=-1<0")+" で<b>実数解がない</b>。よって共通な実数解はなく、不適。</p>"),
  step(5,"結論","<p>"+I("a=-3")+"。（共通解は "+I("x=1")+"）</p>")],
 answer=r"a=-3",
 practice=[r"x^2+ax+3=0,\ x^2+3x+a=0\ \text{が共通な実数解をもつ}\ a",r"x^2-ax+4=0,\ x^2-4x+a=0\ \text{が共通な実数解をもつ}\ a",r"x^2+ax+5=0,\ x^2+5x+a=0\ \text{が共通な実数解をもつ}\ a"],
 pans=[
  ("<p>共通解 "+I("k")+"：差をとると "+I("(a-3)k+3-a=0")+"、"+I("(a-3)(k-1)=0")+"。</p><p>"+I("k=1")+"：①"+I("1+a+3=0")+" より "+I("a=-4")+"（②も "+I("1+3-4=0")+" 成立）。</p><p>"+I("a=3")+"：両方とも "+I("x^2+3x+3=0")+"、"+I("D=9-12<0")+" で実数解なし。不適。</p>",r"a=-4"),
  ("<p>差をとると "+I("(-a+4)k+4-a=0")+"、"+I("(4-a)(k+1)=0")+"。</p><p>"+I("k=-1")+"：①"+I("1+a+4=0")+" より "+I("a=-5")+"（②も "+I("1+4-5=0")+" 成立）。</p><p>"+I("a=4")+"：両方とも "+I("x^2-4x+4=(x-2)^2=0")+"、実数解 "+I("x=2")+" をもつので適する。</p>",r"a=4,\ -5"),
  ("<p>差をとると "+I("(a-5)k+5-a=0")+"、"+I("(a-5)(k-1)=0")+"。</p><p>"+I("k=1")+"：①"+I("1+a+5=0")+" より "+I("a=-6")+"（②も "+I("1+5-6=0")+" 成立）。</p><p>"+I("a=5")+"：両方とも "+I("x^2+5x+5=0")+"、"+I("D=25-20=5>0")+" で実数解をもつので適する。</p>",r"a=5,\ -6")])
def common(c1,c2):
    out=[]
    for av in [sp.Rational(k,1) for k in range(-12,13)]:
        r1=[v for v in sp.solve(c1(av),x) if v.is_real]; r2=[v for v in sp.solve(c2(av),x) if v.is_real]
        if set(r1)&set(r2): out.append(av)
    return out
assert common(lambda A:x**2+A*x+2,lambda A:x**2+2*x+A)==[-3]
assert common(lambda A:x**2+A*x+3,lambda A:x**2+3*x+A)==[-4]
assert common(lambda A:x**2-A*x+4,lambda A:x**2-4*x+A)==[-5,4]
assert common(lambda A:x**2+A*x+5,lambda A:x**2+5*x+A)==[-6,5]

CHE=[
 (r"x^2+ax+a+3=0\ \text{が重解をもつような}\ a\ \text{の値と重解を求めよ。}",
  "<p>"+I("D=a^2-4(a+3)=a^2-4a-12=(a-6)(a+2)=0")+" より "+I("a=6,\\ -2")+"。重解 "+I("x=-\\dfrac a2")+"。</p><p>"+I("a=6")+"：重解 "+I("x=-3")+"。"+I("a=-2")+"：重解 "+I("x=1")+"。</p>",
  r"a=6:\ x=-3,\quad a=-2:\ x=1",1),
 (r"x^2-3x-5=0\ \text{の2解を}\ \alpha,\beta\ \text{とするとき},\ \alpha^2+\beta^2,\ \alpha^3+\beta^3\ \text{を求めよ。}",
  "<p>"+I("\\alpha+\\beta=3,\\ \\alpha\\beta=-5")+"。</p>"+D(r"\alpha^2+\beta^2=3^2-2\cdot(-5)=9+10=19")+D(r"\alpha^3+\beta^3=3^3-3\cdot(-5)\cdot3=27+45=72"),
  r"\alpha^2+\beta^2=19,\ \ \alpha^3+\beta^3=72",2),
 (r"x^2-4x+a=0\ \text{の2つの解の差が}\ 2\sqrt3\ \text{であるとき},\ a\ \text{の値を求めよ。}",
  "<p>"+I("\\alpha+\\beta=4,\\ \\alpha\\beta=a")+"。"+I("(\\alpha-\\beta)^2=16-4a=(2\\sqrt3)^2=12")+" より "+I("a=1")+"。確かめ："+I("x^2-4x+1=0")+" の解は "+I("x=2\\pm\\sqrt3")+"、差は "+I("2\\sqrt3")+"。</p>",
  r"a=1",3),
 (r"x^2-2ax+2a+3=0\ \text{が異なる2つの正の解をもつような}\ a\ \text{の範囲を求めよ。}",
  "<p>"+I("\\dfrac D4=a^2-(2a+3)=(a-3)(a+1)>0")+" より "+I("a<-1,\\ a>3")+"。和 "+I("2a>0")+" より "+I("a>0")+"。積 "+I("2a+3>0")+" より "+I("a>-\\dfrac32")+"。共通部分：</p>"+D(r"a>3"),
  r"a>3",4),
 (r"x^2+ax+6=0,\ x^2+6x+a=0\ \text{が共通な実数解をもつような}\ a\ \text{の値を求めよ。}",
  "<p>差をとると "+I("(a-6)k+6-a=0")+"、"+I("(a-6)(k-1)=0")+"。</p><p>"+I("k=1")+"：①"+I("1+a+6=0")+" より "+I("a=-7")+"（②も "+I("1+6-7=0")+" 成立）。</p><p>"+I("a=6")+"：両方とも "+I("x^2+6x+6=0")+"、"+I("\\dfrac D4=9-6=3>0")+" で実数解をもつので適する。</p>",
  r"a=6,\ -7",5)]
assert sorted(sp.solve(sp.discriminant(x**2+a*x+a+3,x),a))==[-2,6] and sym(x**2-3*x-5)==(19,72)
assert sorted(sp.solve(x**2-4*x+1,x))==[2-sp.sqrt(3),2+sp.sqrt(3)]
for av in np.arange(-8,8.01,0.25): assert ok_pos(av,lambda t:[1,-2*t,2*t+3])==(av>3)
assert common(lambda A:x**2+A*x+6,lambda A:x**2+6*x+A)==[-7,6]

UNIT=dict(subject="1",ci=2,ui=2,chapter="2次関数",name="2次方程式",
  intro="重解・解と係数の関係・解の条件・解の符号・共通解など、2次方程式の難問に挑みます。",
  examples=EXS,chapter_end=CHE)
