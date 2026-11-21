# -*- coding: utf-8 -*-
# 実数（平方根・絶対値）（数学I 数と式）
from tools import *
import sympy as sp
x,y=sp.symbols('x y')
s2,s3,s5,s7,s10,s6=[sp.sqrt(k) for k in (2,3,5,7,10,6)]
EXS=[]
def ex(**k): EXS.append(k)

# ===== 例題1 二重根号 =====
ex(title="二重根号をはずす",
 problem="次の式の二重根号をはずして簡単にせよ。"+D(r"\sqrt{11+6\sqrt2}"),
 approach="<p>次の公式を使う（"+I("a>b>0")+"）。</p>"+D(r"\sqrt{(a+b)+2\sqrt{ab}}=\sqrt a+\sqrt b")+D(r"\sqrt{(a+b)-2\sqrt{ab}}=\sqrt a-\sqrt b")+"<p>まず中身を "+I("(a+b)+2\\sqrt{ab}")+" の形に直し、<b>足して "+I("a+b")+"、かけて "+I("ab")+" になる2数</b>を探す。</p>",
 kotsu="中身は「2人の合計」と「2人の積」の暗号。足して・かけて、ぴったりの2人組を見つけ出す。",
 steps=[
  step(1,r"\(2\sqrt{\ \ }\) の形に直す","<p>"+I("6\\sqrt2=2\\times3\\sqrt2")+"。"+I("3\\sqrt2=\\sqrt{9\\times2}=\\sqrt{18}")+" なので、</p>"+D(r"6\sqrt2=2\sqrt{18}\ \Rightarrow\ \sqrt{11+6\sqrt2}=\sqrt{11+2\sqrt{18}}")),
  step(2,"足して11、かけて18になる2数を探す","<p>18の約数の組 "+I("(1,18),\\ (2,9),\\ (3,6)")+" のうち、足して11になるのは "+I("2+9=11")+"。</p>"),
  step(3,"公式を使う","<p>"+I(r"\sqrt{a+b+2\sqrt{ab}}=\sqrt a+\sqrt b")+"（"+I("a=9,\\ b=2")+"）を使う。"+I("9+2=11,\\ 9\\times2=18")+" である。</p>"+D(r"\sqrt{11+2\sqrt{18}}=\sqrt{9+2+2\sqrt{9\cdot2}}=\sqrt{(\sqrt9+\sqrt2)^2}=\sqrt9+\sqrt2=3+\sqrt2")),
  step(4,"確かめる（2乗する）",D(r"(3+\sqrt2)^2=9+6\sqrt2+2=11+6\sqrt2"))],
 answer=r"3+\sqrt2",
 practice=[r"\sqrt{7+4\sqrt3}",r"\sqrt{12-2\sqrt{35}}",r"\sqrt{6+2\sqrt5}"],
 pans=[
  ("<p>"+I("4\\sqrt3=2\\times2\\sqrt3=2\\sqrt{12}")+"（"+I("2\\sqrt3=\\sqrt{12}")+"）なので "+I("\\sqrt{7+2\\sqrt{12}}")+"。</p><p>12の約数の組 "+I("(1,12),\\ (2,6),\\ (3,4)")+" のうち、足して7になるのは "+I("3+4=7")+"。</p>"+D(r"\sqrt{7+2\sqrt{12}}=\sqrt4+\sqrt3=2+\sqrt3")+"<p>確かめ："+I("(2+\\sqrt3)^2=4+4\\sqrt3+3=7+4\\sqrt3")+"。</p>",r"2+\sqrt3"),
  ("<p>35の約数の組 "+I("(1,35),\\ (5,7)")+" のうち、足して12になるのは "+I("5+7=12")+"。</p><p>引き算の形なので、大きい方から小さい方を引く（"+I("\\sqrt7>\\sqrt5")+"）。</p>"+D(r"\sqrt{12-2\sqrt{35}}=\sqrt7-\sqrt5")+"<p>確かめ："+I("(\\sqrt7-\\sqrt5)^2=7-2\\sqrt{35}+5=12-2\\sqrt{35}")+"。</p>",r"\sqrt7-\sqrt5"),
  ("<p>"+I("2\\sqrt5")+" の形になっている。5の約数の組 "+I("(1,5)")+" で、足して6になる。</p>"+D(r"\sqrt{6+2\sqrt5}=\sqrt5+\sqrt1=\sqrt5+1")+"<p>確かめ："+I("(\\sqrt5+1)^2=5+2\\sqrt5+1=6+2\\sqrt5")+"。</p>",r"\sqrt5+1")])
for e,v in ((sp.sqrt(11+6*s2),3+s2),(sp.sqrt(7+4*s3),2+s3),(sp.sqrt(12-2*sp.sqrt(35)),s7-s5),(sp.sqrt(6+2*s5),s5+1)): assert abs(float(e-v))<1e-12

# ===== 例題2 有理化と対称式 =====
ex(title="分母の有理化と対称式",
 problem="次の問いに答えよ。"+D(r"x=\dfrac{\sqrt5+\sqrt3}{\sqrt5-\sqrt3},\quad y=\dfrac{\sqrt5-\sqrt3}{\sqrt5+\sqrt3}\ \text{のとき},\ x^2+y^2\ \text{と}\ x^3+y^3\ \text{の値}"),
 approach="<p>"+I("x,\\ y")+" をそれぞれ求めるのではなく、<b>和 "+I("x+y")+" と積 "+I("xy")+"</b> を先に出す。あとは対称式の公式で計算する。</p>"+D(r"x^2+y^2=(x+y)^2-2xy")+D(r"x^3+y^3=(x+y)^3-3xy(x+y)"),
 kotsu="2人の名前（x, y）より、2人の「合計」と「積」だけ聞き出せば、他の数字は全部計算できる。",
 steps=[
  step(1,r"\(x\) の分母を有理化する","<p>分母と分子に "+I("\\sqrt5+\\sqrt3")+" をかける。</p>"+D(r"x=\dfrac{(\sqrt5+\sqrt3)^2}{(\sqrt5-\sqrt3)(\sqrt5+\sqrt3)}=\dfrac{5+2\sqrt{15}+3}{5-3}=\dfrac{8+2\sqrt{15}}{2}=4+\sqrt{15}")),
  step(2,r"\(y\) の分母を有理化する","<p>分母と分子に "+I("\\sqrt5-\\sqrt3")+" をかける。</p>"+D(r"y=\dfrac{(\sqrt5-\sqrt3)^2}{(\sqrt5+\sqrt3)(\sqrt5-\sqrt3)}=\dfrac{5-2\sqrt{15}+3}{5-3}=\dfrac{8-2\sqrt{15}}{2}=4-\sqrt{15}")),
  step(3,"和と積を求める",D(r"x+y=(4+\sqrt{15})+(4-\sqrt{15})=8")+D(r"xy=(4+\sqrt{15})(4-\sqrt{15})=16-15=1")),
  step(4,r"\(x^2+y^2\) を求める",D(r"x^2+y^2=(x+y)^2-2xy=8^2-2\cdot1=64-2=62")),
  step(5,r"\(x^3+y^3\) を求める",D(r"x^3+y^3=(x+y)^3-3xy(x+y)=8^3-3\cdot1\cdot8=512-24=488"))],
 answer=r"x^2+y^2=62,\quad x^3+y^3=488",
 practice=[r"x=\dfrac{\sqrt3+1}{\sqrt3-1},\ y=\dfrac{\sqrt3-1}{\sqrt3+1}\ \text{のとき},\ x^2+y^2,\ x^3+y^3",
           r"x=\dfrac{\sqrt7+\sqrt3}{\sqrt7-\sqrt3},\ y=\dfrac{\sqrt7-\sqrt3}{\sqrt7+\sqrt3}\ \text{のとき},\ x^2+y^2,\ x^3+y^3",
           r"x=\sqrt5+2,\ y=\sqrt5-2\ \text{のとき},\ x^2+y^2,\ x^3+y^3"],
 pans=[
  ("<p>"+I("x=\\dfrac{(\\sqrt3+1)^2}{3-1}=\\dfrac{3+2\\sqrt3+1}{2}=\\dfrac{4+2\\sqrt3}{2}=2+\\sqrt3")+"、"+I("y=\\dfrac{(\\sqrt3-1)^2}{3-1}=\\dfrac{4-2\\sqrt3}{2}=2-\\sqrt3")+"。</p>"+D(r"x+y=4,\quad xy=4-3=1")+D(r"x^2+y^2=4^2-2\cdot1=14")+D(r"x^3+y^3=4^3-3\cdot1\cdot4=64-12=52"),r"x^2+y^2=14,\ \ x^3+y^3=52"),
  ("<p>"+I("x=\\dfrac{(\\sqrt7+\\sqrt3)^2}{7-3}=\\dfrac{10+2\\sqrt{21}}{4}=\\dfrac{5+\\sqrt{21}}{2}")+"、"+I("y=\\dfrac{(\\sqrt7-\\sqrt3)^2}{7-3}=\\dfrac{10-2\\sqrt{21}}{4}=\\dfrac{5-\\sqrt{21}}{2}")+"。</p>"+D(r"x+y=\dfrac{5+\sqrt{21}+5-\sqrt{21}}{2}=5,\quad xy=\dfrac{25-21}{4}=1")+D(r"x^2+y^2=5^2-2\cdot1=23")+D(r"x^3+y^3=5^3-3\cdot1\cdot5=125-15=110"),r"x^2+y^2=23,\ \ x^3+y^3=110"),
  ("<p>"+I("x+y=(\\sqrt5+2)+(\\sqrt5-2)=2\\sqrt5")+"、"+I("xy=(\\sqrt5+2)(\\sqrt5-2)=5-4=1")+"。</p>"+D(r"x^2+y^2=(2\sqrt5)^2-2\cdot1=20-2=18")+D(r"x^3+y^3=(2\sqrt5)^3-3\cdot1\cdot2\sqrt5=8\cdot5\sqrt5-6\sqrt5=40\sqrt5-6\sqrt5=34\sqrt5"),r"x^2+y^2=18,\ \ x^3+y^3=34\sqrt5")])
def _chk(xv,yv,a,b):
    assert sp.simplify(xv**2+yv**2-a)==0 and sp.simplify(xv**3+yv**3-b)==0
_chk((s5+s3)/(s5-s3),(s5-s3)/(s5+s3),62,488)
_chk((s3+1)/(s3-1),(s3-1)/(s3+1),14,52)
_chk((s7+s3)/(s7-s3),(s7-s3)/(s7+s3),23,110)
_chk(s5+2,s5-2,18,34*s5)

# ===== 例題3 整数部分・小数部分 =====
f3=nl("i13_e3",2.8,4.2,[3,4],["3","4"],segs=[],pts=[(2+float(s3),"closed")],w=70)
ex(title="整数部分と小数部分",
 problem=I(r"\dfrac{1}{2-\sqrt3}")+" の整数部分を "+I("a")+"、小数部分を "+I("b")+" とする。"+I("a,\\ b")+" の値と、"+I("b^2+2b")+" の値を求めよ。",
 approach="<p>① まず分母を有理化して簡単にする。② "+I("\\sqrt3")+" の大きさを不等式ではさんで、整数部分を決める。③ 小数部分は「<b>もとの数 − 整数部分</b>」。</p>",
 kotsu="小数部分 = 全体から整数部分を引いた残り。数直線で、3と4の間のどこにいるかを見る。",
 steps=[
  step(1,"分母を有理化する",D(r"\dfrac1{2-\sqrt3}=\dfrac{2+\sqrt3}{(2-\sqrt3)(2+\sqrt3)}=\dfrac{2+\sqrt3}{4-3}=2+\sqrt3")),
  step(2,r"\(\sqrt3\) の大きさをはさむ","<p>"+I("1.7^2=2.89<3<3.24=1.8^2")+" より "+I("1.7<\\sqrt3<1.8")+"。各辺に2を足して</p>"+D(r"3.7<2+\sqrt3<3.8")+"<p>よって "+I("2+\\sqrt3")+" は3と4の間にある（図）。</p>"+f3),
  step(3,r"\(a\) と \(b\) を決める","<p>整数部分は "+I("a=3")+"。小数部分は</p>"+D(r"b=(2+\sqrt3)-3=\sqrt3-1")),
  step(4,r"\(b^2+2b\) を計算する",D(r"b^2=(\sqrt3-1)^2=3-2\sqrt3+1=4-2\sqrt3")+D(r"2b=2\sqrt3-2")+D(r"b^2+2b=(4-2\sqrt3)+(2\sqrt3-2)=2"))],
 answer=r"a=3,\quad b=\sqrt3-1,\quad b^2+2b=2",
 practice=[r"\dfrac1{3-\sqrt7}\ \text{の整数部分}\ a,\ \text{小数部分}\ b\ \text{について},\ a,\ b,\ b^2+b",
           r"\sqrt{10}\ \text{の整数部分}\ a,\ \text{小数部分}\ b\ \text{について},\ a,\ b,\ b+\dfrac1b",
           r"\dfrac1{\sqrt6-2}\ \text{の整数部分}\ a,\ \text{小数部分}\ b\ \text{について},\ a,\ b,\ b^2+2b"],
 pans=[
  ("<p>有理化：</p>"+D(r"\dfrac1{3-\sqrt7}=\dfrac{3+\sqrt7}{(3-\sqrt7)(3+\sqrt7)}=\dfrac{3+\sqrt7}{9-7}=\dfrac{3+\sqrt7}2")+"<p>"+I("2.6^2=6.76<7<7.29=2.7^2")+" より "+I("2.6<\\sqrt7<2.7")+"。"+I("5.6<3+\\sqrt7<5.7")+" なので、2で割って</p>"+D(r"2.8<\dfrac{3+\sqrt7}2<2.85")+"<p>整数部分 "+I("a=2")+"。小数部分</p>"+D(r"b=\dfrac{3+\sqrt7}2-2=\dfrac{\sqrt7-1}2")+D(r"b^2=\dfrac{(\sqrt7-1)^2}4=\dfrac{8-2\sqrt7}4=\dfrac{4-\sqrt7}2")+D(r"b^2+b=\dfrac{4-\sqrt7}2+\dfrac{\sqrt7-1}2=\dfrac32"),r"a=2,\ b=\dfrac{\sqrt7-1}2,\ b^2+b=\dfrac32"),
  ("<p>"+I("9<10<16")+" より "+I("3<\\sqrt{10}<4")+"。整数部分 "+I("a=3")+"、小数部分 "+I("b=\\sqrt{10}-3")+"。</p>"+D(r"\dfrac1b=\dfrac1{\sqrt{10}-3}=\dfrac{\sqrt{10}+3}{10-9}=\sqrt{10}+3")+D(r"b+\dfrac1b=(\sqrt{10}-3)+(\sqrt{10}+3)=2\sqrt{10}"),r"a=3,\ b=\sqrt{10}-3,\ b+\dfrac1b=2\sqrt{10}"),
  ("<p>有理化：</p>"+D(r"\dfrac1{\sqrt6-2}=\dfrac{\sqrt6+2}{(\sqrt6-2)(\sqrt6+2)}=\dfrac{\sqrt6+2}{6-4}=\dfrac{\sqrt6+2}2")+"<p>"+I("2.4^2=5.76<6<6.25=2.5^2")+" より "+I("2.4<\\sqrt6<2.5")+"。"+I("4.4<\\sqrt6+2<4.5")+" なので、2で割って "+I("2.2<\\dfrac{\\sqrt6+2}2<2.25")+"。</p><p>整数部分 "+I("a=2")+"。小数部分</p>"+D(r"b=\dfrac{\sqrt6+2}2-2=\dfrac{\sqrt6-2}2")+D(r"b^2=\dfrac{6-4\sqrt6+4}4=\dfrac{5-2\sqrt6}2")+D(r"2b=\sqrt6-2")+D(r"b^2+2b=\dfrac{5-2\sqrt6}2+\dfrac{2\sqrt6-4}2=\dfrac12"),r"a=2,\ b=\dfrac{\sqrt6-2}2,\ b^2+2b=\dfrac12")])
bb=s3-1; assert sp.simplify(bb**2+2*bb-2)==0
b1=(s7-1)/2; assert sp.simplify(b1**2+b1-sp.Rational(3,2))==0
b3=(s6-2)/2; assert sp.simplify(b3**2+2*b3-sp.Rational(1,2))==0
assert abs(float(1/(3-s7))-2.8229)<1e-3 and abs(float(1/(s6-2))-2.2247)<1e-3

# ===== 例題4 絶対値の方程式 =====
def _lines(ax,a,b,ra,rb,rc):
    for xx in (a,b): ax.plot([xx,xx],[-.55,.9],color="#888",lw=1,ls="--")
    ax.text((a-2.6)/1.0+0.3,0.6,"①",ha="center",fontsize=14,color=RED)
    ax.text((a+b)/2,0.6,"②",ha="center",fontsize=14,color=RED)
    ax.text(b+1.6,0.6,"③",ha="center",fontsize=14,color=RED)
    ax.text(a-1.4,-0.95,ra,ha="center",fontsize=11); ax.text((a+b)/2,-0.95,rb,ha="center",fontsize=11); ax.text(b+1.4,-0.95,rc,ha="center",fontsize=11)
f4=nl("i13_e4",-3.5,5,[-1,2],["-1","2"],pad=0.9,w=75,size=(6.2,1.7),extra=lambda ax:_lines(ax,-1,2,"x<-1","-1≦x<2","x≧2"))
ex(title="絶対値の方程式（場合分け）",
 problem="次の方程式を解け。"+D(r"|x-2|+|x+1|=5"),
 approach="<p>絶対値の中身が0になる "+I("x=2")+" と "+I("x=-1")+" で、<b>数直線を3つの範囲に分けて</b>考える。各範囲で、絶対値の中身が正か負かが決まるので、絶対値をはずせる。</p>"+D(r"|A|=\begin{cases}A&(A\geqq0)\\-A&(A<0)\end{cases}"),
 kotsu="信号の色が変わる地点（-1 と 2）で道を3つに区切り、区間ごとにルールを変えて走る。",
 steps=[
  step(1,"場合分けの境目を図にする","<p>境目は "+I("x=-1")+" と "+I("x=2")+"。範囲を ① ② ③ とする。</p>"+f4),
  step(2,r"① \(x<-1\) のとき","<p>"+I("x-2<0")+"、"+I("x+1<0")+" なので "+I("|x-2|=-(x-2)")+"、"+I("|x+1|=-(x+1)")+"。</p>"+D(r"-(x-2)-(x+1)=5")+D(r"-x+2-x-1=5\ \Rightarrow\ -2x+1=5\ \Rightarrow\ x=-2")+"<p>"+I("x=-2")+" は "+I("x<-1")+" をみたすので解。</p>"),
  step(3,r"② \(-1\leqq x<2\) のとき","<p>"+I("x-2<0")+"、"+I("x+1\\geqq0")+" なので "+I("|x-2|=-(x-2)")+"、"+I("|x+1|=x+1")+"。</p>"+D(r"-(x-2)+(x+1)=5")+D(r"-x+2+x+1=5\ \Rightarrow\ 3=5")+"<p>これは成り立たない。この範囲に解はない。</p>"),
  step(4,r"③ \(x\geqq2\) のとき","<p>"+I("x-2\\geqq0")+"、"+I("x+1>0")+" なので "+I("|x-2|=x-2")+"、"+I("|x+1|=x+1")+"。</p>"+D(r"(x-2)+(x+1)=5")+D(r"2x-1=5\ \Rightarrow\ x=3")+"<p>"+I("x=3")+" は "+I("x\\geqq2")+" をみたすので解。</p>"),
  step(5,"確かめる","<p>"+I("x=-2")+"："+I("|-2-2|+|-2+1|=4+1=5")+"。"+I("x=3")+"："+I("|3-2|+|3+1|=1+4=5")+"。</p>")],
 answer=r"x=-2,\ 3",
 practice=[r"|x-1|+|x-4|=7",r"|x+2|+|x-3|=9",r"|x-5|+|x+3|=10"],
 pans=[
  ("<p>境目は "+I("x=1,\\ 4")+"。</p><p>① "+I("x<1")+"："+I("-(x-1)-(x-4)=7")+" → "+I("-2x+5=7")+" → "+I("x=-1")+"（"+I("x<1")+" をみたす）。</p><p>② "+I("1\\leqq x<4")+"："+I("(x-1)-(x-4)=7")+" → "+I("3=7")+"（不成立）。</p><p>③ "+I("x\\geqq4")+"："+I("(x-1)+(x-4)=7")+" → "+I("2x-5=7")+" → "+I("x=6")+"（"+I("x\\geqq4")+" をみたす）。</p>",r"x=-1,\ 6"),
  ("<p>境目は "+I("x=-2,\\ 3")+"。</p><p>① "+I("x<-2")+"："+I("-(x+2)-(x-3)=9")+" → "+I("-2x+1=9")+" → "+I("x=-4")+"。</p>"+"<p>【注意】"+I("-(x+2)-(x-3)=-x-2-x+3=-2x+1")+"。"+I("-2x+1=9")+" より "+I("x=-4")+"（"+I("x<-2")+" をみたす）。</p><p>② "+I("-2\\leqq x<3")+"："+I("(x+2)-(x-3)=9")+" → "+I("5=9")+"（不成立）。</p><p>③ "+I("x\\geqq3")+"："+I("(x+2)+(x-3)=9")+" → "+I("2x-1=9")+" → "+I("x=5")+"。</p>",r"x=-4,\ 5"),
  ("<p>境目は "+I("x=-3,\\ 5")+"。</p><p>① "+I("x<-3")+"："+I("-(x-5)-(x+3)=10")+" → "+I("-x+5-x-3=10")+" → "+I("-2x+2=10")+" → "+I("x=-4")+"。</p><p>② "+I("-3\\leqq x<5")+"："+I("-(x-5)+(x+3)=10")+" → "+I("8=10")+"（不成立）。</p><p>③ "+I("x\\geqq5")+"："+I("(x-5)+(x+3)=10")+" → "+I("2x-2=10")+" → "+I("x=6")+"。</p>",r"x=-4,\ 6")])
import itertools
def _sol(f,lo=-30,hi=30):
    return [k/2 for k in range(lo*2,hi*2) if abs(f(k/2))<1e-9]
assert _sol(lambda t:abs(t-2)+abs(t+1)-5)==[-2,3]
assert _sol(lambda t:abs(t-1)+abs(t-4)-7)==[-1,6]
assert _sol(lambda t:abs(t+2)+abs(t-3)-9)==[-4,5]
assert _sol(lambda t:abs(t-5)+abs(t+3)-10)==[-4,6]

# ===== 例題5 無理数の係数比較 =====
ex(title="無理数の係数比較（有理数 a, b を求める）",
 problem=I("a,\\ b")+" は有理数とする。次の等式をみたす "+I("a,\\ b")+" の値を求めよ。"+D(r"(1+\sqrt2)a+(3-2\sqrt2)b=11-4\sqrt2"),
 approach="<p>"+I("\\sqrt2")+" は無理数なので、<b>有理数 "+I("p,\\ q")+" について "+I("p+q\\sqrt2=0")+" ならば "+I("p=0,\\ q=0")+"</b> が成り立つ。左辺を「有理数の部分」＋「"+I("\\sqrt2")+" の部分」にまとめ、両方を比べる。</p>",
 kotsu="りんご（有理数）とみかん（√2）は混ぜて数えられない。りんごはりんご同士、みかんはみかん同士で個数を比べる。",
 steps=[
  step(1,r"\(p+q\sqrt2\) の形に整理する","<p>展開して、有理数の部分と "+I("\\sqrt2")+" の部分に分ける。</p>"+D(r"(1+\sqrt2)a+(3-2\sqrt2)b=a+\sqrt2a+3b-2\sqrt2b=(a+3b)+(a-2b)\sqrt2")),
  step(2,"右辺との差を取る","<p>右辺は "+I("11-4\\sqrt2")+"。移項して</p>"+D(r"\{(a+3b)-11\}+\{(a-2b)+4\}\sqrt2=0")),
  step(3,"係数を比べる","<p>"+I("a,\\ b")+" は有理数なので、かっこの中も有理数。よって両方とも0。</p>"+D(r"a+3b=11\quad\cdots①,\qquad a-2b=-4\quad\cdots②")),
  step(4,"連立方程式を解く","<p>① − ② ："+I("5b=15")+" より "+I("b=3")+"。①に代入して "+I("a+9=11")+"、"+I("a=2")+"。</p>"),
  step(5,"確かめる",D(r"(1+\sqrt2)\cdot2+(3-2\sqrt2)\cdot3=2+2\sqrt2+9-6\sqrt2=11-4\sqrt2"))],
 answer=r"a=2,\quad b=3",
 practice=[r"(2+\sqrt3)a+(1-\sqrt3)b=8+\sqrt3",r"(1+\sqrt5)a+(2-3\sqrt5)b=6+\sqrt5",r"(3+\sqrt2)a+(1+2\sqrt2)b=5+5\sqrt2"],
 pans=[
  ("<p>"+I("(2a+b)+(a-b)\\sqrt3=8+\\sqrt3")+"。係数を比べて</p>"+D(r"2a+b=8\ \cdots①,\qquad a-b=1\ \cdots②")+"<p>①＋②："+I("3a=9")+"、"+I("a=3")+"。②より "+I("b=2")+"。</p>"+D(r"(2+\sqrt3)\cdot3+(1-\sqrt3)\cdot2=6+3\sqrt3+2-2\sqrt3=8+\sqrt3"),r"a=3,\ b=2"),
  ("<p>"+I("(a+2b)+(a-3b)\\sqrt5=6+\\sqrt5")+"。係数を比べて</p>"+D(r"a+2b=6\ \cdots①,\qquad a-3b=1\ \cdots②")+"<p>① − ②："+I("5b=5")+"、"+I("b=1")+"。①より "+I("a=4")+"。</p>"+D(r"(1+\sqrt5)\cdot4+(2-3\sqrt5)\cdot1=4+4\sqrt5+2-3\sqrt5=6+\sqrt5"),r"a=4,\ b=1"),
  ("<p>"+I("(3a+b)+(a+2b)\\sqrt2=5+5\\sqrt2")+"。係数を比べて</p>"+D(r"3a+b=5\ \cdots①,\qquad a+2b=5\ \cdots②")+"<p>①×2 − ②："+I("6a-a=10-5")+" より "+I("5a=5")+"、"+I("a=1")+"。①より "+I("b=2")+"。</p>"+D(r"(3+\sqrt2)\cdot1+(1+2\sqrt2)\cdot2=3+\sqrt2+2+4\sqrt2=5+5\sqrt2"),r"a=1,\ b=2")])
assert sp.expand((1+s2)*2+(3-2*s2)*3-(11-4*s2))==0
assert sp.expand((2+s3)*3+(1-s3)*2-(8+s3))==0
assert sp.expand((1+s5)*4+(2-3*s5)-(6+s5))==0
assert sp.expand((3+s2)+(1+2*s2)*2-(5+5*s2))==0

# ===== 章末問題 =====
from fractions import Fraction as Fr
CHE=[
 (r"\sqrt{5+2\sqrt6}+\sqrt{5-2\sqrt6}\ \text{を計算せよ。}",
  "<p>6の約数の組 "+I("(1,6),\\ (2,3)")+" のうち足して5になるのは "+I("2+3=5")+"。</p>"+D(r"\sqrt{5+2\sqrt6}=\sqrt3+\sqrt2")+D(r"\sqrt{5-2\sqrt6}=\sqrt3-\sqrt2")+"<p>（"+I("\\sqrt3>\\sqrt2")+" なので引く向きに注意）</p>"+D(r"(\sqrt3+\sqrt2)+(\sqrt3-\sqrt2)=2\sqrt3"),
  r"2\sqrt3",1),
 (r"x=\dfrac{\sqrt3-\sqrt2}{\sqrt3+\sqrt2},\ y=\dfrac{\sqrt3+\sqrt2}{\sqrt3-\sqrt2}\ \text{のとき},\ x^2+y^2,\ x^3+y^3\ \text{を求めよ。}",
  "<p>"+I("x=\\dfrac{(\\sqrt3-\\sqrt2)^2}{3-2}=3-2\\sqrt6+2=5-2\\sqrt6")+"、"+I("y=\\dfrac{(\\sqrt3+\\sqrt2)^2}{3-2}=5+2\\sqrt6")+"。</p>"+D(r"x+y=10,\qquad xy=25-24=1")+D(r"x^2+y^2=10^2-2\cdot1=98")+D(r"x^3+y^3=10^3-3\cdot1\cdot10=1000-30=970"),
  r"x^2+y^2=98,\ \ x^3+y^3=970",2),
 (r"x=\dfrac{\sqrt5-1}2\ \text{のとき},\ x^2+x-1\ \text{の値と},\ \dfrac1x\ \text{の整数部分を求めよ。}",
  "<p>"+I("x^2=\\dfrac{(\\sqrt5-1)^2}4=\\dfrac{6-2\\sqrt5}4=\\dfrac{3-\\sqrt5}2")+"。</p>"+D(r"x^2+x-1=\dfrac{3-\sqrt5}2+\dfrac{\sqrt5-1}2-1=\dfrac22-1=0")+"<p>"+I("\\dfrac1x=\\dfrac2{\\sqrt5-1}=\\dfrac{2(\\sqrt5+1)}{5-1}=\\dfrac{\\sqrt5+1}2")+"。"+I("2.2<\\sqrt5<2.3")+" より "+I("1.6<\\dfrac{\\sqrt5+1}2<1.65")+"。整数部分は1。</p>",
  r"x^2+x-1=0,\ \text{整数部分は}\ 1",3),
 (r"2|x-1|+|x-4|=7\ \text{を解け。}",
  "<p>境目は "+I("x=1,\\ 4")+"。</p><p>① "+I("x<1")+"："+I("-2(x-1)-(x-4)=7")+" → "+I("-3x+6=7")+" → "+I("x=-\\dfrac13")+"（"+I("x<1")+" をみたす）。</p><p>② "+I("1\\leqq x<4")+"："+I("2(x-1)-(x-4)=7")+" → "+I("x+2=7")+" → "+I("x=5")+"（範囲外）。</p><p>③ "+I("x\\geqq4")+"："+I("2(x-1)+(x-4)=7")+" → "+I("3x-6=7")+" → "+I("x=\\dfrac{13}3")+"（"+I("x\\geqq4")+" をみたす）。</p>",
  r"x=-\dfrac13,\ \dfrac{13}3",4),
 (r"(a+b\sqrt2)^2=17+12\sqrt2\ \text{をみたす正の有理数}\ a,\ b\ \text{を求めよ。}",
  "<p>展開：</p>"+D(r"(a^2+2b^2)+2ab\sqrt2=17+12\sqrt2")+"<p>係数を比べて "+I("a^2+2b^2=17\\ \\cdots①")+"、"+I("ab=6\\ \\cdots②")+"。</p><p>②より "+I("b=\\dfrac6a")+"。①に代入して</p>"+D(r"a^2+\dfrac{72}{a^2}=17\ \Rightarrow\ a^4-17a^2+72=0\ \Rightarrow\ (a^2-8)(a^2-9)=0")+"<p>"+I("a^2=8")+" だと "+I("a=2\\sqrt2")+" は無理数なので不適。"+I("a^2=9")+" より "+I("a=3")+"、"+I("b=2")+"。</p>"+D(r"(3+2\sqrt2)^2=9+12\sqrt2+8=17+12\sqrt2"),
  r"a=3,\ b=2",5)]
assert sp.simplify(sp.sqrt(5+2*s6)+sp.sqrt(5-2*s6)-2*s3)==0
xx=5-2*s6;yy=5+2*s6; assert sp.expand(xx**2+yy**2)==98 and sp.expand(xx**3+yy**3)==970
xx=(s5-1)/2; assert sp.simplify(xx**2+xx-1)==0 and 1<float(1/xx)<2
assert [k for k in range(-60,60) if Fr(k,3) is not None and abs(2*abs(Fr(k,3)-1)+abs(Fr(k,3)-4)-7)==0]==[-1,13]
assert sp.expand((3+2*s2)**2-17-12*s2)==0

UNIT=dict(subject="1",ci=0,ui=2,chapter="数と式",name="実数（平方根・絶対値）",
  intro="二重根号・有理化・整数部分と小数部分・絶対値の場合分けなど、平方根と絶対値の難問に挑みます。",
  examples=EXS,chapter_end=CHE)
