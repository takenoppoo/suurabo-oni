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
# 9 p<x<q の範囲に解をただ1つもつ
def b9(p,q):
    a=sp.Symbol('a'); A=sp.Rational
    fp=sp.expand(p*p-2*a*p+3*a-2); fq=sp.expand(q*q-2*a*q+3*a-2)
    c1,c0=fp.coeff(a,1),fp.coeff(a,0); d1,d0=fq.coeff(a,1),fq.coeff(a,0)
    r1,r2=sorted([A(-c0)/c1,A(-d0)/d1]); assert r1!=r2
    inside=(c1*d1>0)
    ANS=(r"%s<a<%s"%(L(r1),L(r2))) if inside else (r"a<%s,\ \ %s<a"%(L(r1),L(r2)))
    def good(v):
        f=x**2-2*v*x+3*v-2; return f.subs(x,p)*f.subs(x,q)<0
    a0=next((sp.Integer(v) for v in range(-10,11) if good(sp.Integer(v))),None)
    if a0 is None: a0=(r1+r2)/2
    f0=x**2-2*a0*x+3*a0-2; r0=sorted(sp.solve(f0,x))
    fg=quadfig("x133_9_%d_%d"%(p+9,q+9),[(f0,"#b81f36")],[(p,f0.subs(x,p),"x=%d"%p),(q,f0.subs(x,q),"x=%d"%q),(r0[0],0,""),(r0[1],0,"")])
    ineq=D(r"f(%d)\,f(%d)=(%s)(%s)<0"%(p,q,L(fp),L(fq)))
    st=[("$f(x)$ とおく","<p>"+I(r"f(x)=x^2-2ax+3a-2")+" とおく。"+I("x^2")+" の係数が正（下に凸）。"+I("%d<x<%d"%(p,q))+" の範囲に解がただ1つあるとき、"+I("x=%d"%p)+" と "+I("x=%d"%q)+" では "+I("f(x)")+" の符号が逆になる。</p>"+D(r"f(%d)\,f(%d)<0"%(p,q))+"<p>例として "+I("a=%s"%L(a0))+" のグラフ。"+I("x=%d"%p)+" と "+I("x=%d"%q)+" の間で解（"+I("x")+" 軸との交点）が1つ、範囲の外にもう1つある。</p>"+fg),
        ("$f(%d),\\ f(%d)$ を求める"%(p,q),D(r"f(%d)=%d-%da+3a-2=%s"%(p,p*p,2*p,L(fp)))+D(r"f(%d)=%d-%da+3a-2=%s"%(q,q*q,2*q,L(fq)))),
        ("不等式にする",ineq),
        ("解く","<p>左辺が0になるのは "+I("a=%s"%L(r1))+"、"+I("a=%s"%L(r2))+"。"+I("a^2")+" の係数が"+("正" if inside else "負")+"なので、"+("0より小さいのは2つの値の間。" if inside else "0より小さいのは2つの値の外側。")+"</p>"+D(ANS))]
    return r"2次方程式 $x^2-2ax+3a-2=0$ が、$%d$ より大きく $%d$ より小さい範囲に、解をただ1つだけもつような定数 $a$ の範囲を求めよ。"%(p,q),st,ANS
o=[b9(*v) for v in [(1,2),(0,1),(-1,0),(2,3),(-1,1)]]
build(Z,CH,"ある範囲に解をただ1つもつ条件",o,r"<p>$f(x)$ が連続なので、$p<x<q$ に解がただ1つあるとき <b>$f(p)$ と $f(q)$ の符号が逆</b>、すなわち $f(p)f(q)<0$。</p>","両端で符号が逆なら、間でx軸を横切る。",9)
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
