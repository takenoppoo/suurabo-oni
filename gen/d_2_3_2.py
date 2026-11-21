# -*- coding: utf-8 -*-
# 加法定理（数学II 三角関数）
from bh import *
Z=U_(); CH=[]
pi=sp.pi; s2=sp.sqrt(2); s3=sp.sqrt(3)
def V_(e): return L(sp.radsimp(sp.simplify(e)))
def Q(a_,b_): return sp.Rational(a_,b_)
# ===== 例題1 特殊角の和・差で値を求める =====
def b1(d1,d2,sign):
    A=sp.Rational(d1,180)*pi; B=sp.Rational(d2,180)*pi; T=A+sign*B; tot=sp.Rational(d1+sign*d2)
    sA,cA,sB,cB=sp.sin(A),sp.cos(A),sp.sin(B),sp.cos(B); tA,tB=sp.tan(A),sp.tan(B)
    if sign>0:
        sv=sA*cB+cA*sB; cv=cA*cB-sA*sB; tv=(tA+tB)/(1-tA*tB)
    else:
        sv=sA*cB-cA*sB; cv=cA*cB+sA*sB; tv=(tA-tB)/(1+tA*tB)
    assert sp.simplify(sv-sp.sin(T))==0 and sp.simplify(cv-sp.cos(T))==0 and sp.simplify(tv-sp.tan(T))==0
    ss="+" if sign>0 else "-"; sg2="-" if sign>0 else "+"
    steps=[("角を特殊角の和（差）にする",D(r"%d^\circ=%d^\circ%s%d^\circ"%(d1+sign*d2,d1,ss,d2))),
           ("$\\sin$ の加法定理",D(r"\sin%d^\circ=\sin%d^\circ\cos%d^\circ%s\cos%d^\circ\sin%d^\circ=%s\cdot%s%s%s\cdot%s=%s"%(d1+sign*d2,d1,d2,ss,d1,d2,V_(sA),V_(cB),ss,V_(cA),V_(sB),V_(sv)))),
           ("$\\cos$ の加法定理",D(r"\cos%d^\circ=\cos%d^\circ\cos%d^\circ%s\sin%d^\circ\sin%d^\circ=%s\cdot%s%s%s\cdot%s=%s"%(d1+sign*d2,d1,d2,sg2,d1,d2,V_(cA),V_(cB),sg2,V_(sA),V_(sB),V_(cv)))),
           ("$\\tan$ の加法定理",D(r"\tan%d^\circ=\dfrac{\tan%d^\circ%s\tan%d^\circ}{1%s\tan%d^\circ\tan%d^\circ}=\dfrac{%s%s%s}{1%s%s\cdot%s}=%s"%(d1+sign*d2,d1,ss,d2,sg2,d1,d2,V_(tA),ss,V_(tB),sg2,V_(tA),V_(tB),V_(tv))))]
    fgs=ucsum("u232_1_%d_%d_%s"%(d1,d2,"p" if sign>0 else "m"),d1,d2,sign,sp.latex(sp.radsimp(sp.simplify(sp.cos(T)))),sp.latex(sp.radsimp(sp.simplify(sp.sin(T)))))
    steps[0]=(steps[0][0],steps[0][1]+"<p>単位円で見ると、"+I(r"%d^\circ"%tot)+" の動径は、"+I(r"%d^\circ"%d1)+" の動径を "+I(r"%d^\circ"%d2)+(" 分だけ進めた" if sign>0 else " 分だけ戻した")+"もの。点 "+I("P")+" の座標が "+I(r"(\cos%d^\circ,\ \sin%d^\circ)"%(tot,tot))+"。</p>"+fgs)
    prob=r"加法定理を用いて、$\sin%d^\circ,\ \cos%d^\circ,\ \tan%d^\circ$ の値を求めよ。"%(tot,tot,tot)
    return prob,steps,r"\sin%d^\circ=%s,\ \cos%d^\circ=%s,\ \tan%d^\circ=%s"%(tot,V_(sv),tot,V_(cv),tot,V_(tv))
V=[(45,60,-1),(45,30,1),(60,45,1),(135,30,1),(210,45,1)]
V=[(45,30,1),(60,45,-1),(60,45,1),(135,30,-1),(30,45,1)]
o=[b1(*v) for v in V]
build(Z,CH,"特殊角の和・差による値",o,
 r"<p>$$\sin(\alpha\pm\beta)=\sin\alpha\cos\beta\pm\cos\alpha\sin\beta$$ $$\cos(\alpha\pm\beta)=\cos\alpha\cos\beta\mp\sin\alpha\sin\beta$$ $$\tan(\alpha\pm\beta)=\dfrac{\tan\alpha\pm\tan\beta}{1\mp\tan\alpha\tan\beta}$$ 求めたい角を<b>値が分かる角（$30^\circ,45^\circ,60^\circ$ など）の和・差</b>に直す。$\pm$ と $\mp$ の符号の向きに注意。</p>",
 "知らない角は、知っている角の足し算・引き算に分解する。公式の符号の「ねじれ」は cos だけ。",1)
# ===== 例題2 sin α, cos β から =====
def b2(sa,qa,cb,qb):
    ca=sp.sqrt(1-sa**2)*(1 if qa in (1,4) else -1); sb=sp.sqrt(1-cb**2)*(1 if qb in (1,2) else -1)
    sp_=sa*cb+ca*sb; cm=ca*cb+sa*sb
    qn={1:"第1",2:"第2",3:"第3",4:"第4"}
    assert sp.sign(sa)==(1 if qa in (1,2) else -1) and sp.sign(cb)==(1 if qb in (1,4) else -1)
    steps=[("$\\cos\\alpha$ を求める","<p>"+I(r"\alpha")+" は"+qn[qa]+"象限の角。"+I(r"\sin^2\alpha+\cos^2\alpha=1")+" より</p>"+D(r"\cos\alpha=%s\sqrt{1-\left(%s\right)^2}=%s"%("" if qa in (1,4) else "-",L(sa),L(ca)))),
           ("$\\sin\\beta$ を求める","<p>"+I(r"\beta")+" は"+qn[qb]+"象限の角。</p>"+D(r"\sin\beta=%s\sqrt{1-\left(%s\right)^2}=%s"%("" if qb in (1,2) else "-",L(cb),L(sb)))),
           ("$\\sin(\\alpha+\\beta)$",D(r"\sin(\alpha+\beta)=\sin\alpha\cos\beta+\cos\alpha\sin\beta=\left(%s\right)\left(%s\right)+\left(%s\right)\left(%s\right)=%s"%(L(sa),L(cb),L(ca),L(sb),L(sp_)))),
           ("$\\cos(\\alpha-\\beta)$",D(r"\cos(\alpha-\beta)=\cos\alpha\cos\beta+\sin\alpha\sin\beta=\left(%s\right)\left(%s\right)+\left(%s\right)\left(%s\right)=%s"%(L(ca),L(cb),L(sa),L(sb),L(cm))))]
    _n=__import__("hashlib").md5(repr((str(sa),qa,str(cb),qb)).encode()).hexdigest()[:6]
    steps[0]=(steps[0][0],steps[0][1]+"<p>単位円で見ると、"+I(r"\alpha")+" は第%d象限で、点 "%qa+I("P")+" の "+I("y")+" 座標が "+I(r"\sin\alpha=%s"%L(sa))+"。</p>"+ucfig("u232_2a_"+_n,float(sp.atan2(sa,ca)),L(ca),L(sa),r"\alpha","",w=42))
    steps[1]=(steps[1][0],steps[1][1]+"<p>単位円で見ると、"+I(r"\beta")+" は第%d象限で、点 "%qb+I("Q")+" の "+I("x")+" 座標が "+I(r"\cos\beta=%s"%L(cb))+"。</p>"+ucfig("u232_2b_"+_n,float(sp.atan2(sb,cb)),L(cb),L(sb),r"\beta","",w=42))
    prob=r"$\alpha$ は%s象限、$\beta$ は%s象限の角で、$\sin\alpha=%s$、$\cos\beta=%s$ である。$\sin(\alpha+\beta)$ と $\cos(\alpha-\beta)$ の値を求めよ。"%(qn[qa],qn[qb],L(sa),L(cb))
    return prob,steps,r"\sin(\alpha+\beta)=%s,\quad \cos(\alpha-\beta)=%s"%(L(sp_),L(cm))
V=[(sp.Rational(3,5),2,sp.Rational(5,13),1),(sp.Rational(4,5),1,sp.Rational(-12,13),2),(sp.Rational(-5,13),3,sp.Rational(3,5),4),(sp.Rational(-3,5),4,sp.Rational(-8,17),3),(sp.Rational(8,17),2,sp.Rational(-4,5),3)]
o=[b2(*v) for v in V]
build(Z,CH,"象限と加法定理",o,
 r"<p>$\sin\alpha$ だけ分かっているなら、$\cos\alpha$ を $\sin^2\alpha+\cos^2\alpha=1$ から出し、<b>象限で符号</b>を決める。$\alpha,\beta$ の4つの値 $\sin\alpha,\cos\alpha,\sin\beta,\cos\beta$ がそろえば、加法定理が使える。</p>",
 "加法定理は4つの部品（$\\sin\\alpha,\\cos\\alpha,\\sin\\beta,\\cos\\beta$）を使う。まず部品をそろえる。",2)
# ===== 例題3 2倍角・半角 =====
def b3(cv,q_):
    th=sp.Symbol('theta'); sv=sp.sqrt(1-cv**2)*(1 if q_ in (1,2) else -1)
    s2t=2*sv*cv; c2t=2*cv**2-1; t2t=s2t/c2t
    # 半角（θ/2 の象限は 0<θ<2π なら θ/2 in (0,π) sin>0）
    hs=sp.sqrt((1-cv)/2); hc=sp.sqrt((1+cv)/2)*(1 if q_ in (1,4) else -1)  # θ/2 ∈ (0,π/2) if q∈{1,... }
    # 0<θ<π(q=1,2): θ/2∈(0,π/2) cos>0 ; π<θ<2π(q=3,4): θ/2∈(π/2,π) cos<0
    hc=sp.sqrt((1+cv)/2)*(1 if q_ in (1,2) else -1)
    assert sp.simplify(hs**2-(1-cv)/2)==0
    steps=[("$\\sin\\theta$ を求める","<p>"+I(r"\theta")+" は第%d象限（"%q_+I(r"%s"%("0<\\theta<\\pi" if q_ in (1,2) else "\\pi<\\theta<2\\pi"))+"）。</p>"+D(r"\sin\theta=%s\sqrt{1-\left(%s\right)^2}=%s"%("" if q_ in (1,2) else "-",L(cv),L(sv)))),
           ("2倍角の公式",D(r"\sin2\theta=2\sin\theta\cos\theta=2\left(%s\right)\left(%s\right)=%s"%(L(sv),L(cv),L(s2t)))+D(r"\cos2\theta=2\cos^2\theta-1=2\left(%s\right)^2-1=%s"%(L(cv),L(c2t)))),
           ("半角の公式で $\\sin\\dfrac\\theta2$","<p>"+I(r"\sin^2\dfrac\theta2=\dfrac{1-\cos\theta}{2}")+"。"+I(r"\dfrac\theta2")+" の範囲は "+I(r"0<\dfrac\theta2<\pi")+" なので "+I(r"\sin\dfrac\theta2>0")+"。</p>"+D(r"\sin^2\dfrac\theta2=\dfrac{1-\left(%s\right)}2=%s\ \Rightarrow\ \sin\dfrac\theta2=%s"%(L(cv),L((1-cv)/2),L(hs)))),
           ("$\\cos\\dfrac\\theta2$","<p>"+I(r"\cos^2\dfrac\theta2=\dfrac{1+\cos\theta}{2}")+"。"+I(r"\dfrac\theta2")+" は"+("第1象限（"+I(r"0<\dfrac\theta2<\dfrac\pi2")+"）なので正" if q_ in (1,2) else "第2象限（"+I(r"\dfrac\pi2<\dfrac\theta2<\pi")+"）なので負")+"。</p>"+D(r"\cos\dfrac\theta2=%s"%L(hc)))]
    _n=__import__("hashlib").md5(repr((str(cv),q_)).encode()).hexdigest()[:6]
    steps[0]=(steps[0][0],steps[0][1]+ucfig("u232_3_"+_n,float(sp.atan2(sv,cv)),L(cv),L(sv),r"\theta","",w=42))
    prob=r"$0<\theta<2\pi$ で $\cos\theta=%s$、$\theta$ は第%d象限の角である。$\sin2\theta$、$\cos2\theta$、$\sin\dfrac\theta2$、$\cos\dfrac\theta2$ の値を求めよ。"%(L(cv),q_)
    return prob,steps,r"\sin2\theta=%s,\ \cos2\theta=%s,\ \sin\dfrac\theta2=%s,\ \cos\dfrac\theta2=%s"%(L(s2t),L(c2t),L(hs),L(hc))
V=[(sp.Rational(3,5),1),(sp.Rational(-3,5),2),(sp.Rational(7,25),4),(sp.Rational(-5,13),3),(sp.Rational(-4,5),2)]
o=[b3(*v) for v in V]
build(Z,CH,"2倍角・半角の公式",o,
 r"<p>2倍角：$\sin2\theta=2\sin\theta\cos\theta$、$\cos2\theta=\cos^2\theta-\sin^2\theta=2\cos^2\theta-1=1-2\sin^2\theta$。<br>半角：$\sin^2\dfrac\theta2=\dfrac{1-\cos\theta}2$、$\cos^2\dfrac\theta2=\dfrac{1+\cos\theta}2$。<b>半角の符号は $\dfrac\theta2$ の範囲</b>で決める。</p>",
 "半角は「2乗の形」でしか出てこない。2乗を開くとき、ルートの前の符号を忘れない。",3)
# ===== 例題4 三角関数の合成 =====
def b4(a_,b_):
    r_=sp.sqrt(a_**2+b_**2); ca=a_/r_; sa=b_/r_; al=sp.atan2(sa,ca); alp=sp.nsimplify(al/pi); assert alp.q<=12
    steps=[("$a\\sin\\theta+b\\cos\\theta$ の合成","<p>"+I(r"a\sin\theta+b\cos\theta=r\sin(\theta+\alpha)")+"、"+I(r"r=\sqrt{a^2+b^2}")+"、"+I(r"\cos\alpha=\dfrac ar,\ \sin\alpha=\dfrac br")+"。</p>"+D(r"r=\sqrt{(%s)^2+(%s)^2}=%s"%(L(a_),L(b_),L(r_)))),
           ("角 $\\alpha$ を決める",D(r"\cos\alpha=%s,\quad \sin\alpha=%s\ \Rightarrow\ \alpha=%s"%(L(ca),L(sa),PI(alp)))),
           ("合成した式",D(r"y=%s\sin\theta%s\cos\theta=%s\sin\left(\theta%s\right)"%(L(a_),("+"+L(b_) if b_>0 else L(b_)),L(r_),("+"+PI(alp) if alp>0 else PI(alp))))),
           ("最大値・最小値と $\\theta$","<p>"+I(r"0\leqq\theta<2\pi")+" で "+I(r"\theta%s"%("+"+PI(alp) if alp>0 else PI(alp)))+" の範囲は "+I(r"%s\leqq\theta%s<%s"%(PI(alp),("+"+PI(alp) if alp>0 else PI(alp)),PI(2+alp)))+"。</p>")]
    # 最大最小の θ
    tmax=[t_ for t_ in [sp.Rational(1,2)-alp+2*k for k in (-1,0,1)] if 0<=t_<2]; tmin=[t_ for t_ in [-sp.Rational(1,2)-alp+2*k for k in (-1,0,1,2)] if 0<=t_<2]
    steps[3]=("最大値・最小値と $\\theta$","<p>"+I(r"-1\leqq\sin(\theta+\alpha)\leqq1")+"、"+I(r"\theta+\alpha")+" は "+I(r"\pi")+" の周期を含む範囲を動くので、最大・最小をとる。</p>"+D(r"\text{最大値 }%s\ \ (\theta=%s),\qquad \text{最小値 }-%s\ \ (\theta=%s)"%(L(r_),PI(tmax[0]),L(r_),PI(tmin[0]))))
    _n=__import__("hashlib").md5(repr((str(a_),str(b_))).encode()).hexdigest()[:6]
    steps[1]=(steps[1][0],steps[1][1]+"<p>点 "+I("(a,\\ b)=(%s,\\ %s)"%(L(a_),L(b_)))+" の向き（原点からの角）が "+I(r"\alpha")+"。単位円上では次の点になる。</p>"+ucfig("u232_4_"+_n,float(sp.atan2(sa,ca)),L(ca),L(sa),r"\alpha","",w=42))
    prob=r"$0\leqq\theta<2\pi$ のとき、$y=%s\sin\theta%s\cos\theta$ の最大値・最小値と、そのときの $\theta$ の値を求めよ。"%(L(a_),("+"+L(b_) if b_>0 else L(b_)))
    return prob,steps,r"\text{最大値 }%s\ (\theta=%s),\quad \text{最小値 }-%s\ (\theta=%s)"%(L(r_),PI(tmax[0]),L(r_),PI(tmin[0]))
V=[(s3,1),(1,s3),(1,-1),(-1,s3),(s3,-3)]
o=[b4(*v) for v in V]
build(Z,CH,"三角関数の合成",o,
 r"<p>$$a\sin\theta+b\cos\theta=\sqrt{a^2+b^2}\,\sin(\theta+\alpha)$$ ただし $\cos\alpha=\dfrac a{\sqrt{a^2+b^2}},\ \sin\alpha=\dfrac b{\sqrt{a^2+b^2}}$。点 $(a,b)$ を座標平面にとり、原点からの距離が $r$、$x$ 軸との角が $\alpha$。</p>",
 "$\\sin$ と $\\cos$ の足し算は、ひとつの波に合体できる。波の大きさは $\\sqrt{a^2+b^2}$。",4)
# ===== 例題5 tan の加法定理で角を求める =====
def b5(a_,b_):
    tv=(a_+b_)/(1-a_*b_); assert tv==1
    steps=[("$\\tan(\\alpha+\\beta)$ を計算する",D(r"\tan(\alpha+\beta)=\dfrac{\tan\alpha+\tan\beta}{1-\tan\alpha\tan\beta}=\dfrac{%s+%s}{1-%s\cdot%s}=\dfrac{%s}{%s}=%s"%(L(a_),L(b_),L(a_),L(b_),L(a_+b_),L(1-a_*b_),L(tv)))),
           ("$\\alpha+\\beta$ の範囲を調べる","<p>"+I(r"\tan\alpha=%s>0,\ \tan\beta=%s>0"%(L(a_),L(b_)))+" で "+I(r"0<\alpha,\beta<\dfrac\pi2")+" だから "+I(r"0<\alpha+\beta<\pi")+"。</p>"),
           ("角を決める","<p>"+I(r"0<\alpha+\beta<\pi")+" の範囲で "+I(r"\tan(\alpha+\beta)=1")+" となる角は "+I(r"\dfrac\pi4")+" のみ。</p>"+D(r"\alpha+\beta=\dfrac{\pi}{4}"))]
    prob=r"$\alpha,\ \beta$ は $0<\alpha<\dfrac\pi2,\ 0<\beta<\dfrac\pi2$ を満たし、$\tan\alpha=%s,\ \tan\beta=%s$ である。$\alpha+\beta$ の値を求めよ。"%(L(a_),L(b_))
    return prob,steps,r"\alpha+\beta=\dfrac\pi4"
V=[(sp.Rational(1,2),sp.Rational(1,3)),(sp.Rational(1,4),sp.Rational(3,5)),(sp.Rational(1,5),sp.Rational(2,3)),(sp.Rational(1,6),sp.Rational(5,7)),(sp.Rational(1,7),sp.Rational(3,4))]
o=[b5(*v) for v in V]
build(Z,CH,"tan の加法定理と角の決定",o,
 r"<p>$$\tan(\alpha+\beta)=\dfrac{\tan\alpha+\tan\beta}{1-\tan\alpha\tan\beta}$$ 値から角を決めるときは、<b>角の範囲</b>を先に調べておく。範囲の中で $\tan$ がその値になる角は1つだけ。</p>",
 "値だけでは角は決まらない。「どの範囲にいるか」とセットで1つに決まる。",5)
UNIT=finish(Z,CH,2,1,"三角関数","加法定理","加法定理による特殊角の値、象限と符号、2倍角・半角、三角関数の合成、tanの加法定理と角の決定まで、公式を使いこなす難問に挑みます。")
