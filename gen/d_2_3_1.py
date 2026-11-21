# -*- coding: utf-8 -*-
# 一般角と三角関数のグラフ（数学II 三角関数）
from bh import *
import math
Z=U_(); CH=[]
pi=sp.pi
# ===== 例題1 弧度法・扇形 =====
def b1(deg,rd,r_,th):
    rad1=sp.Rational(deg,180); dg2=sp.Rational(rd[0],rd[1])*180; th_=sp.Rational(*th); ll=r_*th_; S=sp.Rational(1,2)*r_*r_*th_
    steps=[("(1) 度数→弧度（$180^\\circ=\\pi$）",D(r"%d^\circ=%d\times\dfrac{\pi}{180}=%s"%(deg,deg,PI(rad1)))),
           ("(2) 弧度→度数",D(r"%s=%s\times\dfrac{180^\circ}{\pi}=%s^\circ"%(PI(sp.Rational(*rd)),L(sp.Rational(*rd)),L(dg2)))),
           ("(3) 扇形の弧の長さ","<p>半径 "+I("r")+"、中心角 "+I(r"\theta")+"（ラジアン）の扇形：</p>"+D(r"l=r\theta,\qquad S=\dfrac12r^2\theta=\dfrac12rl")+D(r"l=%d\times%s=%s"%(r_,PI(th_),PI(ll)))),
           ("(3) 扇形の面積",D(r"S=\dfrac12\times%d^2\times%s=%s"%(r_,PI(th_),PI(S))))]
    prob=r"(1) $%d^\circ$ を弧度で表せ。(2) $%s$ を度数で表せ。(3) 半径 $%d$、中心角 $%s$ の扇形の弧の長さ $l$ と面積 $S$ を求めよ。"%(deg,PI(sp.Rational(*rd)),r_,PI(th_))
    return prob,steps,r"\text{(1) }%s\quad \text{(2) }%s^\circ\quad \text{(3) }l=%s,\ S=%s"%(PI(rad1),L(dg2),PI(ll),PI(S))
V=[(150,(7,12),6,(5,6)),(225,(5,18),8,(3,4)),(-240,(13,12),9,(2,3)),(315,(11,30),10,(3,5)),(75,(4,9),12,(5,8))]
o=[b1(*v) for v in V]
build(Z,CH,"弧度法と扇形の弧の長さ・面積",o,
 r"<p>$180^\circ=\pi$ ラジアン。$1\text{ rad}=\dfrac{180^\circ}\pi$。<br>半径 $r$、中心角 $\theta$（ラジアン）の扇形：弧の長さ $l=r\theta$、面積 $S=\dfrac12r^2\theta=\dfrac12rl$。</p>",
 "弧度法は「半径と同じ長さの弧に対する角が1」。角×半径がそのまま弧の長さになる。",1)
# ===== 例題2 一般角の三角関数の値 =====
def quad(t0):
    if t0<sp.Rational(1,2): return 1
    if t0<1: return 2
    if t0<sp.Rational(3,2): return 3
    return 4
def val1(fn_name,a_,b_):
    th=sp.Rational(a_,b_); t0=th-2*sp.floor(th/2)  # 0<=t0<2 (πの係数)
    qd=quad(t0); ref={1:t0,2:1-t0,3:t0-1,4:2-t0}[qd]
    fn={'sin':sp.sin,'cos':sp.cos,'tan':sp.tan}[fn_name]; v=sp.simplify(fn(th*pi)); v2=sp.simplify(fn(ref*pi))
    sg={'sin':{1:1,2:1,3:-1,4:-1},'cos':{1:1,2:-1,3:-1,4:1},'tan':{1:1,2:-1,3:1,4:-1}}[fn_name][qd]
    assert sp.simplify(v-sg*v2)==0
    sgtxt="正" if sg>0 else "負"
    s=("<p>"+I(r"\%s %s"%(fn_name,PI(th)))+"：")
    if th!=t0: s+=I(r"%s=%s%+d\cdot2\pi"%(PI(th),PI(t0),int(sp.floor(th/2)))) +"（周期 "+I(r"2\pi")+" で "+I(r"0\leqq\theta<2\pi")+" に直す）。"
    s+="角 "+I(PI(t0))+" は第%d象限、基準角 "%qd+I(PI(ref))+"。第%d象限で "%qd+I(r"\%s"%fn_name)+" は"+sgtxt+"。</p>"
    s+=D(r"\%s %s=%s\%s %s=%s"%(fn_name,PI(th),"" if sg>0 else "-",fn_name,PI(ref),L(v)))
    nm="u231_%s_%s%d_%d"%(fn_name,"m" if a_<0 else "p",abs(a_),b_)
    cxl=sp.latex(sp.nsimplify(sp.cos(t0*pi))); syl=sp.latex(sp.nsimplify(sp.sin(t0*pi)))
    s+="<p>単位円で確かめる。角 "+I(PI(t0))+" の動径と単位円の交点 "+I("P")+" の座標が "+I(r"(\cos\theta,\ \sin\theta)")+" になる。</p>"
    s+=ucfig(nm,float(t0)*math.pi,cxl,syl,PI(t0),(PI(ref) if ref!=t0 else ""),w=46)
    s+="<p>"+I("P")+" の座標から "+I(r"\cos\theta=%s,\ \sin\theta=%s"%(cxl,syl))+("、"+I(r"\tan\theta=\dfrac{\sin\theta}{\cos\theta}=%s"%L(sp.simplify(sp.sin(t0*pi)/sp.cos(t0*pi)))) if fn_name=="tan" else "")+"。</p>"
    return s,v
def b2(trip):
    parts=[];vals=[]
    for fn_name,a_,b_ in trip:
        s,v=val1(fn_name,a_,b_); parts.append((r"\%s\,%s"%(fn_name,PI(sp.Rational(a_,b_))),s,v))
    steps=[("$%s$ の値"%p[0],p[1]) for p in parts]
    prob=r"次の値を求めよ。 $$"+r",\qquad ".join(p[0] for p in parts)+"$$"
    return prob,steps,r"\quad ".join("%s=%s"%(p[0],L(p[2])) for p in parts)
V=[[('sin',7,6),('cos',-5,4),('tan',11,3)],[('cos',5,3),('sin',-3,4),('tan',7,6)],[('tan',-5,4),('sin',11,6),('cos',13,6)],[('sin',17,6),('tan',-7,3),('cos',-7,6)],[('cos',11,4),('tan',5,6),('sin',-4,3)]]
o=[b2(v) for v in V]
build(Z,CH,"一般角の三角関数の値",o,
 r"<p>①周期 $2\pi$ で $0\leqq\theta<2\pi$ に直す ②<b>象限</b>を調べる ③<b>基準角</b>（$\theta$ から軸までの鋭角）を求める ④象限による符号をつける。<br>符号：第1象限は全部正、第2象限は $\sin$ のみ正、第3象限は $\tan$ のみ正、第4象限は $\cos$ のみ正。</p>",
 "角を「基準角」に折りたたんで、符号は象限で決める。値の大きさは基準角の値だけでよい。",2)
def fq(ax):
    th=7*np.pi/6; ax.set_aspect("equal"); ax.set_xlim(-1.6,1.6); ax.set_ylim(-1.45,1.45); ax.axis("off")
    cc=np.linspace(0,2*np.pi,300); ax.plot(np.cos(cc),np.sin(cc),color="#555",lw=1.3)
    ax.annotate("",xy=(1.5,0),xytext=(-1.5,0),arrowprops=dict(arrowstyle="->",lw=1)); ax.annotate("",xy=(0,1.4),xytext=(0,-1.4),arrowprops=dict(arrowstyle="->",lw=1))
    ax.plot([0,np.cos(th)],[0,np.sin(th)],color="#b81f36",lw=2); ax.plot([np.cos(th)],[np.sin(th)],"o",color="#b81f36")
    t2=np.linspace(0,th,100); ax.plot(.35*np.cos(t2),.35*np.sin(t2),color="#1f6fb8",lw=1.4)
    ax.text(np.cos(th)-.25,np.sin(th)-.12,r"$P$",fontsize=11); ax.text(.45,.38,r"$\frac{7}{6}\pi$",fontsize=10,color="#1f6fb8"); ax.text(1.05,-.18,"1",fontsize=9); ax.text(-1.2,-.18,"-1",fontsize=9)
make_fig("i231_e2",fq,size=(3.2,3.0))
# ===== 例題3 相互関係 =====
def b3(kind,v,q_):
    # kind 'sin','cos','tan'  q_ 象限
    s,c,t=sp.symbols('s c t'); 
    if kind=='sin': sv=v; cv2=1-sv**2; cv=sp.sqrt(cv2)*(1 if q_ in (1,4) else -1); 
    elif kind=='cos': cv=v; sv2=1-cv**2; sv=sp.sqrt(sv2)*(1 if q_ in (1,2) else -1)
    if kind=='sin': tv=sv/cv
    else: tv=sv/cv
    if kind=='sin': assert sp.sign(sv)==(1 if q_ in (1,2) else -1)
    if kind=='cos': assert sp.sign(cv)==(1 if q_ in (1,4) else -1)
    qn={1:"第1象限",2:"第2象限",3:"第3象限",4:"第4象限"}[q_]
    if kind=='sin':
        steps=[("$\\cos\\theta$ を求める","<p>"+I(r"\sin^2\theta+\cos^2\theta=1")+" より</p>"+D(r"\cos^2\theta=1-\left(%s\right)^2=%s"%(L(sv),L(cv2)))+"<p>"+I(r"\theta")+" は"+qn+"なので "+I(r"\cos\theta")+("は正" if cv>0 else "は負")+"。</p>"+D(r"\cos\theta=%s"%L(cv))),
               ("$\\tan\\theta$ を求める",D(r"\tan\theta=\dfrac{\sin\theta}{\cos\theta}=%s\div\left(%s\right)=%s"%(L(sv),L(cv),L(tv))))]
        prob=r"$\theta$ は%s の角で $\sin\theta=%s$ である。$\cos\theta$、$\tan\theta$ の値を求めよ。"%(qn,L(sv)); ans=r"\cos\theta=%s,\quad \tan\theta=%s"%(L(cv),L(tv))
    else:
        steps=[("$\\sin\\theta$ を求める","<p>"+I(r"\sin^2\theta=1-\cos^2\theta")+" より</p>"+D(r"\sin^2\theta=1-\left(%s\right)^2=%s"%(L(cv),L(sv2)))+"<p>"+I(r"\theta")+" は"+qn+"なので "+I(r"\sin\theta")+("は正" if sv>0 else "は負")+"。</p>"+D(r"\sin\theta=%s"%L(sv))),
               ("$\\tan\\theta$ を求める",D(r"\tan\theta=\dfrac{\sin\theta}{\cos\theta}=\left(%s\right)\div\left(%s\right)=%s"%(L(sv),L(cv),L(tv))))]
        prob=r"$\theta$ は%s の角で $\cos\theta=%s$ である。$\sin\theta$、$\tan\theta$ の値を求めよ。"%(qn,L(cv)); ans=r"\sin\theta=%s,\quad \tan\theta=%s"%(L(sv),L(tv))
    thp=float(sp.atan2(sv,cv)); thp=thp+2*math.pi if thp<0 else thp
    fg=ucfig("u231_x3_%s_%s_%d"%(kind,str(v).replace("/","_").replace("-","m"),q_),thp,L(cv),L(sv),r"\theta","",w=44)
    steps[0]=(steps[0][0],"<p>"+qn+"の角 "+I(r"\theta")+" の動径と単位円の交点を "+I("P")+" とすると、"+I("P")+" の座標は "+I(r"(\cos\theta,\ \sin\theta)")+"。象限で符号が決まる。</p>"+fg+steps[0][1])
    return prob,steps,ans
V=[('sin',sp.Rational(3,5),2),('cos',sp.Rational(-5,13),3),('sin',sp.Rational(-8,17),4),('cos',sp.Rational(7,25),1),('sin',sp.Rational(-12,13),3)]
o=[b3(*v) for v in V]
build(Z,CH,"象限と三角関数の相互関係",o,
 r"<p>$$\sin^2\theta+\cos^2\theta=1,\qquad \tan\theta=\dfrac{\sin\theta}{\cos\theta}$$ 2乗から値を求めたあと、<b>象限で符号を決める</b>のを忘れない。</p>",
 "2乗してから平方根をとると、答えが「プラスとマイナス」の2つ出る。どちらか選ぶのは象限。",3)
# ===== 例題4 y=A sin(bθ-c) のグラフ =====
CNT=0
def b4(A,b,c):
    global CNT
    CNT+=1; ph=c/b; f=lambda t_:A*np.sin(b*t_-float(c*pi))
    # 最大・最小のθ（0≤θ<2π）
    thmax=sorted([(sp.Rational(1,2)+c+2*k)/b for k in range(-6,12) if 0<=(sp.Rational(1,2)+c+2*k)/b<2]); thmin=sorted([(-sp.Rational(1,2)+c+2*k)/b for k in range(-6,12) if 0<=(-sp.Rational(1,2)+c+2*k)/b<2])
    per=sp.Rational(2)/b
    xt=[(float(k*sp.pi/2),pil(k,2)) for k in range(1,5)]
    pts=[(float(t_*pi),A,"",0,0) for t_ in thmax]+[(float(t_*pi),-A,"",0,0) for t_ in thmin]
    fig=trigfig("i231_e4_%d"%CNT,f,(-.3,2*np.pi+.5),(-A-1,A+1.2),xt,[(A,str(A)),(-A,str(-A))],pts=pts,hlines=[(A,"#bbb"),(-A,"#bbb")])
    sgn="-" if c>0 else "+"
    steps=[("周期・振幅・平行移動を読む","<p>"+I("y=%s\\sin\\left(%s\\theta%s\\right)=%s\\sin %s\\left(\\theta%s\\right)"%(A,("" if b==1 else b),(("-"+PI(c)) if c>0 else ("+"+PI(-c))),A,("" if b==1 else b),(("-"+PI(ph)) if ph>0 else ("+"+PI(-ph)))))+"。</p>"+D(r"\text{周期}=\dfrac{2\pi}{%d}=%s,\quad \text{振幅}=%d,\quad \text{右へ }%s\text{ だけ平行移動}"%(b,PI(per),A,PI(ph)))),
           ("最大値・最小値","<p>"+I(r"-1\leqq\sin(\cdots)\leqq1")+" だから</p>"+D(r"\text{最大値 }%d,\qquad \text{最小値 }%d"%(A,-A))),
           ("最大・最小になる $\\theta$（$0\\leqq\\theta<2\\pi$）","<p>最大："+I(r"%s\theta-%s=\dfrac{\pi}{2}+2k\pi"%(b if b!=1 else "",PI(c)))+" より </p>"+D(r"\theta=%s"%r",\ ".join(PI(t_) for t_ in thmax))+"<p>最小："+I(r"%s\theta-%s=-\dfrac{\pi}{2}+2k\pi"%(b if b!=1 else "",PI(c)))+" より</p>"+D(r"\theta=%s"%r",\ ".join(PI(t_) for t_ in thmin))),
           ("グラフ","<p>赤い曲線がグラフ（点は最大・最小）。</p>"+fig)]
    prob=r"関数 $y=%d\sin\left(%s\theta-%s\right)$（$0\leqq\theta<2\pi$）の周期、最大値・最小値と、そのときの $\theta$ の値を求め、グラフをかけ。"%(A,("" if b==1 else b),PI(c))
    return prob,steps,r"\text{周期 }%s,\ \text{最大値 }%d\ (\theta=%s),\ \text{最小値 }%d\ (\theta=%s)"%(PI(per),A,r",\ ".join(PI(t_) for t_ in thmax),-A,r",\ ".join(PI(t_) for t_ in thmin))
V=[(2,2,sp.Rational(1,3)),(3,1,sp.Rational(1,4)),(1,3,sp.Rational(1)),(2,2,sp.Rational(1,2)),(3,2,sp.Rational(1,3))]
o=[b4(*v) for v in V]
build(Z,CH,"y=A sin(bθ−c) の周期・最大最小・グラフ",o,
 r"<p>$y=A\sin(b\theta-c)=A\sin b\left(\theta-\dfrac cb\right)$：振幅 $|A|$、周期 $\dfrac{2\pi}{|b|}$、$y=A\sin b\theta$ を $\theta$ 軸方向に $\dfrac cb$ だけ平行移動したグラフ。最大・最小は 括弧の中が $\dfrac\pi2$、$-\dfrac\pi2$ のとき。</p>",
 "$\\sin$ の波を、「縦に $A$ 倍、横に $\\frac1b$ 倍に縮めて、右へずらす」。",4)
# ===== 例題5 扇形の面積の最大 =====
def b5(Lg):
    r=sp.Symbol('r'); S=r*(sp.Rational(Lg,2)-r); rm=sp.Rational(Lg,4); Sm=S.subs(r,rm); ll=Lg-2*rm; th=ll/rm
    steps=[("弧の長さ $l$ を半径 $r$ で表す","<p>周の長さは "+I("2r+l=%d"%Lg)+"、したがって</p>"+D(r"l=%d-2r\quad(0<r<%d)"%(Lg,Lg//2))),
           ("面積を $r$ の式にする",D(r"S=\dfrac12rl=\dfrac12r(%d-2r)=-r^2+%dr"%(Lg,Lg//2))),
           ("平方完成する",D(r"S=-\left(r-%s\right)^2+%s"%(L(rm),L(Sm)))),
           ("最大値と中心角","<p>"+I("r=%s"%L(rm))+"（"+I("0<r<%d"%(Lg//2))+" を満たす）のとき最大。このとき "+I(r"l=%d-2\cdot%s=%s"%(Lg,L(rm),L(ll)))+"、</p>"+D(r"\theta=\dfrac lr=\dfrac{%s}{%s}=%d\ \text{(ラジアン)}"%(L(ll),L(rm),th)))]
    prob=r"周の長さが $%d$ の扇形のうち、面積が最大になるものについて、そのときの半径、中心角（ラジアン）、面積の最大値を求めよ。"%Lg
    return prob,steps,r"\text{半径 }%s,\ \text{中心角 }%d\ \text{ラジアン},\ \text{面積の最大値 }%s"%(L(rm),th,L(Sm))
V=[20,24,32,36,28]
o=[b5(v) for v in V]
build(Z,CH,"周が一定の扇形の面積の最大",o,
 r"<p>扇形の周の長さ $=2r+l$（半径2本＋弧）。面積 $S=\dfrac12rl$。条件から $l$ を $r$ で表して<b>1文字にし、平方完成</b>で最大値を求める。</p>",
 "周の長さが決まっているので、半径を変えれば弧も変わる。面積を半径だけの式にすれば、ただの2次関数。",5)
UNIT=finish(Z,CH,2,0,"三角関数","一般角と三角関数のグラフ","弧度法と扇形、一般角の値、象限と相互関係、グラフの周期と最大・最小、扇形の最大まで、三角関数の基礎を徹底的に固める難問に挑みます。")
