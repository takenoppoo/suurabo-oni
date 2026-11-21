# -*- coding: utf-8 -*-
# 指数関数（数学II 指数関数・対数関数）
from bh import *
from gq import *
def _ap(st,i,h): st[i]=(st[i][0],st[i][1]+h)
Z=U_(); CH=[]
def Q(a_,b_=1): return sp.Rational(a_,b_)
def pw(b_,e_): return r"%s^{%s}"%(("%d"%b_ if sp.Rational(b_).q==1 else L(sp.Rational(b_))),L(sp.Rational(e_)))
def pwb(b_,e_):
    s=("%d"%b_ if sp.Rational(b_).q==1 else r"\left(%s\right)"%L(sp.Rational(b_)))
    return s+"^{"+L(sp.Rational(e_))+"}"
def ppow(n_):
    f=sp.factorint(n_); assert len(f)==1; p_,k_=list(f.items())[0]; return p_,k_
# ===== 例題1 指数の計算 =====
def b1(terms):
    # terms=[(op,base,exp)] ; base は素数の累乗
    val=sp.Integer(1); ex_=[]; steps_t=[]; prime=None
    for op,bs,e_ in terms:
        p_,k_=ppow(bs); prime=prime or p_; assert p_==prime
        ee=sp.Rational(k_)*sp.Rational(e_); ex_.append((op,bs,e_,k_,ee)); val=val*(sp.Integer(p_)**ee if op=='*' else sp.Integer(p_)**(-ee))
    assert sp.simplify(val)==sp.Rational(val)
    expr=""
    for i,(op,bs,e_,k_,ee) in enumerate(ex_):
        expr+=("" if i==0 else (r"\times " if op=='*' else r"\div "))+pwb(bs,e_)
    steps=[("底を素数 $%d$ にそろえる"%prime,D(r"\begin{aligned}"+r"\\ ".join(r"%s&=\left(%d^{%d}\right)^{%s}=%d^{%s}"%(pwb(bs,e_),prime,k_,L(sp.Rational(e_)),prime,L(ee)) for op,bs,e_,k_,ee in ex_)+r"\end{aligned}")),
           ("指数の計算に直す","<p>"+I(r"a^m\times a^n=a^{m+n},\quad a^m\div a^n=a^{m-n}")+"。</p>"+D(r"%d^{%s}"%(prime,"".join(("" if i==0 else ("+" if op=='*' else "-"))+("("+L(ee)+")" if ee<0 else L(ee)) for i,(op,bs,e_,k_,ee) in enumerate(ex_)))+"=%d^{%s}"%(prime,L(sp.simplify(sum((ee if op=='*' else -ee) for op,bs,e_,k_,ee in ex_)))))),
           ("値を求める",D(r"%d^{%s}=%s"%(prime,L(sp.simplify(sum((ee if op=='*' else -ee) for op,bs,e_,k_,ee in ex_))),L(val))))]
    return r"次の計算をせよ。 $$"+expr+"$$",steps,L(val)
V=[[('*',27,Q(2,3)),('*',4,Q(-1,2)),('/',8,Q(-1,3))] if False else [('*',8,Q(2,3)),('*',16,Q(3,4)),('/',4,Q(-1,2))],[('*',27,Q(2,3)),('*',9,Q(-1,2)),('/',81,Q(-1,4))],[('*',32,Q(3,5)),('/',4,Q(1,2)),('*',8,Q(-1,3))],[('*',16,Q(-3,4)),('*',64,Q(2,3)),('/',8,Q(1,3))],[('*',125,Q(2,3)),('/',25,Q(-1,2)),('*',5,Q(-1))]]
o=[b1(t) for t in V]
build(Z,CH,"有理数の指数の計算",o,
 r"<p>$a^{\frac mn}=\sqrt[n]{a^m}$、$a^{-n}=\dfrac1{a^n}$。底が累乗の形なら<b>同じ素数にそろえて</b>から指数の計算：$a^m a^n=a^{m+n}$、$\dfrac{a^m}{a^n}=a^{m-n}$、$(a^m)^n=a^{mn}$。</p>",
 "バラバラの数も、素数という「同じ部品」に分解すれば、指数のたし算・ひき算だけで済む。",1)
# ===== 例題2 a^x + a^{-x} =====
def b2(a_,k):
    u=sp.Symbol('u',positive=True); sol=sp.solve(u+1/u-k,u); uu=max(sol); assert uu>1
    s2=k**2-2; s3=k**3-3*k; d2=sp.sqrt(k**2-4); assert sp.simplify(uu-1/uu-d2)==0
    steps=[("$t=%d^x$ とおく"%a_,"<p>"+I(r"%d^{-x}=\dfrac1{%d^x}=\dfrac1t"%(a_,a_))+"。"+I("x>0")+" で "+I("%d>1"%a_)+" より "+I("t>1")+"。条件は "+I(r"t+\dfrac1t=%s"%L(k))+"。</p>"),
           ("$%d^{2x}+%d^{-2x}$"%(a_,a_),D(r"t^2+\dfrac1{t^2}=\left(t+\dfrac1t\right)^2-2=\left(%s\right)^2-2=%s"%(L(k),L(s2)))),
           ("$%d^{3x}+%d^{-3x}$"%(a_,a_),D(r"t^3+\dfrac1{t^3}=\left(t+\dfrac1t\right)^3-3\left(t+\dfrac1t\right)=\left(%s\right)^3-3\cdot%s=%s"%(L(k),L(k),L(s3)))),
           ("$%d^x-%d^{-x}$"%(a_,a_),"<p>"+I(r"\left(t-\dfrac1t\right)^2=\left(t+\dfrac1t\right)^2-4=%s"%L(k**2-4))+"。"+I("t>1")+" より "+I(r"t-\dfrac1t>0")+"。</p>"+D(r"t-\dfrac1t=\sqrt{%s}=%s"%(L(k**2-4),L(d2))))]
    prob=r"$x>0$ のとき、$%d^x+%d^{-x}=%s$ である。(1) $%d^{2x}+%d^{-2x}$ (2) $%d^{3x}+%d^{-3x}$ (3) $%d^x-%d^{-x}$ の値を求めよ。"%(a_,a_,L(k),a_,a_,a_,a_,a_,a_)
    return prob,steps,r"\text{(1) }%s\quad \text{(2) }%s\quad \text{(3) }%s"%(L(s2),L(s3),L(d2))
V=[(2,Q(5,2)),(3,Q(10,3)),(2,Q(17,4)),(5,Q(26,5)),(3,Q(82,9))]
o=[b2(*v) for v in V]
build(Z,CH,"a^x+a^(-x) の値からの展開",o,
 r"<p>$t=a^x$ とおくと $a^{-x}=\dfrac1t$。対称式の公式を使う：$$t^2+\dfrac1{t^2}=\left(t+\dfrac1t\right)^2-2,\quad t^3+\dfrac1{t^3}=\left(t+\dfrac1t\right)^3-3\left(t+\dfrac1t\right),\quad \left(t-\dfrac1t\right)^2=\left(t+\dfrac1t\right)^2-4$$ 差の符号は $t>1$ か $0<t<1$ かで決める。</p>",
 "$t$ と $\\frac1t$ は和と積（積はいつも1）の関係。和さえ分かれば、2乗・3乗・差が出てくる。",2)
# ===== 例題3 指数方程式 =====
def b3(b_,r1,r2):
    t=sp.Symbol('t'); ok=[r for r in (r1,r2) if r>0]; 
    xs=[sp.log(r,b_) for r in ok]; xs=[sp.nsimplify(sp.simplify(z)) for z in xs]
    for r,xx in zip(ok,xs): assert sp.simplify(b_**xx-r)==0
    ng=[r for r in (r1,r2) if r<=0]
    eq=r"%d^{2x}%s%s%d^{x}%s%d=0"%(b_,("-" if (r1+r2)>0 else "+"),"" if abs(r1+r2)==1 else str(abs(r1+r2)),b_,"+" if r1*r2>0 else "-",abs(r1*r2))
    steps=[("$t=%d^x$ とおく"%b_,"<p>"+I(r"%d^{2x}=\left(%d^x\right)^2=t^2"%(b_,b_))+"。指数関数は常に正なので "+I("t>0")+"。</p>"+D(L(t**2-(r1+r2)*t+r1*r2)+"=0")),
           ("$t$ の2次方程式を解く",D(fac(r1)+fac(r2)+r"=0\ \Rightarrow\ t=%s,\ %s"%(L(r1),L(r2)))),
           ("$t>0$ に合うものを選ぶ","<p>"+(("<b>"+", ".join(I("t=%s"%L(r)) for r in ng)+"</b> は "+I("t>0")+" に合わない。<br>") if ng else "")+"採用するのは "+I("t=%s"%r",\ ".join(L(r) for r in ok))+"。</p>"),
           ("$x$ を求める","<p>"+"<br>".join(I(r"%d^x=%s\ \Rightarrow\ x=%s"%(b_,L(r),L(xx))) for r,xx in zip(ok,xs))+"</p>")]
    _f=sp.Integer(b_)**x
    _ap(steps,2,"<p>"+I("t=%d^x"%b_)+" のグラフ。<b>"+I("t>0")+"</b> の側にしか値がない（"+I("t\\leqq0")+" には届かない）。</p>"+graph("x241_3_%d_%d_%d"%(b_,r1,r2),[(lambda v,b=b_:float(b)**v,"#b81f36","-")],(-3,3.2),(-1.5,float(b_)**3 if b_<4 else 30),pts=[(float(xx),float(r),"t=%s"%r,0.12,0.0) for r,xx in zip(ok,xs)],yticks=[(float(r),"%s"%r) for r in ok],w=46,size=(4.0,2.8)))
    prob=r"方程式 $%s$ を解け。"%eq
    return prob,steps,r"x=%s"%r",\ ".join(L(xx) for xx in xs)
V=[(2,2,4),(3,3,9),(2,4,-1),(3,1,27),(2,8,-2)]
o=[b3(*v) for v in V]
build(Z,CH,"指数方程式（置き換え）",o,
 r"<p>$a^x=t$ とおくと、$a^{2x}=t^2$。<b>$t>0$ に注意</b>して $t$ の方程式を解く。$a^x$ は常に正だから、$t\leqq0$ の解は捨てる。$t=a^k$ の形なら $x=k$。</p>",
 "$a^x$ は「正の数しかとらない」。置き換えたら、まず $t>0$ をメモしておく。",3)
# ===== 例題4 指数不等式 =====
def b4(b_,p1,q1,m_,c_,op):
    Q1=x**2+p1*x+q1; R1=m_*(x+c_); diff=sp.expand(Q1-R1); rts=sp.solve(diff,x); assert len(rts)==2 and all(r.is_real for r in rts)
    rr=sorted(rts); big=b_>1
    # 元の不等式: b^Q1 op b'^(x+c) , b'=b^m
    flip=not big; op2=op
    if flip: op2={'<':'>','>':'<','<=':'>=','>=':'<='}[op]
    sym={'<':'<','>':'>','<=':r'\leqq','>=':r'\geqq'}
    # 解の判定
    def sat(xx):
        v1=float(Q1.subs(x,xx)); v2=float(R1.subs(x,xx)); 
        return {'<':v1<v2,'>':v1>v2,'<=':v1<=v2,'>=':v1>=v2}[op2]
    mid=(rr[0]+rr[1])/2; out=rr[1]+1
    inside=sat(mid); inc=op2 in ('<=','>=')
    if inside: ans=(L(rr[0])+(r"\leqq" if inc else "<")+"x"+(r"\leqq" if inc else "<")+L(rr[1]))
    else: ans=("x"+(r"\leqq" if inc else "<")+L(rr[0])+r",\ "+L(rr[1])+(r"\leqq" if inc else "<")+"x")
    bt=(r"\left(\dfrac12\right)" if b_==Q(1,2) else r"\left(\dfrac13\right)" if b_==Q(1,3) else "%d"%b_)
    bm=(r"\left(\dfrac1{%d}\right)"%(int(1/b_)**m_) if b_<1 else "%d"%(int(b_)**m_))
    lhs=r"%s^{%s}"%(bt,L(Q1)); rhs=r"%s^{%s}"%(bm,L(sp.expand(x+c_)) if True else "")
    base_txt="%s"%(bt)
    steps=[("底をそろえる","<p>"+I(r"%s=%s^{%d}"%(bm,bt,m_))+" なので、右辺は</p>"+D(r"%s^{%s}=\left(%s^{%d}\right)^{%s}=%s^{%s}"%(bm,L(x+c_),bt,m_,L(x+c_),bt,L(sp.expand(R1))))),
           ("底の大小で不等号の向きを決める","<p>底 "+I(L(b_))+(" は 1 より大きい" if big else " は 0 と 1 の間")+"。"+("指数の大小と不等号の向きは<b>同じ</b>。" if big else "指数の大小と不等号の向きは<b>逆</b>になる。")+"</p>"+D(L(Q1)+sym[op2]+L(sp.expand(R1)))),
           ("2次不等式を解く",D(L(diff)+sym[op2]+"0")+D(L(sp.factor(diff))+sym[op2]+"0")+"<p>"+I(r"x=%s,\ %s"%(L(rr[0]),L(rr[1])))+" が境界。</p>"+D(ans))]
    prob=r"不等式 $%s%s%s^{%s}$ を解け。"%(lhs,sym[op],bm,L(x+c_))
    return prob,steps,ans
V=[(2,-2,1,2,-1,'<'),(Q(1,2),1,-2,2,0,'>='),(3,4,-2,3,0,'>'),(Q(1,3),-1,0,2,0,'<'),(2,6,3,2,0,'>=')]
o=[b4(*v) for v in V]
build(Z,CH,"指数不等式（底の大小に注意）",o,
 r"<p>底をそろえて指数どうしを比べる。$$a>1:\ a^p<a^q\iff p<q,\qquad 0<a<1:\ a^p<a^q\iff p>q$$ <b>底が1より小さいときは不等号の向きが逆</b>になる。そのあとは2次不等式。</p>",
 "底が1より大きい指数関数は右上がり、1より小さいと右下がり。右下がりなら、大小が逆さま。",4)
f=nl("i241_e4",-2,6,[1,3],["1","3"],segs=[(1,3)],pts=[(1,"open"),(3,"open")],w=60,size=(5.6,1.2))
def fexp(ax):
    xs=np.linspace(-3,3,200); ax.plot(xs,2**xs,color="#b81f36",lw=2); ax.plot(xs,0.5**xs,color="#1f6fb8",lw=2,ls="--")
    ax.set_xlim(-3,3); ax.set_ylim(-.5,6); ax.axis("off"); ax.annotate("",xy=(3,0),xytext=(-3,0),arrowprops=dict(arrowstyle="->",lw=1)); ax.annotate("",xy=(0,6),xytext=(0,-.4),arrowprops=dict(arrowstyle="->",lw=1))
    ax.text(2.2,5.3,r"$y=2^x$",color="#b81f36",fontsize=11); ax.text(-2.9,5.3,r"$y=(\frac{1}{2})^x$",color="#1f6fb8",fontsize=11); ax.plot([0],[1],"o",color="#222",ms=4); ax.text(.15,1.2,"1",fontsize=10)
make_fig("i241_e4g",fexp,size=(4.0,2.6)); addfig(Z.E[3],1,img("i241_e4g",52)); addfig(Z.E[3],2,f)
# ===== 例題5 指数関数の最大・最小 =====
def b5(b_,p_,q_,al,be):
    t=sp.Symbol('t'); lo=sp.Integer(b_)**al; hi=sp.Integer(b_)**be; y=t**2-p_*t+q_; vx=sp.Rational(p_,2)
    cand=[(y.subs(t,lo),lo),(y.subs(t,hi),hi)]+([(y.subs(t,vx),vx)] if lo<=vx<=hi else []); mx=max(cand,key=lambda z:z[0]); mn=min(cand,key=lambda z:z[0])
    def xv(tt): return sp.nsimplify(sp.log(tt,b_)) if tt>0 else None
    comp=sp.expand(y-(t-vx)**2)
    steps=[("$t=%d^x$ とおいて範囲を求める"%b_,"<p>"+I(r"%d\leqq x\leqq %d"%(al,be))+" で "+I(r"%d^x"%b_)+" は増加するから</p>"+D(r"%s\leqq t\leqq %s"%(L(lo),L(hi)))),
           ("$y$ を $t$ の式にする",D(r"y=%d^{2x}-%d\cdot%d^x+%d=t^2-%dt+%d"%(b_,p_,b_,q_,p_,q_))+D(r"y=\left(t-%s\right)^2%s"%(L(vx),("+"+L(comp) if comp>0 else L(comp)) if comp!=0 else ""))),
           ("範囲内での最大・最小","<p>頂点 "+I(r"t=%s"%L(vx))+(" は範囲内。" if lo<=vx<=hi else " は範囲外。")+"頂点と両端の値を比べる。</p>"+D(r",\quad ".join(r"t=%s:\ y=%s"%(L(tt),L(vv)) for vv,tt in cand))),
           ("答え（$x$ の値に戻す）","<p>最大値 "+I(L(mx[0]))+"（"+I(r"x=%s"%L(xv(mx[1])))+"）、最小値 "+I(L(mn[0]))+"（"+I(r"x=%s"%L(xv(mn[1])))+"）。</p>")]
    _a=[(float(lo),float(y.subs(t,lo)),"")]
    _ap(steps,2,"<p>"+I("y=t^2-%dt+%d"%(p_,q_))+" のグラフ（太線が "+I(r"%s\leqq t\leqq %s"%(L(lo),L(hi)))+" の範囲）。</p>"+quadfig("x241_5_%d_%d_%d_%d_%d"%(b_,p_,q_,al,be),[(y.subs(t,x),"#b81f36")],pts=[(lo,y.subs(t,lo),"") ,(hi,y.subs(t,hi),"")]+([(vx,y.subs(t,vx),"")] if lo<=vx<=hi else []),axis=vx,xr=(min(0,float(lo)-1),float(hi)+1),hl=[(lo,hi)]))
    prob=r"$%d\leqq x\leqq %d$ のとき、関数 $y=%d^{2x}-%d\cdot%d^x+%d$ の最大値・最小値と、そのときの $x$ の値を求めよ。"%(al,be,b_,p_,b_,q_)
    return prob,steps,r"\text{最大値 }%s\ (x=%s),\quad \text{最小値 }%s\ (x=%s)"%(L(mx[0]),L(xv(mx[1])),L(mn[0]),L(xv(mn[1])))
V=[(2,4,1,-1,3),(3,6,2,-1,2),(2,8,10,0,3),(2,2,5,-2,2),(2,16,50,1,5)]
o=[b5(*v) for v in V]
build(Z,CH,"指数関数の最大・最小",o,
 r"<p>$a^x=t$ とおいて $t$ の2次関数にする。<b>$x$ の範囲から $t$ の範囲</b>を求める（$a>1$ なら $a^\alpha\leqq t\leqq a^\beta$）。平方完成して、範囲つき2次関数の最大・最小を調べる。</p>",
 "$x$ の動く範囲が $t$ の動く範囲に変わる。範囲の変換がこの問題の急所。",5)
UNIT=finish(Z,CH,3,0,"指数関数・対数関数","指数関数","有理数の指数、a^x+a^{-x}、指数方程式・不等式、置き換えによる最大・最小まで、指数関数の総合力を問う難問に挑みます。")
