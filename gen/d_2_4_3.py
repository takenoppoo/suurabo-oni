# -*- coding: utf-8 -*-
# 常用対数（数学II 指数関数・対数関数）
from bh import *
import math
Z=U_(); CH=[]
l2=sp.Rational(3010,10000); l3=sp.Rational(4771,10000)
def dec(q): return "%.4f"%float(q)
def lgterms(a,b,c):
    toks=[]
    if a: toks.append((a,"0.3010"))
    if b: toks.append((b,"0.4771"))
    if c: toks.append((c,r"(1-0.3010)"))
    s=""
    for i,(k,v) in enumerate(toks):
        sg="-" if k<0 else ("+" if i>0 else "")
        kk=abs(k); s+=sg+(v if kk==1 else r"%d\times %s"%(kk,v))
    return s
def lgval(a,b,c): return a*l2+b*l3+c*(1-l2)
def pw2(a,b,c):
    out=[]
    for p_,e_ in ((2,a),(3,b),(5,c)):
        if e_==0: continue
        out.append(str(p_) if e_==1 else "%d^{%d}"%(p_,e_))
    return r"\times ".join(out)
def lgsym(a,b,c):
    out=[]
    for p_,e_ in ((2,a),(3,b),(5,c)):
        if e_==0: continue
        sg="-" if e_<0 else ("+" if out else "")
        k=abs(e_); out.append(sg+("" if k==1 else str(k))+r"\log_{10}%d"%p_)
    return "".join(out)
# ===== 例題1 値の計算 =====
def b1(a,b,c):
    N=sp.Integer(2)**a*sp.Integer(3)**b*sp.Integer(5)**c; v=lgval(a,b,c)
    assert abs(float(v)-math.log10(float(N)))<2e-3
    st=[("素因数分解の形に直す","<p>"+I(L(N)+"="+pw2(a,b,c))+"。</p>"),
        ("$\\log_{10}$ を分ける","<p>"+I(r"\log_{10}MN=\log_{10}M+\log_{10}N,\quad \log_{10}M^k=k\log_{10}M")+"。</p>"+D(r"\log_{10}%s=%s"%(L(N),lgsym(a,b,c)))),
        ("$\\log_{10}5$ は $1-\\log_{10}2$ で表す" if c else "与えられた値を代入する","<p>"+(I(r"\log_{10}5=\log_{10}\dfrac{10}{2}=1-\log_{10}2")+"。</p>" if c else "")+D(r"\log_{10}%s=%s"%(L(N),lgterms(a,b,c)))),
        ("計算する",D(r"\log_{10}%s=%s"%(L(N),dec(v))))]
    return r"$\log_{10}2=0.3010,\ \log_{10}3=0.4771$ として、$\log_{10}%s$ の値を求めよ。"%L(N),st,dec(v)
V=[(3,2,0),(-1,2,1),(4,1,-1),(2,-2,2),(5,0,-2)]
o=[b1(*v) for v in V]
build(Z,CH,"常用対数の値の計算",o,
 r"<p>真数を $2^a3^b5^c$ の形にして、$\log_{10}$ を和・差・倍に分ける。$\log_{10}5=1-\log_{10}2$、$\log_{10}10=1$ が大事なつなぎ役。</p>",
 "数を「素数のレゴ」に分解して、レゴ1個ずつの対数をたし算する。5だけは 10÷2 と見る。",1)
# ===== 例題2 桁数 =====
def b2(a,b,c,n):
    base=2**a*3**b*5**c; v=n*lgval(a,b,c); d=int(math.floor(v))+1
    assert len(str(base**n))==d
    st=[("常用対数をとる",D(r"\log_{10}%s^{%d}=%d\log_{10}%s=%d\times\left(%s\right)"%(L(sp.Integer(base)) if False else base,n,n,base,n,lgsym(a,b,c)))),
        ("値を計算する",D((r"%d\times%s=%s"%(n,lgterms(a,b,c),dec(v))) if (a==0 and b==0) else (r"%d\times\left(%s\right)=%s"%(n,lgterms(a,b,c),dec(v))))),
        ("桁数を判定する","<p>"+I(r"%d\leqq\log_{10}x<%d"%(d-1,d))+" のとき $x$ は "+I("%d"%d)+" 桁。</p>"+D(r"%d\leqq %s<%d\ \Rightarrow\ \text{%d 桁}"%(d-1,dec(v),d,d)))]
    return r"$\log_{10}2=0.3010,\ \log_{10}3=0.4771$ として、$%d^{%d}$ は何桁の整数か。"%(base,n),st,r"%d\text{ 桁}"%d
V=[(1,0,0,30),(0,1,0,20),(2,1,0,10),(0,0,1,40),(1,1,0,15)]
o=[b2(*v) for v in V]
build(Z,CH,"累乗の桁数",o,
 r"<p>$x$ が $k$ 桁の整数 $\iff 10^{k-1}\leqq x<10^k\iff k-1\leqq\log_{10}x<k$。$\log_{10}x^n=n\log_{10}x$ を求め、整数部分に $1$ を加えたものが桁数。</p>",
 "桁数 ＝ 常用対数の整数部分 ＋ 1。0.3010×30＝9.03 → 整数部分9 → 10桁。",2)
# ===== 例題3 小数第何位 =====
def b3(a,b,n):
    base=2**a*3**b; v=n*lgval(a,b,0); k=int(math.ceil(float(v)))
    x=sp.Rational(1,base**n); assert sp.Rational(1,10**k)<=x<sp.Rational(1,10**(k-1))
    st=[("常用対数をとる",D(r"\log_{10}\left(\dfrac1{%d}\right)^{%d}=-%d\log_{10}%d=-%d\times\left(%s\right)=-%s"%(base,n,n,base,n,lgsym(a,b,0),dec(v)))),
        ("整数ではさむ","<p>"+I(r"-%d\leqq\log_{10}x<-%d"%(k,k-1))+" のとき "+I(r"10^{-%d}\leqq x<10^{-%d}"%(k,k-1))+"。</p>"+D(r"-%d\leqq -%s<-%d"%(k,dec(v),k-1))),
        ("小数第何位かを決める","<p>"+I(r"10^{-%d}\leqq x<10^{-%d}"%(k,k-1))+" より、$x$ を小数で書くと小数第 "+I(str(k))+" 位にはじめて 0 でない数字が現れる。</p>")]
    return r"$\log_{10}2=0.3010,\ \log_{10}3=0.4771$ として、$\left(\dfrac1{%d}\right)^{%d}$ を小数で表したとき、小数第何位にはじめて 0 でない数字が現れるか。"%(base,n),st,r"\text{小数第 %d 位}"%k
V=[(1,0,20),(0,1,30),(1,1,10),(2,1,12),(2,0,25)]
o=[b3(*v) for v in V]
build(Z,CH,"小数第何位に初めて0でない数字が現れるか",o,
 r"<p>$10^{-k}\leqq x<10^{-(k-1)}$ ならば、$x$ は小数第 $k$ 位にはじめて 0 でない数字が現れる。$k-1\leqq$ ではなく <b>$-k\leqq\log_{10}x<-k+1$</b> ではさむ。</p>",
 "$0.0001=10^{-4}$ は小数第4位。log が $-4$ 以上 $-3$ 未満なら第4位。",3)
# ===== 例題4 最小のn =====
def b4(a,b,c,t):
    r=sp.Rational(2)**a*sp.Rational(3)**b*sp.Rational(5)**c; v=lgval(a,b,c); assert v<0
    q=sp.Rational(t)/(-v); n=int(math.floor(float(q)))+1
    assert (r**n<sp.Rational(1,10**t)) and not (r**(n-1)<sp.Rational(1,10**t))
    st=[("両辺の常用対数をとる",D(r"\log_{10}%s^n<\log_{10}10^{-%d}\ \Rightarrow\ n\log_{10}%s<-%d"%("\\left(%s\\right)"%L(r),t,L(r),t))),
        ("$\\log_{10}%s$ の値"%L(r),"<p>"+I(L(r)+"="+pw2(a,b,c))+"。</p>"+D(r"\log_{10}%s=%s=%s"%(L(r),lgterms(a,b,c),dec(v)))),
        ("負の数でわる（不等号の向きが変わる）",D(r"%s\,n<-%d\ \Rightarrow\ n>\dfrac{%d}{%s}=%.2f\cdots"%(dec(v),t,t,dec(-v),float(q)))),
        ("最小の整数",D(r"n=%d"%n))]
    return r"$\log_{10}2=0.3010,\ \log_{10}3=0.4771$ として、$\left(%s\right)^n<10^{-%d}$ を満たす最小の整数 $n$ を求めよ。"%(L(r),t),st,"n=%d"%n
V=[(2,0,-1,2),(1,-1,0,3),(0,1,-1,4),(-1,2,-1,2),(-1,-1,1,3)]
o=[b4(*v) for v in V]
build(Z,CH,"不等式を満たす最小の整数",o,
 r"<p>両辺の<b>常用対数</b>をとって $n$ をおろす。$\log_{10}r$ が<b>負</b>のとき、両辺をわると<b>不等号の向きが逆</b>になる。出た値を超える最小の整数が答え。</p>",
 "1より小さい数を何回もかけると小さくなる。log が負になる点だけ要注意。",4)
# ===== 例題5 最高位 =====
TAB=[(1,r"0",0,r"\log_{10}2",l2),(2,r"\log_{10}2",l2,r"\log_{10}3",l3),(3,r"\log_{10}3",l3,r"\log_{10}4",2*l2),(4,r"\log_{10}4",2*l2,r"\log_{10}5",1-l2),(5,r"\log_{10}5",1-l2,r"\log_{10}6",l2+l3),(8,r"\log_{10}8",3*l2,r"\log_{10}9",2*l3),(9,r"\log_{10}9",2*l3,r"1",sp.Integer(1))]
def b5(a,b,n):
    base=2**a*3**b; v=n*lgval(a,b,0); m=int(math.floor(float(v))); f=v-m
    dd=int(str(base**n)[0]); row=[t for t in TAB if t[4]<=f<t[6-1+0]] if False else [t for t in TAB if t[2]<=f<t[4]]
    assert len(row)==1 and row[0][0]==dd; d,lt,lv,ht,hv=row[0][0],row[0][1],row[0][2],row[0][3],row[0][4]
    assert min(abs(f-lv),abs(f-hv))>sp.Rational(2,1000)
    st=[("常用対数をとる",D(r"\log_{10}%d^{%d}=%d\times\left(%s\right)=%s=%d+%s"%(base,n,n,lgsym(a,b,0),dec(v),m,dec(f)))),
        ("小数部分をはさむ","<p>"+I(r"%s\leqq %s<%s"%(r"\log_{10}%d"%d if d!=1 else "0",dec(f),ht))+" となる $d$ を探す（$\\log_{10}d\\leqq f<\\log_{10}(d+1)$）。</p>"+D(r"%s\leqq %s<%s\ \Rightarrow\ %s\leqq %s<%s"%(dec(lv),dec(f),dec(hv),lt if d!=1 else "0",dec(f),ht))),
        ("最高位の数字","<p>"+I(r"\log_{10}%d\leqq \log_{10}%d^{%d}-%d<\log_{10}%s"%(d,base,n,m,str(d+1)))+" より "+I(r"%d\times10^{%d}\leqq %d^{%d}<%s\times10^{%d}"%(d,m,base,n,str(d+1),m))+"。最高位の数字は "+I(str(d))+"。</p>")]
    return r"$\log_{10}2=0.3010,\ \log_{10}3=0.4771$ として、$%d^{%d}$ の最高位の数字を求めよ。"%(base,n),st,"%d"%d
V=[(1,0,30),(0,1,20),(0,1,10),(1,1,20),(1,0,25)]
o=[b5(*v) for v in V]
build(Z,CH,"最高位の数字",o,
 r"<p>$\log_{10}x^n=m+f\ (m$ は整数、$0\leqq f<1)$ とすると $x^n=10^f\times10^m$。$d\leqq10^f<d+1$ すなわち <b>$\log_{10}d\leqq f<\log_{10}(d+1)$</b> となる $d$ が最高位の数字。</p>",
 "整数部分は桁数、小数部分は先頭の数字を決める。小数部分を $\\log_{10}1,\\log_{10}2,\\dots$ の表にあてはめる。",5)
UNIT=finish(Z,CH,3,2,"指数関数・対数関数","常用対数","桁数、小数第何位、最小のn、最高位の数字まで、常用対数の応用を一気に総復習します。")
