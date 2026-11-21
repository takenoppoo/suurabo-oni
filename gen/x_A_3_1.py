# -*- coding: utf-8 -*-
from bh import *
import math, itertools
Z=U_(); CH=[]; R=sp.Rational
# 6 gcd のとりうる値
def b6(a,b,c,d):
    det=abs(a*d-b*c); vals=sorted({math.gcd(a*n+b,c*n+d) for n in range(1,2000)}); assert all(det%v==0 for v in vals)
    st=[("$g$ とおいて消去","<p>"+I("g=\\gcd(%dn+%d,\\ %dn+%d)"%(a,b,c,d))+"。"+I("g")+" は両方の約数。</p>"+D(r"%d(%dn+%d)-%d(%dn+%d)=%d"%(c,a,b,a,c,d,c*b-a*d if True else 0)) if False else "<p>"+I("g=\\gcd(%dn+%d,\\ %dn+%d)"%(a,b,c,d))+"。"+I("g")+" は2つの数の約数なので、1次結合も割り切る。</p>"+D(r"%d(%dn+%d)-%d(%dn+%d)=%d"%(c,a,b,a,c,d,c*b-a*d))),
        ("$g$ は %d の約数"%det,"<p>"+I("g")+" は "+I(str(det))+" の約数。</p>"+D(r"g\in\{%s\}"%(r",\ ".join(str(v) for v in sp.divisors(det))))),
        ("実際にとる値","<p>"+I("n")+" を動かして調べると</p>"+D(r"g=%s"%(r",\ ".join(str(v) for v in vals))))]
    return r"自然数 $n$ に対して、$\gcd(%dn+%d,\ %dn+%d)$ がとりうる値をすべて求めよ。"%(a,b,c,d),st,r"%s"%(r",\ ".join(str(v) for v in vals))
o=[b6(*v) for v in [(3,1,5,7),(2,3,5,1),(4,1,3,5),(5,2,3,7),(3,2,4,9)]]
build(Z,CH,"1次式の最大公約数のとりうる値",o,r"<p>$g$ を共通の約数とし、<b>$n$ を消去する1次結合</b>をつくると定数になる。$g$ はその定数の約数。実際にとる値は $n$ に具体的な値を入れて確認する。</p>","2つの式を組み合わせて、文字 $n$ を消してしまう。",6)
# 7 倍数の証明
CASES=[
 (r"n^5-n",30,r"n^5-n=n(n^2-1)(n^2+1)=(n-1)n(n+1)(n^2+1)",r"連続3整数の積なので <b>2 と 3 の倍数</b>。5 については $n\equiv0,\pm1$ なら $(n-1)n(n+1)$ が5の倍数、$n\equiv\pm2$ なら $n^2+1\equiv4+1\equiv0$ で5の倍数。",lambda n:n**5-n),
 (r"n^3+5n",6,r"n^3+5n=(n^3-n)+6n=(n-1)n(n+1)+6n",r"$(n-1)n(n+1)$ は連続3整数の積で 2 と 3 の倍数（よって6の倍数）。$6n$ も6の倍数。和も6の倍数。",lambda n:n**3+5*n),
 (r"n^5-5n^3+4n",120,r"n^5-5n^3+4n=n(n^2-1)(n^2-4)=(n-2)(n-1)n(n+1)(n+2)",r"連続5整数の積。5の倍数が必ず1つ、3の倍数が少なくとも1つ。偶数が2つ以上あり、そのうち一つは4の倍数なので $2^3=8$ の倍数。$120=8\times3\times5$ で互いに素。",lambda n:n**5-5*n**3+4*n),
 (r"n^4-n^2",12,r"n^4-n^2=n^2(n-1)(n+1)",r"$(n-1)n(n+1)$ が3の倍数。$n$ が偶数なら $n^2$ が4の倍数、$n$ が奇数なら $(n-1)(n+1)$ が2つの連続偶数で8の倍数。いずれも4の倍数。$12=3\times4$。",lambda n:n**4-n**2),
 (r"n^7-n",42,r"n^7-n=n(n^6-1)=n(n^3-1)(n^3+1)",r"$n^7-n=(n^3-n)(n^4+n^2+1)\cdot$ 型に整理すると、連続3整数の積から 2・3 の倍数。7 については $n\equiv0,\pm1,\pm2,\pm3\pmod7$ で $n^7\equiv n$ を確認（フェルマーの小定理）。$42=2\times3\times7$。",lambda n:n**7-n)]
def b7(i):
    ex_,m,fac,expl,f=CASES[i]; assert all(f(n)%m==0 for n in range(-60,60))
    fs=sp.factorint(m)
    st=[("因数分解",D(fac)),
        ("倍数であることの根拠","<p>"+expl+"</p>"),
        ("結論","<p>"+I(ex_)+" は "+I(" , ".join(str(p**e) for p,e in sorted(fs.items())))+" のどれでも割り切れ、これらは互いに素。よって "+I(str(m))+" の倍数。</p>")]
    return r"整数 $n$ について、$%s$ は $%d$ の倍数であることを証明せよ。"%(ex_,m),st,r"\text{証明終}"
o=[b7(i) for i in [0,1,2,3,4]]
build(Z,CH,"整数式が倍数であることの証明",o,r"<p>まず<b>因数分解して連続する整数の積</b>をつくる。連続 $k$ 整数の積は $k!$ の倍数。互いに素な素数の冪ごとに「必ず含まれる」ことを示し、合体させる。</p>","素数ごとに別々に保証して、最後に合体。",7)
# 8 中国剰余
def b8(m1,r1,m2,r2):
    sol=[n for n in range(1,m1*m2+1) if n%m1==r1 and n%m2==r2]; n0=sol[0]
    st=[("条件を式にする","<p>"+I("n=%dk+%d"%(m1,r1))+"（"+I("k")+" は0以上の整数）。</p>"),
        ("もう一つの条件に代入","<p>"+I("%dk+%d\\equiv%d\\pmod{%d}"%(m1,r1,r2,m2))+"。</p>"+D(r"%dk\equiv%d\pmod{%d}"%(m1,(r2-r1)%m2,m2))),
        ("$k$ を求める","<p>"+I("k=%d,%d,\\cdots"%(1,2) if False else "k")+" を順に調べて、最小の "+I("k=%d"%((n0-r1)//m1))+"。</p>"+D(r"n=%d\cdot%d+%d=%d"%(m1,(n0-r1)//m1,r1,n0))),
        ("周期","<p>"+I(r"%d"%m1)+" と "+I(r"%d"%m2)+" は互いに素なので、条件をみたす数は "+I(r"%d"%(m1*m2))+" ごとにくり返す。</p>"+D(r"n=%d,\ %d,\ \cdots"%(n0,n0+m1*m2)))]
    return r"$%d$ で割ると $%d$ 余り、$%d$ で割ると $%d$ 余る自然数 $n$ のうち、最小のものを求めよ。"%(m1,r1,m2,r2),st,str(n0)
o=[b8(*v) for v in [(7,3,5,2),(8,5,3,1),(9,4,5,3),(11,6,4,3),(7,2,6,5)]]
build(Z,CH,"2つの余りの条件をみたす最小の数",o,r"<p>一方の条件を $n=mk+r$ と表し、<b>もう一方の条件に代入</b>して $k$ の合同式をつくる。小さい $k$ から順に調べ、最小の $n$ を見つける。</p>","1つ目の条件で形を決め、2つ目の条件でしぼりこむ。",8)
# 9 n! の末尾の0
def b9(N):
    k=sum(N//5**i for i in range(1,6) if 5**i<=N); assert len(str(math.factorial(N)))-len(str(math.factorial(N)).rstrip("0"))==k
    terms=[(i,N//5**i) for i in range(1,6) if 5**i<=N]
    st=[("10 は 2×5","<p>末尾の0の個数は、"+I(str(N)+"!")+" に含まれる "+I("10=2\\times5")+" の個数。2 は 5 より多いので、<b>5 の個数</b>で決まる。</p>"),
        ("5 の倍数を数える","<p>"+I("1\\sim%d"%N)+" の中の 5, 25, 125 の倍数の個数を足す（25 の倍数は5を2個含む）。</p>"+D(r"%s=%d"%("+".join(r"\left\lfloor\dfrac{%d}{%d}\right\rfloor"%(N,5**i) for i,_ in terms),k))),
        ("結論","<p>末尾に "+I(str(k))+" 個の0が並ぶ。</p>")]
    return r"$%d!$ を計算したとき、末尾に0が連続して何個並ぶか。"%N,st,str(k)
o=[b9(N) for N in [50,100,150,200,250]]
build(Z,CH,"n! の末尾に並ぶ 0 の個数",o,r"<p>末尾の0は $10=2\times5$ の個数。素因数の 2 は十分あるので<b>5 の指数</b>を数える。$\left\lfloor\dfrac N5\right\rfloor+\left\lfloor\dfrac N{25}\right\rfloor+\left\lfloor\dfrac N{125}\right\rfloor+\cdots$</p>","10 をつくる材料のうち、不足するのは 5 の方。",9)
# 10 既約分数の個数
def b10(N):
    cnt=sum(1 for k in range(1,N+1) if math.gcd(k,N)==1); fs=sp.factorint(N)
    st=[("既約になる条件","<p>"+I(r"\dfrac{k}{%d}"%N)+" が既約 "+I(r"\iff\gcd(k,%d)=1"%N)+"。</p>"),
        ("素因数分解","<p>"+I("%d=%s"%(N,r"\times".join(str(p)+("^{%d}"%e if e>1 else "") for p,e in sorted(fs.items()))))+"。素因数 "+I(",\\ ".join(str(p) for p in fs))+" の倍数を除く。</p>"),
        ("個数（オイラーの関数）",D(r"%d\times%s=%d"%(N,r"\times".join(r"\left(1-\dfrac1{%d}\right)"%p for p in fs),cnt)))]
    return r"$1\leqq k\leqq %d$ である整数 $k$ のうち、分数 $\dfrac{k}{%d}$ がこれ以上約分できない（既約分数である）ものの個数を求めよ。"%(N,N),st,str(cnt)
o=[b10(N) for N in [60,72,84,90,120]]
build(Z,CH,"既約分数の個数（素因数の倍数を除く）",o,r"<p>$\dfrac kN$ が既約 $\iff \gcd(k,N)=1$。$N$ の素因数 $p$ の倍数を除く。個数は $N\prod\left(1-\dfrac1p\right)$（各素因数ごとに割合をかける）。</p>","約分できる原因は、共通の素因数。それを持つ数を除く。",10)
XU=finishx(Z,CH)
