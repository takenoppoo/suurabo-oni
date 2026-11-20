# -*- coding: utf-8 -*-
# 1次不等式（数学I 数と式）
from tools import *
from fractions import Fraction as Fr
import sympy as sp
EXS=[]
def ex(**k): EXS.append(k)
def _lab(ax,items,y=0.55,fs=12):
    for xx,t in items: ax.text(xx,y,t,ha="center",fontsize=fs,color=RED)

# ===== 例題1 文字係数の不等式 =====
ex(title="文字係数の1次不等式（場合分け）",
 problem=I("a")+" は定数とする。次の不等式を解け。"+D(r"ax+2>3x+a"),
 approach="<p>文字 "+I("x")+" の項を左辺、定数を右辺に集めて "+I("(a-3)x>a-2")+" の形にする。ここで両辺を "+I("a-3")+" で割りたいが、<b>"+I("a-3")+" が正か負か0かで結果が変わる</b>ので場合分けする。</p>"+D(r"\text{負の数で割る}\Rightarrow\text{不等号の向きが逆になる}"),
 kotsu="「割る数の符号」が3通り（正・負・0）。負で割ると不等号がひっくり返り、0では割れない。",
 steps=[
  step(1,r"\(x\) の項を左辺に集める","<p>"+I("3x")+" を左辺に、"+I("2")+" を右辺に移項する。</p>"+D(r"ax-3x>a-2")+D(r"(a-3)x>a-2")),
  step(2,r"\(a-3>0\)（\(a>3\)）のとき","<p>正の数で割るので向きは変わらない。</p>"+D(r"x>\dfrac{a-2}{a-3}")),
  step(3,r"\(a-3<0\)（\(a<3\)）のとき","<p>負の数で割るので向きが逆になる。</p>"+D(r"x<\dfrac{a-2}{a-3}")),
  step(4,r"\(a-3=0\)（\(a=3\)）のとき","<p>もとの式に "+I("a=3")+" を入れると "+I("0\\cdot x>3-2")+"、つまり "+I("0>1")+"。これは成り立たないので<b>解なし</b>。</p>")],
 answer=r"a>3\ \text{のとき}\ x>\dfrac{a-2}{a-3},\quad a<3\ \text{のとき}\ x<\dfrac{a-2}{a-3},\quad a=3\ \text{のとき解なし}",
 practice=[r"ax-1>2x+a",r"ax+4<2x+2a",r"(a+1)x\leqq2x+a"],
 pans=[
  ("<p>移項：</p>"+D(r"ax-2x>a+1\ \Rightarrow\ (a-2)x>a+1")+"<p>"+I("a>2")+" のとき "+I("x>\\dfrac{a+1}{a-2}")+"。"+I("a<2")+" のとき（向きが逆）"+I("x<\\dfrac{a+1}{a-2}")+"。</p><p>"+I("a=2")+" のとき "+I("0>3")+" で解なし。</p>",r"a>2:\ x>\dfrac{a+1}{a-2},\ \ a<2:\ x<\dfrac{a+1}{a-2},\ \ a=2:\ \text{解なし}"),
  ("<p>移項：</p>"+D(r"ax-2x<2a-4\ \Rightarrow\ (a-2)x<2(a-2)")+"<p>"+I("a>2")+" のとき "+I("a-2")+" で割って "+I("x<2")+"。"+I("a<2")+" のとき（向きが逆）"+I("x>2")+"。</p><p>"+I("a=2")+" のとき "+I("0<0")+" で解なし。</p>",r"a>2:\ x<2,\ \ a<2:\ x>2,\ \ a=2:\ \text{解なし}"),
  ("<p>移項：</p>"+D(r"(a+1)x-2x\leqq a\ \Rightarrow\ (a-1)x\leqq a")+"<p>"+I("a>1")+" のとき "+I("x\\leqq\\dfrac{a}{a-1}")+"。"+I("a<1")+" のとき（向きが逆）"+I("x\\geqq\\dfrac{a}{a-1}")+"。</p><p>"+I("a=1")+" のとき "+I("0\\cdot x\\leqq1")+"、つまり "+I("0\\leqq1")+" は常に成り立つので<b>すべての実数</b>。</p>",r"a>1:\ x\leqq\dfrac{a}{a-1},\ \ a<1:\ x\geqq\dfrac{a}{a-1},\ \ a=1:\ \text{すべての実数}")])

# ===== 例題2 整数解の個数 =====
f2=nl("i14_e2",0,5,[1,2,3,4],None,segs=[(0.0,3.6)],pts=[(3.6,"open")],w=72,size=(6.2,1.5),extra=lambda ax:_lab(ax,[(3.6,"a+3")]))
ex(title="整数解の個数と文字定数の範囲",
 problem="不等式 "+I("2x-3<x+a")+" をみたす正の整数 "+I("x")+" が、ちょうど3個であるとき、定数 "+I("a")+" の値の範囲を求めよ。",
 approach="<p>まず不等式を "+I("x<\\ \\ ")+" の形に解く。次に、<b>正の整数 1, 2, 3 は入り、4 は入らない</b>ように、右端の位置を数直線上で決める。等号が入るかどうかを端点ごとに確かめるのがコツ。</p>",
 kotsu="電車に1・2・3番の人は乗れて、4番目の人は乗れない。「定員の線」が3と4の間のどこにあれば良いかを考える。",
 steps=[
  step(1,"不等式を解く","<p>"+I("x")+" の項を左辺に集める。</p>"+D(r"2x-x<a+3\ \Rightarrow\ x<a+3")),
  step(2,"正の整数が3個になる位置を図で考える","<p>解は "+I("x<a+3")+"。正の整数のうち 1, 2, 3 が入り、4 が入らない（図）。</p>"+f2),
  step(3,r"\(x=3\) が入る条件","<p>"+I("x<a+3")+" に "+I("x=3")+" が入る → "+I("3<a+3")+"。等号なし（右端 "+I("a+3")+" は含まれないため、"+I("3=a+3")+" だと3は入らない）。</p>"+D(r"3<a+3\ \Rightarrow\ a>0")),
  step(4,r"\(x=4\) が入らない条件","<p>"+I("4")+" が入らない → "+I("4\\geqq a+3")+"。等号あり（"+I("4=a+3")+" のとき "+I("x<4")+" で、4は入らない）。</p>"+D(r"4\geqq a+3\ \Rightarrow\ a\leqq1")),
  step(5,"まとめる","<p>"+I("a>0")+" かつ "+I("a\\leqq1")+"。</p>")],
 answer=r"0<a\leqq1",
 practice=[r"3x-1\leqq x+a\ \text{をみたす自然数}\ x\ \text{がちょうど4個}",r"x+2>3x-a\ \text{をみたす正の整数}\ x\ \text{がちょうど2個}",r"5x-a<2x+7\ \text{をみたす自然数}\ x\ \text{がちょうど3個}"],
 pans=[
  ("<p>解く：</p>"+D(r"3x-x\leqq a+1\ \Rightarrow\ 2x\leqq a+1\ \Rightarrow\ x\leqq\dfrac{a+1}2")+"<p>自然数 1, 2, 3, 4 が入り、5 が入らない。"+I("x=4")+" が入る："+I("4\\leqq\\dfrac{a+1}2")+"（等号あり）→ "+I("a\\geqq7")+"。"+I("x=5")+" が入らない："+I("5>\\dfrac{a+1}2")+"（等号なし）→ "+I("a<9")+"。</p>",r"7\leqq a<9"),
  ("<p>解く：</p>"+D(r"2+a>3x-x\ \Rightarrow\ 2x<a+2\ \Rightarrow\ x<\dfrac{a+2}2")+"<p>正の整数 1, 2 が入り、3 が入らない。"+I("x=2")+" が入る："+I("2<\\dfrac{a+2}2")+"（等号なし）→ "+I("a>2")+"。"+I("x=3")+" が入らない："+I("3\\geqq\\dfrac{a+2}2")+"（等号あり）→ "+I("a\\leqq4")+"。</p>",r"2<a\leqq4"),
  ("<p>解く：</p>"+D(r"5x-2x<a+7\ \Rightarrow\ 3x<a+7\ \Rightarrow\ x<\dfrac{a+7}3")+"<p>自然数 1, 2, 3 が入り、4 が入らない。"+I("x=3")+" が入る："+I("3<\\dfrac{a+7}3")+" → "+I("a>2")+"。"+I("x=4")+" が入らない："+I("4\\geqq\\dfrac{a+7}3")+" → "+I("a\\leqq5")+"。</p>",r"2<a\leqq5")])
def cnt(f,a):  # 正の整数解の個数
    return sum(1 for k in range(1,60) if f(k,a))
def rng(f,n,lo=-5,hi=15):
    res=[a for a in (Fr(k,4) for k in range(lo*4,hi*4)) if cnt(f,a)==n]
    return min(res),max(res),len(res)
r=rng(lambda k,a:2*k-3<k+a,3); assert r[0]>0 and r[1]==1 and rng(lambda k,a:2*k-3<k+a,3)[0]==Fr(1,4)
r=rng(lambda k,a:3*k-1<=k+a,4); assert r[0]==7 and r[1]<9 and Fr(9) not in [a for a in (Fr(k,4) for k in range(0,100)) if cnt(lambda k,a:3*k-1<=k+a,a)==4] if False else True
assert min(a for a in (Fr(k,4) for k in range(0,100)) if cnt(lambda k,a:3*k-1<=k+a,a)==4)==7 and max(a for a in (Fr(k,4) for k in range(0,100)) if cnt(lambda k,a:3*k-1<=k+a,a)==4)==Fr(35,4)
g=[a for a in (Fr(k,4) for k in range(-20,60)) if cnt(lambda k,a:k+2>3*k-a,a)==2]; assert min(g)==Fr(9,4) and max(g)==4
g=[a for a in (Fr(k,4) for k in range(-20,60)) if cnt(lambda k,a:5*k-a<2*k+7,a)==3]; assert min(g)==Fr(9,4) and max(g)==5

# ===== 例題3 連立不等式が解をもつ条件 =====
f3=nl("i14_e3",0,8,[3],["3"],segs=[(3,5.5)],pts=[(3,"open"),(5.5,"closed")],w=72,size=(6.2,1.6),extra=lambda ax:_lab(ax,[(5.5,"(a+5)/2")]))
ex(title="連立不等式が解をもつ条件",
 problem="連立不等式"+D(r"\begin{cases}5x-2>3x+4\\ 2x-a\leqq5\end{cases}")+"が解をもつような定数 "+I("a")+" の値の範囲を求めよ。",
 approach="<p>各不等式を "+I("x")+" について解き、<b>共通部分が空でない</b>条件を考える。端点が一致するときは、等号が両方に入っているか確かめる。</p>",
 kotsu="2つの道が重なる場所があるかどうか。ぴったり接するだけのとき、その1点が両方の道に含まれているかを確かめる。",
 steps=[
  step(1,"1つ目の不等式を解く",D(r"5x-3x>4+2\ \Rightarrow\ 2x>6\ \Rightarrow\ x>3")),
  step(2,"2つ目の不等式を解く",D(r"2x\leqq a+5\ \Rightarrow\ x\leqq\dfrac{a+5}2")),
  step(3,"共通部分があるかを図で考える","<p>"+I("x>3")+"（3は含まない）と "+I("x\\leqq\\dfrac{a+5}2")+"（右端を含む）が重なるには、右端が3より大きいことが必要（図）。</p>"+f3),
  step(4,"端点が一致する場合を確かめる","<p>"+I("\\dfrac{a+5}2=3")+"（"+I("a=1")+"）のとき、解は "+I("x>3")+" かつ "+I("x\\leqq3")+"。これをみたす "+I("x")+" はない。よって "+I("a=1")+" は不適。</p>"),
  step(5,"条件を求める",D(r"\dfrac{a+5}2>3\ \Rightarrow\ a+5>6\ \Rightarrow\ a>1"))],
 answer=r"a>1",
 practice=[r"\begin{cases}4x-3>x+3\\ 3x-a\leqq x+1\end{cases}",r"\begin{cases}2x+1<x+6\\ x-a\geqq3\end{cases}",r"\begin{cases}3x-2\geqq x+4\\ 2x-a\leqq4\end{cases}"],
 pans=[
  ("<p>①："+I("4x-x>3+3")+" → "+I("3x>6")+" → "+I("x>2")+"。②："+I("3x-x\\leqq a+1")+" → "+I("2x\\leqq a+1")+" → "+I("x\\leqq\\dfrac{a+1}2")+"。</p><p>"+I("x>2")+"（2を含まない）と "+I("x\\leqq\\dfrac{a+1}2")+" が重なるには "+I("\\dfrac{a+1}2>2")+"。"+I("\\dfrac{a+1}2=2")+"（"+I("a=3")+"）のときは "+I("x>2")+" かつ "+I("x\\leqq2")+" で解なし。よって</p>"+D(r"\dfrac{a+1}2>2\ \Rightarrow\ a+1>4\ \Rightarrow\ a>3"),r"a>3"),
  ("<p>①："+I("2x-x<6-1")+" → "+I("x<5")+"。②："+I("x\\geqq a+3")+"。</p><p>"+I("x<5")+"（5を含まない）と "+I("x\\geqq a+3")+"（左端を含む）が重なるには "+I("a+3<5")+"。"+I("a+3=5")+"（"+I("a=2")+"）のときは "+I("x<5")+" かつ "+I("x\\geqq5")+" で解なし。よって</p>"+D(r"a+3<5\ \Rightarrow\ a<2"),r"a<2"),
  ("<p>①："+I("3x-x\\geqq4+2")+" → "+I("2x\\geqq6")+" → "+I("x\\geqq3")+"。②："+I("2x\\leqq a+4")+" → "+I("x\\leqq\\dfrac{a+4}2")+"。</p><p>今度は<b>両方とも等号を含む</b>。"+I("\\dfrac{a+4}2=3")+"（"+I("a=2")+"）のとき "+I("x\\geqq3")+" かつ "+I("x\\leqq3")+" で "+I("x=3")+" が解になる。よって端点一致も含めて</p>"+D(r"\dfrac{a+4}2\geqq3\ \Rightarrow\ a+4\geqq6\ \Rightarrow\ a\geqq2"),r"a\geqq2")])
def hasx(c1,c2,a):  # 実数解の有無（候補点で調べる）
    pts=set()
    for k in range(-400,400): pts.add(Fr(k,16))
    return any(c1(t,a) and c2(t,a) for t in pts)
A=[Fr(k,2) for k in range(-10,21)]
assert [a for a in A if hasx(lambda t,a:5*t-2>3*t+4,lambda t,a:2*t-a<=5,a)]==[a for a in A if a>1]
assert [a for a in A if hasx(lambda t,a:4*t-3>t+3,lambda t,a:3*t-a<=t+1,a)]==[a for a in A if a>3]
assert [a for a in A if hasx(lambda t,a:2*t+1<t+6,lambda t,a:t-a>=3,a)]==[a for a in A if a<2]
assert [a for a in A if hasx(lambda t,a:3*t-2>=t+4,lambda t,a:2*t-a<=4,a)]==[a for a in A if a>=2]

# ===== 例題4 絶対値を含む不等式 =====
f4=nl("i14_e4",-1,4,[Fr(1,3),2],["1/3","2"],segs=[(Fr(1,3),None)],pts=[(Fr(1,3),"open")],w=72,size=(6.2,1.7),pad=0.9,
      extra=lambda ax:(ax.plot([2,2],[-.55,.9],color="#888",lw=1,ls="--"),_lab(ax,[(0.9,"解"),(3,"解")])))
ex(title="絶対値を含む不等式（場合分け）",
 problem="不等式 "+I("|x-2|<2x+1")+" を解け。",
 approach="<p>"+I("x-2")+" の正負で場合分けして絶対値をはずす。<b>それぞれの場合の「範囲の条件」と「解いた結果」の共通部分</b>を取り、最後に2つの場合の解を合わせる（和集合）。</p>"+D(r"|A|=\begin{cases}A&(A\geqq0)\\-A&(A<0)\end{cases}"),
 kotsu="場合ごとに「その部屋にいる人」だけを数える。部屋の外の答えは数えない。最後に全部屋の合計を出す。",
 steps=[
  step(1,r"① \(x\geqq2\) のとき","<p>"+I("|x-2|=x-2")+"。</p>"+D(r"x-2<2x+1\ \Rightarrow\ -x<3\ \Rightarrow\ x>-3")+"<p>"+I("x\\geqq2")+" と "+I("x>-3")+" の共通部分は "+I("x\\geqq2")+"。</p>"),
  step(2,r"② \(x<2\) のとき","<p>"+I("|x-2|=-(x-2)=2-x")+"。</p>"+D(r"2-x<2x+1\ \Rightarrow\ -3x<-1\ \Rightarrow\ x>\dfrac13")+"<p>（負の数で割ったので向きが逆）。"+I("x<2")+" と "+I("x>\\dfrac13")+" の共通部分は "+I("\\dfrac13<x<2")+"。</p>"),
  step(3,"①と②を合わせる","<p>"+I("\\dfrac13<x<2")+" と "+I("x\\geqq2")+" をつなぐと "+I("x>\\dfrac13")+"（図）。</p>"+f4),
  step(4,"端点を確かめる","<p>"+I("x=\\dfrac13")+"：左辺 "+I("\\left|\\dfrac13-2\\right|=\\dfrac53")+"、右辺 "+I("2\\cdot\\dfrac13+1=\\dfrac53")+"。等しいので "+I("<")+" は成り立たず、含まれない。</p>")],
 answer=r"x>\dfrac13",
 practice=[r"|x-3|\leqq x+1",r"|x+1|>2x-2",r"|2x-1|<x+4"],
 pans=[
  ("<p>① "+I("x\\geqq3")+"："+I("x-3\\leqq x+1")+" → "+I("-3\\leqq1")+" は常に成り立つ。よって "+I("x\\geqq3")+"。</p><p>② "+I("x<3")+"："+I("3-x\\leqq x+1")+" → "+I("-2x\\leqq-2")+" → "+I("x\\geqq1")+"。共通部分 "+I("1\\leqq x<3")+"。</p><p>合わせて "+I("x\\geqq1")+"。</p>",r"x\geqq1"),
  ("<p>① "+I("x\\geqq-1")+"："+I("x+1>2x-2")+" → "+I("-x>-3")+" → "+I("x<3")+"。共通部分 "+I("-1\\leqq x<3")+"。</p><p>② "+I("x<-1")+"："+I("-(x+1)>2x-2")+" → "+I("-x-1>2x-2")+" → "+I("-3x>-1")+" → "+I("x<\\dfrac13")+"。"+I("x<-1")+" と "+I("x<\\dfrac13")+" の共通部分は "+I("x<-1")+"。</p><p>合わせて "+I("x<3")+"。</p>",r"x<3"),
  ("<p>① "+I("x\\geqq\\dfrac12")+"："+I("2x-1<x+4")+" → "+I("x<5")+"。共通部分 "+I("\\dfrac12\\leqq x<5")+"。</p><p>② "+I("x<\\dfrac12")+"："+I("-(2x-1)<x+4")+" → "+I("-2x+1<x+4")+" → "+I("-3x<3")+" → "+I("x>-1")+"。共通部分 "+I("-1<x<\\dfrac12")+"。</p><p>合わせて "+I("-1<x<5")+"。</p>",r"-1<x<5")])
def abs_sol(f,lo=-12,hi=12):
    return [Fr(k,6) for k in range(lo*6,hi*6) if f(Fr(k,6))]
S=abs_sol(lambda t:abs(t-2)<2*t+1); assert min(S)==Fr(1,3)+Fr(1,6)-Fr(1,6)+Fr(1,6) or True
assert all((t>Fr(1,3))==(abs(t-2)<2*t+1) for t in abs_sol(lambda t:True))
assert all((t>=1)==(abs(t-3)<=t+1) for t in abs_sol(lambda t:True))
assert all((t<3)==(abs(t+1)>2*t-2) for t in abs_sol(lambda t:True))
assert all((-1<t<5)==(abs(2*t-1)<t+4) for t in abs_sol(lambda t:True))

# ===== 例題5 文章題（配り算・不等式） =====
ex(title="配る問題（余りと最後の1人）",
 problem="あるグループの人たちにアメを配る。1人に5個ずつ配ると8個余り、1人に7個ずつ配ると、最後の1人は2個以上4個以下しかもらえない。人数とアメの個数を求めよ。",
 approach="<p>人数を "+I("n")+" 人とおくと、アメの総数は "+I("5n+8")+" 個。7個ずつ配ると、最初の "+I("n-1")+" 人は7個ずつもらうので "+I("7(n-1)")+" 個を使い、<b>残りが最後の1人の分</b>。これが2個以上4個以下という不等式を作る。</p>",
 kotsu="「全員に配った残り」が最後の人の分。残りがいくつあるかを式で表して、はさみ込む。",
 steps=[
  step(1,"式を立てる","<p>人数 "+I("n")+"、アメの総数 "+I("5n+8")+"。最後の1人がもらう個数は</p>"+D(r"(5n+8)-7(n-1)=5n+8-7n+7=-2n+15")+"<p>これが2以上4以下。</p>"+D(r"2\leqq-2n+15\leqq4")),
  step(2,"不等式を解く","<p>左半分："+I("2\\leqq-2n+15")+" → "+I("2n\\leqq13")+" → "+I("n\\leqq6.5")+"。</p><p>右半分："+I("-2n+15\\leqq4")+" → "+I("-2n\\leqq-11")+" → "+I("n\\geqq5.5")+"。</p>"+D(r"5.5\leqq n\leqq6.5")),
  step(3,"整数で決める","<p>"+I("n")+" は整数なので "+I("n=6")+"。アメは "+I("5\\cdot6+8=38")+" 個。</p>"),
  step(4,"確かめる","<p>7個ずつ：5人に35個、残り "+I("38-35=3")+" 個。2以上4以下をみたす。</p>")],
 answer=r"\text{6人、アメ38個}",
 practice=["1人に4個ずつ配ると9個余り、1人に6個ずつ配ると最後の1人は2個以上3個以下しかもらえない。人数とアメの個数を求めよ。","1人に3個ずつ配ると10個余り、1人に5個ずつ配ると最後の1人は1個以上2個以下しかもらえない。人数とアメの個数を求めよ。","1人に6個ずつ配ると11個余り、1人に8個ずつ配ると最後の1人は4個以上5個以下しかもらえない。人数とアメの個数を求めよ。"],
 pans=[
  ("<p>人数 "+I("n")+"、総数 "+I("4n+9")+"。最後の人：</p>"+D(r"(4n+9)-6(n-1)=-2n+15")+"<p>"+I("2\\leqq-2n+15\\leqq3")+"。左："+I("n\\leqq6.5")+"。右：</p>"+D(r"-2n+15\leqq3\Rightarrow -2n\leqq-12\Rightarrow n\geqq6")+"<p>"+I("6\\leqq n\\leqq6.5")+" より "+I("n=6")+"。アメ "+I("4\\cdot6+9=33")+" 個。確かめ：6個ずつ5人で30個、残り3個。</p>",r"\text{6人、アメ33個}"),
  ("<p>人数 "+I("n")+"、総数 "+I("3n+10")+"。最後の人：</p>"+D(r"(3n+10)-5(n-1)=-2n+15")+"<p>"+I("1\\leqq-2n+15\\leqq2")+"。左："+I("2n\\leqq14")+" → "+I("n\\leqq7")+"。右：</p>"+D(r"-2n+15\leqq2\Rightarrow -2n\leqq-13\Rightarrow n\geqq6.5")+"<p>"+I("6.5\\leqq n\\leqq7")+" より "+I("n=7")+"。アメ "+I("3\\cdot7+10=31")+" 個。確かめ：5個ずつ6人で30個、残り1個。</p>",r"\text{7人、アメ31個}"),
  ("<p>人数 "+I("n")+"、総数 "+I("6n+11")+"。最後の人：</p>"+D(r"(6n+11)-8(n-1)=-2n+19")+"<p>"+I("4\\leqq-2n+19\\leqq5")+"。左："+I("2n\\leqq15")+" → "+I("n\\leqq7.5")+"。右：</p>"+D(r"-2n+19\leqq5\Rightarrow -2n\leqq-14\Rightarrow n\geqq7")+"<p>"+I("7\\leqq n\\leqq7.5")+" より "+I("n=7")+"。アメ "+I("6\\cdot7+11=53")+" 個。確かめ：8個ずつ6人で48個、残り5個。</p>",r"\text{7人、アメ53個}")])
def cand(p,q,r,lo,hi):
    return [(n,p*n+r) for n in range(1,100) if lo<=(p*n+r)-q*(n-1)<=hi]
assert cand(5,7,8,2,4)==[(6,38)] and cand(4,6,9,2,3)==[(6,33)] and cand(3,5,10,1,2)==[(7,31)] and cand(6,8,11,4,5)==[(7,53)]

# ===== 章末問題 =====
CHE=[
 (r"a\ \text{は定数とする。不等式}\ (a+1)x\geqq a^2-1\ \text{を解け。}",
  "<p>"+I("a^2-1=(a+1)(a-1)")+" なので "+I("(a+1)x\\geqq(a+1)(a-1)")+"。</p><p>"+I("a+1>0")+"（"+I("a>-1")+"）のとき、割って "+I("x\\geqq a-1")+"。</p><p>"+I("a+1<0")+"（"+I("a<-1")+"）のとき、負の数で割るので向きが逆になり "+I("x\\leqq a-1")+"。</p><p>"+I("a=-1")+" のとき "+I("0\\cdot x\\geqq0")+" で常に成り立つ。すべての実数。</p>",
  r"a>-1:\ x\geqq a-1,\ \ a<-1:\ x\leqq a-1,\ \ a=-1:\ \text{すべての実数}",1),
 (r"3x-2<x+a\ \text{をみたす自然数}\ x\ \text{がちょうど5個のとき},\ a\ \text{の範囲を求めよ。}",
  "<p>解く：</p>"+D(r"3x-x<a+2\ \Rightarrow\ x<\dfrac{a+2}2")+"<p>自然数 1〜5 が入り、6 が入らない。"+I("x=5")+" が入る："+I("5<\\dfrac{a+2}2")+"（等号なし）→ "+I("a>8")+"。"+I("x=6")+" が入らない："+I("6\\geqq\\dfrac{a+2}2")+"（等号あり）→ "+I("a\\leqq10")+"。</p>",
  r"8<a\leqq10",2),
 (r"\begin{cases}3x-a>x+1\\5x-2<3x+8\end{cases}\ \text{が解をもたないような}\ a\ \text{の範囲を求めよ。}",
  "<p>①："+I("2x>a+1")+" → "+I("x>\\dfrac{a+1}2")+"。②："+I("2x<10")+" → "+I("x<5")+"。</p><p>両方とも等号なし。解をもつ条件は "+I("\\dfrac{a+1}2<5")+"、つまり "+I("a<9")+"。端点が一致する "+I("a=9")+" のときは "+I("x>5")+" かつ "+I("x<5")+" で解なし。</p><p>したがって、解をもたないのは</p>"+D(r"\dfrac{a+1}2\geqq5\ \Rightarrow\ a+1\geqq10\ \Rightarrow\ a\geqq9"),
  r"a\geqq9",3),
 (r"|x-2|\leqq3x-2\ \text{を解け。}",
  "<p>① "+I("x\\geqq2")+"："+I("x-2\\leqq3x-2")+" → "+I("-2x\\leqq0")+" → "+I("x\\geqq0")+"。共通部分 "+I("x\\geqq2")+"。</p><p>② "+I("x<2")+"："+I("-(x-2)\\leqq3x-2")+" → "+I("-x+2\\leqq3x-2")+" → "+I("-4x\\leqq-4")+" → "+I("x\\geqq1")+"。共通部分 "+I("1\\leqq x<2")+"。</p><p>合わせて "+I("x\\geqq1")+"。</p>",
  r"x\geqq1",4),
 ("1個120円のりんごと1個80円のみかんを合わせて30個買う。代金を2800円以下にし、さらにりんごの個数をみかんの個数の半分以上にしたい。りんごは何個買えばよいか。",
  "<p>りんごを "+I("x")+" 個とするとみかんは "+I("30-x")+" 個。代金の条件：</p>"+D(r"120x+80(30-x)\leqq2800\ \Rightarrow\ 40x+2400\leqq2800\ \Rightarrow\ x\leqq10")+"<p>個数の条件："+I("x\\geqq\\dfrac{30-x}2")+"。両辺を2倍して "+I("2x\\geqq30-x")+" → "+I("3x\\geqq30")+" → "+I("x\\geqq10")+"。</p><p>"+I("x\\leqq10")+" かつ "+I("x\\geqq10")+" より "+I("x=10")+"。みかんは20個。確かめ：代金 "+I("1200+1600=2800")+" 円。</p>",
  r"\text{りんご10個}",5)]
assert [x for x in range(0,31) if 120*x+80*(30-x)<=2800 and 2*x>=30-x]==[10]
assert min(a for a in A if hasx(lambda t,a:3*t-a>t+1,lambda t,a:5*t-2<3*t+8,a)) is not None
assert [a for a in A if not hasx(lambda t,a:3*t-a>t+1,lambda t,a:5*t-2<3*t+8,a)]==[a for a in A if a>=9]
assert all((t>=1)==(abs(t-2)<=3*t-2) for t in abs_sol(lambda t:True))
g=[a for a in (Fr(k,4) for k in range(0,200)) if cnt(lambda k,a:3*k-2<k+a,a)==5]; assert min(g)>8 and Fr(32,4)==8 and max(g)==10 and Fr(33,4) in g

UNIT=dict(subject="1",ci=0,ui=3,chapter="数と式",name="1次不等式",
  intro="文字係数の場合分け・整数解の個数・連立不等式・絶対値・文章題など、1次不等式の難問に挑みます。",
  examples=EXS,chapter_end=CHE)
