# -*- coding: utf-8 -*-
from bh import *
from gq import *
Z=U_(); CH=[]
R=sp.Rational
# 6 解の比
def b6(s,m):
    beta=R(s,m+1); alpha=m*beta; k=alpha*beta; assert beta.q==1
    assert sorted(sp.solve(x**2-s*x+k,x))==sorted([alpha,beta])
    st=[("解を文字でおく","<p>解の比が "+I("%d:1"%m)+" なので、解を "+I(r"\alpha=%d\beta"%m)+"、"+I(r"\beta")+" とおく。</p>"),
        ("解と係数の関係","<p>"+I(r"\alpha+\beta=%d"%s)+"、"+I(r"\alpha\beta=k")+"。</p>"+D(r"%d\beta+\beta=%d\ \Rightarrow\ \beta=%s"%(m,s,L(beta)))),
        ("$k$ を求める",D(r"\alpha=%s,\ \ k=\alpha\beta=%s\cdot%s=%s"%(L(alpha),L(alpha),L(beta),L(k)))+"<p>確認：解は "+I("%s,\\ %s"%(L(alpha),L(beta)))+"（実数）。</p>")]
    fg=quadfig("x133_6_%d_%d"%(s,m),[(x**2-s*x+k,"#b81f36")],[(beta,0,"(%s, 0)"%L(beta)),(alpha,0,"(%s, 0)"%L(alpha)),(R(s,2),k-R(s*s,4)*(-1)*0-R(s*s,4)+k-k+0,"")],axis=R(s,2))
    st[0]=(st[0][0],st[0][1]+"<p>2つの解は "+I("x")+" 軸との交点。比が "+I("%d:1"%m)+" になる位置を図で確かめる。</p>"+fg)
    return r"2次方程式 $x^2-%dx+k=0$ の2つの解の比が $%d:1$ であるとき、定数 $k$ の値を求めよ。"%(s,m),st,r"k=%s"%L(k)
o=[b6(*v) for v in [(6,2),(8,3),(10,4),(9,2),(12,3)]]
build(Z,CH,"2つの解の比が与えられたとき",o,r"<p>解を $\alpha=m\beta,\ \beta$ とおいて、<b>解と係数の関係</b>（和）から $\beta$ を求め、積から定数を決める。最後に実数解かを確認。</p>","比は文字ひとつで表す。和から決めて、積に代入。",6)
# 7 解の差
def b7(p,d):
    k=R(p*p-d*d,4); assert sp.discriminant(x**2-p*x+k,x)>0
    r_=sp.solve(x**2-p*x+k,x); assert abs(abs(r_[0]-r_[1])-d)==0
    st=[("差の2乗を作る","<p>"+I(r"(\alpha-\beta)^2=(\alpha+\beta)^2-4\alpha\beta")+"。</p>"+D(r"%d^2=%d^2-4k"%(d,p))),
        ("$k$ を求める",D(r"4k=%d-%d=%d\ \Rightarrow\ k=%s"%(p*p,d*d,p*p-d*d,L(k)))),
        ("実数解の確認","<p>"+I(r"D=%d^2-4\cdot%s=%d>0"%(p,L(k),d*d))+"。</p>")]
    r1_,r2_=sorted(r_)
    fg=quadfig("x133_7_%d_%d"%(p,d),[(x**2-p*x+k,"#b81f36")],[(r1_,0,"α"),(r2_,0,"β")],axis=R(p,2))
    st[0]=(st[0][0],st[0][1]+"<p>2つの解の間の長さ "+I(r"|\alpha-\beta|=%d"%d)+" が、"+I("x")+" 軸から切り取る線分の長さ。</p>"+fg)
    return r"2次方程式 $x^2-%dx+k=0$ の2つの解 $\alpha,\ \beta$ について $|\alpha-\beta|=%d$ となるように、定数 $k$ の値を定めよ。"%(p,d),st,r"k=%s"%L(k)
o=[b7(*v) for v in [(5,3),(7,1),(6,2),(9,5),(8,4)]]
build(Z,CH,"解の差が与えられたとき",o,r"<p>$(\alpha-\beta)^2=(\alpha+\beta)^2-4\alpha\beta$ を使う。$|\alpha-\beta|=d$ の両辺を2乗すれば絶対値が消える。</p>","差は2乗すると、和と積だけで書ける。",7)
# 8 α²,β² を解とする
def b8(p,q):
    s=p*p-2*q; pr=q*q; assert sp.simplify(sp.expand((x-1)*0)+0)==0
    al=sp.Symbol('al'); 
    st=[("基本量","<p>"+I(r"\alpha+\beta=%d,\ \ \alpha\beta=%d"%(p,q))+"。</p>"),
        ("新しい和と積",D(r"\alpha^2+\beta^2=(\alpha+\beta)^2-2\alpha\beta=%d^2-2\cdot%d=%d"%(p,q,s))+D(r"\alpha^2\beta^2=(\alpha\beta)^2=%d^2=%d"%(q,pr))),
        ("2次方程式",D(r"x^2-%dx+%d=0"%(s,pr)))]
    return r"$x^2-%dx+%d=0$ の2つの解を $\alpha,\ \beta$ とするとき、$\alpha^2,\ \beta^2$ を解とする2次方程式を1つ求めよ。"%(p,q),st,r"x^2-%dx+%d=0"%(s,pr)
o=[b8(*v) for v in [(4,1),(5,3),(6,2),(3,1),(7,5)]]
build(Z,CH,"解の式を解とする2次方程式",o,r"<p>新しい2解の<b>和と積</b>を $\alpha+\beta,\ \alpha\beta$ で表し、$x^2-(\text{和})x+(\text{積})=0$ に入れる。</p>","解そのものを求めず、和と積だけで新しい方程式を作る。",8)
# 9 1つは k より大, 1つは小
def b9(kk):
    # x^2 - 2a x + a + 2? choose: x^2 -2ax + 3a -2 = 0 ; roots one >kk one <kk ⇒ f(kk)<0 ⇒ kk^2 -2a kk +3a-2<0
    a=sp.Symbol('a'); ineq=kk**2-2*a*kk+3*a-2
    lin=sp.expand(ineq); c1=lin.coeff(a,1); c0=lin.coeff(a,0)
    sol=sp.solve(ineq<0,a)
    st=[("$f(x)$ とおく","<p>"+I(r"f(x)=x^2-2ax+3a-2")+"。"+I("x^2")+" の係数が正（下に凸）なので、2つの解の間に "+I("x=%d"%kk)+" があるための条件は "+I(r"f(%d)<0"%kk)+"。</p>"),
        ("不等式にする",D(r"f(%d)=%d-%da+3a-2=%s<0"%(kk,kk*kk,2*kk,L(lin)))),
        ("解く",D(r"%s"%sp.latex(sol).replace("\\frac","\\dfrac")))]
    a0=[v_ for v_ in range(-10,11) if (ineq.subs(a,v_)<0)][0]
    f0=x**2-2*a0*x+3*a0-2; r0=sorted(sp.solve(f0,x))
    fg=quadfig("x133_9_%d"%(kk+9),[(f0,"#b81f36")],[(kk,f0.subs(x,kk),"x=%d"%kk),(r0[0],0,""),(r0[1],0,"")],axis=kk)
    st[0]=(st[0][0],st[0][1]+"<p>例として "+I("a=%d"%a0)+" のグラフ。点線の位置 "+I("x=%d"%kk)+" で "+I("f(x)<0")+" になり、解（"+I("x")+" 軸との交点）が両側に1つずつある。</p>"+fg)
    return r"2次方程式 $x^2-2ax+3a-2=0$ が、$%d$ より大きい解と $%d$ より小さい解を1つずつもつような定数 $a$ の範囲を求めよ。"%(kk,kk),st,r"%s"%sp.latex(sol).replace("\\frac","\\dfrac")
o=[b9(v) for v in [1,2,0,3,-1]]
build(Z,CH,"2つの解の間に数がある条件",o,r"<p>下に凸の $f(x)$ で、解の間に $k$ があるのは<b>$f(k)<0$</b>。$D>0$ は自動的に成り立つので、確認は不要。</p>","谷底より上でなく、谷底の下にくる点が2解の間。",9)
# 10 整数解
def b10(N):
    # x^2 + k x + N=0 ; 整数解をもつ整数 k (N>0)
    ks=set()
    for d in sp.divisors(N):
        ks.add(-(d+N//d)); ks.add(d+N//d)
    ks=sorted(ks); 
    # verify
    for kk in ks:
        r_=sp.solve(x**2+kk*x+N,x); assert all(r.is_integer for r in r_)
    st=[("解を整数 $\\alpha,\\beta$ とおく","<p>"+I(r"\alpha\beta=%d,\ \ \alpha+\beta=-k"%N)+"。</p>"),
        ("積が %d となる整数の組"%N,"<p>"+I(r"(\alpha,\beta)=%s"%(r",\ ".join("(%d,%d)"%(d,N//d) for d in sp.divisors(N) if d<=N//d)+","+r",\ ".join("(%d,%d)"%(-d,-N//d) for d in sp.divisors(N) if d<=N//d)))+"。</p>"),
        ("$k=-(\\alpha+\\beta)$","<p>各組の和から "+I(r"k=-(\alpha+\beta)")+" を計算する。</p>"+wtable([I(r"\alpha"),I(r"\beta"),I(r"\alpha+\beta"),I(r"k=-(\alpha+\beta)")],[[I(str(s*d)),I(str(s*(N//d))),I(str(s*(d+N//d))),I(str(-s*(d+N//d)))] for s in (1,-1) for d in sp.divisors(N) if d<=N//d])+"<p>よって "+I(r"k=%s"%(r",\ ".join(str(kk) for kk in ks)))+"。</p>")]
    return r"2次方程式 $x^2+kx+%d=0$ が整数の解をもつような整数 $k$ をすべて求めよ。"%N,st,r"k=%s"%(r",\ ".join(str(kk) for kk in ks))
o=[b10(N) for N in [12,18,20,24,30]]
build(Z,CH,"整数解をもつ条件",o,r"<p>解を整数 $\alpha,\beta$ とおくと $\alpha\beta=$ 定数、$\alpha+\beta=-k$。<b>積が定数になる整数の組</b>（正・負の両方）をすべて挙げ、和から $k$ を出す。</p>","積が決まっているなら、かけ算の組を全部書き出す。",10)
XU=finishx(Z,CH)
