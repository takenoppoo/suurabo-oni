# -*- coding: utf-8 -*-
# 正弦定理・余弦定理（数学I 図形と計量）
from tools import *
import sympy as sp, numpy as np, math
EXS=[]
def ex(**k): EXS.append(k)
r3=sp.sqrt(3); r2=sp.sqrt(2); r6=sp.sqrt(6)
d2r=math.radians

def tri_sas(b,c,A):
    a=math.sqrt(b*b+c*c-2*b*c*math.cos(d2r(A)))
    R=a/(2*math.sin(d2r(A))); S=0.5*b*c*math.sin(d2r(A)); return a,R,S
# ===== 例題1 余弦定理＋外接円＋面積 =====
t1=tri("i42_e1",[(0,0),(8,0),(2.5,4.33)],["A","B","C"],sides={(0,1):"c=8",(1,2):"a",(2,0):"b=5"},angles={0:"60°"},w=40,size=(3.6,2.8))
ex(title="余弦定理・外接円の半径・面積",
 problem="△ABC で "+I("b=5,\\ c=8,\\ A=60^\\circ")+" のとき、辺 "+I("a")+"、外接円の半径 "+I("R")+"、面積 "+I("S")+" を求めよ。"+t1,
 approach="<p>2辺とその<b>間の角</b>がわかっているので、<b>余弦定理</b>で残りの辺 "+I("a")+" を求める。</p>"+D(r"a^2=b^2+c^2-2bc\cos A")+"<p>外接円の半径は<b>正弦定理</b> "+I("\\dfrac a{\\sin A}=2R")+"、面積は "+I("S=\\dfrac12bc\\sin A")+"。</p>",
 kotsu="「2辺とはさむ角」なら余弦定理で第3の辺。辺と対角のペアが1組そろったら、正弦定理で外接円の半径。",
 steps=[
  step(1,"余弦定理で "+I("a")+" を求める",D(r"a^2=5^2+8^2-2\cdot5\cdot8\cos60^\circ=25+64-80\cdot\dfrac12=89-40=49")+"<p>"+I("a>0")+" より "+I("a=7")+"。</p>"),
  step(2,"正弦定理で "+I("R")+" を求める",D(r"\dfrac{a}{\sin A}=2R\ \Rightarrow\ 2R=\dfrac7{\sin60^\circ}=\dfrac7{\frac{\sqrt3}2}=\dfrac{14}{\sqrt3}")+D(r"R=\dfrac7{\sqrt3}=\dfrac{7\sqrt3}3")),
  step(3,"面積を求める",D(r"S=\dfrac12bc\sin A=\dfrac12\cdot5\cdot8\cdot\dfrac{\sqrt3}2=10\sqrt3"))],
 answer=r"a=7,\quad R=\dfrac{7\sqrt3}3,\quad S=10\sqrt3",
 practice=[r"b=3,\ c=5,\ A=120^\circ\ \text{のとき},\ a,\ R,\ S",r"b=4,\ c=5,\ A=60^\circ\ \text{のとき},\ a,\ R,\ S",r"b=2,\ c=3\sqrt2,\ A=45^\circ\ \text{のとき},\ a,\ R,\ S"],
 pans=[
  ("<p>"+I("a^2=9+25-2\\cdot3\\cdot5\\cos120^\\circ=34-30\\cdot\\left(-\\dfrac12\\right)=34+15=49")+"、"+I("a=7")+"。</p>"+D(r"R=\dfrac a{2\sin120^\circ}=\dfrac7{2\cdot\frac{\sqrt3}2}=\dfrac7{\sqrt3}=\dfrac{7\sqrt3}3")+D(r"S=\dfrac12\cdot3\cdot5\cdot\dfrac{\sqrt3}2=\dfrac{15\sqrt3}4"),r"a=7,\ R=\dfrac{7\sqrt3}3,\ S=\dfrac{15\sqrt3}4"),
  ("<p>"+I("a^2=16+25-2\\cdot4\\cdot5\\cos60^\\circ=41-20=21")+"、"+I("a=\\sqrt{21}")+"。</p>"+D(r"R=\dfrac{\sqrt{21}}{2\sin60^\circ}=\dfrac{\sqrt{21}}{\sqrt3}=\sqrt7")+D(r"S=\dfrac12\cdot4\cdot5\cdot\dfrac{\sqrt3}2=5\sqrt3"),r"a=\sqrt{21},\ R=\sqrt7,\ S=5\sqrt3"),
  ("<p>"+I("a^2=4+18-2\\cdot2\\cdot3\\sqrt2\\cos45^\\circ=22-12\\sqrt2\\cdot\\dfrac{\\sqrt2}2=22-12=10")+"、"+I("a=\\sqrt{10}")+"。</p>"+D(r"R=\dfrac{\sqrt{10}}{2\sin45^\circ}=\dfrac{\sqrt{10}}{\sqrt2}=\sqrt5")+D(r"S=\dfrac12\cdot2\cdot3\sqrt2\cdot\dfrac{\sqrt2}2=3"),r"a=\sqrt{10},\ R=\sqrt5,\ S=3")])
for (b,c,A,a_,R_,S_) in ((5,8,60,7,7*math.sqrt(3)/3,10*math.sqrt(3)),(3,5,120,7,7*math.sqrt(3)/3,15*math.sqrt(3)/4),(4,5,60,math.sqrt(21),math.sqrt(7),5*math.sqrt(3)),(2,3*math.sqrt(2),45,math.sqrt(10),math.sqrt(5),3)):
    a,R,S=tri_sas(b,c,A); assert abs(a-a_)<1e-9 and abs(R-R_)<1e-9 and abs(S-S_)<1e-9

# ===== 例題2 正弦定理（2通りの三角形） =====
t2=tri("i42_e2",[(0,0),(6.2,0),(1.7,1.0)],["A","B","C"],angles={0:""},w=40,size=(3.6,2.0))
def amb(A,a,b):
    sB=b*math.sin(d2r(A))/a; out=[]
    if sB>1+1e-12: return out
    B1=math.degrees(math.asin(min(1,sB)))
    for B in sorted({round(B1,9),round(180-B1,9)}):
        if A+B<180-1e-9:
            C=180-A-B; c=a*math.sin(d2r(C))/math.sin(d2r(A)); out.append((B,C,c))
    return out
ex(title="正弦定理で角を求める（解が2通りの場合）",
 problem="△ABC で "+I("A=30^\\circ,\\ a=2,\\ b=2\\sqrt3")+" のとき、"+I("B,\\ C,\\ c")+" を求めよ。",
 approach="<p>辺 "+I("a")+" とその対角 "+I("A")+"、辺 "+I("b")+" がわかっているので、<b>正弦定理</b> "+I("\\dfrac a{\\sin A}=\\dfrac b{\\sin B}")+" で "+I("\\sin B")+" を求める。"+I("0^\\circ<B<180^\\circ")+" では "+I("\\sin B=k")+" をみたす "+I("B")+" が<b>2つ</b>ある（"+I("B")+" と "+I("180^\\circ-B")+"）。<b>"+I("A+B<180^\\circ")+" をみたすものだけ</b>が三角形をつくる。</p>",
 kotsu="sin の値には角が2つ（鋭角とその補角）対応する。両方とも三角形の内角として成り立つか、A との合計が 180° 未満かで確かめる。",
 steps=[
  step(1,r"\(\sin B\) を求める",D(r"\dfrac{2}{\sin30^\circ}=\dfrac{2\sqrt3}{\sin B}\ \Rightarrow\ \sin B=\dfrac{2\sqrt3\cdot\frac12}{2}=\dfrac{\sqrt3}2")),
  step(2,r"\(B\) の候補","<p>"+I("0^\\circ<B<180^\\circ")+" で "+I("\\sin B=\\dfrac{\\sqrt3}2")+" となるのは "+I("B=60^\\circ")+" または "+I("B=120^\\circ")+"。</p>"),
  step(3,r"\(A+B<180^\circ\) を確かめる","<p>"+I("30^\\circ+60^\\circ=90^\\circ")+"、"+I("30^\\circ+120^\\circ=150^\\circ")+"。どちらも "+I("180^\\circ")+" 未満なので<b>2通りとも成り立つ</b>。</p>"),
  step(4,r"① \(B=60^\circ\) のとき","<p>"+I("C=180^\\circ-30^\\circ-60^\\circ=90^\\circ")+"。"+I("c=\\dfrac{a\\sin C}{\\sin A}=\\dfrac{2\\cdot1}{\\frac12}=4")+"。</p>"),
  step(5,r"② \(B=120^\circ\) のとき","<p>"+I("C=180^\\circ-30^\\circ-120^\\circ=30^\\circ")+"。"+I("c=\\dfrac{2\\sin30^\\circ}{\\sin30^\\circ}=2")+"（"+I("A=C")+" なので "+I("c=a=2")+"）。</p>")],
 answer=r"B=60^\circ,\ C=90^\circ,\ c=4\quad\text{または}\quad B=120^\circ,\ C=30^\circ,\ c=2",
 practice=[r"A=45^\circ,\ a=2,\ b=\sqrt6\ \text{のとき},\ B,\ C,\ c",r"A=60^\circ,\ a=3\sqrt2,\ b=\sqrt6\ \text{のとき},\ B,\ C,\ c",r"A=30^\circ,\ a=3,\ b=3\sqrt2\ \text{のとき},\ B,\ C,\ c"],
 pans=[
  ("<p>"+I("\\sin B=\\dfrac{\\sqrt6\\sin45^\\circ}2=\\dfrac{\\sqrt6\\cdot\\frac{\\sqrt2}2}2=\\dfrac{\\sqrt{12}}4=\\dfrac{\\sqrt3}2")+"。"+I("B=60^\\circ,\\ 120^\\circ")+"（"+I("45^\\circ+120^\\circ=165^\\circ<180^\\circ")+" で両方可）。</p><p>"+I("B=60^\\circ")+"："+I("C=75^\\circ")+"、"+I("c=\\dfrac{2\\sin75^\\circ}{\\sin45^\\circ}=\\dfrac{2\\cdot\\frac{\\sqrt6+\\sqrt2}4}{\\frac{\\sqrt2}2}=\\dfrac{\\sqrt6+\\sqrt2}{\\sqrt2}=\\sqrt3+1")+"。</p><p>"+I("B=120^\\circ")+"："+I("C=15^\\circ")+"、"+I("c=\\dfrac{2\\sin15^\\circ}{\\sin45^\\circ}=\\dfrac{\\sqrt6-\\sqrt2}{\\sqrt2}=\\sqrt3-1")+"。</p>",r"B=60^\circ,C=75^\circ,c=\sqrt3+1\ \ \text{または}\ \ B=120^\circ,C=15^\circ,c=\sqrt3-1"),
  ("<p>"+I("\\sin B=\\dfrac{\\sqrt6\\sin60^\\circ}{3\\sqrt2}=\\dfrac{\\sqrt6\\cdot\\frac{\\sqrt3}2}{3\\sqrt2}=\\dfrac{\\frac{3\\sqrt2}2}{3\\sqrt2}=\\dfrac12")+"。"+I("B=30^\\circ,\\ 150^\\circ")+"。"+I("A+B=60^\\circ+150^\\circ=210^\\circ>180^\\circ")+" なので "+I("B=150^\\circ")+" は不適。</p><p>"+I("B=30^\\circ")+"："+I("C=90^\\circ")+"、"+I("c=\\dfrac{3\\sqrt2\\cdot1}{\\frac{\\sqrt3}2}=\\dfrac{6\\sqrt2}{\\sqrt3}=2\\sqrt6")+"。</p>",r"B=30^\circ,\ C=90^\circ,\ c=2\sqrt6\ \ (\text{1通りのみ})"),
  ("<p>"+I("\\sin B=\\dfrac{3\\sqrt2\\cdot\\frac12}3=\\dfrac{\\sqrt2}2")+"。"+I("B=45^\\circ,\\ 135^\\circ")+"（"+I("30^\\circ+135^\\circ=165^\\circ<180^\\circ")+" で両方可）。</p><p>"+I("B=45^\\circ")+"："+I("C=105^\\circ")+"、"+I("c=\\dfrac{3\\sin105^\\circ}{\\sin30^\\circ}=6\\cdot\\dfrac{\\sqrt6+\\sqrt2}4=\\dfrac{3(\\sqrt6+\\sqrt2)}2")+"。</p><p>"+I("B=135^\\circ")+"："+I("C=15^\\circ")+"、"+I("c=6\\sin15^\\circ=6\\cdot\\dfrac{\\sqrt6-\\sqrt2}4=\\dfrac{3(\\sqrt6-\\sqrt2)}2")+"。</p>",r"B=45^\circ,C=105^\circ,c=\dfrac{3(\sqrt6+\sqrt2)}2\ \ \text{または}\ \ B=135^\circ,C=15^\circ,c=\dfrac{3(\sqrt6-\sqrt2)}2")])
r=amb(30,2,2*math.sqrt(3)); assert [(round(B),round(C),round(c,6)) for B,C,c in r]==[(60,90,4.0),(120,30,2.0)]
r=amb(45,2,math.sqrt(6)); assert [round(B) for B,C,c in r]==[60,120] and abs(r[0][2]-(math.sqrt(3)+1))<1e-9 and abs(r[1][2]-(math.sqrt(3)-1))<1e-9
r=amb(60,3*math.sqrt(2),math.sqrt(6)); assert len(r)==1 and round(r[0][0])==30 and abs(r[0][2]-2*math.sqrt(6))<1e-9
r=amb(30,3,3*math.sqrt(2)); assert [round(B) for B,C,c in r]==[45,135] and abs(r[0][2]-1.5*(math.sqrt(6)+math.sqrt(2)))<1e-9 and abs(r[1][2]-1.5*(math.sqrt(6)-math.sqrt(2)))<1e-9

# ===== 例題3 角の二等分線の長さ（面積を利用） =====
def bis(name,ab,ac,A):
    Ar=d2r(A); B=np.array([ab,0.0]); C=np.array([ac*math.cos(Ar),ac*math.sin(Ar)])
    Dp=(ac*B+ab*C)/(ab+ac)
    P=[(0,0),tuple(B),tuple(C)]
    def extra(ax): ax.plot([0,Dp[0]],[0,Dp[1]],color=RED,lw=1.8); ax.text(Dp[0]+0.15,Dp[1]-0.35,"D",fontsize=14)
    return tri(name,P,["A","B","C"],sides={(0,1):f"{ab}",(2,0):f"{ac}"},angles={0:f"{A}°"},extra=extra,w=42,size=(3.8,3.0))
t3=bis("i42_e3",4,6,120)
ex(title="角の二等分線の長さ（面積で立式）",
 problem="△ABC で "+I("AB=4,\\ AC=6,\\ A=120^\\circ")+" である。"+I("A")+" の二等分線が辺 BC と交わる点を D とするとき、線分 AD の長さを求めよ。"+t3,
 approach="<p>三角形の面積を<b>2通りに表して等式を作る</b>。△ABC の面積は、△ABD と △ACD の面積の和。</p>"+D(r"\triangle ABC=\triangle ABD+\triangle ACD")+"<p>"+I("\\angle BAD=\\angle CAD=60^\\circ")+" を使って、各面積を "+I("\\dfrac12\\cdot\\text{辺}\\cdot\\text{辺}\\cdot\\sin")+" で表す。</p>",
 kotsu="大きな三角形の面積 ＝ 二等分線で切った2つの小さな三角形の面積の和。未知の AD が両方に登場して、方程式になる。",
 steps=[
  step(1,"△ABC の面積",D(r"\triangle ABC=\dfrac12\cdot4\cdot6\cdot\sin120^\circ=12\cdot\dfrac{\sqrt3}2=6\sqrt3")),
  step(2,"△ABD と △ACD の面積","<p>"+I("AD=x")+" とおく。"+I("\\angle BAD=\\angle CAD=60^\\circ")+"。</p>"+D(r"\triangle ABD=\dfrac12\cdot4\cdot x\cdot\sin60^\circ=\dfrac12\cdot4x\cdot\dfrac{\sqrt3}2=\sqrt3\,x")+D(r"\triangle ACD=\dfrac12\cdot6\cdot x\cdot\sin60^\circ=\dfrac12\cdot6x\cdot\dfrac{\sqrt3}2=\dfrac{3\sqrt3}2\,x")),
  step(3,"面積の和で式を立てる",D(r"6\sqrt3=\sqrt3x+\dfrac{3\sqrt3}2x=\dfrac{5\sqrt3}2x")),
  step(4,r"\(x\) を求める","<p>両辺を "+I("\\sqrt3")+" で割って</p>"+D(r"6=\dfrac52x\ \Rightarrow\ x=\dfrac{12}5"))],
 answer=r"AD=\dfrac{12}5",
 practice=[r"AB=3,\ AC=6,\ A=120^\circ\ \text{のとき},\ \text{二等分線}\ AD",r"AB=5,\ AC=3,\ A=60^\circ\ \text{のとき},\ \text{二等分線}\ AD",r"AB=2,\ AC=4,\ A=120^\circ\ \text{のとき},\ \text{二等分線}\ AD"],
 pans=[
  ("<p>"+I("\\triangle ABC=\\dfrac12\\cdot3\\cdot6\\cdot\\dfrac{\\sqrt3}2=\\dfrac{9\\sqrt3}2")+"。"+I("AD=x")+"、"+I("\\angle BAD=\\angle CAD=60^\\circ")+"：</p>"+D(r"\dfrac12\cdot3x\cdot\dfrac{\sqrt3}2+\dfrac12\cdot6x\cdot\dfrac{\sqrt3}2=\dfrac{9\sqrt3}4x")+D(r"\dfrac{9\sqrt3}2=\dfrac{9\sqrt3}4x\ \Rightarrow\ x=2"),r"AD=2"),
  ("<p>"+I("\\triangle ABC=\\dfrac12\\cdot5\\cdot3\\cdot\\dfrac{\\sqrt3}2=\\dfrac{15\\sqrt3}4")+"。"+I("\\angle BAD=\\angle CAD=30^\\circ")+"、"+I("\\sin30^\\circ=\\dfrac12")+"：</p>"+D(r"\dfrac12\cdot5x\cdot\dfrac12+\dfrac12\cdot3x\cdot\dfrac12=\dfrac54x+\dfrac34x=2x")+D(r"\dfrac{15\sqrt3}4=2x\ \Rightarrow\ x=\dfrac{15\sqrt3}8"),r"AD=\dfrac{15\sqrt3}8"),
  ("<p>"+I("\\triangle ABC=\\dfrac12\\cdot2\\cdot4\\cdot\\dfrac{\\sqrt3}2=2\\sqrt3")+"。"+I("\\angle BAD=\\angle CAD=60^\\circ")+"：</p>"+D(r"\dfrac12\cdot2x\cdot\dfrac{\sqrt3}2+\dfrac12\cdot4x\cdot\dfrac{\sqrt3}2=\dfrac{3\sqrt3}2x")+D(r"2\sqrt3=\dfrac{3\sqrt3}2x\ \Rightarrow\ x=\dfrac43"),r"AD=\dfrac43")])
def adl(ab,ac,A):
    Ar=d2r(A); B=np.array([ab,0.0]); C=np.array([ac*math.cos(Ar),ac*math.sin(Ar)]); D=(ac*B+ab*C)/(ab+ac); return np.linalg.norm(D)
assert abs(adl(4,6,120)-12/5)<1e-9 and abs(adl(3,6,120)-2)<1e-9 and abs(adl(5,3,60)-15*math.sqrt(3)/8)<1e-9 and abs(adl(2,4,120)-4/3)<1e-9

# ===== 例題4 鈍角三角形になる条件 =====
ex(title="三角形の形（鈍角三角形になる条件）",
 problem="3辺の長さが "+I("x,\\ x+1,\\ x+2")+" である三角形が鈍角三角形になるような "+I("x")+" の値の範囲を求めよ。",
 approach="<p>2つの条件を<b>両方</b>みたす "+I("x")+" を求める。</p><ol><li><b>三角形が存在する</b>：最大辺 &lt; 他の2辺の和</li><li><b>鈍角三角形</b>：<b>最大辺の2乗 &gt; 他の2辺の2乗の和</b>（最大角が鈍角 ⇔ その対辺の2乗が大きい。余弦定理で "+I("\\cos C<0")+"）</li></ol>",
 kotsu="三角形の成立 → 鈍角になる、の2段階。2段階目は最大の辺について三平方の定理の不等式を作る。",
 steps=[
  step(1,"最大辺を決める","<p>最大辺は "+I("x+2")+"（辺の長さは正なので "+I("x>0")+"）。</p>"),
  step(2,"三角形が存在する条件",D(r"x+(x+1)>x+2\ \Rightarrow\ x>1")),
  step(3,"鈍角になる条件",D(r"(x+2)^2>x^2+(x+1)^2")+D(r"x^2+4x+4>x^2+x^2+2x+1\ \Rightarrow\ 0>x^2-2x-3\ \Rightarrow\ x^2-2x-3<0")+D(r"(x-3)(x+1)<0\ \Rightarrow\ -1<x<3")),
  step(4,"共通部分を求める","<p>"+I("x>1")+" と "+I("-1<x<3")+" の共通部分：</p>"+D(r"1<x<3")),
  step(5,"確かめる","<p>"+I("x=2")+"：辺 "+I("2,3,4")+"。"+I("4^2=16>2^2+3^2=13")+" で鈍角三角形。"+I("x=3")+"：辺 "+I("3,4,5")+" は直角三角形で不適。</p>")],
 answer=r"1<x<3",
 practice=[r"\text{3辺が}\ x,\ x+2,\ x+4\ \text{の三角形が鈍角三角形}",r"\text{3辺が}\ x,\ x+3,\ x+6\ \text{の三角形が鈍角三角形}",r"\text{3辺が}\ x-1,\ x,\ x+1\ \text{の三角形が鈍角三角形}"],
 pans=[
  ("<p>最大辺 "+I("x+4")+"。存在：</p>"+D(r"x+(x+2)>x+4\Rightarrow x>2")+"<p>鈍角：</p>"+D(r"(x+4)^2>x^2+(x+2)^2\Rightarrow x^2+8x+16>2x^2+4x+4\Rightarrow x^2-4x-12<0\Rightarrow(x-6)(x+2)<0")+"<p>"+I("-2<x<6")+"。共通部分：</p>"+D(r"2<x<6"),r"2<x<6"),
  ("<p>最大辺 "+I("x+6")+"。存在："+I("x+(x+3)>x+6")+" より "+I("x>3")+"。鈍角：</p>"+D(r"(x+6)^2>x^2+(x+3)^2\Rightarrow x^2+12x+36>2x^2+6x+9\Rightarrow x^2-6x-27<0\Rightarrow(x-9)(x+3)<0")+"<p>"+I("-3<x<9")+"。共通部分：</p>"+D(r"3<x<9"),r"3<x<9"),
  ("<p>最大辺 "+I("x+1")+"、"+I("x-1>0")+" より "+I("x>1")+"。存在："+I("(x-1)+x>x+1")+" より "+I("x>2")+"。鈍角：</p>"+D(r"(x+1)^2>(x-1)^2+x^2\Rightarrow x^2+2x+1>2x^2-2x+1\Rightarrow x^2-4x<0\Rightarrow x(x-4)<0")+"<p>"+I("0<x<4")+"。共通部分：</p>"+D(r"2<x<4"),r"2<x<4")])
def obtuse(sides):
    s=sorted(sides); return s[0]>0 and s[0]+s[1]>s[2] and s[2]**2>s[0]**2+s[1]**2
xs=[k/20 for k in range(1,400)]
assert all(obtuse([v,v+1,v+2])==(1<v<3) for v in xs)
assert all(obtuse([v,v+2,v+4])==(2<v<6) for v in xs)
assert all(obtuse([v,v+3,v+6])==(3<v<9) for v in xs)
assert all(obtuse([v-1,v,v+1])==(2<v<4) for v in xs)

# ===== 例題5 内接円・外接円（ヘロン） =====
t5=tri("i42_e5",[(0,0),(14,0),(5,12)],["A","B","C"],sides={(0,1):"14",(1,2):"15",(2,0):"13"},w=40,size=(3.8,3.2))
ex(title="3辺から面積・内接円・外接円の半径",
 problem="△ABC の3辺が "+I("a=14,\\ b=15,\\ c=13")+" であるとき、面積 "+I("S")+"、内接円の半径 "+I("r")+"、外接円の半径 "+I("R")+" を求めよ。"+t5,
 approach="<p><b>ヘロンの公式</b>：<b>"+I("s=\\dfrac{a+b+c}2")+"</b> として "+I("S=\\sqrt{s(s-a)(s-b)(s-c)}")+"。または余弦定理で "+I("\\cos")+"、"+I("\\sin")+" を求めて "+I("S=\\dfrac12bc\\sin A")+"。</p>"+D(r"S=\dfrac12r(a+b+c)\quad(\text{内接円})\qquad R=\dfrac{abc}{4S}\quad(\text{外接円})")+"<p>面積から内接円と外接円の半径が出る。</p>",
 kotsu="面積さえ出せば、内接円（S＝½×r×周）も外接円（R＝abc／4S）も一直線。",
 steps=[
  step(1,"ヘロンの公式で面積を求める","<p>"+I("s=\\dfrac{14+15+13}2=21")+"。</p>"+D(r"S=\sqrt{21\cdot(21-14)(21-15)(21-13)}=\sqrt{21\cdot7\cdot6\cdot8}")+D(r"=\sqrt{7056}=84\quad(84^2=7056)")+"<p>（"+I("21\\cdot7\\cdot6\\cdot8=3\\cdot7\\cdot7\\cdot6\\cdot8=7^2\\cdot144=(7\\cdot12)^2")+" と因数分解すると計算しやすい。）</p>"),
  step(2,"内接円の半径",D(r"S=\dfrac12r(a+b+c)\ \Rightarrow\ 84=\dfrac12\cdot r\cdot42=21r\ \Rightarrow\ r=4")),
  step(3,"外接円の半径",D(r"R=\dfrac{abc}{4S}=\dfrac{14\cdot15\cdot13}{4\cdot84}=\dfrac{2730}{336}=\dfrac{65}8"))],
 answer=r"S=84,\quad r=4,\quad R=\dfrac{65}8",
 practice=[r"a=5,\ b=6,\ c=7\ \text{のとき},\ S,\ r,\ R",r"a=7,\ b=8,\ c=9\ \text{のとき},\ S,\ r,\ R",r"a=4,\ b=5,\ c=7\ \text{のとき},\ S,\ r,\ R"],
 pans=[
  ("<p>"+I("s=9")+"。"+I("S=\\sqrt{9\\cdot4\\cdot3\\cdot2}=\\sqrt{216}=6\\sqrt6")+"。</p>"+D(r"r=\dfrac{2S}{a+b+c}=\dfrac{12\sqrt6}{18}=\dfrac{2\sqrt6}3")+D(r"R=\dfrac{5\cdot6\cdot7}{4\cdot6\sqrt6}=\dfrac{210}{24\sqrt6}=\dfrac{35}{4\sqrt6}=\dfrac{35\sqrt6}{24}"),r"S=6\sqrt6,\ r=\dfrac{2\sqrt6}3,\ R=\dfrac{35\sqrt6}{24}"),
  ("<p>"+I("s=12")+"。"+I("S=\\sqrt{12\\cdot5\\cdot4\\cdot3}=\\sqrt{720}=12\\sqrt5")+"。</p>"+D(r"r=\dfrac{2S}{a+b+c}=\dfrac{24\sqrt5}{24}=\sqrt5")+D(r"R=\dfrac{7\cdot8\cdot9}{4\cdot12\sqrt5}=\dfrac{504}{48\sqrt5}=\dfrac{21}{2\sqrt5}=\dfrac{21\sqrt5}{10}"),r"S=12\sqrt5,\ r=\sqrt5,\ R=\dfrac{21\sqrt5}{10}"),
  ("<p>"+I("s=8")+"。"+I("S=\\sqrt{8\\cdot4\\cdot3\\cdot1}=\\sqrt{96}=4\\sqrt6")+"。</p>"+D(r"r=\dfrac{2S}{a+b+c}=\dfrac{8\sqrt6}{16}=\dfrac{\sqrt6}2")+D(r"R=\dfrac{4\cdot5\cdot7}{4\cdot4\sqrt6}=\dfrac{140}{16\sqrt6}=\dfrac{35}{4\sqrt6}=\dfrac{35\sqrt6}{24}"),r"S=4\sqrt6,\ r=\dfrac{\sqrt6}2,\ R=\dfrac{35\sqrt6}{24}")])
def hero(a,b,c):
    s=(a+b+c)/2; S=math.sqrt(s*(s-a)*(s-b)*(s-c)); return S,2*S/(a+b+c),a*b*c/(4*S)
for (a,b,c),(S_,r_,R_) in (((14,15,13),(84,4,65/8)),((5,6,7),(6*math.sqrt(6),2*math.sqrt(6)/3,35*math.sqrt(6)/24)),((7,8,9),(12*math.sqrt(5),math.sqrt(5),21*math.sqrt(5)/10)),((4,5,7),(4*math.sqrt(6),math.sqrt(6)/2,35*math.sqrt(6)/24))):
    S,r,R=hero(a,b,c); assert abs(S-S_)<1e-9 and abs(r-r_)<1e-9 and abs(R-R_)<1e-9

CHE=[
 (r"\triangle ABC\ \text{で}\ b=8,\ c=15,\ A=60^\circ\ \text{のとき},\ a,\ R,\ S\ \text{を求めよ。}",
  "<p>"+I("a^2=64+225-2\\cdot8\\cdot15\\cdot\\dfrac12=289-120=169")+"、"+I("a=13")+"。</p>"+D(r"R=\dfrac{13}{2\sin60^\circ}=\dfrac{13}{\sqrt3}=\dfrac{13\sqrt3}3")+D(r"S=\dfrac12\cdot8\cdot15\cdot\dfrac{\sqrt3}2=30\sqrt3"),
  r"a=13,\ R=\dfrac{13\sqrt3}3,\ S=30\sqrt3",1),
 (r"\triangle ABC\ \text{で}\ A=30^\circ,\ a=4,\ b=4\sqrt3\ \text{のとき},\ B,\ C,\ c\ \text{を求めよ。}",
  "<p>"+I("\\sin B=\\dfrac{4\\sqrt3\\cdot\\frac12}4=\\dfrac{\\sqrt3}2")+"。"+I("B=60^\\circ,\\ 120^\\circ")+"（"+I("30^\\circ+120^\\circ<180^\\circ")+" で両方可）。</p><p>"+I("B=60^\\circ")+"："+I("C=90^\\circ")+"、"+I("c=\\dfrac{4\\cdot1}{\\frac12}=8")+"。</p><p>"+I("B=120^\\circ")+"："+I("C=30^\\circ")+"、"+I("c=a=4")+"。</p>",
  r"B=60^\circ,C=90^\circ,c=8\ \ \text{または}\ \ B=120^\circ,C=30^\circ,c=4",2),
 (r"\triangle ABC\ \text{で}\ AB=4,\ AC=12,\ A=120^\circ\ \text{のとき},\ A\ \text{の二等分線が}\ BC\ \text{と交わる点を}\ D\ \text{として},\ AD\ \text{を求めよ。}",
  "<p>"+I("\\triangle ABC=\\dfrac12\\cdot4\\cdot12\\cdot\\dfrac{\\sqrt3}2=12\\sqrt3")+"。"+I("AD=x")+"、"+I("\\angle BAD=\\angle CAD=60^\\circ")+"：</p>"+D(r"\dfrac12\cdot4x\cdot\dfrac{\sqrt3}2+\dfrac12\cdot12x\cdot\dfrac{\sqrt3}2=\sqrt3x+3\sqrt3x=4\sqrt3x")+D(r"12\sqrt3=4\sqrt3x\ \Rightarrow\ x=3"),
  r"AD=3",3),
 (r"\text{3辺が}\ x-2,\ x,\ x+2\ \text{の三角形が鈍角三角形になるような}\ x\ \text{の範囲を求めよ。}",
  "<p>最大辺 "+I("x+2")+"、"+I("x-2>0")+" より "+I("x>2")+"。存在："+I("(x-2)+x>x+2")+" より "+I("x>4")+"。鈍角：</p>"+D(r"(x+2)^2>(x-2)^2+x^2\Rightarrow x^2+4x+4>2x^2-4x+4\Rightarrow x^2-8x<0\Rightarrow x(x-8)<0")+"<p>"+I("0<x<8")+"。共通部分：</p>"+D(r"4<x<8"),
  r"4<x<8",4),
 (r"a=7,\ b=15,\ c=20\ \text{のとき},\ \triangle ABC\ \text{の面積}\ S,\ \text{内接円の半径}\ r,\ \text{外接円の半径}\ R\ \text{を求めよ。}",
  "<p>"+I("s=\\dfrac{7+15+20}2=21")+"。"+I("S=\\sqrt{21\\cdot14\\cdot6\\cdot1}=\\sqrt{1764}=42")+"。</p>"+D(r"r=\dfrac{2S}{a+b+c}=\dfrac{84}{42}=2")+D(r"R=\dfrac{7\cdot15\cdot20}{4\cdot42}=\dfrac{2100}{168}=\dfrac{25}2"),
  r"S=42,\ r=2,\ R=\dfrac{25}2",5)]
a,R,S=tri_sas(8,15,60); assert abs(a-13)<1e-9 and abs(R-13*math.sqrt(3)/3)<1e-9 and abs(S-30*math.sqrt(3))<1e-9
r=amb(30,4,4*math.sqrt(3)); assert [(round(B),round(C),round(c,6)) for B,C,c in r]==[(60,90,8.0),(120,30,4.0)]
assert abs(adl(4,12,120)-3)<1e-9
assert all(obtuse([v-2,v,v+2])==(4<v<8) for v in xs)
S,r_,R_=hero(7,15,20); assert abs(S-42)<1e-9 and abs(r_-2)<1e-9 and abs(R_-12.5)<1e-9

UNIT=dict(subject="1",ci=3,ui=1,chapter="図形と計量",name="正弦定理・余弦定理",
  intro="余弦定理・正弦定理の使い分け、解が2通りの三角形、角の二等分線、三角形の形の判定、ヘロンの公式と内接円・外接円など、難問に挑みます。",
  examples=EXS,chapter_end=CHE)
