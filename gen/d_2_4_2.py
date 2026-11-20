# -*- coding: utf-8 -*-
# 対数関数（数学II 指数関数・対数関数）
from bh import *
import math
Z=U_(); CH=[]
def Q(a_,b_=1): return sp.Rational(a_,b_)
def lg(b_): return r"\log_{%s}"%(b_ if not isinstance(b_,sp.Rational) or b_.q==1 else L(b_))
# ===== 例題1 底の変換 =====
def b1(a_,b_,k,m):
    v=(1+Q(k,2))*(1+Q(m,2))
    assert abs((math.log(b_,a_)+math.log(b_**k,a_**2))*(math.log(a_,b_)+math.log(a_**m,b_**2))-float(v))<1e-9
    steps=[("底を $%d$ にそろえる（底の変換公式）"%a_,"<p>"+I(r"\log_c b=\dfrac{\log_a b}{\log_a c}")+"。</p>"+D(r"\log_{%d}%d^{%d}=\dfrac{\log_{%d}%d^{%d}}{\log_{%d}%d^2}=\dfrac{%d\log_{%d}%d}{2}=%s\log_{%d}%d"%(a_**2,b_,k,a_,b_,k,a_,a_,k,a_,b_,L(Q(k,2)),a_,b_))),
           ("第1の括弧をまとめる",D(r"\log_{%d}%d+\log_{%d}%d^{%d}=\log_{%d}%d+%s\log_{%d}%d=%s\log_{%d}%d"%(a_,b_,a_**2,b_,k,a_,b_,L(Q(k,2)),a_,b_,L(1+Q(k,2)),a_,b_))),
           ("第2の括弧をまとめる","<p>同様に底を "+I(str(b_))+" にそろえる。</p>"+D(r"\log_{%d}%d+\log_{%d}%d^{%d}=\log_{%d}%d+%s\log_{%d}%d=%s\log_{%d}%d"%(b_,a_,b_**2,a_,m,b_,a_,L(Q(m,2)),b_,a_,L(1+Q(m,2)),b_,a_))),
           ("積を計算する","<p>"+I(r"\log_a b\cdot\log_b a=1")+" を使う。</p>"+D(r"%s\log_{%d}%d\cdot%s\log_{%d}%d=%s\cdot%s\cdot1=%s"%(L(1+Q(k,2)),a_,b_,L(1+Q(m,2)),b_,a_,L(1+Q(k,2)),L(1+Q(m,2)),L(v))))]
    prob=r"次の値を求めよ。 $$\left(\log_{%d}%d+\log_{%d}%d^{%d}\right)\left(\log_{%d}%d+\log_{%d}%d^{%d}\right)$$"%(a_,b_,a_**2,b_,k,b_,a_,b_**2,a_,m)
    return prob,steps,L(v)
V=[(2,3,2,2),(3,5,4,2),(2,5,6,4),(5,2,2,6),(3,2,4,4)]
o=[b1(*v) for v in V]
build(Z,CH,"底の変換公式と対数の計算",o,
 r"<p>$\log_a b\cdot\log_b a=1$。底の変換：$\log_c b=\dfrac{\log_a b}{\log_a c}$。<b>底を1つにそろえ</b>、$\log_a M^k=k\log_a M$ で係数を出す。$\log_{a^n}b^m=\dfrac mn\log_a b$。</p>",
 "底が違うのは「単位が違う」のと同じ。単位（底）をそろえてから計算する。",1)
# ===== 例題2 対数方程式 =====
def b2(b_,p_,q_,n_):
    N=sp.Integer(b_)**n_; eq=sp.expand((x+p_)*(x+q_)-N); rts=sp.solve(eq,x); dom=max(-p_,-q_); ok=[r for r in rts if r>dom]; ng=[r for r in rts if r<=dom]
    assert len(ok)==1 and all(r==int(r) for r in rts)
    steps=[("真数条件","<p>真数は正："+I("%s>0"%L(x+p_))+"、"+I("%s>0"%L(x+q_))+"。共通部分は</p>"+D(r"x>%d"%dom)),
           ("1つの対数にまとめる","<p>"+I(r"\log_a M+\log_a N=\log_a MN")+"、"+I(r"n=\log_a a^n")+"。</p>"+D(r"\log_{%d}\{%s%s\}=%d\ \Rightarrow\ %s%s=%d^{%d}=%d"%(b_,"("+L(x+p_)+")","("+L(x+q_)+")",n_,"("+L(x+p_)+")","("+L(x+q_)+")",b_,n_,N))),
           ("2次方程式を解く",D(L(eq)+"=0")+D(L(sp.factor(eq))+r"=0\ \Rightarrow\ x=%s"%r",\ ".join(L(r) for r in sorted(rts)))),
           ("真数条件で選ぶ","<p>"+I(r"x>%d"%dom)+" を満たすのは "+I("x=%s"%L(ok[0]))+"。"+(("<b>"+I("x=%s"%L(ng[0]))+"</b> は真数条件に反するので解でない。") if ng else "")+"</p>")]
    prob=r"方程式 $\log_{%d}%s+\log_{%d}%s=%d$ を解け。"%(b_,"("+L(x+p_)+")",b_,"("+L(x+q_)+")",n_) if p_!=0 and q_!=0 else r"方程式 $\log_{%d}%s+\log_{%d}%s=%d$ を解け。"%(b_,("x" if p_==0 else "("+L(x+p_)+")"),b_,("x" if q_==0 else "("+L(x+q_)+")"),n_)
    return prob,steps,r"x=%s"%L(ok[0])
V=[(2,-1,1,3),(3,0,-6,3),(2,3,-1,5),(3,1,-5,3),(5,0,-4,1)]
o=[b2(*v) for v in V]
build(Z,CH,"対数方程式（真数条件）",o,
 r"<p>①<b>真数条件</b>（真数 $>0$）を先に書く ②$\log_a M+\log_a N=\log_a MN$ などで1つにまとめ、$\log_a A=n\iff A=a^n$ ③解いたら真数条件に合うか確認。</p>",
 "対数の中身（真数）は正の数しか入れない。解けても、入場資格（真数条件）がなければ失格。",2)
# ===== 例題3 対数不等式 =====
def b3(b_,p_,q_,op,n_):
    big=b_>1; N=sp.Rational(b_)**n_; dom=max(-p_,-q_); eq=sp.expand((x+p_)*(x+q_)-N); rts=sorted(sp.solve(eq,x)); assert all(r.is_real for r in rts) and len(rts)==2
    sym={'<':'<','>':'>','<=':r'\leqq','>=':r'\geqq'}; op2=op if big else {'<':'>','>':'<','<=':'>=','>=':'<='}[op]
    inc=op2 in ('<=','>=')
    def sat(xx): v=float(((xx+p_)*(xx+q_))); n2=float(N); return {'<':v<n2,'>':v>n2,'<=':v<=n2,'>=':v>=n2}[op2]
    # 領域: 2次不等式の解と x>dom の共通部分
    mid=(rts[0]+rts[1])/2
    if sat(mid): reg=("(%s,%s)"%(rts[0],rts[1]))
    # 数値走査で区間を求める
    import numpy as np
    xs_=np.linspace(float(dom)+1e-6,float(dom)+30,300001); vals=((xs_+p_)*(xs_+q_)); m={'<':vals<float(N),'>':vals>float(N),'<=':vals<=float(N)+1e-9,'>=':vals>=float(N)-1e-9}[op2]
    idx=np.where(m)[0]; lo=float(xs_[idx[0]]); hi=float(xs_[idx[-1]]); infinite=idx[-1]==len(xs_)-1
    lo_e=(sp.nsimplify(round(lo,3)) if lo>float(dom)+1e-3 else dom)
    hi_e=sp.nsimplify(round(hi,3))
    lo_incl=inc and lo>float(dom)+1e-3
    ans=(L(lo_e)+(r"\leqq" if lo_incl else "<")+"x") + ("" if infinite else (r"\leqq" if inc else "<")+L(hi_e))
    if infinite: ans=("x"+(r"\geqq" if lo_incl else ">")+L(lo_e))
    steps=[("真数条件",D(r"x>%d"%dom)),
           ("底に注意して不等式を作る","<p>"+I(r"\log_{%s}\{%s%s\}%s%d"%(L(b_) if b_.q==1 else L(b_),"("+L(x+p_)+")","("+L(x+q_)+")",sym[op],n_))+"。底 "+I(L(b_))+(" は 1 より大きいので向きは<b>そのまま</b>。" if big else " は 1 より小さいので向きは<b>逆</b>。")+"</p>"+D(r"%s%s%s%s%s^{%d}=%s"%("("+L(x+p_)+")","("+L(x+q_)+")",sym[op2],"",("\\left(%s\\right)"%L(b_) if not big else str(b_)),n_,L(N)))),
           ("2次不等式を解く",D(L(eq)+sym[op2]+"0")+D(L(sp.factor(eq))+sym[op2]+"0")),
           ("真数条件との共通部分をとる","<p>2次不等式の解と "+I("x>%d"%dom)+" の共通部分：</p>"+D(ans))]
    prob=r"不等式 $\log_{%s}%s+\log_{%s}%s%s%d$ を解け。"%(L(b_),("x" if p_==0 else "("+L(x+p_)+")"),L(b_),("x" if q_==0 else "("+L(x+q_)+")"),sym[op],n_)
    return prob,steps,ans
V=[(2,-1,1,'<',3),(Q(1,2),0,-2,'>=',-3),(3,0,-6,'>',3),(Q(1,3),0,-2,'<',-1),(2,3,-1,'>=',5)]
V=[(sp.Integer(2),-1,1,'<',3),(Q(1,2),0,-2,'>=',-3),(sp.Integer(3),0,-6,'>',3),(Q(1,3),0,-2,'<',-1),(sp.Integer(2),3,-1,'>=',5)]
o=[b3(*v) for v in V]
build(Z,CH,"対数不等式（底と真数条件）",o,
 r"<p>$$a>1:\ \log_a A<\log_a B\iff 0<A<B,\qquad 0<a<1:\ \log_a A<\log_a B\iff A>B>0$$ 底が1より小さいときは<b>向きが逆</b>。必ず<b>真数条件との共通部分</b>で答える。</p>",
 "底が小さい対数は右下がり。右下がりなら、大小が逆さま。最後に入場資格（真数条件）を確認。",3)
f=nl("i242_e3",0,6,[1,3],["1","3"],segs=[(1,3)],pts=[(1,"open"),(3,"open")],w=60,size=(5.6,1.2))
addfig(Z.E[2],3,f)
# ===== 例題4 対数の2次関数 =====
def b4(b_,n_,al,be):
    t=sp.Symbol('t'); y=t*(n_-t); lo=sp.Integer(al); hi=sp.Integer(be); vx=sp.Rational(n_,2)
    cand=[(y.subs(t,lo),lo),(y.subs(t,hi),hi)]+([(y.subs(t,vx),vx)] if lo<=vx<=hi else []); mx=max(cand,key=lambda z:z[0]); mn=min(cand,key=lambda z:z[0])
    xv=lambda tt:sp.Integer(b_)**tt
    comp=-(t-vx)**2+vx**2
    steps=[("$t=\\log_{%d}x$ とおく"%b_,"<p>"+I(r"\log_{%d}\dfrac{%d^{%d}}{x}=%d-\log_{%d}x=%d-t"%(b_,b_,n_,n_,b_,n_))+"。</p>"+D(r"y=t(%d-t)"%n_)),
           ("$t$ の範囲",D(r"%s\leqq x\leqq %s\ \Rightarrow\ %d\leqq t\leqq %d"%(L(xv(lo)),L(xv(hi)),al,be))+"<p>（底 "+I(str(b_))+" は 1 より大きいので増加関数。）</p>"),
           ("平方完成して最大・最小",D(r"y=-t^2+%dt=-\left(t-%s\right)^2+%s"%(n_,L(vx),L(vx**2)))+"<p>頂点 "+I(r"t=%s"%L(vx))+(" は範囲内。" if lo<=vx<=hi else " は範囲外。")+"</p>"+D(r",\quad ".join(r"t=%s:\ y=%s"%(L(tt),L(vv)) for vv,tt in cand))),
           ("答え（$x$ に戻す）","<p>最大値 "+I(L(mx[0]))+"（"+I(r"x=%s"%L(xv(mx[1])))+"）、最小値 "+I(L(mn[0]))+"（"+I(r"x=%s"%L(xv(mn[1])))+"）。</p>")]
    prob=r"$%s\leqq x\leqq %s$ のとき、関数 $y=\log_{%d}x\cdot\log_{%d}\dfrac{%d}{x}$ の最大値・最小値と、そのときの $x$ の値を求めよ。"%(L(xv(lo)),L(xv(hi)),b_,b_,b_**n_)
    return prob,steps,r"\text{最大値 }%s\ (x=%s),\quad \text{最小値 }%s\ (x=%s)"%(L(mx[0]),L(xv(mx[1])),L(mn[0]),L(xv(mn[1])))
V=[(2,4,-1,4),(3,2,-2,1),(2,6,0,5),(2,2,-3,2),(3,4,-1,3)]
o=[b4(*v) for v in V]
build(Z,CH,"対数関数の最大・最小",o,
 r"<p>$\log_a x=t$ とおくと、$\log_a(\text{積})$ は $t$ の和・差で書ける。$t$ の2次関数にして、<b>$x$ の範囲から $t$ の範囲</b>を求め、範囲つきの最大・最小を調べる。</p>",
 "対数をまとめて $t$ とおけば、ただの2次関数。範囲も $t$ に直すのを忘れない。",4)
# ===== 例題5 大小比較 =====
def b5(m1,m2,k):
    A=math.log2(m1); B=0.5*math.log2(m2); C=k/2
    vals={"P":(A,m1),"Q":(B,math.sqrt(m2)),"R":(C,math.sqrt(2**k))}
    order=sorted(vals.items(),key=lambda z:z[1][0])
    assert abs(order[0][1][0]-order[1][1][0])>1e-3 and abs(order[1][1][0]-order[2][1][0])>1e-3
    # 引数の2乗を比べる
    args={"P":m1**2,"Q":m2,"R":2**k}
    steps=[("すべて底が $2$ の対数にそろえる","<p>"+I(r"\log_4 %d=\dfrac{\log_2 %d}{\log_2 4}=\dfrac12\log_2 %d=\log_2\sqrt{%d}"%(m2,m2,m2,m2))+"、"+I(r"\dfrac{%d}{2}=\log_2 2^{%s}=\log_2\sqrt{%d}"%(k,L(Q(k,2)),2**k))+"。</p>"+D(r"P=\log_2 %d,\quad Q=\log_2\sqrt{%d},\quad R=\log_2\sqrt{%d}"%(m1,m2,2**k))),
           ("真数を比べる（底 2 は 1 より大きい）","<p>"+I(r"\log_2 X")+" は増加関数なので、<b>真数の大小</b>がそのまま対数の大小。真数を2乗して比べる。</p>"+D(r"%d^2=%d,\quad \left(\sqrt{%d}\right)^2=%d,\quad \left(\sqrt{%d}\right)^2=%d"%(m1,m1**2,m2,m2,2**k,2**k))),
           ("大小を決める","<p>"+I(r"%s<%s<%s"%tuple(str(args[n]) for n,_ in order))+" より</p>"+D(r"%s<%s<%s"%tuple(n for n,_ in order)))]
    prob=r"3つの数 $P=\log_2 %d,\ Q=\log_4 %d,\ R=\dfrac{%d}{2}$ を、小さい順に並べよ。"%(m1,m2,k)
    return prob,steps,r"%s<%s<%s"%tuple(n for n,_ in order)
V=[(3,10,3),(5,24,5),(7,45,5),(6,30,5),(9,70,6)]
o=[b5(*v) for v in V]
build(Z,CH,"対数の大小比較",o,
 r"<p>大小を比べるには、<b>底をそろえて真数を比べる</b>。底が1より大きければ $\log_a X$ は増加関数、$0<a<1$ なら減少関数。有理数は $\dfrac k2=\log_2 2^{k/2}$ のように対数に直す。</p>",
 "全員を同じものさし（底2）で測り直す。ものさしの目盛りが大きいほど、数も大きい。",5)
UNIT=finish(Z,CH,3,1,"指数関数・対数関数","対数関数","底の変換、対数方程式・不等式、対数の最大・最小、対数の大小比較まで、対数関数の総合力を問う難問に挑みます。")
