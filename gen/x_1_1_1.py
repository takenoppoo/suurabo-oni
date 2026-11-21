# -*- coding: utf-8 -*-
from bh import *
from math import comb
Z=U_(); CH=[]
R=sp.Rational
# 6 定数項
def b6(a,c,n):
    # (a x^2 + c/x)^n の定数項: C(n,r) a^(n-r) c^r x^(2(n-r)-r)=x^0 → r=2n/3
    r_=2*n//3; assert 2*n%3==0; v=comb(n,r_)*a**(n-r_)*c**r_
    e=sp.expand((a*x**2+c/x)**n); assert e.coeff(x,0)==v
    st=[("一般項を書く",D(r"{}_{%d}\mathrm{C}_{r}(%sx^2)^{%d-r}\left(\dfrac{%s}{x}\right)^{r}={}_{%d}\mathrm{C}_{r}\,%s^{%d-r}%s^{r}\,x^{%d-3r}"%(n,L(a),n,L(c),n,L(a),n,L(c),2*n))),
        ("$x$ の指数を0にする","<p>"+I(r"%d-3r=0"%(2*n))+" より "+I("r=%d"%r_)+"。</p>"),
        ("定数項を計算",D(r"{}_{%d}\mathrm{C}_{%d}\cdot%s^{%d}\cdot%s^{%d}=%d\cdot%d\cdot%d=%d"%(n,r_,L(a),n-r_,L(c),r_,comb(n,r_),a**(n-r_),c**r_,v)))]
    return r"$\left(%sx^2+\dfrac{%s}{x}\right)^{%d}$ の展開式における定数項を求めよ。"%(L(a),L(c),n),st,L(v)
o=[b6(*v) for v in [(1,2,6),(2,1,9),(1,-1,6),(3,1,6),(1,2,9)]]
build(Z,CH,"二項定理（定数項を求める）",o,r"<p>$(a+b)^n$ の一般項 ${}_n\mathrm{C}_ra^{n-r}b^r$ を書き、<b>$x$ の指数が0になる $r$</b> を求める。$x^2$ と $\dfrac1x$ が混ざるので、指数をていねいに整理する。</p>","先に「どの $r$ 番目の項か」を決めてから、その1項だけ計算する。",6)
# 7 (1+x)^n(1-x)^n
def b7(n,m):
    v=comb(n,m)*(-1)**m; assert sp.expand((1+x)**n*(1-x)**n).coeff(x,2*m)==v
    st=[("まとめる","<p>指数がそろっているので "+I(r"A^nB^n=(AB)^n")+"。</p>"+D(r"(1+x)^n(1-x)^n=\{(1+x)(1-x)\}^n=(1-x^2)^{%d}"%n)),
        ("一般項","<p>"+I(r"(1-x^2)^{%d}"%n)+" の一般項は</p>"+D(r"{}_{%d}\mathrm{C}_{r}(-x^2)^r={}_{%d}\mathrm{C}_{r}(-1)^rx^{2r}"%(n,n))),
        ("$x^{%d}$ の係数"%(2*m),"<p>"+I("2r=%d"%(2*m))+" より "+I("r=%d"%m)+"。</p>"+D(r"(-1)^{%d}{}_{%d}\mathrm{C}_{%d}=%d"%(m,n,m,v)))]
    return r"$(1+x)^{%d}(1-x)^{%d}$ の展開式における $x^{%d}$ の係数を求めよ。"%(n,n,2*m),st,L(v)
o=[b7(*v) for v in [(8,3),(10,2),(9,4),(7,3),(12,5)]]
build(Z,CH,"指数がそろった積の係数",o,r"<p>$(1+x)^n(1-x)^n=(1-x^2)^n$ とまとめてから、$(1-x^2)^n$ の一般項で係数を求める。偶数次の項しかないことに注意。</p>","まとめ買いしてから数える。ばらばらに展開しない。",7)
# 8 余り
def b8(base,e,mod):
    v=pow(base,e,mod); 
    if base==11 and mod==100: p1=r"11^{%d}=(10+1)^{%d}=1+%d\cdot10+{}_{%d}\mathrm{C}_2\cdot10^2+\cdots"%(e,e,e,e)
    elif base==9: p1=r"9^{%d}=(10-1)^{%d}=(-1)^{%d}+%d\cdot10\cdot(-1)^{%d}+{}_{%d}\mathrm{C}_2\cdot10^2(-1)^{%d}+\cdots"%(e,e,e,e,e-1,e,e-2)
    else: p1=""
    k_=(1,10)[0]
    if base==11: low=(1+e*10)%100
    else: low=((-1)**e+e*10*(-1)**(e-1))%100
    assert low==v,(low,v)
    st=[("二項定理で展開","<p>"+I(r"%d=10+%d"%(base,base-10) if base==11 else r"%d=10-1"%base)+" とみる。</p>"+D(p1)),
        ("100 の倍数を除く","<p>"+I(r"10^2")+" 以上の項は 100 の倍数。残る下2けた分だけを計算する。</p>"+D(r"\equiv %s\pmod{100}"%(r"1+%d\cdot10=%d"%(e,1+10*e) if base==11 else r"%d%+d\cdot10"%((-1)**e,e*(-1)**(e-1)))+r"\ \to\ %d"%v)),
        ("余り","<p>余りは "+I(str(v))+"。</p>")]
    return r"$%d^{%d}$ を $%d$ でわった余りを求めよ。"%(base,e,mod),st,str(v)
o=[b8(*v) for v in [(11,20,100),(11,37,100),(9,20,100),(11,56,100),(9,31,100)]]
build(Z,CH,"二項定理で余りを求める",o,r"<p>わる数に近い数 $(10\pm1)$ で表して<b>二項定理で展開</b>し、$100$ の倍数になる項を捨てる。残る項は先頭2〜3項だけ。</p>","大きな累乗は、キリのよい数の ±1 に化けさせて展開する。",8)
# 9 係数の和
def b9(n):
    f=sp.expand((x**2-x+1)**n); tot=f.subs(x,1); alt=f.subs(x,-1); ev=(tot+alt)//2; od=(tot-alt)//2
    assert sum(f.coeff(x,i) for i in range(0,2*n+1,2))==ev and sum(f.coeff(x,i) for i in range(1,2*n+1,2))==od
    st=[("全係数の和","<p>"+I("x=1")+" を代入。</p>"+D(r"a_0+a_1+\cdots+a_{%d}=(1-1+1)^{%d}=1^{%d}=%d"%(2*n,n,n,tot))),
        ("符号を交互にした和","<p>"+I("x=-1")+" を代入。</p>"+D(r"a_0-a_1+a_2-\cdots+a_{%d}=(1+1+1)^{%d}=3^{%d}=%d"%(2*n,n,n,alt))),
        ("偶数次の和","<p>2式を足して2でわる。</p>"+D(r"a_0+a_2+\cdots+a_{%d}=\dfrac{%d+%d}{2}=\dfrac{%d}{2}=%d"%(2*n,tot,alt,tot+alt,ev)))]
    return r"$(x^2-x+1)^{%d}=a_0+a_1x+a_2x^2+\cdots+a_{%d}x^{%d}$ のとき、$a_0+a_2+a_4+\cdots+a_{%d}$ の値を求めよ。"%(n,2*n,2*n,2*n),st,str(ev)
o=[b9(n) for n in [4,5,6,7,8]]
build(Z,CH,"係数の和（x=1, x=-1 の代入）",o,r"<p>$x=1$ で<b>全係数の和</b>、$x=-1$ で<b>偶数次の和−奇数次の和</b>が得られる。2式の和・差から、偶数次・奇数次の和を分ける。</p>","代入は「係数を全部足す」スイッチ。$-1$ なら奇数次だけ符号が反転する。",9)
# 10 x^n+y^n
def b10(p,q,n):
    s={0:2,1:p}
    for i in range(2,n+1): s[i]=p*s[i-1]-q*s[i-2]
    X=sp.Symbol('X'); roots=sp.solve(X**2-p*X+q,X); v=sp.simplify(sum(r_**n for r_ in roots)); assert v==s[n]
    st=[("基本式",D(r"x+y=%d,\quad xy=%d"%(p,q))),
        ("漸化式","<p>"+I(r"x^{k+1}+y^{k+1}=(x+y)(x^k+y^k)-xy(x^{k-1}+y^{k-1})")+"。"+I(r"s_k=x^k+y^k")+" とおくと</p>"+D(r"s_{k+1}=%d\,s_k-%d\,s_{k-1}"%(p,q))),
        ("順に求める","<p>"+I(r"s_0=2,\ s_1=%d"%p)+"。</p>"+D(r"\ ".join(r"s_{%d}=%d,"%(i,s[i]) for i in range(2,n+1)))+"<p>よって "+I(r"x^{%d}+y^{%d}=%d"%(n,n,s[n]))+"。</p>")]
    return r"$x+y=%d,\ xy=%d$ のとき、$x^{%d}+y^{%d}$ の値を求めよ。"%(p,q,n,n),st,str(s[n])
o=[b10(*v) for v in [(4,1,6),(3,1,6),(5,2,5),(6,4,6),(4,2,7)]]
build(Z,CH,"累乗和を漸化式で求める",o,r"<p>$s_k=x^k+y^k$ とおく。$s_{k+1}=(x+y)s_k-xy\,s_{k-1}$ を使って、小さい方から順に $s_2,s_3,\cdots$ と積み上げる。$x,y$ を求めない。</p>","1つ前と2つ前から次を作る階段。値を求めずに登る。",10)
XU=finishx(Z,CH)
