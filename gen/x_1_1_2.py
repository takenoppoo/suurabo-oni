# -*- coding: utf-8 -*-
from bh import *
Z=U_(); CH=[]
R=sp.Rational
def F(e): return sp.factor(e)
# 6 因数定理


def subs_txt(cs,r):
    """多項式の係数 cs（高次→低次）に x=r を代入した式を、項ごとに書き出す"""
    n=len(cs)-1; rr=str(r) if r>=0 else "(%d)"%r; parts=[]
    for i,c in enumerate(cs):
        k=n-i
        if k==0: t="%d"%c
        else:
            base=rr if k==1 else "%s^{%d}"%(rr,k)
            t=base if c==1 else ("-"+base if c==-1 else "%d\\cdot %s"%(c,base))
        parts.append(t)
    return "+".join(parts).replace("+-","-")
def synth(cs,r,e,dv):
    """組立除法の表を、1列ずつ書き出す"""
    row2=[]; row3=[cs[0]]
    for c_ in cs[1:]:
        row2.append(row3[-1]*r); row3.append(c_+row2[-1])
    q=row3[:-1]; rem=row3[-1]; assert rem==0
    head=["係数"]+["\\(%d\\)"%c_ for c_ in cs]
    t=wtable([""]+["\\(%d\\)"%c_ for c_ in cs],[["\\(%d\\) を下ろしてかける"%r,""]+["\\(%d\\)"%v for v in row2],["たして下へ"]+["\\(%d\\)"%v for v in row3]])
    qe=sp.expand(sp.quo(e,dv,x))
    return ("<p>"+I(L(e))+" を "+I(L(dv))+" でわる。係数を並べ、左に "+I("%d"%r)+" をおく。</p>"+t+
      "<p>左から順に「<b>たす → "+I("%d"%r)+" をかける → 次の列へ</b>」をくり返す。いちばん右（余り）が "+I("0")+"、残りが商の係数。</p>"+
      D(r"%s=(%s)(%s)"%(L(e),L(dv),L(qe))))
def b6(r1,r2,r3,a):
    e=sp.expand(a*(x-r1)*(x-r2)*(x-r3)); 
    cs=[e.coeff(x,i) for i in (3,2,1,0)]
    assert F(e)==sp.factor(a*(x-r1)*(x-r2)*(x-r3))
    st=[("因数定理で1つ見つける","<p>定数項の約数から候補を探す。"+I("x=%d"%r1)+" を代入すると</p>"+D(r"P(%d)=%s=%d"%(r1,subs_txt(cs,r1),e.subs(x,r1)))+"<p>0 なので "+I("x-%s"%L(r1) if r1>=0 else "x+%s"%L(-r1))+" を因数にもつ。</p>"),
        ("組立除法で割る",synth(cs,r1,e,x-r1)),
        ("商をさらに因数分解",D(r"%s=%s"%(L(sp.expand(sp.quo(e,x-r1,x))),L(F(sp.quo(e,x-r1,x)))))+D(r"%s=%s"%(L(e),L(F(e)))))]
    return r"$%s$ を因数分解せよ。"%L(e),st,L(F(e))
o=[b6(*v) for v in [(1,2,3,1),(-1,2,-3,1),(2,-3,4,1),(1,-2,-5,2),(3,-1,-4,1)]]
build(Z,CH,"3次式の因数分解（因数定理）",o,r"<p>$P(\alpha)=0$ なら $(x-\alpha)$ が因数。<b>定数項の約数 ÷ 最高次の係数の約数</b>を $\alpha$ の候補に代入し、見つけたら割り算して2次式にする。</p>","まず1つ「当たり」を引き当てる。あとは割り算で一気に楽になる。",6)
# 7 複2次式
def b7(m,n):
    c=2*m-n**2; e=x**4+c*x**2*y**2+m**2*y**4; fct=(x**2+n*x*y+m*y**2)*(x**2-n*x*y+m*y**2); assert sp.expand(fct-e)==0
    st=[("平方の形をつくる","<p>"+I(r"y^4")+" の項は "+I(r"(%s y^2)^2"%L(m))+"、"+I(r"x^4=(x^2)^2")+"。中央の項が "+I(r"2\cdot x^2\cdot %sy^2=%sx^2y^2"%(L(m),L(2*m)))+" になるように足し引きする。</p>"+D(r"(x^2+%sy^2)^2=x^4+%sx^2y^2+%sy^4"%(L(m),L(2*m),L(m**2)))+"<p>与式の "+I(r"x^2y^2")+" の項は "+I(r"%sx^2y^2=%sx^2y^2-%sx^2y^2"%(L(c),L(2*m),L(n**2)))+" と書けるので</p>"+D(r"%s=(x^2+%sy^2)^2-%sx^2y^2"%(L(e),L(m),L(n**2)))),
        ("平方の差にする",D(r"=(x^2+%sy^2)^2-(%sxy)^2"%(L(m),L(n)))),
        ("公式 $A^2-B^2$",D(r"=(x^2+%sxy+%sy^2)(x^2-%sxy+%sy^2)"%(L(n),L(m),L(n),L(m))))]
    return r"$%s$ を因数分解せよ。"%L(e),st,L(fct) if False else r"(x^2+%sxy+%sy^2)(x^2-%sxy+%sy^2)"%(L(n),L(m),L(n),L(m))
o=[b7(*v) for v in [(3,2),(2,1),(5,3),(4,2),(6,4)]]
build(Z,CH,"複2次式（平方の差に直す）",o,r"<p>$x^4+ax^2y^2+b^2y^4$ は $(x^2\pm by^2)^2$ に直して<b>中央の項を足し引き</b>し、$A^2-B^2$ の形にする。</p>","平方をつくるために同じ量を足して引く。値は変わらない。",7)
# 8 6次
def b8(c):
    e=x**6-c**6; f=(x-c)*(x+c)*(x**2+c*x+c**2)*(x**2-c*x+c**2); assert sp.expand(f-e)==0
    st=[("$A^2-B^2$ を使う","<p>"+I("x^6=(x^3)^2")+"、"+I("%d^6=(%d^3)^2"%(c,c))+"。</p>"+D(r"x^6-%d=(x^3-%d)(x^3+%d)"%(c**6,c**3,c**3))),
        ("3乗の公式","<p>"+I(r"A^3-B^3=(A-B)(A^2+AB+B^2)")+"、"+I(r"A^3+B^3=(A+B)(A^2-AB+B^2)")+" を使う（"+I("A=x,\\ B=%d"%c)+"）。</p>"+D(r"x^3-%d=(x-%d)(x^2+%dx+%d),\qquad x^3+%d=(x+%d)(x^2-%dx+%d)"%(c**3,c,c,c**2,c**3,c,c,c**2))),
        ("まとめる",D(r"x^6-%d=(x-%d)(x+%d)(x^2+%dx+%d)(x^2-%dx+%d)"%(c**6,c,c,c,c**2,c,c**2)))]
    return r"$x^6-%d$ を因数分解せよ。"%c**6,st,r"(x-%d)(x+%d)(x^2+%dx+%d)(x^2-%dx+%d)"%(c,c,c,c**2,c,c**2)
o=[b8(c) for c in [2,3,1+1+1+1,5,6]]
build(Z,CH,"6次式（平方の差と3乗の公式）",o,r"<p>$x^6-a^6$ は<b>まず $A^2-B^2$</b>（$A=x^3$）で2つに分け、次に $A^3\pm B^3$ の公式でさらに分ける。$2$次式 $x^2\pm ax+a^2$ はこれ以上分けられない。</p>","先に大きく2つに割り、次に細かく割る。順番を逆にすると見つけにくい。",8)
# 9 置き換え→さらに因数分解
def b9(u,v,w):
    # (x^2+ax)^2 + b(x^2+ax) + c, with x^2+ax+p=(x+u)(x+v), other x^2+ax+q root w
    a_=u+v; p_=u*v; q_=w  # other factor x^2+a x+q
    e=sp.expand((x**2+a_*x+p_)*(x**2+a_*x+q_)); X=sp.Symbol('X'); bb=-(p_+q_)*0
    T_=x**2+a_*x; coef_b=p_+q_; coef_c=p_*q_
    fct=F(e); 
    st=[("かたまりで置き換える","<p>"+I("X=%s"%L(T_))+" とおく。</p>"+D(r"%s=X^2%s"%(L(e) if False else r"(%s)^2%s%s"%(L(T_),("+" if coef_b>=0 else "")+L(coef_b)+"("+L(T_)+")",("+" if coef_c>=0 else "")+L(coef_c)),("+" if coef_b>=0 else "")+L(coef_b)+"X"+("+" if coef_c>=0 else "")+L(coef_c)))),
        ("$X$ で因数分解",D(r"X^2%s%sX%s%s=(X+%s)(X+%s)"%("","+"+L(coef_b) if coef_b>=0 else L(coef_b),"+" if coef_c>=0 else "",L(coef_c),L(p_),L(q_)) if False else r"X^2%+dX%+d=(X%+d)(X%+d)"%(coef_b,coef_c,p_,q_))),
        ("$X$ をもどし、さらに分解",D(r"(%s)(%s)=%s"%(L(x**2+a_*x+p_),L(x**2+a_*x+q_),L(fct))))]
    return r"$%s$ を因数分解せよ。"%(r"(%s)^2%+d(%s)%+d"%(L(T_),coef_b,L(T_),coef_c)),st,L(fct)
o=[b9(*v) for v in [(1,2,5),(1,3,6),(2,3,-4),(1,4,7),(2,2,-3)]]
build(Z,CH,"置き換えのあと、さらに因数分解",o,r"<p>共通のかたまり $X=x^2+ax$ で2次式にする。因数分解後は <b>$X$ をもどし、さらに因数分解できる因数がないか</b>を必ず確かめる。</p>","置き換えは通過点。ゴールまで、もどしてもう一度チェック。",9)
# 10 n^4+4
def b10(n):
    v=n**4+4; f1=n*n+2*n+2; f2=n*n-2*n+2; assert f1*f2==v
    fa=sp.factorint(v); txt=r"\times".join(str(p)+("^{%d}"%e if e>1 else "") for p,e in sorted(fa.items()))
    st=[("式を $n$ で表す","<p>"+I("n^4+4=(n^2)^2+4")+"。平方をつくって差にする。</p>"+D(r"n^4+4=(n^2+2)^2-4n^2=(n^2+2n+2)(n^2-2n+2)")),
        ("$n=%d$ を代入"%n,D(r"%d^4+4=(%d+%d+2)(%d-%d+2)=%d\times%d"%(n,n*n,2*n,n*n,2*n,f1,f2))),
        ("さらに素因数分解","<p>"+I("%d=%s"%(f1,r"\times".join(str(p) for p,e in sp.factorint(f1).items() for _ in range(e))))+"、"+I("%d=%s"%(f2,r"\times".join(str(p) for p,e in sp.factorint(f2).items() for _ in range(e))))+"。</p>"+D(r"%d=%s"%(v,txt)))]
    return r"$%d^4+4$ を素因数分解せよ。"%n,st,r"%d=%s"%(v,txt)
o=[b10(n) for n in [5,9,11,13,15]]
build(Z,CH,"因数分解を使った素因数分解",o,r"<p>$n^4+4=(n^2+2n+2)(n^2-2n+2)$ を覚えるのではなく、<b>平方をつくって差にする</b>手順で導く。数値を入れたあと、各因数が素数かどうかを確認する。</p>","大きな数は、まず式の形で割ってから数に直す。",10)
XU=finishx(Z,CH)
