# -*- coding: utf-8 -*-
# 恒等式・等式の証明・不等式の証明（数学II いろいろな式）
from bh import *
Z=U_(); CH=[]
A_,B_,C_,D_=sp.symbols('a b c d')
# ===== 例題1 恒等式の係数決定（係数比較） =====
def b1(Pp,s):
    rhs=A_*(x-s)**3+B_*(x-s)**2+C_*(x-s)+D_
    sol=sp.solve(sp.Poly(sp.expand(rhs-Pp),x).all_coeffs(),[A_,B_,C_,D_],dict=True)[0]
    ex=sp.expand(rhs); cs=sp.Poly(ex,x).all_coeffs(); ps=sp.Poly(sp.expand(Pp),x).all_coeffs()
    eqs=[L(cc)+"="+L(pp) for cc,pp in zip(cs,ps)]
    assert sp.expand(rhs.subs(sol)-Pp)==0
    ans=r"a=%s,\ b=%s,\ c=%s,\ d=%s"%tuple(L(sol[v]) for v in (A_,B_,C_,D_))
    steps=[("右辺を展開して $x$ について整理する",D(r"\begin{aligned}\text{右辺}&=a(x-%d)^3+b(x-%d)^2+c(x-%d)+d\\ &="%(s,s,s)+L(ex)[0:0]+r"%s\end{aligned}"%L(sp.collect(ex,x)))),
           ("両辺の係数を比べる","<p>恒等式なので、両辺の各次数の係数が等しい。</p>"+D(r"\begin{cases}"+r"\\ ".join(["x^3:\\ "+eqs[0],"x^2:\\ "+eqs[1],"x^1:\\ "+eqs[2],"x^0:\\ "+eqs[3]])+r"\end{cases}")),
           ("上から順に解く",D(r"a=%s,\quad b=%s,\quad c=%s,\quad d=%s"%tuple(L(sol[v]) for v in (A_,B_,C_,D_)))+"<p>確かめ：右辺に代入して展開すると左辺と一致する。</p>")]
    prob=r"等式 $"+L(Pp)+"=a(x-%d)^3+b(x-%d)^2+c(x-%d)+d$ が $x$ についての恒等式となるように、定数 $a,b,c,d$ の値を定めよ。"%(s,s,s)
    return prob,steps,ans
V=[(2*x**3-3*x**2+5*x+1,2),(x**3+4*x**2-x+6,1),(3*x**3-x**2+2*x-5,-1),(2*x**3+x**2-4*x+3,3),(4*x**3-5*x**2+x+2,-2)]
o=[b1(*v) for v in V]
build(Z,CH,"恒等式の係数決定（係数比較）",o,
 r"<p>$x$ についての<b>恒等式</b>とは、$x$ にどんな値を入れても成り立つ等式。両辺を整理して<b>同じ次数の係数を比べる</b>（係数比較法）。または適当な値を代入する（数値代入法）。</p>",
 "恒等式は「どの $x$ で見ても同じ姿」。両辺が同じ多項式だから、係数も1つずつ一致する。",1)
# ===== 例題2 分数式の恒等式 =====
def b2(p_,q_,al,be):
    num=p_*x+q_; sol=sp.solve(sp.Poly(sp.expand(A_*(x-be)+B_*(x-al)-num),x).all_coeffs(),[A_,B_],dict=True)[0]
    assert sp.simplify(sol[A_]/(x-al)+sol[B_]/(x-be)-num/((x-al)*(x-be)))==0
    steps=[("両辺に分母 $(x-%d)(x-%d)$ を掛けて分母を払う"%(al,be) if False else "分母を払う",D(L(num)+"=a"+P(x-be)+"+b"+P(x-al))),
           ("右辺を展開して $x$ で整理する",D(L(num)+"="+L(sp.collect(sp.expand(A_*(x-be)+B_*(x-al)),x)))),
           ("係数を比べて連立方程式を解く",D(r"\begin{cases}x:\ a+b=%d\\ \text{定数項}:\ %s=%d\end{cases}"%(p_,L(-be*A_-al*B_),q_))+"<p>解くと</p>"+D(r"a=%s,\quad b=%s"%(L(sol[A_]),L(sol[B_])))),
           ("別解（数値代入法）","<p>"+I("x=%d"%al)+" を代入：「"+I(str(p_*al+q_)+"=a("+str(al-be)+")")+"」より "+I("a=%s"%L(sol[A_]))+"。"+I("x=%d"%be)+" を代入：「"+I(str(p_*be+q_)+"=b("+str(be-al)+")")+"」より "+I("b=%s"%L(sol[B_]))+"。</p>")]
    prob=r"等式 $"+fr(L(num),"("+L(x-al)+")("+L(x-be)+")")+"="+fr("a",L(x-al))+"+"+fr("b",L(x-be))+r"$ が $x$ についての恒等式となるように、定数 $a,b$ の値を定めよ。"
    return prob,steps,r"a=%s,\ b=%s"%(L(sol[A_]),L(sol[B_]))
V=[(5,1,1,-2),(7,-4,2,-1),(3,10,-3,2),(9,-3,1,4),(4,-9,3,-1)]
o=[b2(*v) for v in V]
build(Z,CH,"分数式の恒等式（部分分数分解）",o,
 r"<p>分母を払って<b>整式の恒等式</b>に直す。次に係数比較か数値代入で $a,b$ を決める。分母の因数 $x-\alpha$ を 0 にする値 $x=\alpha$ を代入すると、一方の文字だけが残って速い。</p>",
 "分母が邪魔なら、両辺に分母を掛けて消す。消えたら、あとは整式の恒等式。",2)
# ===== 例題3 条件つき等式の証明 =====
def b3(Lh,Rh,name):
    f=lambda e:sp.expand(e.subs(C_,-A_-B_))
    l,r_=f(Lh),f(Rh); assert sp.expand(l-r_)==0
    steps=[("条件を使って文字を1つ減らす","<p>"+I("a+b+c=0")+" より "+I("c=-a-b")+"。これを両辺に代入する。</p>"),
           ("左辺を展開する",D(r"\text{左辺}="+L(Lh.subs(C_,-A_-B_))+"="+L(l))),
           ("右辺を展開する",D(r"\text{右辺}="+L(Rh.subs(C_,-A_-B_))+"="+L(r_))),
           ("結論","<p>左辺 "+I("=")+" 右辺。（証明終）</p>")]
    prob=r"$a+b+c=0$ のとき、等式 $"+L(Lh)+"="+L(Rh)+r"$ が成り立つことを証明せよ。"
    return prob,steps,r"\text{（左辺）}=\text{（右辺）}\quad\text{（証明終）}"
a_,b_,c_=A_,B_,C_
V=[(a_**3+b_**3+c_**3,3*a_*b_*c_),(a_**2-b_*c_,b_**2-c_*a_),((a_+b_)*(b_+c_)*(c_+a_),-a_*b_*c_),((a_**2+b_**2+c_**2)**2,2*(a_**4+b_**4+c_**4)),(a_**2+a_*b_+b_**2,b_**2+b_*c_+c_**2)]
o=[b3(*v,"") for v in V]
Z.ex("条件つき等式の証明（文字消去）",o[0][0],
 r"<p>条件式があるときは、<b>文字を1つ消去</b>して証明する。$a+b+c=0$ なら $c=-a-b$ を両辺に代入し、<b>左辺と右辺をそれぞれ展開</b>して同じ式になることを示す。</p>",
 "条件は「文字を減らす道具」。1文字消えれば、あとは機械的な展開だけ。",
 o[0][1],o[0][2],[z[0] for z in o[1:4]],[(flat(z[1]),z[2]) for z in o[1:4]])
CH.append((o[4][0],flat(o[4][1]),o[4][2],3))
# ===== 例題4 不等式の証明（差をとる） =====
def b4(Lh,Rh,dec,eqc,vars_):
    diff=sp.expand(Lh-Rh); assert sp.expand(diff-dec)==0
    steps=[("左辺 $-$ 右辺 を計算する",D(r"\text{左辺}-\text{右辺}="+L(Lh)+"-"+P(Rh)+"="+L(diff))),
           ("平方の和（または平方）に変形する",D(L(diff)+"="+L(dec if not hasattr(dec,'args') else dec).replace("",""))),
           ("0以上であることを示す","<p>実数の平方は 0 以上なので、上の式は 0 以上。よって 左辺 "+I(r"\geqq")+" 右辺。</p>"),
           ("等号が成り立つ条件","<p>"+eqc+"</p>")]
    return steps
def mkpf(Lh,Rh,decTex,eqc):
    diff=sp.expand(Lh-Rh)
    steps=[("左辺 $-$ 右辺 を計算する",D(r"\text{左辺}-\text{右辺}="+L(diff))),
           ("平方の和（または平方）に変形する",D(L(diff)+"="+decTex)),
           ("0以上であることを示す","<p>実数の平方は 0 以上なので、上の式は 0 以上。よって 左辺 "+I(r"\geqq")+" 右辺。</p>"),
           ("等号が成り立つ条件","<p>"+eqc+"</p>")]
    return steps
def pf(Lh,Rh,dec,decTex,eqc):
    assert sp.expand(Lh-Rh-dec)==0
    return r"$"+L(Lh)+r"\geqq "+L(Rh)+r"$ を証明せよ。ただし文字はすべて実数とし、等号が成り立つときの条件も答えよ。",mkpf(Lh,Rh,decTex,eqc),r"\text{（証明終）}\ \ \text{等号成立：}"+eqc.replace("<br>","")
x_,y_,z_=sp.symbols('x y z')
e1=(a_**2+b_**2+c_**2,a_*b_+b_*c_+c_*a_,R(1,2)*((a_-b_)**2+(b_-c_)**2+(c_-a_)**2),r"\dfrac12\left\{(a-b)^2+(b-c)^2+(c-a)^2\right\}","$a=b=c$ のとき。")
e2=(a_**2+b_**2+1,a_*b_+a_+b_,R(1,2)*((a_-b_)**2+(a_-1)**2+(b_-1)**2),r"\dfrac12\left\{(a-b)^2+(a-1)^2+(b-1)^2\right\}","$a=b=1$ のとき。")
e3=((a_**2+b_**2)*(x_**2+y_**2),(a_*x_+b_*y_)**2,(a_*y_-b_*x_)**2,r"(ay-bx)^2","$ay=bx$ のとき。")
e4=(a_**2+b_**2+c_**2+3,2*(a_+b_+c_),(a_-1)**2+(b_-1)**2+(c_-1)**2,r"(a-1)^2+(b-1)^2+(c-1)^2","$a=b=c=1$ のとき。")
e5=(4*a_**2+9*b_**2+c_**2,6*a_*b_+2*b_*c_*0+4*a_*c_*0+0,None,None,None)
e5=(a_**2+2*b_**2+2*c_**2,2*a_*b_+2*b_*c_,(a_-b_)**2+(b_-c_)**2+c_**2*0+b_**2*0+0,None,None)
# e5 を確かめて正しい形に
e5L=a_**2+2*b_**2+c_**2; e5R=2*a_*b_+2*b_*c_; e5d=(a_-b_)**2+(b_-c_)**2; assert sp.expand(e5L-e5R-e5d)==0
e5=(e5L,e5R,e5d,r"(a-b)^2+(b-c)^2","$a=b=c$ のとき。")
o=[pf(*e) for e in (e1,e2,e3,e4,e5)]
Z.ex("不等式の証明（差をとって平方の和にする）",o[0][0],
 r"<p>不等式 $A\geqq B$ の証明は <b>$A-B\geqq0$ を示す</b>のが基本。差を展開して<b>平方の和</b>の形に直せば、「実数の平方は 0 以上」から結論が出る。等号は、すべての平方が 0 になるとき。</p>",
 "「差がマイナスにならない」ことを見せる。2乗は絶対にマイナスにならないので、2乗の形に持ち込む。",
 o[0][1],o[0][2],[z[0] for z in o[1:4]],[(flat(z[1]),z[2]) for z in o[1:4]])
CH.append((o[4][0],flat(o[4][1]),o[4][2],4))
# ===== 例題5 相加平均・相乗平均 =====
def b5(p_,q_,s):
    u=sp.symbols('u',positive=True); f=p_*x+q_/(x-s)
    mn=2*sp.sqrt(p_*q_)+p_*s; x0=s+sp.sqrt(sp.Rational(q_,p_)); assert sp.simplify(sp.diff(f,x).subs(x,x0))==0 and sp.simplify(f.subs(x,x0)-mn)==0
    sr=sp.sqrt(p_*q_)
    steps=[("積が定数になるように変形する","<p>"+I("x>%d"%s)+" より "+I("x-%d>0"%s)+"。"+I("u=x-%d"%s)+" とおくと "+I("u>0")+"。</p>"+D(L(f)+"="+L(p_)+"u+"+fr(str(q_),"u")+("+%d"%(p_*s) if p_*s>0 else ("%d"%(p_*s) if p_*s<0 else "")))),
           ("相加・相乗平均の不等式を使う","<p>"+I("u>0,\\ \\frac{q}{u}>0")+r" だから、$A+B\geqq2\sqrt{AB}$ より</p>"+D(L(p_)+"u+"+fr(str(q_),"u")+r"\geqq 2\sqrt{%d u\cdot\dfrac{%d}{u}}=2\sqrt{%d}=%s"%(p_,q_,p_*q_,L(2*sr)))),
           ("最小値",D(L(f)+r"\geqq %s%s=%s"%(L(2*sr),("+%d"%(p_*s) if p_*s>0 else ("%d"%(p_*s) if p_*s<0 else "")),L(mn)))),
           ("等号が成り立つ条件","<p>"+I("%du=\\dfrac{%d}{u}"%(p_,q_))+" すなわち "+I("u^2=%s"%L(sp.Rational(q_,p_)))+"、"+I("u=%s"%L(sp.sqrt(sp.Rational(q_,p_))))+"（"+I("u>0")+" を満たす）。よって "+I("x=%s"%L(x0))+" のとき最小。</p>")]
    prob=r"$x>%d$ のとき、$%s$ の最小値と、そのときの $x$ の値を求めよ。"%(s,L(f)) 
    return prob,steps,r"x=%s\ \text{のとき最小値 }%s"%(L(x0),L(mn))
V=[(1,4,1),(2,18,0),(3,12,2),(4,9,-1),(5,20,3)]
o=[b5(*v) for v in V]
build(Z,CH,"相加・相乗平均で最小値を求める",o,
 r"<p>$A>0,\ B>0$ のとき $$\dfrac{A+B}{2}\geqq\sqrt{AB}\quad(\text{等号は }A=B)$$ 積 $AB$ が<b>定数</b>になるように式を変形して使う。等号が成り立つ $x$ が範囲に入っているかを必ず確認する。</p>",
 "和が最小になるのは2つがつり合うとき。シーソーが水平になる点が最小。",5)
UNIT=finish(Z,CH,0,2,"いろいろな式","恒等式・等式の証明・不等式の証明","恒等式の係数決定、部分分数、条件つき等式の証明、不等式の証明、相加・相乗平均の最小値まで、式変形の力を試します。")
