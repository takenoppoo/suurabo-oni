# -*- coding: utf-8 -*-
# 三角比（数学I 図形と計量）
from tools import *
import sympy as sp, numpy as np
EXS=[]
def ex(**k): EXS.append(k)
rad=np.deg2rad
S=sp.symbols('s c')

# ===== 例題1 sinθ+cosθ =====
sc1=semicircle("i41_e1",[(float((1-sp.sqrt(7))/4),"cosθ")],mode="cos",w=44,note="")
ex(title="sinθ+cosθ の値から他の値を求める",
 problem=I("0^\\circ<\\theta<180^\\circ")+" で "+I("\\sin\\theta+\\cos\\theta=\\dfrac12")+" のとき、次の値を求めよ。"+D(r"\sin\theta\cos\theta,\qquad \sin\theta-\cos\theta,\qquad \sin^3\theta+\cos^3\theta"),
 approach="<p>与えられた式を<b>2乗</b>して "+I("\\sin^2\\theta+\\cos^2\\theta=1")+" を使うと、積 "+I("\\sin\\theta\\cos\\theta")+" が出る。和と積がわかれば、対称式の公式で他の値が求まる。</p>"+D(r"\sin^3\theta+\cos^3\theta=(\sin\theta+\cos\theta)^3-3\sin\theta\cos\theta(\sin\theta+\cos\theta)")+"<p>"+I("\\sin\\theta-\\cos\\theta")+" は2乗して求め、<b>符号は角の範囲から判断</b>する。</p>",
 kotsu="sin と cos を2人の登場人物と見て、「和」と「積」を押さえる。引き算（差）は2乗してから、符号を範囲で決める。",
 steps=[
  step(1,r"\(\sin\theta\cos\theta\) を求める","<p>両辺を2乗する。</p>"+D(r"(\sin\theta+\cos\theta)^2=\dfrac14")+D(r"\sin^2\theta+2\sin\theta\cos\theta+\cos^2\theta=\dfrac14")+D(r"1+2\sin\theta\cos\theta=\dfrac14\ \Rightarrow\ 2\sin\theta\cos\theta=-\dfrac34\ \Rightarrow\ \sin\theta\cos\theta=-\dfrac38")),
  step(2,r"\(\sin\theta-\cos\theta\) を求める",D(r"(\sin\theta-\cos\theta)^2=1-2\sin\theta\cos\theta=1+\dfrac34=\dfrac74")+"<p>"+I("0^\\circ<\\theta<180^\\circ")+" で "+I("\\sin\\theta>0")+"。積が負（"+I("-\\dfrac38")+"）なので "+I("\\cos\\theta<0")+"。よって "+I("\\sin\\theta-\\cos\\theta>0")+"。</p>"+D(r"\sin\theta-\cos\theta=\dfrac{\sqrt7}2")+sc1),
  step(3,r"\(\sin^3\theta+\cos^3\theta\) を求める",D(r"(\sin\theta+\cos\theta)^3-3\sin\theta\cos\theta(\sin\theta+\cos\theta)=\left(\dfrac12\right)^3-3\cdot\left(-\dfrac38\right)\cdot\dfrac12=\dfrac18+\dfrac9{16}=\dfrac{2+9}{16}=\dfrac{11}{16}"))],
 answer=r"\sin\theta\cos\theta=-\dfrac38,\quad \sin\theta-\cos\theta=\dfrac{\sqrt7}2,\quad \sin^3\theta+\cos^3\theta=\dfrac{11}{16}",
 practice=[r"0^\circ<\theta<180^\circ,\ \sin\theta+\cos\theta=\dfrac13\ \text{のとき},\ \sin\theta\cos\theta,\ \sin\theta-\cos\theta,\ \sin^3\theta+\cos^3\theta",
           r"0^\circ<\theta<180^\circ,\ \sin\theta+\cos\theta=\dfrac{\sqrt2}2\ \text{のとき},\ \sin\theta\cos\theta,\ \sin\theta-\cos\theta,\ \sin^3\theta+\cos^3\theta",
           r"0^\circ<\theta<180^\circ,\ \sin\theta+\cos\theta=-\dfrac15\ \text{のとき},\ \sin\theta\cos\theta,\ \sin\theta-\cos\theta,\ \sin^3\theta+\cos^3\theta"],
 pans=[
  ("<p>2乗：</p>"+D(r"1+2\sin\theta\cos\theta=\dfrac19\Rightarrow\sin\theta\cos\theta=-\dfrac49")+"<p>"+I("(\\sin\\theta-\\cos\\theta)^2=1+\\dfrac89=\\dfrac{17}9")+"。"+I("\\sin\\theta>0,\\ \\cos\\theta<0")+" より "+I("\\sin\\theta-\\cos\\theta=\\dfrac{\\sqrt{17}}3")+"。</p>"+D(r"\sin^3\theta+\cos^3\theta=\dfrac1{27}-3\cdot\left(-\dfrac49\right)\cdot\dfrac13=\dfrac1{27}+\dfrac49=\dfrac{1+12}{27}=\dfrac{13}{27}"),r"-\dfrac49,\ \ \dfrac{\sqrt{17}}3,\ \ \dfrac{13}{27}"),
  ("<p>2乗：</p>"+D(r"1+2\sin\theta\cos\theta=\dfrac12\Rightarrow\sin\theta\cos\theta=-\dfrac14")+"<p>"+I("(\\sin\\theta-\\cos\\theta)^2=1+\\dfrac12=\\dfrac32")+"。符号は正："+I("\\sin\\theta-\\cos\\theta=\\dfrac{\\sqrt6}2")+"。</p>"+D(r"\sin^3\theta+\cos^3\theta=\left(\dfrac{\sqrt2}2\right)^3-3\cdot\left(-\dfrac14\right)\cdot\dfrac{\sqrt2}2=\dfrac{\sqrt2}4+\dfrac{3\sqrt2}8=\dfrac{5\sqrt2}8"),r"-\dfrac14,\ \ \dfrac{\sqrt6}2,\ \ \dfrac{5\sqrt2}8"),
  ("<p>2乗：</p>"+D(r"1+2\sin\theta\cos\theta=\dfrac1{25}\Rightarrow\sin\theta\cos\theta=-\dfrac{12}{25}")+"<p>"+I("(\\sin\\theta-\\cos\\theta)^2=1+\\dfrac{24}{25}=\\dfrac{49}{25}")+"。符号は正："+I("\\sin\\theta-\\cos\\theta=\\dfrac75")+"。</p>"+D(r"\sin^3\theta+\cos^3\theta=\left(-\dfrac15\right)^3-3\cdot\left(-\dfrac{12}{25}\right)\cdot\left(-\dfrac15\right)=-\dfrac1{125}-\dfrac{36}{125}=-\dfrac{37}{125}")+"<p>（確かめ："+I("\\sin\\theta=\\dfrac35,\\ \\cos\\theta=-\\dfrac45")+"）。</p>",r"-\dfrac{12}{25},\ \ \dfrac75,\ \ -\dfrac{37}{125}")])
def solve_sc(sv):
    # sinθ,cosθ with s+c=sv, 0<θ<180
    t=sp.symbols('t'); sc_=(sv**2-1)/2
    roots=sp.solve(t**2-sv*t+sc_,t); roots=sorted(roots,key=lambda r:float(r))
    c,s=roots[0],roots[1]  # sin>0>cos (積<0)
    assert float(s)>0>float(c)
    return s,c
for sv,(p,d,q) in ((sp.Rational(1,2),(-sp.Rational(3,8),sp.sqrt(7)/2,sp.Rational(11,16))),(sp.Rational(1,3),(-sp.Rational(4,9),sp.sqrt(17)/3,sp.Rational(13,27))),(sp.sqrt(2)/2,(-sp.Rational(1,4),sp.sqrt(6)/2,5*sp.sqrt(2)/8)),(-sp.Rational(1,5),(-sp.Rational(12,25),sp.Rational(7,5),-sp.Rational(37,125)))):
    s_,c_=solve_sc(sv); assert abs(float(s_*c_-p))<1e-12 and abs(float(s_-c_-d))<1e-12 and abs(float(s_**3+c_**3-q))<1e-12

# ===== 例題2 tanθ から =====
ex(title="tanθ の値から式の値を求める",
 problem=I("\\tan\\theta=2")+" のとき、次の値を求めよ。"+D(r"\dfrac{2\sin\theta+\cos\theta}{\sin\theta-3\cos\theta},\qquad \sin^2\theta+\sin\theta\cos\theta"),
 approach="<p><b>(1) 分数式</b>：分母分子を "+I("\\cos\\theta")+" で割ると "+I("\\tan\\theta")+" だけの式になる（"+I("\\tan\\theta=\\dfrac{\\sin\\theta}{\\cos\\theta}")+"）。</p><p><b>(2) "+I("\\sin\\theta,\\cos\\theta")+" の2次式</b>：分母に "+I("1=\\sin^2\\theta+\\cos^2\\theta")+" を入れて分数にし、分母分子を "+I("\\cos^2\\theta")+" で割る。"+I("1+\\tan^2\\theta=\\dfrac1{\\cos^2\\theta}")+" を使ってもよい。</p>",
 kotsu="sin と cos が混ざった式は、cos でまとめて割ると tan だけの世界に引っ越せる。",
 steps=[
  step(1,"分数式（1次）：分母分子を "+I("\\cos\\theta")+" で割る","<p>"+I("\\cos\\theta\\neq0")+"（"+I("\\tan\\theta")+" が存在するので）。</p>"+D(r"\dfrac{2\sin\theta+\cos\theta}{\sin\theta-3\cos\theta}=\dfrac{2\tan\theta+1}{\tan\theta-3}=\dfrac{2\cdot2+1}{2-3}=\dfrac5{-1}=-5")),
  step(2,"2次式：分母に 1 を入れる",D(r"\sin^2\theta+\sin\theta\cos\theta=\dfrac{\sin^2\theta+\sin\theta\cos\theta}{\sin^2\theta+\cos^2\theta}")),
  step(3,r"分母分子を \(\cos^2\theta\) で割る",D(r"=\dfrac{\tan^2\theta+\tan\theta}{\tan^2\theta+1}=\dfrac{4+2}{4+1}=\dfrac65"))],
 answer=r"-5,\quad \dfrac65",
 practice=[r"\tan\theta=3\ \text{のとき},\ \dfrac{\sin\theta+2\cos\theta}{2\sin\theta-\cos\theta},\ \ \sin^2\theta-2\sin\theta\cos\theta",r"\tan\theta=-3\ \text{のとき},\ \dfrac{2\sin\theta+\cos\theta}{\sin\theta-\cos\theta},\ \ \sin\theta\cos\theta",r"\tan\theta=4\ \text{のとき},\ \dfrac{3\sin\theta-\cos\theta}{\sin\theta+2\cos\theta},\ \ \sin^2\theta+3\sin\theta\cos\theta"],
 pans=[
  ("<p>分母分子を "+I("\\cos\\theta")+" で割る：</p>"+D(r"\dfrac{\tan\theta+2}{2\tan\theta-1}=\dfrac{3+2}{6-1}=1")+"<p>2次式：</p>"+D(r"\dfrac{\tan^2\theta-2\tan\theta}{\tan^2\theta+1}=\dfrac{9-6}{9+1}=\dfrac3{10}"),r"1,\ \ \dfrac3{10}"),
  ("<p>分母分子を "+I("\\cos\\theta")+" で割る：</p>"+D(r"\dfrac{2\tan\theta+1}{\tan\theta-1}=\dfrac{-6+1}{-3-1}=\dfrac{-5}{-4}=\dfrac54")+"<p>2次式（積）：</p>"+D(r"\sin\theta\cos\theta=\dfrac{\tan\theta}{\tan^2\theta+1}=\dfrac{-3}{9+1}=-\dfrac3{10}"),r"\dfrac54,\ \ -\dfrac3{10}"),
  ("<p>分母分子を "+I("\\cos\\theta")+" で割る：</p>"+D(r"\dfrac{3\tan\theta-1}{\tan\theta+2}=\dfrac{12-1}{4+2}=\dfrac{11}6")+"<p>2次式：</p>"+D(r"\dfrac{\tan^2\theta+3\tan\theta}{\tan^2\theta+1}=\dfrac{16+12}{16+1}=\dfrac{28}{17}"),r"\dfrac{11}6,\ \ \dfrac{28}{17}")])
for tv,f1_,f2_ in ((2,lambda s,c:(2*s+c)/(s-3*c),lambda s,c:s*s+s*c),(3,lambda s,c:(s+2*c)/(2*s-c),lambda s,c:s*s-2*s*c),(-3,lambda s,c:(2*s+c)/(s-c),lambda s,c:s*c),(4,lambda s,c:(3*s-c)/(s+2*c),lambda s,c:s*s+3*s*c)):
    th=np.arctan(tv); s,c=np.sin(th),np.cos(th)
    exp={2:(-5,6/5),3:(1,3/10),-3:(5/4,-3/10),4:(11/6,28/17)}[tv]
    assert abs(f1_(s,c)-exp[0])<1e-9 and abs(f2_(s,c)-exp[1])<1e-9

# ===== 例題3 最大最小 =====
ex(title="三角比の2次式の最大・最小",
 problem=I("0^\\circ\\leqq\\theta\\leqq180^\\circ")+" のとき、"+I("y=\\cos^2\\theta+\\sin\\theta")+" の最大値と最小値、およびそのときの "+I("\\theta")+" の値を求めよ。",
 approach="<p>"+I("\\cos^2\\theta=1-\\sin^2\\theta")+" で<b>どちらかの三角比にそろえ</b>、"+I("t=\\sin\\theta")+" とおいて <b>"+I("t")+" の2次関数</b>にする。そのとき <b>"+I("t")+" の範囲</b>（"+I("0^\\circ\\leqq\\theta\\leqq180^\\circ")+" では "+I("0\\leqq\\sin\\theta\\leqq1")+"）を忘れない。</p>",
 kotsu="三角比を1種類にそろえて置き換え、置き換えた文字が走れる範囲（t の範囲）をチェックする。",
 steps=[
  step(1,r"\(\sin\theta\) にそろえる",D(r"y=\cos^2\theta+\sin\theta=(1-\sin^2\theta)+\sin\theta=-\sin^2\theta+\sin\theta+1")),
  step(2,r"\(t=\sin\theta\) とおき、範囲を調べる","<p>"+I("0^\\circ\\leqq\\theta\\leqq180^\\circ")+" より "+I("0\\leqq t\\leqq1")+"。</p>"+D(r"y=-t^2+t+1=-\left(t-\dfrac12\right)^2+\dfrac54")),
  step(3,"最大・最小を調べる","<p>頂点 "+I("t=\\dfrac12")+" は範囲内。最大は "+I("t=\\dfrac12")+" のとき "+I("\\dfrac54")+"。両端："+I("t=0")+" で "+I("y=1")+"、"+I("t=1")+" で "+I("y=-1+1+1=1")+"。最小は "+I("1")+"（"+I("t=0,\\ 1")+"）。</p>"),
  step(4,r"\(\theta\) を求める","<p>最大："+I("\\sin\\theta=\\dfrac12")+" より "+I("\\theta=30^\\circ,\\ 150^\\circ")+"。</p><p>最小："+I("\\sin\\theta=0")+" より "+I("\\theta=0^\\circ,\\ 180^\\circ")+"、"+I("\\sin\\theta=1")+" より "+I("\\theta=90^\\circ")+"。</p>")],
 answer=r"\theta=30^\circ,150^\circ\ \text{で最大値}\ \dfrac54,\quad \theta=0^\circ,90^\circ,180^\circ\ \text{で最小値}\ 1",
 practice=[r"0^\circ\leqq\theta\leqq180^\circ\ \text{のとき},\ y=\sin^2\theta-2\cos\theta\ \text{の最大・最小}",r"0^\circ\leqq\theta\leqq180^\circ\ \text{のとき},\ y=\cos^2\theta-2\sin\theta\ \text{の最大・最小}",r"0^\circ\leqq\theta\leqq180^\circ\ \text{のとき},\ y=\sin^2\theta+\cos\theta\ \text{の最大・最小}"],
 pans=[
  ("<p>"+I("t=\\cos\\theta")+"（"+I("-1\\leqq t\\leqq1")+"）。"+I("y=1-t^2-2t=-(t+1)^2+2")+"。頂点 "+I("t=-1")+" は範囲の左端。最大 "+I("t=-1")+" で "+I("2")+"（"+I("\\theta=180^\\circ")+"）。最小は "+I("t=1")+" のとき "+I("y=-(1+1)^2+2=-2")+"（"+I("\\theta=0^\\circ")+"）。</p>",r"\theta=180^\circ\ \text{で最大}\ 2,\ \ \theta=0^\circ\ \text{で最小}\ -2"),
  ("<p>"+I("t=\\sin\\theta")+"（"+I("0\\leqq t\\leqq1")+"）。"+I("y=1-t^2-2t=-(t+1)^2+2")+"。頂点 "+I("t=-1")+" は範囲外（左）。範囲内で単調に減少。最大は "+I("t=0")+" で "+I("1")+"（"+I("\\theta=0^\\circ,180^\\circ")+"）。最小は "+I("t=1")+" で "+I("-2")+"（"+I("\\theta=90^\\circ")+"）。</p>",r"\theta=0^\circ,180^\circ\ \text{で最大}\ 1,\ \ \theta=90^\circ\ \text{で最小}\ -2"),
  ("<p>"+I("t=\\cos\\theta")+"（"+I("-1\\leqq t\\leqq1")+"）。"+I("y=1-t^2+t=-\\left(t-\\dfrac12\\right)^2+\\dfrac54")+"。頂点 "+I("t=\\dfrac12")+" は範囲内で最大 "+I("\\dfrac54")+"（"+I("\\theta=60^\\circ")+"）。両端："+I("t=1:\\ 1")+"、"+I("t=-1:\\ 1-1-1=-1")+"。軸から遠い "+I("t=-1")+" で最小 "+I("-1")+"（"+I("\\theta=180^\\circ")+"）。</p>",r"\theta=60^\circ\ \text{で最大}\ \dfrac54,\ \ \theta=180^\circ\ \text{で最小}\ -1")])
th=np.linspace(0,np.pi,180001)
def ex_(f): v=f(th); return v.max(),v.min()
a_,b_=ex_(lambda t:np.cos(t)**2+np.sin(t)); assert abs(a_-1.25)<1e-6 and abs(b_-1)<1e-6
a_,b_=ex_(lambda t:np.sin(t)**2-2*np.cos(t)); assert abs(a_-2)<1e-6 and abs(b_+2)<1e-6
a_,b_=ex_(lambda t:np.cos(t)**2-2*np.sin(t)); assert abs(a_-1)<1e-6 and abs(b_+2)<1e-6
a_,b_=ex_(lambda t:np.sin(t)**2+np.cos(t)); assert abs(a_-1.25)<1e-6 and abs(b_+1)<1e-6

# ===== 例題4 方程式 =====
s4=semicircle("i41_e4",[(0.5,"1/2"),(-1,"-1")],mode="cos",w=46,note="")
ex(title="三角比の方程式（範囲に注意）",
 problem=I("0^\\circ\\leqq\\theta\\leqq180^\\circ")+" のとき、方程式 "+I("2\\sin^2\\theta-\\cos\\theta-1=0")+" を解け。",
 approach="<p>"+I("\\sin^2\\theta=1-\\cos^2\\theta")+" で<b>"+I("\\cos\\theta")+" だけの式</b>にし、"+I("t=\\cos\\theta")+" とおく。解いた "+I("t")+" の値が<b>範囲 "+I("-1\\leqq t\\leqq1")+" に入るか</b>を確かめ、次に単位円（半円）で "+I("\\theta")+" を求める。</p>",
 kotsu="2次方程式の答えが全部使えるとは限らない。t の走れる範囲に入る答えだけを採用して、角度に戻す。",
 steps=[
  step(1,r"\(\cos\theta\) だけの式にする",D(r"2(1-\cos^2\theta)-\cos\theta-1=0\ \Rightarrow\ -2\cos^2\theta-\cos\theta+1=0\ \Rightarrow\ 2\cos^2\theta+\cos\theta-1=0")),
  step(2,r"\(t=\cos\theta\) とおいて解く","<p>"+I("-1\\leqq t\\leqq1")+"。</p>"+D(r"2t^2+t-1=0\ \Rightarrow\ (2t-1)(t+1)=0\ \Rightarrow\ t=\dfrac12,\ -1")+"<p>どちらも範囲内。</p>"),
  step(3,r"\(\theta\) を求める","<p>"+I("\\cos\\theta=\\dfrac12")+" より "+I("\\theta=60^\\circ")+"。"+I("\\cos\\theta=-1")+" より "+I("\\theta=180^\\circ")+"。（図）</p>"+s4)],
 answer=r"\theta=60^\circ,\ 180^\circ",
 practice=[r"0^\circ\leqq\theta\leqq180^\circ,\ \ 2\cos^2\theta+\sin\theta-1=0",r"0^\circ\leqq\theta\leqq180^\circ,\ \ 2\sin^2\theta+3\cos\theta-3=0",r"0^\circ\leqq\theta\leqq180^\circ,\ \ 2\cos^2\theta-\cos\theta-1=0"],
 pans=[
  ("<p>"+I("\\cos^2\\theta=1-\\sin^2\\theta")+" で "+I("\\sin\\theta")+" にそろえる：</p>"+D(r"2(1-\sin^2\theta)+\sin\theta-1=0\Rightarrow 2\sin^2\theta-\sin\theta-1=0\Rightarrow(2\sin\theta+1)(\sin\theta-1)=0")+"<p>"+I("\\sin\\theta=-\\dfrac12")+" は "+I("0^\\circ\\leqq\\theta\\leqq180^\\circ")+" で "+I("\\sin\\theta\\geqq0")+" なので<b>不適</b>。"+I("\\sin\\theta=1")+" より "+I("\\theta=90^\\circ")+"。</p>",r"\theta=90^\circ"),
  ("<p>"+I("\\cos\\theta")+" にそろえる：</p>"+D(r"2(1-\cos^2\theta)+3\cos\theta-3=0\Rightarrow 2\cos^2\theta-3\cos\theta+1=0\Rightarrow(2\cos\theta-1)(\cos\theta-1)=0")+"<p>"+I("\\cos\\theta=\\dfrac12")+" より "+I("\\theta=60^\\circ")+"、"+I("\\cos\\theta=1")+" より "+I("\\theta=0^\\circ")+"。</p>",r"\theta=0^\circ,\ 60^\circ"),
  ("<p>"+I("\\cos\\theta=t")+"：</p>"+D(r"2t^2-t-1=0\Rightarrow(2t+1)(t-1)=0\Rightarrow t=-\dfrac12,\ 1")+"<p>"+I("\\cos\\theta=-\\dfrac12")+" より "+I("\\theta=120^\\circ")+"、"+I("\\cos\\theta=1")+" より "+I("\\theta=0^\\circ")+"。</p>",r"\theta=0^\circ,\ 120^\circ")])
def solv(f):
    return [d for d in range(0,181) if abs(f(rad(d)))<1e-9]
assert solv(lambda t:2*np.sin(t)**2-np.cos(t)-1)==[60,180]
assert solv(lambda t:2*np.cos(t)**2+np.sin(t)-1)==[90]
assert solv(lambda t:2*np.sin(t)**2+3*np.cos(t)-3)==[0,60]
assert solv(lambda t:2*np.cos(t)**2-np.cos(t)-1)==[0,120]

# ===== 例題5 和が一定の変換 =====
ex(title="90°-θ の変換を使う和・積",
 problem="次の値を求めよ。"+D(r"\sin^2 10^\circ+\sin^2 20^\circ+\sin^2 30^\circ+\cdots+\sin^2 80^\circ"),
 approach="<p>"+I("\\sin(90^\\circ-\\theta)=\\cos\\theta")+" を使う。<b>角の和が "+I("90^\\circ")+" になる2つをペアにする</b>と、"+I("\\sin^2\\theta+\\sin^2(90^\\circ-\\theta)=\\sin^2\\theta+\\cos^2\\theta=1")+"。</p>",
 kotsu="端から順に、足して90°になる角をペアにする。ペアの和が1になるので、ペアの数だけ数えればよい。",
 steps=[
  step(1,"ペアを作る","<p>"+I("10^\\circ+80^\\circ=90^\\circ")+"、"+I("20^\\circ+70^\\circ")+"、"+I("30^\\circ+60^\\circ")+"、"+I("40^\\circ+50^\\circ")+" の4組。</p>"),
  step(2,"各ペアの和を計算する",D(r"\sin^2 80^\circ=\sin^2(90^\circ-10^\circ)=\cos^2 10^\circ")+D(r"\sin^2 10^\circ+\sin^2 80^\circ=\sin^2 10^\circ+\cos^2 10^\circ=1")+"<p>他の3組も同様に 1。</p>"),
  step(3,"合計する","<p>4組なので "+I("1\\times4=4")+"。</p>")],
 answer=r"4",
 practice=[r"\cos^2 5^\circ+\cos^2 15^\circ+\cos^2 25^\circ+\cdots+\cos^2 85^\circ",r"\tan10^\circ\tan20^\circ\tan30^\circ\cdots\tan80^\circ",r"\sin^21^\circ+\sin^22^\circ+\sin^23^\circ+\cdots+\sin^289^\circ"],
 pans=[
  ("<p>"+I("5^\\circ+85^\\circ=90^\\circ")+"、"+I("15^\\circ+75^\\circ")+"、"+I("25^\\circ+65^\\circ")+"、"+I("35^\\circ+55^\\circ")+" の4組。"+I("\\cos^2 85^\\circ=\\sin^2 5^\\circ")+" なので各ペアの和は "+I("\\cos^2 5^\\circ+\\sin^2 5^\\circ=1")+"。</p><p>残りの "+I("\\cos^2 45^\\circ=\\left(\\dfrac{\\sqrt2}2\\right)^2=\\dfrac12")+"。</p>"+D(r"4+\dfrac12=\dfrac92"),r"\dfrac92"),
  ("<p>"+I("\\tan(90^\\circ-\\theta)=\\dfrac1{\\tan\\theta}")+"。"+I("10^\\circ+80^\\circ")+" などペアの積は "+I("\\tan10^\\circ\\cdot\\tan80^\\circ=\\tan10^\\circ\\cdot\\dfrac1{\\tan10^\\circ}=1")+"。"+I("10,20,30,40,50,60,70,80")+" の8個が4組で、すべてのペアの積が1。</p>"+D(r"1\times1\times1\times1=1"),r"1"),
  ("<p>"+I("1^\\circ+89^\\circ,\\ 2^\\circ+88^\\circ,\\dots,44^\\circ+46^\\circ")+" の44組で各1。残りは "+I("\\sin^245^\\circ=\\dfrac12")+"。</p>"+D(r"44+\dfrac12=\dfrac{89}2"),r"\dfrac{89}2")])
assert abs(sum(np.sin(rad(d))**2 for d in range(10,81,10))-4)<1e-9
assert abs(sum(np.cos(rad(d))**2 for d in range(5,86,10))-4.5)<1e-9
assert abs(np.prod([np.tan(rad(d)) for d in range(10,81,10)])-1)<1e-9
assert abs(sum(np.sin(rad(d))**2 for d in range(1,90))-44.5)<1e-9

CHE=[
 (r"0^\circ<\theta<180^\circ,\ \sin\theta+\cos\theta=\dfrac35\ \text{のとき},\ \sin\theta\cos\theta,\ \sin^3\theta+\cos^3\theta\ \text{を求めよ。}",
  "<p>2乗：</p>"+D(r"1+2\sin\theta\cos\theta=\dfrac9{25}\Rightarrow\sin\theta\cos\theta=-\dfrac8{25}")+D(r"\sin^3\theta+\cos^3\theta=\left(\dfrac35\right)^3-3\cdot\left(-\dfrac8{25}\right)\cdot\dfrac35=\dfrac{27}{125}+\dfrac{72}{125}=\dfrac{99}{125}"),
  r"\sin\theta\cos\theta=-\dfrac8{25},\ \ \sin^3\theta+\cos^3\theta=\dfrac{99}{125}",1),
 (r"\tan\theta=3\ \text{のとき},\ \dfrac{\sin\theta+\cos\theta}{\sin\theta-\cos\theta},\ \ \sin\theta\cos\theta-\cos^2\theta\ \text{を求めよ。}",
  "<p>分母分子を "+I("\\cos\\theta")+" で割る：</p>"+D(r"\dfrac{\tan\theta+1}{\tan\theta-1}=\dfrac{3+1}{3-1}=2")+D(r"\sin\theta\cos\theta-\cos^2\theta=\dfrac{\tan\theta-1}{\tan^2\theta+1}=\dfrac{3-1}{9+1}=\dfrac15"),
  r"2,\ \ \dfrac15",2),
 (r"0^\circ\leqq\theta\leqq180^\circ\ \text{のとき},\ y=\cos^2\theta+2\sin\theta\ \text{の最大値と最小値を求めよ。}",
  "<p>"+I("t=\\sin\\theta")+"（"+I("0\\leqq t\\leqq1")+"）。"+I("y=1-t^2+2t=-(t-1)^2+2")+"。頂点 "+I("t=1")+" は範囲の右端で最大 "+I("2")+"（"+I("\\theta=90^\\circ")+"）。最小は "+I("t=0")+" で "+I("1")+"（"+I("\\theta=0^\\circ,180^\\circ")+"）。</p>",
  r"\theta=90^\circ\ \text{で最大}\ 2,\ \ \theta=0^\circ,180^\circ\ \text{で最小}\ 1",3),
 (r"0^\circ\leqq\theta\leqq180^\circ,\ \ 2\cos^2\theta-\sin\theta-1=0\ \text{を解け。}",
  "<p>"+I("\\sin\\theta")+" にそろえる：</p>"+D(r"2(1-\sin^2\theta)-\sin\theta-1=0\Rightarrow2\sin^2\theta+\sin\theta-1=0\Rightarrow(2\sin\theta-1)(\sin\theta+1)=0")+"<p>"+I("\\sin\\theta=-1")+" は "+I("\\sin\\theta\\geqq0")+" に反するので不適。"+I("\\sin\\theta=\\dfrac12")+" より "+I("\\theta=30^\\circ,\\ 150^\\circ")+"。</p>",
  r"\theta=30^\circ,\ 150^\circ",4),
 (r"\sin^25^\circ+\sin^215^\circ+\sin^225^\circ+\cdots+\sin^285^\circ\ \text{の値を求めよ。}",
  "<p>"+I("5^\\circ+85^\\circ,\\ 15^\\circ+75^\\circ,\\ 25^\\circ+65^\\circ,\\ 35^\\circ+55^\\circ")+" の4組で各1。残りの "+I("\\sin^245^\\circ=\\dfrac12")+"。</p>"+D(r"4+\dfrac12=\dfrac92"),
  r"\dfrac92",5)]
for tv in (3,):
    t_=np.arctan(tv); assert abs((np.sin(t_)+np.cos(t_))/(np.sin(t_)-np.cos(t_))-2)<1e-9 and abs(np.sin(t_)*np.cos(t_)-np.cos(t_)**2-0.2)<1e-9
a_,b_=ex_(lambda t:np.cos(t)**2+2*np.sin(t)); assert abs(a_-2)<1e-6 and abs(b_-1)<1e-6
assert solv(lambda t:2*np.cos(t)**2-np.sin(t)-1)==[30,150]
assert abs(sum(np.sin(rad(d))**2 for d in range(5,86,10))-4.5)<1e-9
s_,c_=solve_sc(sp.Rational(3,5)) if False else (None,None)
assert abs((3/5)**3-3*(-8/25)*(3/5)-99/125)<1e-12

UNIT=dict(subject="1",ci=3,ui=0,chapter="図形と計量",name="三角比",
  intro="sinθ+cosθ の値から他の値を求める問題、tanθ を使った式の値、三角比の最大・最小、方程式、90°−θ の変換など、三角比の難問に挑みます。",
  examples=EXS,chapter_end=CHE)
