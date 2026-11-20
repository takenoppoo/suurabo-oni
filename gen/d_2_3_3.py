# -*- coding: utf-8 -*-
# 三角関数の方程式・不等式・最大最小（数学II 三角関数）
from bh import *
Z=U_(); CH=[]
pi=sp.pi; s2=sp.sqrt(2); s3=sp.sqrt(3)
def Q(a_,b_=1): return sp.Rational(a_,b_)
def inner(b,c,var=r"\theta"):
    return ("" if b==1 else str(b))+var+("" if c==0 else (("+"+PI(c)) if c>0 else PI(c)))
FN={'sin':sp.sin,'cos':sp.cos,'tan':sp.tan}
NF={'sin':np.sin,'cos':np.cos,'tan':np.tan}
def base_sols(fn,v):
    """t=係数π の集合 (周期付き) : [(t0,period)]"""
    if fn=='sin':
        t0=sp.nsimplify(sp.asin(v)/pi); return [(t0,2),(1-t0,2)]
    if fn=='cos':
        t0=sp.nsimplify(sp.acos(v)/pi); return [(t0,2),(-t0,2)]
    t0=sp.nsimplify(sp.atan(v)/pi); return [(t0,1)]
# ===== 例題1 基本の方程式 =====
def b1(fn,b,c,v):
    lo=c; hi=2*b+c; sols=[]
    for t0,per in base_sols(fn,v):
        k=-30
        while True:
            tt=t0+per*k
            if tt>=hi: break
            if tt>=lo: sols.append(tt)
            k+=1
    sols=sorted(set(sols)); ths=[(t-c)/b for t in sols]
    for t in ths: assert 0<=t<2 and abs(float(FN[fn](float((b*t+c))*np.pi))-float(v))<1e-9
    assert len(ths)>=2
    steps=[("$t=%s$ とおいて範囲を調べる"%inner(b,c).replace(r"\theta","\\theta"),"<p>"+I(r"0\leqq\theta<2\pi")+" より</p>"+D(r"%s\leqq t<%s"%(PI(lo),PI(hi)))),
           ("$\\%s\\,t=%s$ を解く"%(fn,L(v)),"<p>単位円（"+("$y$ 座標" if fn=='sin' else "$x$ 座標" if fn=='cos' else "傾き")+"）で考えて、範囲内の "+I("t")+" を求める。</p>"+D(r"t=%s"%r",\ ".join(PI(t) for t in sols))),
           ("$\\theta$ に直す","<p>"+I(r"t=%s"%inner(b,c,r"\theta"))+" より "+I(r"\theta=\dfrac{t%s}{%d}"%(("" if c==0 else ("-"+PI(c) if c>0 else "+"+PI(-c))),b))+"。</p>"+D(r"\theta=%s"%r",\ ".join(PI(t) for t in ths)))]
    prob=r"$0\leqq\theta<2\pi$ のとき、方程式 $\%s\left(%s\right)=%s$ を解け。"%(fn,inner(b,c),L(v))
    return prob,steps,r"\theta=%s"%r",\ ".join(PI(t) for t in ths)
V=[('sin',2,Q(-1,3),Q(1,2)),('cos',2,Q(1,6),-s3/2),('sin',1,Q(-1,4),s2/2),('tan',2,Q(-1,6),1),('cos',3,Q(-1,3),Q(1,2))]
o=[b1(*v) for v in V]
build(Z,CH,"sin(bθ+c)=v の解き方",o,
 r"<p>①$t=b\theta+c$ とおき、$\theta$ の範囲から<b>$t$ の範囲</b>を求める ②$\sin t=v$（など）を<b>$t$ の範囲で</b>解く（単位円） ③$\theta=\dfrac{t-c}{b}$ に戻す。$b>1$ のとき $t$ の範囲が広がるので解の個数が増える。</p>",
 "角を $t$ という1つの文字に置き換えて、いつもの方程式にする。範囲を広げ忘れない。",1)
# ===== 例題2 sin, cos の2次方程式 =====
def eqtex(a_,b_,c_,typ):
    f2=r"\cos^2\theta" if typ=='A' else r"\sin^2\theta"; f1=r"\sin\theta" if typ=='A' else r"\cos\theta"
    return sx2([(a_,f2),(b_,f1),(c_,"")])
def sx2(terms):
    s=""
    for c_,m_ in terms:
        c_=sp.nsimplify(c_)
        if c_==0: continue
        body=(L(abs(c_)) if (abs(c_)!=1 or m_=="") else "")+m_
        s+=("-" if c_<0 else ("+" if s else ""))+body
    return s
def thetas(fn,v):
    out=[]
    for t0,per in base_sols(fn,v):
        for k in range(-3,4):
            tt=t0+per*k
            if 0<=tt<2: out.append(tt)
    return sorted(set(out))
def b2(typ,a_,r1,r2):
    b_=a_*(r1+r2); c_=-a_-a_*r1*r2; t=sp.Symbol('t')
    fn='sin' if typ=='A' else 'cos'; sq='cos' if typ=='A' else 'sin'
    ths=[]; steps=[]
    roots=sorted([r1,r2])
    quad=sp.expand(-a_*t**2+b_*t+a_+c_); assert sp.simplify(quad+a_*(t-r1)*(t-r2))==0
    ok=[r for r in roots if abs(r)<=1]; ng=[r for r in roots if abs(r)>1]
    allth=[]
    for r in ok: allth+=thetas(fn,r)
    allth=sorted(set(allth))
    vs=r"\sin\theta" if typ=='A' else r"\cos\theta"
    bt=(("+" if b_>0 else "")+cf(b_)+vs) if b_!=0 else ""
    ct=(("+"+L(c_)) if c_>0 else L(c_)) if c_!=0 else ""
    steps=[("1種類の三角関数にそろえる","<p>"+I(r"\%s^2\theta=1-\%s^2\theta"%(sq,fn))+" を使い、"+I(vs)+" だけの式にする。</p>"+D(eqtex(a_,b_,c_,typ)+"=0")+D(L(a_)+r"\left(1-\%s^2\theta\right)"%fn+bt+ct+"=0")),
           ("$t=%s$ とおいて2次方程式を解く"%vs,"<p>"+I(r"-1\leqq t\leqq1")+" に注意。整理して</p>"+D(L(quad)+"=0")+D(L(-a_)+fac(r1)+fac(r2)+r"=0\ \Rightarrow\ t=%s,\ %s"%(L(roots[0]),L(roots[1])))),
           ("範囲に合う解を選ぶ","<p>"+(("<b>"+", ".join("$t=%s$"%L(r) for r in ng)+"</b> は "+I(r"-1\leqq t\leqq1")+" に合わない（解なし）。<br>") if ng else "")+"範囲に合うのは "+I(r"t=%s"%r",\ ".join(L(r) for r in ok))+"。</p>"),
           ("$\\theta$ を求める（$0\\leqq\\theta<2\\pi$）","<p>"+"<br>".join(I(r"%s=%s"%(vs,L(r)))+" より "+I(r"\theta=%s"%r",\ ".join(PI(t_) for t_ in thetas(fn,r))) for r in ok)+"</p>")]
    prob=r"$0\leqq\theta<2\pi$ のとき、方程式 $%s=0$ を解け。"%eqtex(a_,b_,c_,typ)
    return prob,steps,r"\theta=%s"%r",\ ".join(PI(t_) for t_ in allth)
V=[('A',2,1,Q(-1,2)),('A',2,Q(1,2),-2),('B',2,-1,Q(1,2)),('B',2,1,Q(-1,2)),('A',2,Q(-1,2),-1)]
o=[b2(*v) for v in V]
build(Z,CH,"sin と cos が混ざった2次方程式",o,
 r"<p>$\sin^2\theta+\cos^2\theta=1$ で<b>1種類にそろえる</b>。$\sin\theta=t$（または $\cos\theta=t$）とおいて2次方程式を解き、<b>$-1\leqq t\leqq1$ に合うものだけ</b>を残して $\theta$ を求める。</p>",
 "2種類の登場人物を1種類にまとめる。解の中に「ありえない値（2など）」が混ざるのが罠。",2)
# ===== 例題3 不等式 =====
CNT3=0
def intervals(fn,b,c,op,v):
    th=np.linspace(0,2*np.pi,40001)[:-1]; f=NF[fn](b*th+float(c)*np.pi); vv=float(v)
    m={'>':f>vv,'>=':f>=vv-1e-12,'<':f<vv,'<=':f<=vv+1e-12}[op]
    iv=[];start=None
    for i,mm in enumerate(m):
        if mm and start is None: start=i
        if (not mm) and start is not None: iv.append((start,i-1)); start=None
    if start is not None: iv.append((start,len(m)-1))
    out=[]
    for a_,b_ in iv:
        lo_=sp.nsimplify(th[a_]/np.pi if a_>0 else 0).limit_denominator(24); hi_=sp.nsimplify((th[b_]+(th[1]-th[0]))/np.pi).limit_denominator(24) if b_<len(th)-1 else sp.Integer(2)
        out.append((lo_,hi_))
    return out
def b3(fn,b,c,op,v):
    global CNT3
    CNT3+=1; ivs=intervals(fn,b,c,op,v)
    f=lambda t_:float(NF[fn](b*t_+float(c)*np.pi))
    xt=[(float(k*np.pi/2),pil(k,2)) for k in range(1,5)]
    hl=[(float(a_*pi),float(b_*pi),"#1f6fb8") for a_,b_ in ivs]
    fig=trigfig("i233_e3_%d"%CNT3,f,(-.3,2*np.pi+.5),(-1.5,1.5),xt,[(1,"1"),(-1,"-1")],hl=hl,hlines=[(float(v),"#b81f36")],w=62)
    sym={'>':r">",'>=':r"\geqq",'<':r"<",'<=':r"\leqq"}[op]
    lo=c; hi=2*b+c
    base=base_sols(fn,v)
    steps=[("$t=%s$ とおいて範囲を調べる"%inner(b,c),D(r"%s\leqq t<%s"%(PI(lo),PI(hi)))),
           ("グラフで $y=\\%s\\,t$ と $y=%s$ の上下を見る"%(fn,L(v)),"<p>"+I(r"\%s\,t%s%s"%(fn,sym,L(v)))+" を満たす部分を、グラフ（または単位円）から読む。境界は "+I(r"\%s\,t=%s"%(fn,L(v)))+" の解。</p>"),
           ("$\\theta$ の範囲に直す","<p>$\\theta$ のグラフにして図に示す（青い太線が答えの範囲、赤い破線が $y=%s$）。</p>"%L(v)+fig),
           ("答え",D(r"\ \text{または}\ ".join(("%s%s\\theta%s%s"%(PI(a_),"<" if op in ('>','<') and a_!=0 else r"\leqq" if True else "",("<" if (op in ('>','<') and b_!=2) else r"\leqq" if b_!=2 else "<"),PI(b_))) for a_,b_ in ivs)))]
    prob=r"$0\leqq\theta<2\pi$ のとき、不等式 $\%s\left(%s\right)%s%s$ を解け。"%(fn,inner(b,c),sym,L(v))
    ans=r"\ ,\ ".join(("%s%s\\theta%s%s"%(PI(a_),("<" if (op in ('>','<') and a_!=0) else r"\leqq"),("<" if (op in ('>','<') and b_!=2) else r"\leqq" if b_!=2 else "<"),PI(b_))) for a_,b_ in ivs)
    return prob,steps,ans
V=[('sin',1,Q(-1,6),'>',Q(1,2)),('cos',1,Q(1,3),'<=',Q(-1,2)),('sin',2,0,'>=',s3/2),('cos',2,Q(-1,3),'>',0),('sin',1,Q(1,6),'<',-s2/2)]
o=[b3(*v) for v in V]
build(Z,CH,"三角不等式",o,
 r"<p>$t=b\theta+c$ とおいて $t$ の範囲で不等式を解く。<b>グラフ（または単位円）</b>で「どの範囲で値が $v$ より大きいか（小さいか）」を読み、境界の値を $\theta$ に戻す。$>,<$ は端を含まず、$\geqq,\leqq$ は端を含む。</p>",
 "波が基準線の上に出ている部分（または下に潜っている部分）の「θ の幅」を答える。",3)
# ===== 例題4 2次関数にして最大最小 =====
def b4(a_,b_,c_):
    t=sp.Symbol('t'); y=sp.expand(-a_*t**2+b_*t+a_+c_); vx=sp.Rational(b_,2*a_); vy=y.subs(t,vx)
    cand=[(y.subs(t,-1),-1),(y.subs(t,1),1)]+([(vy,vx)] if -1<=vx<=1 else [])
    mx=max(cand,key=lambda z:z[0]); mn=min(cand,key=lambda z:z[0])
    comp=-a_*(t-vx)**2+vy; assert sp.expand(comp-y)==0
    steps=[("$\\sin\\theta=t$ とおいて1文字にする","<p>"+I(r"\cos^2\theta=1-\sin^2\theta")+"、"+I(r"-1\leqq t\leqq1")+"。</p>"+D(r"y=%s\left(1-t^2\right)%s%s=%s"%(L(a_),("+"+L(b_)+"t" if b_>0 else L(b_)+"t"),("+"+L(c_) if c_>0 else L(c_)),L(y)))),
           ("平方完成する",D(r"y=%s"%(L(comp)))),
           ("$-1\\leqq t\\leqq1$ での最大・最小","<p>頂点 "+I(r"t=%s"%L(vx))+(" は範囲の内側。" if -1<=vx<=1 else " は範囲の外側。")+" 両端と頂点の値を比べる。</p>"+D(r",\quad ".join(r"t=%s:\ y=%s"%(L(tt),L(vv)) for vv,tt in cand))),
           ("答え","<p>最大値 "+I(L(mx[0]))+"（"+I(r"\sin\theta=%s"%L(mx[1]))+"）、最小値 "+I(L(mn[0]))+"（"+I(r"\sin\theta=%s"%L(mn[1]))+"）。</p>")]
    prob=r"関数 $y=%s\cos^2\theta%s\sin\theta%s$ の最大値・最小値を求めよ。（$\theta$ はすべての実数）"%(L(a_),("+"+L(b_) if b_>0 else L(b_)),("+"+L(c_) if c_>0 else L(c_)) if c_!=0 else "")
    return prob,steps,r"\text{最大値 }%s\ (\sin\theta=%s),\quad \text{最小値 }%s\ (\sin\theta=%s)"%(L(mx[0]),L(mx[1]),L(mn[0]),L(mn[1]))
V=[(2,4,-1),(2,-2,0),(1,-3,0),(3,6,-2),(2,3,-2)]
o=[b4(*v) for v in V]
build(Z,CH,"1つの三角関数にそろえて最大・最小",o,
 r"<p>$\cos^2\theta=1-\sin^2\theta$ で $\sin\theta=t$ にそろえ、<b>$t$ の2次関数</b>にする。$t$ の範囲は $-1\leqq t\leqq1$。<b>範囲つきの2次関数の最大・最小</b>（頂点と両端）として解く。</p>",
 "文字が $t$ に置き換わると、ただの2次関数。「$t$ の動ける範囲」を絶対に忘れない。",4)
# ===== 例題5 sinθ+cosθ=t の置き換え =====
def b5(q_,r_):
    t=sp.Symbol('t'); y=sp.expand((t**2-1)+q_*t+r_); vx=sp.Rational(-q_,2)
    ends=[-s2,s2]; cand=[(sp.expand(y.subs(t,e)),e) for e in ends]+([(y.subs(t,vx),vx)] if -s2<=vx<=s2 else [])
    num=lambda z:float(z[0]); mx=max(cand,key=num); mn=min(cand,key=num)
    comp=sp.expand(y-(t-vx)**2); 
    steps=[("$t=\\sin\\theta+\\cos\\theta$ とおく","<p>"+I(r"t=\sqrt2\sin\left(\theta+\dfrac\pi4\right)")+" だから "+I(r"-\sqrt2\leqq t\leqq\sqrt2")+"。</p>"),
           ("$\\sin\\theta\\cos\\theta$ を $t$ で表す","<p>"+I(r"t^2=1+2\sin\theta\cos\theta")+" より</p>"+D(r"2\sin\theta\cos\theta=t^2-1")),
           ("$y$ を $t$ の2次関数にする",D(r"y=(t^2-1)%s%s=%s"%(("+"+L(q_)+"t" if q_>0 else L(q_)+"t"),("+"+L(r_) if r_>0 else L(r_)) if r_!=0 else "",L(y)))+D(r"y=\left(t%s\right)^2%s"%(("+"+L(-vx) if vx<0 else "-"+L(vx)) if vx!=0 else "",("+"+L(comp) if comp>0 else L(comp)) if comp!=0 else ""))),
           ("$-\\sqrt2\\leqq t\\leqq\\sqrt2$ での最大・最小","<p>頂点 "+I(r"t=%s"%L(vx))+(" は範囲の内側。" if -s2<=vx<=s2 else " は範囲の外側。")+"</p>"+D(r",\quad ".join(r"t=%s:\ y=%s"%(L(e),L(sp.simplify(vv))) for vv,e in cand))),
           ("答え","<p>最大値 "+I(L(sp.simplify(mx[0])))+"、最小値 "+I(L(sp.simplify(mn[0])))+"。</p>")]
    prob=r"$0\leqq\theta<2\pi$ のとき、$y=2\sin\theta\cos\theta%s(\sin\theta+\cos\theta)%s$ の最大値・最小値を求めよ。"%(("+"+L(q_) if q_>0 else L(q_)),(("+"+L(r_) if r_>0 else L(r_)) if r_!=0 else ""))
    return prob,steps,r"\text{最大値 }%s,\quad \text{最小値 }%s"%(L(sp.simplify(mx[0])),L(sp.simplify(mn[0])))
V=[(-2,0),(1,0),(-4,1),(3,-1),(-1,2)]
o=[b5(*v) for v in V]
build(Z,CH,"sinθ+cosθ=t とおく最大・最小",o,
 r"<p>$\sin\theta+\cos\theta=t$ とおくと、$\sin\theta\cos\theta=\dfrac{t^2-1}2$。$t=\sqrt2\sin\left(\theta+\dfrac\pi4\right)$ より<b>$-\sqrt2\leqq t\leqq\sqrt2$</b>。$\sin\theta$ と $\cos\theta$ の対称式は、すべて $t$ で書ける。</p>",
 "$\\sin$ と $\\cos$ の和と積はセット。和を $t$ とおけば積も $t$ で書ける。",5)
UNIT=finish(Z,CH,2,2,"三角関数","三角関数の方程式・不等式・最大最小","基本の方程式、sinとcosが混ざった2次方程式、三角不等式、2次関数への帰着、sinθ+cosθの置き換えまで、三角関数の総合問題に挑みます。")
