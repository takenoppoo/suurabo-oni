# -*- coding: utf-8 -*-
from bh import *
Z=U_(); CH=[]; R=sp.Rational; x=sp.symbols("x"); i_=sp.I
def b6(a,b,n):
    z=a+b*i_; v=sp.expand((z)**n); 
    st=[("2乗を求める","<p>"+D(r"(%s)^2=%s"%(L(z),L(sp.expand(z**2)))))]
    w=sp.expand(z**2)
    st.append(("くり返す","<p>"+D(r"(%s)^4=(%s)^2=%s"%(L(z),L(w),L(sp.expand(w**2))))))
    st.append(("%d乗"%n,D(r"(%s)^{%d}=%s"%(L(z),n,L(v)))))
    return r"$(%s)^{%d}$ を計算せよ。"%(L(z),n),st,L(v)
o=[b6(*v) for v in [(1,1,8),(1,-1,6),(1,1,10),(1,sp.sqrt(3),3),(sp.sqrt(3),1,6)]]
build(Z,CH,"複素数の累乗",o,"<p>$(a+bi)^2$ を作って<b>2乗をくり返す</b>。$(1+i)^2=2i$ のように、実数・純虚数になる形を見つけると速い。</p>","一気に何乗もせず、2乗ずつ小さく積み上げる。",6)
def b7(p,q):
    a,b=sp.symbols("a b"); s=-p; pr=q
    s2=s*s-2*pr; p2=pr*pr
    st=[("解と係数の関係","<p>"+I("\\alpha+\\beta=%d,\\ \\alpha\\beta=%d"%(s,pr))+"。</p>"),
        ("新しい2解の和と積","<p>"+D(r"\alpha^2+\beta^2=(\alpha+\beta)^2-2\alpha\beta=%d,\qquad \alpha^2\beta^2=(\alpha\beta)^2=%d"%(s2,p2))),
        ("2次方程式",D(r"x^2-%d\,x+%d=0"%(s2,p2) if True else ""))]
    return r"2次方程式 $x^2%+dx%+d=0$ の2つの解を $\alpha,\ \beta$ とする。$\alpha^2,\ \beta^2$ を解とする2次方程式を1つ求めよ。"%(p,q),st,r"x^2%+dx%+d=0"%(-s2,p2)
o=[b7(*v) for v in [(-3,1),(2,-4),(-5,2),(1,3),(-4,-3)]]
build(Z,CH,"解を2乗した数を解とする方程式",o,"<p>2解の<b>和と積</b>を求め、$x^2-(\\text{和})x+(\\text{積})=0$。和・積は対称式なので解と係数の関係で。</p>","解そのものを求めず、和と積だけで新しい方程式を組み立てる。",7)
def b8(a,b):
    z=a+b*i_; s=2*a; pr=a*a+b*b
    st=[("共役な解","<p>実数係数なので "+I("%s"%L(z))+" が解なら共役複素数 "+I("%s"%L(sp.conjugate(z)))+" も解。</p>"),
        ("解と係数の関係","<p>和 "+I("%d"%s)+"、積 "+I("%d"%pr)+"。</p>"),
        ("方程式",D(r"x^2-%d\,x+%d=0"%(s,pr)))]
    return r"実数係数の2次方程式 $x^2+px+q=0$ が解 $%s$ をもつとき、$p,\ q$ の値を求めよ。"%L(z),st,r"p=%d,\ q=%d"%(-s,pr)
o=[b8(*v) for v in [(2,3),(-1,2),(3,1),(1,4),(-2,5)]]
build(Z,CH,"虚数解から係数を決める",o,"<p>実数係数の方程式の虚数解は<b>共役とペア</b>。和と積を解と係数の関係に当てはめる。</p>","虚数解はかならず2人1組で現れる。",8)
def b9(a):
    # x^2-2(a)x+a+6=0 two positive; or opposite sign...
    # 2解が異符号: a+? use x^2+2(a-1)x+a^2-9 ... opposite sign: a^2-9<0 => -3<a<3
    st=[("異符号の条件","<p>2解の積が負："+I(r"\alpha\beta=a^2-%d<0"%(a)) if False else "<p>2解が異符号 "+I(r"\iff \alpha\beta<0")+"。（このとき判別式は自動的に正）</p>"),
        ("積","<p>"+I(r"\alpha\beta=a^2-%d"%(a*a))+"。</p>"+D(r"a^2-%d<0"%(a*a))),
        ("答え",D(r"-%d<a<%d"%(a,a)))]
    return r"$x$ の2次方程式 $x^2+2(a-1)x+a^2-%d=0$ が異符号の実数解をもつような定数 $a$ の範囲を求めよ。"%(a*a),st,r"-%d<a<%d"%(a,a)
o=[b9(a) for a in [3,4,2,5,6]]
build(Z,CH,"異符号の2解をもつ条件",o,"<p>異符号 $\\iff$ 積 $<0$。このとき $D=b^2-4ac>0$ は自動的に成り立つので、<b>積の条件だけ</b>でよい。</p>","積がマイナスなら、片方が正で片方が負。",9)
def b10(c,d):
    # sqrt(c+di): find (a+bi)^2 = c+di
    sol=[(a,b) for a in range(-20,21) for b in range(-20,21) if a*a-b*b==c and 2*a*b==d]
    a,b=sol[0]
    st=[("おく","<p>"+I("(p+qi)^2=%d%+di"%(c,d))+"（"+I("p,q")+" は実数）。</p>"),
        ("実部・虚部を比べる","<p>"+D(r"p^2-q^2=%d,\qquad 2pq=%d"%(c,d))),
        ("解く","<p>"+D(r"(p,q)=(%d,%d),\ (%d,%d)"%(a,b,-a,-b)))]
    return r"$(p+qi)^2=%d%+di$ をみたす実数 $p,q$ を求め、$%s$ の平方根を求めよ。"%(c,d,L(c+d*i_)),st,r"\pm(%s)"%L(a+b*i_)
o=[b10(*v) for v in [(5,12),(-3,4),(8,6),(-5,-12),(21,20)]]
build(Z,CH,"複素数の平方根",o,"<p>$(p+qi)^2$ を展開し<b>実部・虚部を比べる</b>。$p^2-q^2$ と $2pq$ の連立から整数解を見つける。</p>","2乗して元に戻る形を、実部と虚部に分けて探す。",10)
XU=finishx(Z,CH)
