# -*- coding: utf-8 -*-
from bh import *
Z=U_(); CH=[]; R=sp.Rational; x,y,z=sp.symbols("x y z")
def b6(p,q,r_):
    a,b,c=sp.symbols("a b c")
    lhs=a*(x-1)*(x-2)+b*(x-1)*(x-3)+c*(x-2)*(x-3); rhs=p*x**2+q*x+r_
    sol=sp.solve([sp.expand(lhs-rhs).coeff(x,i) for i in range(3)],[a,b,c],dict=True)[0]
    # numerator values: x=1: c*(-1)(-2)=2c ; x=2: b*(1)(-1)=-b ; x=3: a*2*1=2a
    assert sol[c]==R(p+q+r_,2) and sol[a]==R(9*p+3*q+r_,2) and sol[b]==-(4*p+2*q+r_)
    st=[("両辺に分母をかける","<p>"+I(r"\dfrac{%s}{(x-1)(x-2)(x-3)}=\dfrac{a}{x-1}+\dfrac{b}{x-2}+\dfrac{c}{x-3}"%L(rhs))+" の分母をはらう。</p>"+D(r"%s=a(x-2)(x-3)+b(x-1)(x-3)+c(x-1)(x-2)"%L(rhs))),
        ("数値代入法","<p>"+I("x=1,2,3")+" を代入すると、それぞれ1つの文字だけ残る。</p>"+D(r"x=1:\ %d=2a\quad x=2:\ %d=-b\quad x=3:\ %d=2c"%(rhs.subs(x,1),rhs.subs(x,2),rhs.subs(x,3)))),
        ("答え",D(r"a=%s,\ b=%s,\ c=%s"%(L(sol[a]),L(sol[b]),L(sol[c]))))]
    # fix: note 'a' at x=1 : a(−1)(−2)=2a
    return r"$\dfrac{%s}{(x-1)(x-2)(x-3)}=\dfrac{a}{x-1}+\dfrac{b}{x-2}+\dfrac{c}{x-3}$ が $x$ についての恒等式となるように $a,b,c$ を定めよ。"%L(rhs),st,r"a=%s,\ b=%s,\ c=%s"%(L(sol[a]),L(sol[b]),L(sol[c]))
o=[b6(*v) for v in [(1,2,3),(2,-1,4),(3,0,5),(1,-3,2),(4,1,-2)]]
build(Z,CH,"3つの部分分数への分解（数値代入法）",o,"<p>分母をはらって<b>整式の恒等式</b>にし、分母を 0 にする $x$ を代入。1つの文字だけが残る。</p>","わざと分母を0にする値を代入して、1つずつ片づける。",6)
def b7(k):
    # a+b+c=0 ... prove a^3+b^3+c^3=3abc
    a,b=sp.symbols("a b"); c=-a-b
    assert sp.expand(a**3+b**3+c**3-3*a*b*c)==0
    st=[("$c$ を消去","<p>"+I("a+b+c=0")+" より "+I("c=-(a+b)")+"。</p>"),
        ("代入して展開","<p>"+D(r"a^3+b^3-(a+b)^3=-3ab(a+b)=3ab\cdot c")+"</p>"),
        ("結論","<p>"+I("a^3+b^3+c^3=3abc")+"。"+("このとき "+I(r"a=%d,\ b=%d,\ c=%d"%(k,k+1,-2*k-1))+" で確認：左辺 "+I(str(k**3+(k+1)**3+(-2*k-1)**3))+"、右辺 "+I(str(3*k*(k+1)*(-2*k-1)))+"。")+"</p>")]
    assert k**3+(k+1)**3+(-2*k-1)**3==3*k*(k+1)*(-2*k-1)
    return r"$a+b+c=0$ のとき、$a^3+b^3+c^3=3abc$ を証明せよ。",st,r"\text{証明終}"
o=[b7(k) for k in [1,2,3,4,5]]
build(Z,CH,"条件つき等式の証明（立方の和）",o,"<p>条件 $a+b+c=0$ で<b>文字を1つ消去</b>してから展開すると、両辺が一致する。</p>","条件で1文字減らせば、あとは展開だけ。",7)
def b8(a,b):
    # prove x^2+y^2 >= 2xy style with weight: a x^2 + b y^2 >= 2 sqrt(ab) xy ; use concrete: x^2+y^2+1>=x+y+xy
    f=lambda u,v:u*u+v*v+1-u-v-u*v
    st=[("差をとる","<p>"+D(r"x^2+y^2+1-(x+y+xy)\ \ \text{ を2倍して平方の和に}")),
        ("平方の和","<p>"+D(r"2(x^2+y^2+1-x-y-xy)=(x-y)^2+(x-1)^2+(y-1)^2\geqq0")),
        ("等号","<p>"+I("x=y=1")+" のとき成り立つ。</p>")]
    return r"すべての実数 $x,\ y$ について $x^2+y^2+1\geqq x+y+xy$ が成り立つことを証明せよ。また等号が成り立つときを求めよ。",st,r"x=y=1"
o=[b8(0,0)]*5
# vary: different inequalities
def mk(title_ineq,lhs_minus_rhs_x2,sq_text,eq_text):
    st=[("差をとる","<p>左辺 $-$ 右辺 を作る。</p>"+D(title_ineq)),("平方の和に直す","<p>"+D(sq_text)+"</p>"),("等号成立",D(eq_text))]
    return st
cases=[
 (r"x^2+y^2+1\geqq x+y+xy",r"2(x^2+y^2+1-x-y-xy)=(x-y)^2+(x-1)^2+(y-1)^2\geqq0",r"x=y=1",lambda x,y:x*x+y*y+1-x-y-x*y),
 (r"x^2+2y^2+2xy+2y+1\geqq0 ",r"x^2+2y^2+2xy+2y+1=(x+y)^2+(y+1)^2\geqq0",r"x+y=0,\ y=-1\ \text{すなわち }(x,y)=(1,-1)",lambda x,y:x*x+2*y*y+2*x*y+2*y+1),
 (r"a^2+b^2+c^2\geqq ab+bc+ca",r"2(a^2+b^2+c^2-ab-bc-ca)=(a-b)^2+(b-c)^2+(c-a)^2\geqq0",r"a=b=c",lambda a,b,c=0:0),
 (r"x^2-4xy+5y^2+2y+1 \geqq0",r"x^2-4xy+5y^2+2y+1=(x-2y)^2+(y+1)^2\geqq0",r"y=-1,\ x=-2",lambda x,y:x*x-4*x*y+5*y*y+2*y+1),
 (r"4x^2+y^2+2\geqq 4x+2y -\,0",r"4x^2+y^2+2-4x-2y=(2x-1)^2+(y-1)^2\geqq0",r"x=\dfrac12,\ y=1",lambda x,y:4*x*x+y*y+2-4*x-2*y)]
import itertools,random
random.seed(1)
for i,(ineq,sq,eq,f) in enumerate(cases):
    if i==2: continue
    for _ in range(100):
        u,v=random.randint(-9,9),random.randint(-9,9); assert f(u,v)>=0
def bb(i):
    ineq,sq,eq,f=cases[i]
    st=[("差をとる","<p>（左辺）$-$（右辺）を作り、平方の和にできるか考える。</p>"),("平方の和に直す",D(sq)),("等号成立",D(eq))]
    stmt=r"次の不等式を証明せよ。等号が成り立つ条件も答えよ。$%s$"%ineq
    return stmt,st,r"\text{証明終。等号は }%s"%eq
o=[bb(i) for i in range(5)]
build(Z,CH,"差をとって平方の和にする不等式の証明",o,"<p>（左辺）$-$（右辺）$\\geqq0$ を示す。<b>平方完成・平方の和</b>に直せば、各項が $\\geqq0$ から結論。等号は各平方が 0 のとき。</p>","マイナスにならない部品（2乗）だけで組み立てる。",8)
def b9(a,b):
    # min of x + a/x? use  x+ b/(x-1)  x>1 : =(x-1)+b/(x-1)+1 >= 2sqrt(b)+1 ; b perfect square
    s=int(b**.5); assert s*s==b
    mn=2*s+1
    import numpy as np
    xs=np.linspace(1.001,60,200000); assert abs((xs+b/(xs-1)).min()-mn)<1e-3
    st=[("形を整える","<p>"+I("x-1>0")+" に注意して</p>"+D(r"x+\dfrac{%d}{x-1}=(x-1)+\dfrac{%d}{x-1}+1"%(b,b))),
        ("相加・相乗平均","<p>"+D(r"(x-1)+\dfrac{%d}{x-1}\geqq2\sqrt{%d}=%d"%(b,b,2*s))),
        ("最小値","<p>等号は "+I(r"x-1=\dfrac{%d}{x-1}"%b)+"、つまり "+I("x=%d"%(s+1))+"。</p>"+D(r"\text{最小値 }%d"%mn))]
    return r"$x>1$ のとき、$x+\dfrac{%d}{x-1}$ の最小値と、そのときの $x$ の値を求めよ。"%b,st,r"x=%d\ \text{のとき最小値 }%d"%(s+1,mn)
o=[b9(0,b) for b in [4,9,16,25,36]]
build(Z,CH,"x+k/(x−1) の最小値（相加・相乗平均）",o,"<p>$x-1=t>0$ とおいて<b>積が定数になる形</b>に変形。$t+\\dfrac{k}{t}\\geqq2\\sqrt k$。等号条件 $t=\\sqrt k$ も確認。</p>","和の最小は、2つが等しいとき。",9)
def b10(a):
    # x+y=a, x,y>0: max of xy = a^2/4 ; min of 1/x+1/y = 4/a
    st=[("相加・相乗平均","<p>"+D(r"%d=x+y\geqq2\sqrt{xy}\ \Longrightarrow\ xy\leqq\dfrac{%d}{4}=%s"%(a,a*a,L(R(a*a,4))))),
        ("逆数の和","<p>"+D(r"\dfrac1x+\dfrac1y=\dfrac{x+y}{xy}=\dfrac{%d}{xy}\geqq\dfrac{%d}{%s}=%s"%(a,a,L(R(a*a,4)),L(R(4,a))))),
        ("等号","<p>"+I(r"x=y=%s"%L(R(a,2)))+" のとき。</p>")]
    return r"$x>0,\ y>0,\ x+y=%d$ のとき、$xy$ の最大値と $\dfrac1x+\dfrac1y$ の最小値を求めよ。"%a,st,r"xy\text{の最大値 }%s,\ \ \dfrac1x+\dfrac1y\text{の最小値 }%s"%(L(R(a*a,4)),L(R(4,a)))
o=[b10(a) for a in [6,10,8,12,14]]
build(Z,CH,"和が一定のときの積の最大・逆数和の最小",o,"<p>和が一定 $\\Rightarrow$ <b>積に相加・相乗平均</b>。逆数の和は $\\dfrac{x+y}{xy}$ と通分して利用。</p>","和が決まっているとき、等しく分けると積が最大。",10)
XU=finishx(Z,CH)
