# -*- coding: utf-8 -*-
# 剰余定理・因数定理・高次方程式（数学II いろいろな式）
from bh import *
Z=U_(); CH=[]
# ===== 例題1 剰余定理（2次式で割った余り） =====
def b1(al,ra,be,rb):
    u=sp.Rational(ra-rb,al-be); v=ra-u*al; assert u*be+v==rb
    Rm=u*x+v
    steps=[("余りを1次式でおく","<p>2次式で割った余りは1次以下。商を "+I("Q(x)")+"、余りを "+I("ax+b")+" とおくと</p>"+D(r"P(x)=(x%+d)(x%+d)Q(x)+ax+b"%(-al,-be))),
           ("剰余定理を使って条件を式にする","<p>"+I("P(x)")+" を "+I("x%+d"%(-al))+" で割った余りは "+I("P(%d)=%d"%(al,ra))+"。上の式に "+I("x=%d"%al)+" を代入すると "+I("(x%+d)"%(-al))+" の項が消えて</p>"+D(r"P(%d)=%da+b=%d"%(al,al,ra))+"<p>同様に "+I("x=%d"%be)+" を代入して</p>"+D(r"P(%d)=%da+b=%d"%(be,be,rb))),
           ("連立方程式を解く",D(r"\begin{cases}%da+b=%d\\ %da+b=%d\end{cases}"%(al,ra,be,rb))+"<p>辺々引くと "+I("%da=%d"%(al-be,ra-rb))+"、"+I("a=%s"%L(u))+"。"+I("b=%d-(%d)\\cdot(%s)=%s"%(ra,al,L(u),L(v)))+"。</p>")]
    prob=r"整式 $P(x)$ を $x%+d$ で割ると余りが $%d$、$x%+d$ で割ると余りが $%d$ である。$P(x)$ を $(x%+d)(x%+d)$ で割ったときの余りを求めよ。"%(-al,ra,-be,rb,-al,-be)
    return prob,steps,r"\text{余り }"+L(Rm)
V=[(1,3,-2,-3),(2,5,-1,-4),(3,7,1,1),(-1,2,4,-8),(2,-3,-3,12)]
o=[b1(*v) for v in V]
build(Z,CH,"剰余定理（2次式で割った余り）",o,
 r"<p><b>剰余定理</b>：整式 $P(x)$ を $x-\alpha$ で割った余りは $P(\alpha)$。2次式で割るときは余りを $ax+b$ とおき、割る式の2つの因数の値 $\alpha,\beta$ を代入して $a,b$ の連立方程式にする。</p>",
 "商の部分は $x=\\alpha$ を入れると $0$ になって消える。残るのは余りだけ。",1)
# ===== 例題2 因数定理で係数決定 =====
def b2(r1,r2,r3):
    cc=-r1*r2*r3
    ee=sp.expand((x-r1)*(x-r2)*(x-r3)); a_=ee.coeff(x,2); b_=ee.coeff(x,1)
    A_,B_=sp.symbols('A B'); Pp=x**3+A_*x**2+B_*x+cc
    sol=sp.solve([Pp.subs(x,r1),Pp.subs(x,r2)],[A_,B_],dict=True)[0]; assert sol[A_]==a_ and sol[B_]==b_
    e1=sp.expand(Pp.subs(x,r1)); e2=sp.expand(Pp.subs(x,r2))
    steps=[("因数定理で2つの式を作る","<p>"+I("P(x)")+" が "+I("x%+d"%(-r1))+" で割り切れる "+I(r"\iff P(%d)=0"%r1)+"。同様に "+I("P(%d)=0"%r2)+"。</p>"+D(r"\begin{cases}P(%d)=%d+a\cdot(%d)+b\cdot(%d)+(%d)=0\\ P(%d)=%d+a\cdot(%d)+b\cdot(%d)+(%d)=0\end{cases}"%(r1,r1**3,r1**2,r1,cc,r2,r2**3,r2**2,r2,cc))),
           ("連立方程式を解く","<p>整理して</p>"+D(r"\begin{cases}%s=0\\ %s=0\end{cases}"%(L(e1),L(e2)))+"<p>これを解いて</p>"+D(r"a=%d,\quad b=%d"%(a_,b_))),
           ("$P(x)$ を因数分解して方程式を解く","<p>"+I("P(x)=%s"%L(ee))+"。"+I("x%+d"%(-r1))+"、"+I("x%+d"%(-r2))+" を因数にもつので、定数項の積から残りの因数が決まる。</p>"+D(r"P(x)=(x%+d)(x%+d)(x%+d)"%(-r1,-r2,-r3))+"<p>（確かめ：定数項 "+I("(%d)(%d)(%d)=%d"%(-r1,-r2,-r3,cc))+" と一致）よって "+I("P(x)=0")+" の解は "+I("x=%d,\\ %d,\\ %d"%(r1,r2,r3))+"。</p>")]
    prob=r"整式 $P(x)=x^3+ax^2+bx%+d$ が $x%+d$ でも $x%+d$ でも割り切れるとき、定数 $a,\ b$ の値を求めよ。また、方程式 $P(x)=0$ を解け。"%(cc,-r1,-r2)
    return prob,steps,r"a=%d,\ b=%d,\quad x=%d,\ %d,\ %d"%(a_,b_,r1,r2,r3)
V=[(1,-2,3),(2,-1,3),(1,3,-4),(-2,2,3),(1,-3,-2)]
o=[b2(*v) for v in V]
build(Z,CH,"因数定理で係数を決める",o,
 r"<p><b>因数定理</b>：$P(x)$ が $x-\alpha$ で割り切れる $\iff P(\alpha)=0$。割り切れる条件を式にして、係数の連立方程式を解く。わかった後は、因数分解して方程式を解く。</p>",
 "割り切れる＝余りが0＝代入して0。条件が1つ増えるごとに、式が1本できる。",2)
# ===== 例題3 3次方程式（組立除法） =====
def rtex(z): return L(z) if sp.im(z)==0 else cx(sp.re(z),sp.im(z))
def b3(r,p_,q_):
    cs=[int(c_) for c_ in sp.Poly(sp.expand((x-r)*(x**2+p_*x+q_)),x).all_coeffs()]
    tex,qq,rem=synth_tex(cs,r); assert rem==0
    disc=p_**2-4*q_; assert disc!=0
    rts=sp.solve(x**2+p_*x+q_,x)
    Pe=sp.Poly(cs,x).as_expr(); Qe=sp.Poly(qq,x).as_expr()
    cands=sorted(set([d for d in range(1,abs(cs[-1])+1) if cs[-1]%d==0]+[-d for d in range(1,abs(cs[-1])+1) if cs[-1]%d==0]))
    ev="+".join(("(%d)\\cdot(%d)^{%d}"%(c_,r,len(cs)-1-i)) if i<len(cs)-1 else "(%d)"%c_ for i,c_ in enumerate(cs))
    sols=[str(r)]+[rtex(z) for z in rts]
    steps=[("解の候補をしぼる","<p>整数の解があれば、定数項 "+I(str(cs[-1]))+" の約数のどれか。候補："+I(r",\ ".join(str(c_) for c_ in cands))+"。順に代入して "+I("P(x)=0")+" になるものを探す。</p>"+D("P(%d)="%r+ev+"=0")+"<p>"+I("P(%d)=0"%r)+" なので "+I("x%+d"%(-r))+" は因数。</p>"),
           ("組立除法で割る","<p>係数 "+I(r",\ ".join(str(c_) for c_ in cs))+" を "+I("x=%d"%r)+" で組立除法する。</p>"+D(tex)+"<p>商は "+I(L(Qe))+"、余り 0。</p>"+D(L(Pe)+"=(x%+d)(%s)"%(-r,L(Qe)))),
           ("2次方程式を解く","<p>"+I("%s=0"%L(Qe))+" を解の公式で解く。判別式 "+I("D=(%d)^2-4\\cdot(%d)=%d"%(p_,q_,disc))+"。</p>"+D(r"x=\dfrac{%d\pm\sqrt{%d}}{2}=%s"%(-p_,disc,r",\ ".join(rtex(z) for z in rts)))),
           ("答え","<p>解は "+I(r"x=%s"%r",\ ".join(sols))+"。</p>")]
    prob=r"3次方程式 $"+L(Pe)+r"=0$ を解け。（複素数の範囲で）"
    return prob,steps,r"x=%s"%r",\ ".join(sols)
V=[(1,-2,5),(2,2,3),(-1,-4,5),(3,0,4),(-2,1,2)]
o=[b3(*v) for v in V]
build(Z,CH,"3次方程式（因数定理＋組立除法）",o,
 r"<p>高次方程式は<b>因数定理</b>で1つの解を見つけ、<b>組立除法</b>で次数を下げる。整数解の候補は<b>定数項の約数</b>（最高次の係数が1のとき）。残った2次方程式は解の公式、虚数解も含めて解く。</p>",
 "1つ解が見つかれば、あとは2次方程式。まず「当たり」を1つ見つけるのが最大の山場。",3)
# ===== 例題4 複2次式 =====
def b4(t1,t2):
    eq=x**4-(t1+t2)*x**2+t1*t2; assert sp.expand((x**2-t1)*(x**2-t2)-eq)==0
    def rr(t_):
        if t_>0:
            s=sp.sqrt(t_); return [L(s),L(-s)]
        s=sp.sqrt(-t_); return [cx(0,s),cx(0,-s)]
    steps=[("$x^2=X$ とおく","<p>"+I("X^2%+dX%+d=0"%(-(t1+t2),t1*t2))+"。</p>"),
           ("$X$ の2次方程式を因数分解して解く",D(r"(X%+d)(X%+d)=0\ \Rightarrow\ X=%d,\ %d"%(-t1,-t2,t1,t2))),
           ("$x$ に戻す","<p>"+I("x^2=%d"%t1)+" より "+I("x=%s"%r",\ ".join(rr(t1)))+"。<br>"+I("x^2=%d"%t2)+" より "+I("x=%s"%r",\ ".join(rr(t2)))+"。</p>")]
    prob=r"方程式 $"+L(eq)+r"=0$ を解け。（複素数の範囲で）"
    return prob,steps,r"x=%s,\ %s"%(r",\ ".join(rr(t1)),r",\ ".join(rr(t2)))
V=[(1,-4),(4,-9),(2,-3),(9,-1),(-2,5)]
o=[b4(*v) for v in V]
build(Z,CH,"複2次方程式",o,
 r"<p>$x^4+ax^2+b=0$ のように $x^2$ の式になっているときは $x^2=X$ とおいて $X$ の2次方程式にする。$X$ が求まったら、$x^2=X$ を解いて $x$ に戻す。$X<0$ のときは $x=\pm\sqrt{-X}\,i$。</p>",
 "かたまり $x^2$ を1つの文字に置き換えれば、見慣れた2次方程式。解き終わったら、必ず戻す。",4)
# ===== 例題5 虚数解をもつ3次方程式 =====
def b5(a0,b0,s):
    nrm=a0**2+b0**2; cc=-s*nrm; Q=x**2-2*a0*x+nrm; Pp=sp.expand(Q*(x-s)); p_=Pp.coeff(x,2); q_=Pp.coeff(x,1)
    steps=[("共役な複素数も解","<p>係数がすべて実数なので、"+I(cx(a0,b0))+" が解なら共役な "+I(cx(a0,-b0))+" も解。</p>"),
           ("この2解を解にもつ2次式",D(r"(x-(%s))(x-(%s))=(x-%d)^2-(%si)^2=x^2%+dx%+d"%(cx(a0,b0),cx(a0,-b0),a0,b0,-2*a0,nrm))),
           ("3次式を作って定数項を比べる","<p>3つ目の解を "+I("s")+" とおくと</p>"+D(r"x^3+px^2+qx%+d=(x^2%+dx%+d)(x-s)"%(cc,-2*a0,nrm))+"<p>定数項を比べて</p>"+D(r"%d=-s\cdot%d\ \Rightarrow\ s=%d"%(cc,nrm,s))),
           ("展開して係数を比べる",D(r"(x^2%+dx%+d)(x%+d)=%s"%(-2*a0,nrm,-s,L(Pp)))+"<p>したがって "+I("p=%d,\\ q=%d"%(p_,q_))+"。他の解は "+I("x=%d"%s)+" と "+I(cx(a0,-b0))+"。</p>")]
    prob=r"実数 $p,q$ に対して、3次方程式 $x^3+px^2+qx%+d=0$ の1つの解が $%s$ であるとき、$p,q$ の値と他の解を求めよ。"%(cc,cx(a0,b0))
    return prob,steps,r"p=%d,\ q=%d,\quad \text{他の解 }%s,\ %d"%(p_,q_,cx(a0,-b0),s)
V=[(1,2,-2),(2,1,3),(1,1,4),(3,1,-1),(2,3,2)]
o=[b5(*v) for v in V]
build(Z,CH,"虚数解をもつ高次方程式",o,
 r"<p><b>実数係数</b>の方程式が虚数解 $a+bi$ をもつなら、共役な $a-bi$ も解。この2解から2次式 $x^2-2ax+(a^2+b^2)$ ができるので、3次式を（2次式）×（1次式）の形に作って係数を比べる。</p>",
 "虚数解はいつも「ペア」で現れる。ペアで1つの実数係数の2次式になる。",5)
UNIT=finish(Z,CH,0,4,"いろいろな式","剰余定理・因数定理・高次方程式","剰余定理、因数定理、組立除法、複2次方程式、虚数解をもつ高次方程式まで、いろいろな式の総仕上げに挑みます。")
