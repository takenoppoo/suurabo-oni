# -*- coding: utf-8 -*-
from bh import *
import math
Z=U_(); CH=[]; R=sp.Rational
L2=0.3010; L3=0.4771; L7=0.8451
def b6(base,b,target,lb):
    # smallest n with base^n > 10^target ; log10(base)=lb
    n=int(target/lb)+1
    assert base**n>10**target and base**(n-1)<=10**target
    st=[("常用対数をとる","<p>"+D(r"%d^n>10^{%d}\ \Rightarrow\ n\log_{10}%d>%d"%(base,target,base,target))),
        ("数値を代入","<p>"+D(r"n>\dfrac{%d}{%s}=%.2f\cdots"%(target,lb,target/lb))),
        ("最小の整数",D(r"n=%d"%n))]
    return r"$\log_{10}%d=%s$ とする。$%d^n>10^{%d}$ をみたす最小の整数 $n$ を求めよ。"%(base,lb,base,target),st,str(n)
o=[b6(2,0,6,.3010),b6(3,0,10,.4771),b6(7,0,8,.8451),b6(2,0,15,.3010),b6(3,0,12,.4771)]
build(Z,CH,"a^n > 10^k をみたす最小の n",o,"<p>両辺の<b>常用対数</b>をとる。$n>\\dfrac{k}{\\log_{10}a}$ の右辺を計算し、<b>切り上げ</b>た整数が最小の $n$。</p>","対数にすれば、指数が係数に降りてくる。",6)
def b7(base,lb,k):
    # smallest n with (1/base)^n < 10^-k  i.e. base^n>10^k
    n=int(k/lb)+1
    assert base**n>10**k and base**(n-1)<=10**k
    st=[("不等式","<p>"+D(r"\left(\dfrac1{%d}\right)^n<10^{-%d}\iff %d^n>10^{%d}"%(base,k,base,k))),
        ("常用対数",D(r"n>\dfrac{%d}{%s}=%.2f\cdots"%(k,lb,k/lb))),
        ("答え",D(r"n=%d"%n))]
    return r"$\log_{10}%d=%s$ とする。$\left(\dfrac1{%d}\right)^n<10^{-%d}$ となる最小の整数 $n$ を求めよ。"%(base,lb,base,k),st,str(n)
o=[b7(2,.3010,5),b7(3,.4771,8),b7(7,.8451,4),b7(2,.3010,9),b7(3,.4771,5)]
build(Z,CH,"(1/a)^n が小さくなる最小の n",o,"<p>$\\left(\\dfrac1a\\right)^n<10^{-k}$ は $a^n>10^k$ と同じ。常用対数をとって $n$ を切り上げる。</p>","割るのをくり返して、いつ 10^{-k} を下回るか。",7)
def b8(n):
    # digits of n! 
    fa=math.factorial(n); d=len(str(fa)); lg=sum(math.log10(i) for i in range(1,n+1))
    st=[("常用対数","<p>"+D(r"\log_{10}%d!=\sum_{k=1}^{%d}\log_{10}k=%.3f\cdots"%(n,n,lg))),
        ("桁数","<p>"+I(r"%d\leqq\log_{10}%d!<%d"%(d-1,n,d))+" より "+I(r"%d!"%n)+" は "+I("%d"%d)+" 桁。</p>")]
    return r"$%d!$ は何桁の数か。（$\log_{10}$ の和を用いる）"%n,st,str(d)
o=[b8(n) for n in [10,15,20,25,30]]
build(Z,CH,"n! の桁数",o,"<p>$N$ が $d$ 桁 $\\iff d-1\\leqq\\log_{10}N<d$。$\\log_{10}n!=\\log_{10}1+\\log_{10}2+\\cdots$ を計算（大きな数は問題文の対数表）。</p>","桁数は、常用対数の整数部分に 1 を足した数。",8)
def b9(a,e):
    v=a**e; d=len(str(v)); top=int(str(v)[0]); lg=e*math.log10(a)
    st=[("常用対数","<p>"+D(r"\log_{10}%d^{%d}=%d\log_{10}%d=%.4f\cdots"%(a,e,e,a,lg))),
        ("小数部分","<p>"+D(r"%.4f=%d+%.4f\ \Rightarrow\ %d^{%d}=10^{%d}\times10^{%.4f}"%(lg,int(lg),lg-int(lg),a,e,int(lg),lg-int(lg)))+"<p>"+I(r"10^{%.4f}=%.2f\cdots"%(lg-int(lg),10**(lg-int(lg))))+" なので最高位の数字は "+I(str(top))+"。</p>"),
        ("桁数","<p>"+I(str(d))+" 桁、最高位 "+I(str(top))+"。</p>")]
    return r"$%d^{%d}$ の桁数と最高位の数字を求めよ（$\log_{10}2=0.3010,\ \log_{10}3=0.4771$ を用いてよい）。"%(a,e),st,r"%d\text{桁},\ \text{最高位 }%d"%(d,top)
o=[b9(2,40),b9(3,30),b9(2,50),b9(3,25),b9(6,20)]
build(Z,CH,"累乗の桁数と最高位の数字",o,"<p>$\\log_{10}a^n=n\\log_{10}a=(\\text{整数})+(\\text{小数})$。整数部分＋1が桁数、<b>小数部分</b>から $10^{\\text{小数部分}}$ を計算して最高位。</p>","小数部分は、最初の数字を教えてくれる。",9)
def b10(n):
    # 2^n and 5^n digits relation: digits(2^n)+digits(5^n)=n+1
    a=len(str(2**n)); b=len(str(5**n)); assert a+b==n+1
    st=[("積は 10^n","<p>"+D(r"2^n\times5^n=10^n")+"</p>"),
        ("桁数の関係","<p>"+I(r"2^{%d}"%n)+" が "+I("%d"%a)+" 桁だから "+I(r"10^{%d}\leqq2^{%d}<10^{%d}"%(a-1,n,a))+"。</p>"+D(r"10^{%d}\cdot5^{%d}\leqq10^{%d}\ \Rightarrow\ \ldots"%(a-1,n,n)) if False else "<p>"+I(r"10^{%d}\leqq2^{%d}<10^{%d}"%(a-1,n,a))+"。"+I("5^{%d}=\\dfrac{10^{%d}}{2^{%d}}"%(n,n,n))+" より "+I(r"10^{%d}<5^{%d}\leqq10^{%d}"%(n-a,n,n-a+1))+"。</p>"),
        ("答え","<p>"+I(r"5^{%d}"%n)+" は "+I("%d"%b)+" 桁。</p>")]
    return r"$2^{%d}$ は $%d$ 桁の数である。$5^{%d}$ は何桁の数か。"%(n,a,n),st,str(b)
o=[b10(n) for n in [20,30,40,50,60]]
build(Z,CH,"2^n の桁数から 5^n の桁数",o,"<p>$2^n\\cdot5^n=10^n$。$2^n$ が $a$ 桁なら $10^{a-1}\\leqq2^n<10^a$。これと $5^n=10^n/2^n$ から $5^n$ の桁数が決まる（$a+b=n+1$）。</p>","2 と 5 を掛けると 10。桁数は足して n+1。",10)
XU=finishx(Z,CH)
