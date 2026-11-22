# -*- coding: utf-8 -*-
from bh import *
import math
Z=U_(); CH=[]; R=sp.Rational; x,u=sp.symbols("x u")
def chk(F,f): assert sp.simplify(sp.diff(F,x)-f)==0
def co(c): return "" if c==1 else ("-" if c==-1 else L(c))
# 6 置換積分 √
def b6(a,b,n):
    f=x*sp.sqrt(a*x+b); F=sp.integrate(f,x); chk(F,f)
    A=co(a); r_=a*x+b; base=r"%sx+%d"%(A,b)
    g=sp.expand(R(2,a*a)*(u**2-b)*u**2); G=sp.integrate(g,u)
    Fn=R(2,15*a*a)*(3*a*x-2*b)*(a*x+b)**R(3,2); assert sp.simplify(Fn-F)==0 or sp.simplify(sp.diff(Fn,x)-f)==0
    st=[("置換を決める","<p>根号の中身を文字にする。</p>"+D(r"u=\sqrt{%s}"%base)+"<p>両辺を2乗して "+I("x")+" を "+I("u")+" で表す。</p>"+D(r"u^2=%s\ \Rightarrow\ x=\dfrac{u^2-%d}{%d}"%(base,b,a) if a!=1 else r"u^2=%s\ \Rightarrow\ x=u^2-%d"%(base,b))),
        ("$dx$ を $u$ で表す","<p>"+I(r"u^2=%s"%base)+" の両辺を微分する。</p>"+D(r"2u\,du=%s\,dx\ \Rightarrow\ dx=%s\,du"%(co(a),r"\dfrac{2u}{%d}"%a if a!=1 else "2u"))),
        ("$u$ の式に書きかえる","<p>"+D(r"\int x\sqrt{%s}\,dx=\int\dfrac{u^2-%d}{%d}\cdot u\cdot\dfrac{2u}{%d}\,du"%(base,b,a,a) if a!=1 else r"\int x\sqrt{%s}\,dx=\int(u^2-%d)\cdot u\cdot2u\,du"%(base,b))+"<p>係数をまとめ、"+I("u")+" の累乗を整理する。</p>"+D(r"=%s\int(u^2-%d)u^2\,du=%s\int(u^4-%su^2)\,du"%(L(R(2,a*a)) if a!=1 else "2",b,L(R(2,a*a)) if a!=1 else "2",co(b)) if b!=0 else "")),
        ("積分する","<p>"+I(r"\int u^ndu=\dfrac{u^{n+1}}{n+1}")+" を使う。</p>"+D(r"=%s\left(\dfrac{u^5}{5}-\dfrac{%su^3}{3}\right)+C=%s+C"%(L(R(2,a*a)) if a!=1 else "2",co(b),L(G)))),
        ("$x$ に戻す","<p>"+I("u^3")+" でくくり、"+I(r"u^2=%s"%base)+" を使う。</p>"+D(r"=%s\,u^3\left(\dfrac{u^2}{5}-\dfrac{%d}{3}\right)=%s\,u^3\cdot\dfrac{3u^2-%d}{15}"%(L(R(2,a*a)) if a!=1 else "2",b,L(R(2,a*a)) if a!=1 else "2",5*b))+"<p>"+I(r"u^2=%s"%base)+"、"+I(r"u^3=(%s)\sqrt{%s}"%(base,base))+" を入れる。</p>"+D(r"3u^2-%d=3(%s)-%d=%s"%(5*b,base,5*b,L(3*a*x+3*b-5*b)))+D(r"=%s(%s)\sqrt{%s}\,(%s)+C"%(L(R(2,15*a*a)),base,base,L(3*a*x-2*b)))+"<p>（"+I(r"(%s)\sqrt{%s}=(%s)^{\frac32}"%(base,base,base))+"）</p>")]
    return r"不定積分 $\displaystyle\int x\sqrt{%s}\,dx$ を求めよ。"%base,st,r"%s(%s)\sqrt{%s}\,(%s)+C"%(L(R(2,15*a*a)),base,base,L(3*a*x-2*b))
o=[b6(*v,1) for v in [(1,1),(2,1),(1,4),(3,1),(2,3)]]
build(Z,CH,"x√(ax+b) の置換積分",o,"<p>根号の中身を $u=\\sqrt{ax+b}$ とおき、$x$ と $dx$ を $u$ で表す。多項式の積分になる。</p>","ルートを文字に置き換えれば、ただの多項式。",6)
# 7 部分分数の積分
def b7(a,b):
    f=1/((x-a)*(x-b)); A=R(1,a-b); B=R(1,b-a)
    def lg(p): return r"\log|x%s|"%("-%d"%p if p>0 else ("" if p==0 else "+%d"%(-p)))
    def fa(p): return "x" if p==0 else ("x-%d"%p if p>0 else "x+%d"%(-p))
    st=[("部分分数に分ける","<p>"+D(r"\dfrac1{(%s)(%s)}=\dfrac{A}{%s}+\dfrac{B}{%s}"%(fa(a),fa(b),fa(a),fa(b)))+"<p>両辺に "+I(r"(%s)(%s)"%(fa(a),fa(b)))+" をかけて分母をはらう。</p>"+D(r"1=A(%s)+B(%s)"%(fa(b),fa(a)))),
        ("$A,B$ を求める","<p>"+I("x=%d"%a)+" を代入すると "+I("B")+" の項が消える。</p>"+D(r"1=A(%d-%s)\ \Rightarrow\ 1=%sA\ \Rightarrow\ A=%s"%(a,("(%d)"%b if b<0 else str(b)),L(a-b),L(A)))+"<p>"+I("x=%d"%b)+" を代入すると "+I("A")+" の項が消える。</p>"+D(r"1=B(%d-%s)\ \Rightarrow\ 1=%sB\ \Rightarrow\ B=%s"%(b,("(%d)"%a if a<0 else str(a)),L(b-a),L(B)))+D(r"\dfrac1{(%s)(%s)}=%s\left(\dfrac1{%s}-\dfrac1{%s}\right)"%(fa(a),fa(b),L(A),fa(a),fa(b)))),
        ("項ごとに積分","<p>"+I(r"\int\dfrac{dx}{x-p}=\log|x-p|")+" を使う。</p>"+D(r"\int\dfrac1{%s}dx=%s,\qquad\int\dfrac1{%s}dx=%s"%(fa(a),lg(a),fa(b),lg(b)))+D(r"%s\left(%s-%s\right)+C"%(L(A),lg(a),lg(b)))),
        ("対数をまとめる","<p>"+I(r"\log|P|-\log|Q|=\log\left|\dfrac PQ\right|")+" を使う。</p>"+D(r"%s\log\left|\dfrac{%s}{%s}\right|+C"%(L(A),fa(a),fa(b))))]
    return r"不定積分 $\displaystyle\int\dfrac{dx}{(%s)(%s)}$ を求めよ。"%(fa(a),fa(b)),st,r"%s\log\left|\dfrac{%s}{%s}\right|+C"%(L(A),fa(a),fa(b))
o=[b7(*v) for v in [(3,1),(2,-1),(5,2),(4,0),(1,-2)]]
build(Z,CH,"1/((x−a)(x−b)) の積分（部分分数）",o,"<p>部分分数に分けて $\\int\\dfrac{dx}{x-a}=\\log|x-a|$ を使う。係数は $\\dfrac1{a-b}$。</p>","分母が積なら、2つの分数の差に分ける。",7)
# 8 部分積分2回
def b8(a,kind):
    f=sp.exp(a*x)*(sp.sin(x) if kind=="sin" else sp.cos(x)); den=a*a+1
    F=sp.exp(a*x)*((a*sp.sin(x)-sp.cos(x)) if kind=="sin" else (a*sp.cos(x)+sp.sin(x)))/den; chk(F,f)
    E="e^{x}" if a==1 else "e^{%dx}"%a
    fa="" if a==1 else r"\dfrac1{%d}"%a; fa2="" if a==1 else r"\dfrac1{%d}"%(a*a)
    s=r"\sin x"; c=r"\cos x"
    ans=r"%s(%s%s-%s)"%(E,co(a),s,c) if kind=="sin" else r"%s(%s%s+%s)"%(E,co(a),c,s)
    T="P" if kind=="sin" else "Q"; Tn=s if kind=="sin" else c
    CD=r"\cdot"
    st=[]
    st.append(("おくものを決める","<p>"+I(r"P=\int %s%s\,dx"%(E,s))+"、"+I(r"Q=\int %s%s\,dx"%(E,c))+" とおく。求めたいのは "+I(T)+"。"+I(E)+" を積分する側にして、"+I("P")+" と "+I("Q")+" をそれぞれ部分積分する。</p>"+D(r"\int %s\,dx=%s%s"%(E,fa,E))))
    st.append(("$P$ を部分積分","<p>"+I(r"f=\sin x,\ f'=\cos x,\ g=%s%s"%(fa,E))+"。</p>"+D(r"P=%s%s\sin x-\int\cos x%s\,dx=%s%s\sin x-%sQ"%(fa,E,CD+fa+E if fa else r"\," +E,fa,E,fa))))
    st.append(("$Q$ を部分積分","<p>"+I(r"f=\cos x,\ f'=-\sin x,\ g=%s%s"%(fa,E))+"。</p>"+D(r"Q=%s%s\cos x-\int(-\sin x)%s\,dx=%s%s\cos x+%sP"%(fa,E,CD+fa+E if fa else r"\," +E,fa,E,fa))))
    if kind=="sin":
        sub=D(r"P=%s%s\sin x-%s\left(%s%s\cos x+%sP\right)"%(fa,E,fa,fa,E,fa)); mv=D(r"P+%sP=%s%s\sin x-%s%s\cos x"%(fa2,fa,E,fa2,E)); 
        mul=D(r"%d P+P=%s\sin x-%s\cos x"%(a*a,L(a)+E if a!=1 else E,E) if a!=1 else r"2P=%s\sin x-%s\cos x"%(E,E))
    else:
        sub=D(r"Q=%s%s\cos x+%s\left(%s%s\sin x-%sQ\right)"%(fa,E,fa,fa,E,fa)); mv=D(r"Q+%sQ=%s%s\cos x+%s%s\sin x"%(fa2,fa,E,fa2,E))
        mul=D(r"%d Q+Q=%s\cos x+%s\sin x"%(a*a,L(a)+E if a!=1 else E,E) if a!=1 else r"2Q=%s\cos x+%s\sin x"%(E,E))
    if a==1: mv=mv.replace(r"+P=","+P=").replace(r"P+P",r"P+P").replace("P+"+fa2+"P","P+P").replace("Q+"+fa2+"Q","Q+Q")
    st.append(("$%s$ だけの式にする"%T,"<p>"+I("P" if kind=="sin" else "Q")+" の式に、もう一方の式を代入し、かっこをはずす。</p>"+sub+"<p>"+I(T)+" を含む項を左辺に集める。</p>"+mv))
    rhs=(r"%s(%s%s-%s)"%(E,co(a),s,c)) if kind=="sin" else (r"%s(%s%s+%s)"%(E,co(a),c,s))
    st.append(("$%s$ について解く"%T,"<p>"+("両辺に "+I(L(a*a))+" をかけて分数をなくす。" if a!=1 else "左辺は "+I("2"+T)+"。")+"</p>"+D(r"%s\,%s=%s"%("(%d+1)"%(a*a) if a!=1 else "2",T,rhs))+"<p>両辺を "+I(L(den))+" でわる。</p>"+D(r"%s=\dfrac{%s}{%d}+C"%(T,ans,den))))
    return r"不定積分 $\displaystyle\int %s%s\,dx$ を求めよ。"%(E,Tn),st,r"\dfrac{%s}{%d}+C"%(ans,den)
o=[b8(1,"sin"),b8(2,"sin"),b8(1,"cos"),b8(3,"sin"),b8(2,"cos")]
build(Z,CH,"e^{ax}sin x, e^{ax}cos x の積分（部分積分2回）",o,"<p>部分積分を<b>2回</b>行うと元の積分 $J$ が現れ、$J=\\cdots-cJ$ の形になる。$J$ について解く。</p>","同じ積分が戻ってきたら、方程式として解く。",8)
def polystr(poly,var):
    """u の多項式 poly を var 文字（\\cos x など）の式に"""
    P=sp.Poly(poly,u); out=""
    for (k,),cf in sorted(P.terms(),key=lambda t:-t[0][0]):
        t=(var if k==1 else r"%s^{%d}"%(var.replace("x",""),k)+"x") if k>0 else ""
        body=("" if abs(cf)==1 and k>0 else L(abs(cf)))+t if k>0 else L(abs(cf))
        out+=("-" if cf<0 else ("+" if out else ""))+body
    return out
def fr(c,k,v): # 係数 c の c u^k を表示
    return ("" if c==1 else L(c))+(v if k==1 else r"%s^{%d}x"%(v[:-2],k))
# 9 sin と cos の累乗
def b9(p,q):
    f=sp.sin(x)**p*sp.cos(x)**q; F=sp.integrate(f,x); chk(F,f)
    odd_s=(p%2==1)
    if odd_s: m=(p-1)//2; w=r"\cos x"; wn=r"\cos"; h=sp.expand((1-u**2)**m*u**q); sg=-1
    else: m=(q-1)//2; w=r"\sin x"; wn=r"\sin"; h=sp.expand((1-u**2)**m*u**p); sg=1
    H=sp.integrate(h,u)*sg
    def term(cf,k,first):
        bd=("" if abs(cf)==1 else L(abs(cf)))+(w if k==1 else r"%s^{%d}x"%(wn,k))
        return ("-" if cf<0 else ("" if first else "+"))+bd
    ans="".join(term(cf,k,i==0) for i,((k,),cf) in enumerate(sorted(sp.Poly(sp.expand(H),u).terms(),key=lambda t:-t[0][0])))
    if odd_s:
        st=[("置換を決める","<p>"+I(r"\sin")+" の指数 "+I(str(p))+" が奇数なので、"+I(r"\sin x")+" を1つ取り出し、"+I(r"u=\cos x")+" とおく。</p>"+D(r"\dfrac{du}{dx}=-\sin x\ \Rightarrow\ \sin x\,dx=-du")),
            ("残りを $\\cos x$ で表す","<p>"+D(r"\sin^{%d}x=\sin^{%d}x\cdot\sin x=(\sin^2x)^{%d}\sin x=(1-\cos^2x)^{%d}\sin x"%(p,p-1,m,m) if m>0 else r"\sin^{%d}x=\sin x"%p)+"<p>したがって</p>"+D(r"\int\sin^{%d}x\cos^{%d}x\,dx=\int(1-\cos^2x)^{%d}\cos^{%d}x\cdot\sin x\,dx"%(p,q,m,q) if m>1 else (r"\int\sin^{%d}x\cos^{%d}x\,dx=\int(1-\cos^2x)\cos^{%d}x\cdot\sin x\,dx"%(p,q,q) if m==1 else r"\int\sin x\cos^{%d}x\,dx"%q))),
            ("$u$ の式にする","<p>"+I(r"\cos x=u,\ \sin x\,dx=-du")+" を代入する。</p>"+D(r"=-\int(1-u^2)^{%d}u^{%d}\,du"%(m,q) if m>0 else r"=-\int u^{%d}\,du"%q)+"<p>展開して "+I("u")+" の多項式にする。</p>"+D(r"=-\int\left(%s\right)du"%L(h))),
            ("積分する","<p>各項に "+I(r"\int u^ndu=\dfrac{u^{n+1}}{n+1}")+" を使う。</p>"+D(r"=-\left(%s\right)+C"%L(sp.integrate(h,u)))+D(r"=%s+C"%L(H))),
            ("$x$ に戻す","<p>"+I(r"u=\cos x")+" を戻す。</p>"+D(r"=%s+C"%ans))]
    else:
        st=[("置換を決める","<p>"+I(r"\cos")+" の指数 "+I(str(q))+" が奇数なので、"+I(r"\cos x")+" を1つ取り出し、"+I(r"u=\sin x")+" とおく。</p>"+D(r"\dfrac{du}{dx}=\cos x\ \Rightarrow\ \cos x\,dx=du")),
            ("残りを $\\sin x$ で表す","<p>"+D(r"\cos^{%d}x=(\cos^2x)^{%d}\cos x=(1-\sin^2x)^{%d}\cos x"%(q,m,m))+"<p>したがって</p>"+D(r"\int\sin^{%d}x\cos^{%d}x\,dx=\int\sin^{%d}x(1-\sin^2x)^{%d}\cdot\cos x\,dx"%(p,q,p,m))),
            ("$u$ の式にする","<p>"+I(r"\sin x=u,\ \cos x\,dx=du")+" を代入し、展開する。</p>"+D(r"=\int u^{%d}(1-u^2)^{%d}du=\int\left(%s\right)du"%(p,m,L(h)))),
            ("積分する","<p>各項に "+I(r"\int u^ndu=\dfrac{u^{n+1}}{n+1}")+" を使う。</p>"+D(r"=%s+C"%L(H))),
            ("$x$ に戻す","<p>"+I(r"u=\sin x")+" を戻す。</p>"+D(r"=%s+C"%ans))]
    sp_=r"\sin^{%d}x"%p if p>1 else r"\sin x"; cq_=r"\cos^{%d}x"%q if q>1 else r"\cos x"
    return r"不定積分 $\displaystyle\int %s%s\,dx$ を求めよ。"%(sp_,cq_),st,r"%s+C"%ans
o=[b9(*v) for v in [(3,2),(2,3),(3,1),(1,4),(5,2)]]
build(Z,CH,"sin と cos の累乗の積の積分",o,"<p>奇数乗の方を1つ分離して $\\sin x\\,dx=-d(\\cos x)$ などと置換し、残りを $\\sin^2+\\cos^2=1$ で一方に統一。</p>","奇数乗は、1つだけ取り出すと置換の手がかりになる。",9)
# 10 ∫tan x 型
def b10(a):
    A=co(a) if a!=1 else ""; f=sp.tan(a*x)
    st=[("$\\tan$ を $\\sin,\\cos$ で表す","<p>"+D(r"\tan %sx=\dfrac{\sin %sx}{\cos %sx}"%(A,A,A))),
        ("分母を微分する","<p>"+I(r"(\cos %sx)'=-%s\sin %sx"%(A,A if a!=1 else "",A))+" なので、分子 "+I(r"\sin %sx"%A)+" は "+I(r"(\cos %sx)'"%A)+" の "+I(r"-\dfrac1{%d}"%a if a!=1 else "-1")+" 倍。</p>"+D(r"\sin %sx=-\dfrac1{%d}\cdot(\cos %sx)'"%(A,a,A) if a!=1 else r"\sin x=-(\cos x)'")),
        ("積分の形に直す","<p>"+D(r"\int\tan %sx\,dx=-\dfrac1{%d}\int\dfrac{(\cos %sx)'}{\cos %sx}dx"%(A,a,A,A) if a!=1 else r"\int\tan x\,dx=-\int\dfrac{(\cos x)'}{\cos x}dx")),
        ("公式を使う","<p>"+I(r"\int\dfrac{g'}{g}dx=\log|g|+C")+" より、</p>"+D(r"=-\dfrac1{%d}\log|\cos %sx|+C"%(a,A) if a!=1 else r"=-\log|\cos x|+C"))]
    return r"不定積分 $\displaystyle\int\tan %sx\,dx$ を求めよ。"%A,st,r"-\dfrac1{%d}\log|\cos %sx|+C"%(a,A) if a!=1 else r"-\log|\cos x|+C"
o=[b10(a) for a in [1,2,3,4,5]]
build(Z,CH,"tan ax の積分",o,"<p>$\\tan ax=\\dfrac{\\sin ax}{\\cos ax}$ と書き、分母の導関数が $-a\\sin ax$ であることから $\\int\\dfrac{f'}{f}=\\log|f|$ を使う。</p>","分子が分母の微分の形なら、対数になる。",10)
XU=finishx(Z,CH)
