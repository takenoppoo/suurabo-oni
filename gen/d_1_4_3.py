# -*- coding: utf-8 -*-
# 図形の面積・空間図形の計量（数学I 図形と計量）
from tools import *
import sympy as sp, numpy as np, math
EXS=[]
def ex(**k): EXS.append(k)
r2,r3,r6,r7=[math.sqrt(k) for k in (2,3,6,7)]

# ===== 例題1 円に内接する四角形 =====
def cyc(name,ab,bc,cd,da):
    # A=(0,0), B=(ab,0), D at angle A from余弦定理
    bd2=None
    # cosA: ab²+da²-2ab·da cosA = bc²+cd²+2bc·cd cosA
    cosA=(ab*ab+da*da-bc*bc-cd*cd)/(2*ab*da+2*bc*cd); A=math.acos(cosA)
    B=np.array([ab,0.0]); D=np.array([da*math.cos(A),da*math.sin(A)])
    # C: |CB|=bc,|CD|=cd, 対角側
    d=np.linalg.norm(D-B); a_=(bc*bc-cd*cd+d*d)/(2*d); h=math.sqrt(max(0,bc*bc-a_*a_)); u=(D-B)/d; n=np.array([-u[1],u[0]])
    C1=B+a_*u+h*n; C2=B+a_*u-h*n
    C=C1 if np.linalg.norm(C1)>np.linalg.norm(C2) else C2
    return [(0,0),tuple(B),tuple(C),tuple(D)],cosA
P1,_=cyc("i43_e1",3,2,3,5)
q1=tri("i43_e1",[(P1[0]),(P1[1]),(P1[2]),(P1[3])],["A","B","C","D"],sides={(0,1):"3",(1,2):"2",(2,3):"3",(3,0):"5"},w=40,size=(3.6,3.0))
def cycq(ab,bc,cd,da):
    cosA=(ab*ab+da*da-bc*bc-cd*cd)/(2*ab*da+2*bc*cd); A=math.acos(cosA); sA=math.sin(A)
    bd=math.sqrt(ab*ab+da*da-2*ab*da*cosA); S=0.5*ab*da*sA+0.5*bc*cd*sA; R=bd/(2*sA); return math.degrees(A),bd,S,R
ex(title="円に内接する四角形",
 problem="円に内接する四角形 ABCD で "+I("AB=3,\\ BC=2,\\ CD=3,\\ DA=5")+" のとき、"+I("\\angle A")+"、対角線 BD、四角形の面積 "+I("S")+"、外接円の半径 "+I("R")+" を求めよ。"+q1,
 approach="<p><b>円に内接する四角形では、向かい合う角の和が "+I("180^\\circ")+"</b>（"+I("\\angle C=180^\\circ-\\angle A")+"、"+I("\\cos C=-\\cos A")+"）。対角線 BD を、△ABD と △CBD の<b>2つの三角形で余弦定理</b>に表して等しいとおくと、"+I("\\cos A")+" が求まる。</p>",
 kotsu="BD をはさんで2つの三角形を作り、同じ BD² を2通りに書く。向かいの角は足して180°なので cos の符号が逆。",
 steps=[
  step(1,"△ABD で余弦定理",D(r"BD^2=3^2+5^2-2\cdot3\cdot5\cos A=34-30\cos A\quad\cdots①")),
  step(2,"△CBD で余弦定理","<p>"+I("\\angle C=180^\\circ-\\angle A")+" より "+I("\\cos C=-\\cos A")+"。</p>"+D(r"BD^2=2^2+3^2-2\cdot2\cdot3\cos C=13+12\cos A\quad\cdots②")),
  step(3,r"\(\cos A\) を求める","<p>①＝②：</p>"+D(r"34-30\cos A=13+12\cos A\ \Rightarrow\ 21=42\cos A\ \Rightarrow\ \cos A=\dfrac12")+"<p>よって "+I("\\angle A=60^\\circ")+"。"+q1),
  step(4,"BD を求める",D(r"BD^2=34-30\cdot\dfrac12=19\ \Rightarrow\ BD=\sqrt{19}")),
  step(5,"面積を求める","<p>"+I("\\angle C=120^\\circ")+"。</p>"+D(r"S=\triangle ABD+\triangle CBD=\dfrac12\cdot3\cdot5\sin60^\circ+\dfrac12\cdot2\cdot3\sin120^\circ=\dfrac{15\sqrt3}4+\dfrac{3\sqrt3}2=\dfrac{21\sqrt3}4")),
  step(6,"外接円の半径（正弦定理）",D(r"2R=\dfrac{BD}{\sin A}=\dfrac{\sqrt{19}}{\frac{\sqrt3}2}=\dfrac{2\sqrt{19}}{\sqrt3}\ \Rightarrow\ R=\dfrac{\sqrt{19}}{\sqrt3}=\dfrac{\sqrt{57}}3"))],
 answer=r"\angle A=60^\circ,\quad BD=\sqrt{19},\quad S=\dfrac{21\sqrt3}4,\quad R=\dfrac{\sqrt{57}}3",
 practice=[r"\text{円に内接する四角形}\ ABCD,\ AB=2,\ BC=1,\ CD=2,\ DA=3",r"\text{円に内接する四角形}\ ABCD,\ AB=1,\ BC=3,\ CD=1,\ DA=2",r"\text{円に内接する四角形}\ ABCD,\ AB=5,\ BC=3,\ CD=5,\ DA=8"],
 pans=[
  ("<p>①："+I("BD^2=4+9-12\\cos A=13-12\\cos A")+"。②："+I("BD^2=1+4+4\\cos A=5+4\\cos A")+"（"+I("\\cos C=-\\cos A")+"）。</p>"+D(r"13-12\cos A=5+4\cos A\Rightarrow8=16\cos A\Rightarrow\cos A=\dfrac12,\ A=60^\circ")+D(r"BD^2=13-6=7,\ BD=\sqrt7")+D(r"S=\dfrac12\cdot2\cdot3\sin60^\circ+\dfrac12\cdot1\cdot2\sin120^\circ=\dfrac{3\sqrt3}2+\dfrac{\sqrt3}2=2\sqrt3")+D(r"R=\dfrac{\sqrt7}{2\sin60^\circ}=\dfrac{\sqrt7}{\sqrt3}=\dfrac{\sqrt{21}}3"),r"A=60^\circ,\ BD=\sqrt7,\ S=2\sqrt3,\ R=\dfrac{\sqrt{21}}3"),
  ("<p>①："+I("BD^2=1+4-4\\cos A=5-4\\cos A")+"。②："+I("BD^2=9+1+6\\cos A\\cdot(-1)\\cdot(-1)")+" ではなく、"+I("BD^2=3^2+1^2-2\\cdot3\\cdot1\\cos C=10+6\\cos A")+"（"+I("\\cos C=-\\cos A")+"）。</p>"+D(r"5-4\cos A=10+6\cos A\Rightarrow-5=10\cos A\Rightarrow\cos A=-\dfrac12,\ A=120^\circ")+D(r"BD^2=5+2=7,\ BD=\sqrt7")+D(r"S=\dfrac12\cdot1\cdot2\sin120^\circ+\dfrac12\cdot3\cdot1\sin60^\circ=\dfrac{\sqrt3}2+\dfrac{3\sqrt3}4=\dfrac{5\sqrt3}4")+D(r"R=\dfrac{\sqrt7}{2\sin120^\circ}=\dfrac{\sqrt{21}}3"),r"A=120^\circ,\ BD=\sqrt7,\ S=\dfrac{5\sqrt3}4,\ R=\dfrac{\sqrt{21}}3"),
  ("<p>①："+I("BD^2=25+64-80\\cos A=89-80\\cos A")+"。②："+I("BD^2=9+25+30\\cos A=34+30\\cos A")+"。</p>"+D(r"89-80\cos A=34+30\cos A\Rightarrow55=110\cos A\Rightarrow\cos A=\dfrac12,\ A=60^\circ")+D(r"BD^2=89-40=49,\ BD=7")+D(r"S=\dfrac12\cdot5\cdot8\sin60^\circ+\dfrac12\cdot3\cdot5\sin120^\circ=10\sqrt3+\dfrac{15\sqrt3}4=\dfrac{55\sqrt3}4")+D(r"R=\dfrac7{2\sin60^\circ}=\dfrac7{\sqrt3}=\dfrac{7\sqrt3}3"),r"A=60^\circ,\ BD=7,\ S=\dfrac{55\sqrt3}4,\ R=\dfrac{7\sqrt3}3")])
for q,exp in (((3,2,3,5),(60,math.sqrt(19),21*r3/4,math.sqrt(57)/3)),((2,1,2,3),(60,r7,2*r3,math.sqrt(21)/3)),((1,3,1,2),(120,r7,5*r3/4,math.sqrt(21)/3)),((5,3,5,8),(60,7,55*r3/4,7*r3/3))):
    out=cycq(*q); assert all(abs(u-v)<1e-9 for u,v in zip(out,exp)),(q,out,exp)

# ===== 例題2 正四面体 =====
def tet(name):
    def fn(ax):
        pts={"A":(0,2.2),"B":(-1.8,0),"C":(1.8,0),"D":(0.6,0.8)}
        for u,v,ls in (("A","B","-"),("A","C","-"),("B","C","-"),("A","D","--"),("B","D","--"),("C","D","--")):
            ax.plot([pts[u][0],pts[v][0]],[pts[u][1],pts[v][1]],color="#333",lw=1.6,ls=ls)
        for k,(x_,y_) in pts.items(): ax.text(x_+0.12,y_+0.15 if k=="A" else y_-0.3,k,fontsize=13)
        ax.set_aspect("equal"); ax.axis("off"); ax.set_xlim(-2.4,2.4); ax.set_ylim(-0.7,2.8)
    make_fig(name,fn,size=(3.2,2.8)); return img(name,38)
tt=tet("i43_e2")
ex(title="正四面体の高さ・体積・内接球",
 problem="1辺の長さが6の正四面体 ABCD について、頂点 A から底面 BCD に下ろした垂線の長さ（高さ）"+I("h")+"、体積 "+I("V")+"、内接球の半径 "+I("r")+" を求めよ。"+tt,
 approach="<p>頂点 A から底面 BCD に下ろした垂線の足 H は、<b>正三角形 BCD の外心（重心）</b>。底面の正三角形の外接円の半径 "+I("BH")+" を正弦定理で求め、直角三角形 ABH に三平方の定理を使う。内接球は、<b>4つの面と中心 I がつくる4つの小さな四面体</b>の体積の和が全体の体積になることを使う。</p>",
 kotsu="垂線の足は底面のちょうど真ん中（外心）。底面の外接円の半径がわかれば、直角三角形で高さが出る。",
 steps=[
  step(1,"底面の正三角形の外接円の半径","<p>正三角形 BCD（1辺6）。正弦定理：</p>"+D(r"2\cdot BH=\dfrac{BC}{\sin60^\circ}=\dfrac6{\frac{\sqrt3}2}=\dfrac{12}{\sqrt3}=4\sqrt3\ \Rightarrow\ BH=2\sqrt3")),
  step(2,"高さを求める（直角三角形 ABH）",D(r"AH^2=AB^2-BH^2=36-12=24\ \Rightarrow\ h=AH=2\sqrt6")),
  step(3,"体積を求める","<p>底面積 "+I("\\triangle BCD=\\dfrac12\\cdot6\\cdot6\\cdot\\sin60^\\circ=9\\sqrt3")+"。</p>"+D(r"V=\dfrac13\cdot9\sqrt3\cdot2\sqrt6=6\sqrt{18}=6\cdot3\sqrt2=18\sqrt2")),
  step(4,"内接球の半径","<p>表面積 "+I("S=4\\times9\\sqrt3=36\\sqrt3")+"。内接球の中心 I と4つの面でできる4つの四面体の体積の和が "+I("V")+"。</p>"+D(r"V=\dfrac13\cdot S\cdot r\ \Rightarrow\ 18\sqrt2=\dfrac13\cdot36\sqrt3\cdot r=12\sqrt3\,r")+D(r"r=\dfrac{18\sqrt2}{12\sqrt3}=\dfrac{3\sqrt2}{2\sqrt3}=\dfrac{3\sqrt6}{6}=\dfrac{\sqrt6}2"))],
 answer=r"h=2\sqrt6,\quad V=18\sqrt2,\quad r=\dfrac{\sqrt6}2",
 practice=[r"1\ \text{辺が}\ 4\ \text{の正四面体の高さ},\ \text{体積},\ \text{内接球の半径}",r"1\ \text{辺が}\ 12\ \text{の正四面体の高さ},\ \text{体積},\ \text{内接球の半径}",r"1\ \text{辺が}\ 3\sqrt2\ \text{の正四面体の高さ},\ \text{体積},\ \text{内接球の半径}"],
 pans=[
  ("<p>"+I("2BH=\\dfrac4{\\sin60^\\circ}=\\dfrac8{\\sqrt3}")+"、"+I("BH=\\dfrac4{\\sqrt3}")+"。"+I("h^2=16-\\dfrac{16}3=\\dfrac{32}3")+"、"+I("h=\\dfrac{4\\sqrt2}{\\sqrt3}=\\dfrac{4\\sqrt6}3")+"。</p>"+D(r"\triangle BCD=\dfrac12\cdot4\cdot4\cdot\dfrac{\sqrt3}2=4\sqrt3,\ V=\dfrac13\cdot4\sqrt3\cdot\dfrac{4\sqrt6}3=\dfrac{16\sqrt{18}}9=\dfrac{16\sqrt2}3")+D(r"S=16\sqrt3,\ V=\dfrac13Sr\Rightarrow\dfrac{16\sqrt2}3=\dfrac{16\sqrt3}3r\Rightarrow r=\dfrac{\sqrt2}{\sqrt3}=\dfrac{\sqrt6}3"),r"h=\dfrac{4\sqrt6}3,\ V=\dfrac{16\sqrt2}3,\ r=\dfrac{\sqrt6}3"),
  ("<p>"+I("2BH=\\dfrac{12}{\\sin60^\\circ}=\\dfrac{24}{\\sqrt3}=8\\sqrt3")+"、"+I("BH=4\\sqrt3")+"。"+I("h^2=144-48=96")+"、"+I("h=4\\sqrt6")+"。</p>"+D(r"\triangle BCD=\dfrac12\cdot12\cdot12\cdot\dfrac{\sqrt3}2=36\sqrt3,\ V=\dfrac13\cdot36\sqrt3\cdot4\sqrt6=48\sqrt{18}=144\sqrt2")+D(r"S=144\sqrt3,\ 144\sqrt2=\dfrac13\cdot144\sqrt3\cdot r\Rightarrow r=\dfrac{3\sqrt2}{\sqrt3}=\sqrt6"),r"h=4\sqrt6,\ V=144\sqrt2,\ r=\sqrt6"),
  ("<p>"+I("2BH=\\dfrac{3\\sqrt2}{\\sin60^\\circ}=\\dfrac{6\\sqrt2}{\\sqrt3}=2\\sqrt6")+"、"+I("BH=\\sqrt6")+"。"+I("h^2=18-6=12")+"、"+I("h=2\\sqrt3")+"。</p>"+D(r"\triangle BCD=\dfrac12\cdot3\sqrt2\cdot3\sqrt2\cdot\dfrac{\sqrt3}2=\dfrac{9\sqrt3}2,\ V=\dfrac13\cdot\dfrac{9\sqrt3}2\cdot2\sqrt3=9")+D(r"S=18\sqrt3,\ 9=\dfrac13\cdot18\sqrt3\cdot r=6\sqrt3r\Rightarrow r=\dfrac9{6\sqrt3}=\dfrac{3}{2\sqrt3}=\dfrac{\sqrt3}2"),r"h=2\sqrt3,\ V=9,\ r=\dfrac{\sqrt3}2")])
def tetra(a): h=a*math.sqrt(2/3); V=a**3/(6*math.sqrt(2)); r=h/4; return h,V,r
for a,exp in ((6,(2*r6,18*r2,r6/2)),(4,(4*r6/3,16*r2/3,r6/3)),(12,(4*r6,144*r2,r6)),(3*r2,(2*r3,9,r3/2))):
    out=tetra(a); assert all(abs(u-v)<1e-9 for u,v in zip(out,exp)),(a,out,exp)

# ===== 例題3 直方体の切断 =====
def cuboid(name,a,b,c):
    def fn(ax):
        import numpy as np
        dx,dy=0.7,0.5
        def pr(x,y,z): return (x+dx*y*0.0+ (y)*dx, z+y*dy)
        A=(0,0,0);B=(a,0,0);D=(0,b,0);E=(0,0,c);F=(a,0,c);H=(0,b,c);C=(a,b,0);G=(a,b,c)
        pts={"A":A,"B":B,"C":C,"D":D,"E":E,"F":F,"G":G,"H":H}
        s=1/max(a,b,c)*2.2
        P={k:((v[0]+0.6*v[1])*s,(v[2]+0.4*v[1])*s) for k,v in pts.items()}
        for u,v in (("A","B"),("B","C"),("C","D"),("D","A"),("E","F"),("F","G"),("G","H"),("H","E"),("A","E"),("B","F"),("C","G"),("D","H")):
            ax.plot([P[u][0],P[v][0]],[P[u][1],P[v][1]],color="#555",lw=1.2,ls="--" if "C" in (u,v) and ("D" in (u,v) or "B" in (u,v) or "G" in (u,v)) and False else "-")
        for u,v in (("A","F"),("F","H"),("H","A")): ax.plot([P[u][0],P[v][0]],[P[u][1],P[v][1]],color=RED,lw=2.2)
        for k in P: ax.text(P[k][0]-0.12,P[k][1]+0.1,k,fontsize=12,color=RED if k in "AFH" else "#222")
        ax.set_aspect("equal"); ax.axis("off")
    make_fig(name,fn,size=(3.6,2.8)); return img(name,42)
cb=cuboid("i43_e3",1,2,2)
ex(title="直方体の切り口の面積と垂線",
 problem="直方体 ABCD-EFGH で "+I("AB=1,\\ AD=2,\\ AE=2")+" とする。△AFH の面積 "+I("S")+" と、頂点 E から平面 AFH に下ろした垂線の長さ "+I("h")+" を求めよ。"+cb,
 approach="<p>△AFH の3辺は直方体の<b>面の対角線</b>。3辺の長さを三平方の定理で求め、二等辺三角形などの形に気づく。</p><p>垂線の長さは<b>四面体 E-AFH の体積を2通りに表す</b>：底面を △AEF（または EF・EH・EA が直角に交わる面）として求めた体積と、底面を △AFH として "+I("\\dfrac13\\cdot S\\cdot h")+" で表した体積が等しい。</p>",
 kotsu="高さが直接わからない三角すいは、体積を「見やすい底面」と「求めたい底面」の2通りで書き、等しいとおく。",
 steps=[
  step(1,"△AFH の3辺を求める",D(r"AF=\sqrt{AB^2+AE^2}=\sqrt{1+4}=\sqrt5")+D(r"AH=\sqrt{AD^2+AE^2}=\sqrt{4+4}=2\sqrt2")+D(r"FH=\sqrt{EF^2+EH^2}=\sqrt{1+4}=\sqrt5")+"<p>"+I("AF=FH=\\sqrt5")+" の二等辺三角形。</p>"),
  step(2,"面積を求める","<p>AH の中点を M とすると "+I("FM\\perp AH")+"。</p>"+D(r"FM=\sqrt{AF^2-AM^2}=\sqrt{5-(\sqrt2)^2}=\sqrt{5-2}=\sqrt3")+D(r"S=\dfrac12\cdot AH\cdot FM=\dfrac12\cdot2\sqrt2\cdot\sqrt3=\sqrt6")),
  step(3,"四面体 E-AFH の体積（底面を △EFH として）","<p>E で3辺 "+I("EA,\\ EF,\\ EH")+" は互いに直角（長さ2, 1, 2）。底面を △EFH、高さを EA とする。</p>"+D(r"V=\dfrac13\cdot\left(\dfrac12\cdot EF\cdot EH\right)\cdot EA=\dfrac13\cdot\left(\dfrac12\cdot1\cdot2\right)\cdot2=\dfrac23")),
  step(4,"底面を △AFH として垂線 "+I("h")+" を求める",D(r"V=\dfrac13\cdot\sqrt6\cdot h=\dfrac23\ \Rightarrow\ h=\dfrac2{\sqrt6}=\dfrac{2\sqrt6}6=\dfrac{\sqrt6}3"))],
 answer=r"S=\sqrt6,\quad h=\dfrac{\sqrt6}3",
 practice=[r"AB=2,\ AD=3,\ AE=6\ \text{のとき},\ \triangle AFH\ \text{の面積と}\ E\ \text{から平面}\ AFH\ \text{への垂線}",r"AB=1,\ AD=1,\ AE=1\ \text{のとき},\ \triangle AFH\ \text{の面積と}\ E\ \text{から平面}\ AFH\ \text{への垂線}",r"AB=1,\ AD=2,\ AE=3\ \text{のとき},\ \triangle AFH\ \text{の面積と}\ E\ \text{から平面}\ AFH\ \text{への垂線}"],
 pans=[
  ("<p>"+I("AF=\\sqrt{4+36}=\\sqrt{40}")+"、"+I("AH=\\sqrt{9+36}=\\sqrt{45}")+"、"+I("FH=\\sqrt{4+9}=\\sqrt{13}")+"。余弦定理：</p>"+D(r"\cos\angle FAH=\dfrac{40+45-13}{2\sqrt{40}\sqrt{45}}=\dfrac{72}{2\cdot30\sqrt2}=\dfrac{3\sqrt2}5")+"<p>"+I("\\sin^2\\angle FAH=1-\\dfrac{18}{25}=\\dfrac7{25}")+"、"+I("\\sin\\angle FAH=\\dfrac{\\sqrt7}5")+"。</p>"+D(r"S=\dfrac12\cdot\sqrt{40}\sqrt{45}\cdot\dfrac{\sqrt7}5=\dfrac12\cdot30\sqrt2\cdot\dfrac{\sqrt7}5=3\sqrt{14}")+D(r"V=\dfrac13\cdot\left(\dfrac12\cdot2\cdot3\right)\cdot6=6,\quad 6=\dfrac13\cdot3\sqrt{14}\cdot h\Rightarrow h=\dfrac6{\sqrt{14}}=\dfrac{3\sqrt{14}}7"),r"S=3\sqrt{14},\ h=\dfrac{3\sqrt{14}}7"),
  ("<p>"+I("AF=AH=FH=\\sqrt2")+"（正三角形）。</p>"+D(r"S=\dfrac{\sqrt3}4\cdot(\sqrt2)^2=\dfrac{\sqrt3}2")+D(r"V=\dfrac13\cdot\left(\dfrac12\cdot1\cdot1\right)\cdot1=\dfrac16,\quad \dfrac16=\dfrac13\cdot\dfrac{\sqrt3}2\cdot h\Rightarrow h=\dfrac1{\sqrt3}=\dfrac{\sqrt3}3"),r"S=\dfrac{\sqrt3}2,\ h=\dfrac{\sqrt3}3"),
  ("<p>"+I("AF=\\sqrt{1+9}=\\sqrt{10}")+"、"+I("AH=\\sqrt{4+9}=\\sqrt{13}")+"、"+I("FH=\\sqrt{1+4}=\\sqrt5")+"。余弦定理：</p>"+D(r"\cos\angle FAH=\dfrac{10+13-5}{2\sqrt{10}\sqrt{13}}=\dfrac{18}{2\sqrt{130}}=\dfrac9{\sqrt{130}}")+"<p>"+I("\\sin^2\\angle FAH=1-\\dfrac{81}{130}=\\dfrac{49}{130}")+"、"+I("\\sin\\angle FAH=\\dfrac7{\\sqrt{130}}")+"。</p>"+D(r"S=\dfrac12\sqrt{130}\cdot\dfrac7{\sqrt{130}}=\dfrac72")+D(r"V=\dfrac13\cdot\left(\dfrac12\cdot1\cdot2\right)\cdot3=1,\quad 1=\dfrac13\cdot\dfrac72\cdot h\Rightarrow h=\dfrac67"),r"S=\dfrac72,\ h=\dfrac67")])
def cubo(a,b,c):
    S=0.5*math.sqrt(a*a*b*b+b*b*c*c+c*c*a*a); V=a*b*c/6; return S,3*V/S
for (a,b,c),exp in (((1,2,2),(r6,r6/3)),((2,3,6),(3*math.sqrt(14),3*math.sqrt(14)/7)),((1,1,1),(r3/2,r3/3)),((1,2,3),(3.5,6/7))):
    out=cubo(a,b,c); assert all(abs(u-v)<1e-9 for u,v in zip(out,exp)),(a,b,c,out,exp)
# 座標で独立検証
def cuboid_coord(a,b,c):
    A=np.array([0,0,0.]);F=np.array([a,0,c]);H=np.array([0,b,c]);E=np.array([0,0,c])
    n=np.cross(F-A,H-A); S=np.linalg.norm(n)/2; h=abs(np.dot(E-A,n))/np.linalg.norm(n); return S,h
for (a,b,c),exp in (((1,2,2),(r6,r6/3)),((2,3,6),(3*math.sqrt(14),3*math.sqrt(14)/7)),((1,1,1),(r3/2,r3/3)),((1,2,3),(3.5,6/7))):
    out=cuboid_coord(a,b,c); assert all(abs(u-v)<1e-9 for u,v in zip(out,exp)),(a,b,c,out,exp)

# ===== 例題4 正四角錐 =====
def pyr(name):
    def fn(ax):
        P={"A":(-1.8,0),"B":(0.9,-0.5),"C":(2.1,0.5),"D":(-0.6,1.0),"O":(0.15,2.9)}
        for u,v,ls in (("A","B","-"),("B","C","-"),("C","D","--"),("D","A","--"),("O","A","-"),("O","B","-"),("O","C","-"),("O","D","--")):
            ax.plot([P[u][0],P[v][0]],[P[u][1],P[v][1]],color="#333",lw=1.6,ls=ls)
        for k,(x_,y_) in P.items(): ax.text(x_+(0.12 if k in "BCO" else -0.28),y_+(0.1 if k in "OD" else -0.3),k,fontsize=13)
        ax.set_aspect("equal"); ax.axis("off"); ax.set_xlim(-2.4,2.6); ax.set_ylim(-1,3.3)
    make_fig(name,fn,size=(3.4,2.9)); return img(name,40)
pf=pyr("i43_e4")
ex(title="正四角錐の高さ・体積・表面積",
 problem="底面が1辺4の正方形 ABCD で、側辺 OA=OB=OC=OD=6 の正四角錐 O-ABCD について、高さ、体積、表面積を求めよ。"+pf,
 approach="<p>頂点 O から底面に下ろした垂線の足 H は、<b>正方形の対角線の交点</b>（中心）。直角三角形 OAH で三平方の定理を使う。表面積は、<b>底面積 ＋ 側面4つ（合同な二等辺三角形）</b>。側面の高さ（斜高）は、辺の中点を通る直角三角形で求める。</p>",
 kotsu="垂線は底面の中心に落ちる。高さは「側辺」と「中心から頂点までの距離（対角線の半分）」の直角三角形。斜高は「側辺」と「底辺の半分」の直角三角形。",
 steps=[
  step(1,"対角線の半分 AH",D(r"AC=4\sqrt2\ \Rightarrow\ AH=\dfrac12AC=2\sqrt2")),
  step(2,"高さ OH（直角三角形 OAH）",D(r"OH^2=OA^2-AH^2=36-8=28\ \Rightarrow\ OH=2\sqrt7")),
  step(3,"体積",D(r"V=\dfrac13\cdot4^2\cdot2\sqrt7=\dfrac{32\sqrt7}3")),
  step(4,"斜高（辺 AB の中点 M と O）","<p>"+I("AM=2")+"、"+I("OM\\perp AB")+"。</p>"+D(r"OM^2=OA^2-AM^2=36-4=32\ \Rightarrow\ OM=4\sqrt2")),
  step(5,"表面積",D(r"\text{側面1つ}=\dfrac12\cdot4\cdot4\sqrt2=8\sqrt2")+D(r"S=4^2+4\cdot8\sqrt2=16+32\sqrt2"))],
 answer=r"\text{高さ}\ 2\sqrt7,\quad V=\dfrac{32\sqrt7}3,\quad \text{表面積}\ 16+32\sqrt2",
 practice=[r"\text{底面が1辺}\ 6\ \text{の正方形},\ \text{側辺}\ 5\ \text{の正四角錐の高さ},\ \text{体積},\ \text{表面積}",r"\text{底面が1辺}\ 2\ \text{の正方形},\ \text{側辺}\ 3\ \text{の正四角錐の高さ},\ \text{体積},\ \text{表面積}",r"\text{底面が1辺}\ 8\ \text{の正方形},\ \text{側辺}\ 9\ \text{の正四角錐の高さ},\ \text{体積},\ \text{表面積}"],
 pans=[
  ("<p>"+I("AH=\\dfrac12\\cdot6\\sqrt2=3\\sqrt2")+"。"+I("OH^2=25-18=7")+"、高さ "+I("\\sqrt7")+"。"+I("V=\\dfrac13\\cdot36\\cdot\\sqrt7=12\\sqrt7")+"。</p><p>斜高："+I("OM^2=25-3^2=16")+"、"+I("OM=4")+"。側面1つ "+I("\\dfrac12\\cdot6\\cdot4=12")+"。</p>"+D(r"\text{表面積}=36+4\cdot12=84"),r"\text{高さ}\sqrt7,\ V=12\sqrt7,\ \text{表面積}\ 84"),
  ("<p>"+I("AH=\\dfrac12\\cdot2\\sqrt2=\\sqrt2")+"。"+I("OH^2=9-2=7")+"、高さ "+I("\\sqrt7")+"。"+I("V=\\dfrac13\\cdot4\\cdot\\sqrt7=\\dfrac{4\\sqrt7}3")+"。</p><p>斜高："+I("OM^2=9-1=8")+"、"+I("OM=2\\sqrt2")+"。側面1つ "+I("\\dfrac12\\cdot2\\cdot2\\sqrt2=2\\sqrt2")+"。</p>"+D(r"\text{表面積}=4+4\cdot2\sqrt2=4+8\sqrt2"),r"\text{高さ}\sqrt7,\ V=\dfrac{4\sqrt7}3,\ \text{表面積}\ 4+8\sqrt2"),
  ("<p>"+I("AH=\\dfrac12\\cdot8\\sqrt2=4\\sqrt2")+"。"+I("OH^2=81-32=49")+"、高さ "+I("7")+"。"+I("V=\\dfrac13\\cdot64\\cdot7=\\dfrac{448}3")+"。</p><p>斜高："+I("OM^2=81-16=65")+"、"+I("OM=\\sqrt{65}")+"。側面1つ "+I("\\dfrac12\\cdot8\\cdot\\sqrt{65}=4\\sqrt{65}")+"。</p>"+D(r"\text{表面積}=64+4\cdot4\sqrt{65}=64+16\sqrt{65}"),r"\text{高さ}\,7,\ V=\dfrac{448}3,\ \text{表面積}\ 64+16\sqrt{65}")])
def pyramid(a,l):
    h=math.sqrt(l*l-a*a/2); V=a*a*h/3; sl=math.sqrt(l*l-a*a/4); S=a*a+4*0.5*a*sl; return h,V,S
for (a,l),exp in (((4,6),(2*r7,32*r7/3,16+32*r2)),((6,5),(r7,12*r7,84)),((2,3),(r7,4*r7/3,4+8*r2)),((8,9),(7,448/3,64+16*math.sqrt(65)))):
    out=pyramid(a,l); assert all(abs(u-v)<1e-9 for u,v in zip(out,exp)),(a,l,out,exp)

# ===== 例題5 中線の長さ =====
ex(title="中線の長さ（余弦定理の2回使用）",
 problem="△ABC で "+I("AB=5,\\ AC=7,\\ BC=8")+" とする。辺 BC の中点を M とするとき、中線 AM の長さを求めよ。",
 approach="<p>① △ABC で余弦定理を使い "+I("\\cos B")+" を求める。② △ABM で、"+I("BM=\\dfrac12BC")+" をもう一度余弦定理に使い、AM を求める。</p>",
 kotsu="角 B は △ABC と △ABM に共通。まず大きい三角形で cos B を出して、小さい三角形に持ち込む。",
 steps=[
  step(1,r"\(\cos B\) を求める（△ABC）",D(r"\cos B=\dfrac{AB^2+BC^2-AC^2}{2\cdot AB\cdot BC}=\dfrac{25+64-49}{2\cdot5\cdot8}=\dfrac{40}{80}=\dfrac12")),
  step(2,"AM を求める（△ABM）","<p>"+I("BM=\\dfrac12BC=4")+"。</p>"+D(r"AM^2=AB^2+BM^2-2\cdot AB\cdot BM\cos B=25+16-2\cdot5\cdot4\cdot\dfrac12=41-20=21")+D(r"AM=\sqrt{21}"))],
 answer=r"AM=\sqrt{21}",
 practice=[r"AB=4,\ AC=6,\ BC=8\ \text{のとき中線}\ AM",r"AB=6,\ AC=8,\ BC=10\ \text{のとき中線}\ AM",r"AB=3,\ AC=5,\ BC=6\ \text{のとき中線}\ AM"],
 pans=[
  ("<p>"+I("\\cos B=\\dfrac{16+64-36}{2\\cdot4\\cdot8}=\\dfrac{44}{64}=\\dfrac{11}{16}")+"。"+I("BM=4")+"：</p>"+D(r"AM^2=16+16-2\cdot4\cdot4\cdot\dfrac{11}{16}=32-22=10\ \Rightarrow\ AM=\sqrt{10}"),r"AM=\sqrt{10}"),
  ("<p>"+I("\\cos B=\\dfrac{36+100-64}{2\\cdot6\\cdot10}=\\dfrac{72}{120}=\\dfrac35")+"。"+I("BM=5")+"：</p>"+D(r"AM^2=36+25-2\cdot6\cdot5\cdot\dfrac35=61-36=25\ \Rightarrow\ AM=5"),r"AM=5"),
  ("<p>"+I("\\cos B=\\dfrac{9+36-25}{2\\cdot3\\cdot6}=\\dfrac{20}{36}=\\dfrac59")+"。"+I("BM=3")+"：</p>"+D(r"AM^2=9+9-2\cdot3\cdot3\cdot\dfrac59=18-10=8\ \Rightarrow\ AM=2\sqrt2"),r"AM=2\sqrt2")])
def med(ab,ac,bc): return math.sqrt((2*ab*ab+2*ac*ac-bc*bc)/4)
assert abs(med(5,7,8)-r7*r3)<1e-9 and abs(med(4,6,8)-math.sqrt(10))<1e-9 and abs(med(6,8,10)-5)<1e-9 and abs(med(3,5,6)-2*r2)<1e-9

CHE=[
 (r"\text{円に内接する四角形}\ ABCD\ \text{で}\ AB=3,\ BC=3,\ CD=5,\ DA=8\ \text{のとき},\ \angle A,\ BD,\ S\ \text{を求めよ。}",
  "<p>①："+I("BD^2=9+64-48\\cos A=73-48\\cos A")+"。②："+I("BD^2=9+25+30\\cos A=34+30\\cos A")+"。</p>"+D(r"73-48\cos A=34+30\cos A\Rightarrow39=78\cos A\Rightarrow\cos A=\dfrac12,\ A=60^\circ")+D(r"BD^2=73-24=49,\ BD=7")+D(r"S=\dfrac12\cdot3\cdot8\sin60^\circ+\dfrac12\cdot3\cdot5\sin120^\circ=6\sqrt3+\dfrac{15\sqrt3}4=\dfrac{39\sqrt3}4"),
  r"A=60^\circ,\ BD=7,\ S=\dfrac{39\sqrt3}4",1),
 (r"1\ \text{辺が}\ 2\sqrt6\ \text{の正四面体の高さ},\ \text{体積},\ \text{内接球の半径を求めよ。}",
  "<p>"+I("2BH=\\dfrac{2\\sqrt6}{\\sin60^\\circ}=\\dfrac{4\\sqrt6}{\\sqrt3}=4\\sqrt2")+"、"+I("BH=2\\sqrt2")+"。"+I("h^2=24-8=16")+"、"+I("h=4")+"。</p>"+D(r"\triangle BCD=\dfrac12\cdot2\sqrt6\cdot2\sqrt6\cdot\dfrac{\sqrt3}2=6\sqrt3,\ V=\dfrac13\cdot6\sqrt3\cdot4=8\sqrt3")+D(r"S=24\sqrt3,\ 8\sqrt3=\dfrac13\cdot24\sqrt3\cdot r\Rightarrow r=1"),
  r"h=4,\ V=8\sqrt3,\ r=1",2),
 (r"\text{直方体}\ ABCD\text{-}EFGH\ \text{で}\ AB=2,\ AD=3,\ AE=5\ \text{のとき},\ \triangle AFH\ \text{の面積と}\ E\ \text{から平面}\ AFH\ \text{への垂線の長さを求めよ。}",
  "<p>"+I("AF=\\sqrt{4+25}=\\sqrt{29}")+"、"+I("AH=\\sqrt{9+25}=\\sqrt{34}")+"、"+I("FH=\\sqrt{4+9}=\\sqrt{13}")+"。余弦定理：</p>"+D(r"\cos\angle FAH=\dfrac{29+34-13}{2\sqrt{29}\sqrt{34}}=\dfrac{50}{2\sqrt{986}}=\dfrac{25}{\sqrt{986}}")+"<p>"+I("\\sin^2\\angle FAH=1-\\dfrac{625}{986}=\\dfrac{361}{986}")+"、"+I("\\sin\\angle FAH=\\dfrac{19}{\\sqrt{986}}")+"。</p>"+D(r"S=\dfrac12\cdot\sqrt{29}\sqrt{34}\cdot\dfrac{19}{\sqrt{986}}=\dfrac12\cdot\sqrt{986}\cdot\dfrac{19}{\sqrt{986}}=\dfrac{19}2")+"<p>"+I("V=\\dfrac13\\cdot\\left(\\dfrac12\\cdot2\\cdot3\\right)\\cdot5=5")+"、"+I("5=\\dfrac13\\cdot\\dfrac{19}2\\cdot h")+" より "+I("h=\\dfrac{30}{19}")+"。</p>",
  r"S=\dfrac{19}2,\ h=\dfrac{30}{19}",3),
 (r"\text{底面が1辺}\ 6\ \text{の正方形},\ \text{側辺}\ \sqrt{34}\ \text{の正四角錐の高さ},\ \text{体積},\ \text{表面積を求めよ。}",
  "<p>"+I("AH=3\\sqrt2")+"、"+I("OH^2=34-18=16")+"、高さ "+I("4")+"。"+I("V=\\dfrac13\\cdot36\\cdot4=48")+"。</p><p>斜高："+I("OM^2=34-9=25")+"、"+I("OM=5")+"。側面1つ "+I("\\dfrac12\\cdot6\\cdot5=15")+"。</p>"+D(r"\text{表面積}=36+4\cdot15=96"),
  r"\text{高さ}\ 4,\ V=48,\ \text{表面積}\ 96",4),
 (r"\triangle ABC\ \text{で}\ AB=5,\ AC=9,\ BC=10\ \text{のとき},\ BC\ \text{の中点を}\ M\ \text{として}\ AM\ \text{を求めよ。}",
  "<p>"+I("\\cos B=\\dfrac{25+100-81}{2\\cdot5\\cdot10}=\\dfrac{44}{100}=\\dfrac{11}{25}")+"。"+I("BM=5")+"：</p>"+D(r"AM^2=25+25-2\cdot5\cdot5\cdot\dfrac{11}{25}=50-22=28\ \Rightarrow\ AM=2\sqrt7"),
  r"AM=2\sqrt7",5)]
out=cycq(3,3,5,8); assert abs(out[0]-60)<1e-9 and abs(out[1]-7)<1e-9 and abs(out[2]-39*r3/4)<1e-9
out=tetra(2*r6); assert abs(out[0]-4)<1e-9 and abs(out[1]-8*r3)<1e-9 and abs(out[2]-1)<1e-9
out=cuboid_coord(2,3,5); assert abs(out[0]-9.5)<1e-9 and abs(out[1]-30/19)<1e-9
out=pyramid(6,math.sqrt(34)); assert abs(out[0]-4)<1e-9 and abs(out[1]-48)<1e-9 and abs(out[2]-96)<1e-9
assert abs(med(5,9,10)-2*r7)<1e-9

UNIT=dict(subject="1",ci=3,ui=2,chapter="図形と計量",name="図形の面積・空間図形の計量",
  intro="円に内接する四角形、正四面体、直方体の切断、正四角錐、中線の長さなど、図形の面積・空間図形の難問に挑みます。",
  examples=EXS,chapter_end=CHE)
