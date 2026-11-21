# -*- coding: utf-8 -*-
from bh import *
import numpy as np, math
Z=U_(); CH=[]; R=sp.Rational; th=sp.symbols("th"); pi=sp.pi
# 6 sinα=a から sin3α
def b6(a):
    a=R(a); s3=3*a-4*a**3
    st=[("3倍角の公式","<p>"+D(r"\sin3\alpha=3\sin\alpha-4\sin^3\alpha")+"</p>"),
        ("代入",D(r"3\cdot%s-4\cdot\left(%s\right)^3=%s"%(L(a),L(a),L(s3))))]
    # verify numerically
    al=math.asin(float(a)); assert abs(math.sin(3*al)-float(s3))<1e-12
    return r"$0<\alpha<\dfrac\pi2$ で $\sin\alpha=%s$ のとき、$\sin3\alpha$ の値を求めよ。"%L(a),st,L(s3)
o=[b6(a) for a in [R(1,2),R(3,5),R(1,3),R(4,5),R(2,3)]]
build(Z,CH,"sin3α の値（3倍角の公式）",o,"<p>3倍角：$\\sin3\\alpha=3\\sin\\alpha-4\\sin^3\\alpha$。$\\sin\\alpha$ が分かれば $\\cos\\alpha$ を求めずに計算できる。</p>","角が3倍になっても、sin だけで書ける公式がある。",6)
# 7 2直線のなす角
def b7(m1,m2):
    t=sp.simplify((m1-m2)/(1+m1*m2)); 
    ang=math.degrees(math.atan(float(t))) ; 
    st=[("傾きと角","<p>直線 "+I("y=%s\\,x"%L(m1))+" の傾きは "+I(r"\tan\alpha=%s"%L(m1))+"、"+I("y=%s\\,x"%L(m2))+" は "+I(r"\tan\beta=%s"%L(m2))+"。</p>"),
        ("加法定理","<p>"+D(r"\tan(\alpha-\beta)=\dfrac{\tan\alpha-\tan\beta}{1+\tan\alpha\tan\beta}=\dfrac{%s-%s}{1+%s\cdot%s}=%s"%(L(m1),L(m2),L(m1),L(m2),L(t)))),
        ("なす角","<p>"+I(r"\tan\theta=%s"%L(abs(t)))+(" より "+I(r"\theta=%s"%("45^\\circ" if abs(t)==1 else ("30^\\circ" if abs(t)==sp.sqrt(3)/3 else ("60^\\circ" if abs(t)==sp.sqrt(3) else "\\theta"))))+"。" if abs(t) in (1,sp.sqrt(3)/3,sp.sqrt(3)) else "。")+"</p>")]
    return r"2直線 $y=%s\,x$ と $y=%s\,x$ のなす鋭角を $\theta$ とするとき、$\tan\theta$ の値を求めよ。"%(L(m1),L(m2)),st,r"\tan\theta=%s"%L(abs(t))
o=[b7(*v) for v in [(3,2),(2,R(1,3)),(R(1,2),R(1,3)),(5,2),(4,R(1,4))]]
build(Z,CH,"2直線のなす角の tan（加法定理）",o,"<p>傾きは $\\tan$（x軸との角）。なす角 $=\\alpha-\\beta$ だから $\\tan(\\alpha-\\beta)=\\dfrac{m_1-m_2}{1+m_1m_2}$。</p>","傾きを角度にみなし、加法定理で差の角を出す。",7)
# 8 tanα=t から sin2α, cos2α
def b8(t):
    t=R(t); s2=2*t/(1+t*t); c2=(1-t*t)/(1+t*t)
    a=math.atan(float(t)); assert abs(math.sin(2*a)-float(s2))<1e-12 and abs(math.cos(2*a)-float(c2))<1e-12
    st=[("tan のまま2倍角","<p>"+D(r"\sin2\alpha=\dfrac{2\tan\alpha}{1+\tan^2\alpha},\qquad \cos2\alpha=\dfrac{1-\tan^2\alpha}{1+\tan^2\alpha}")),
        ("代入",D(r"\sin2\alpha=\dfrac{2\cdot%s}{1+%s}=%s,\qquad \cos2\alpha=\dfrac{1-%s}{1+%s}=%s"%(L(t),L(t*t),L(s2),L(t*t),L(t*t),L(c2))))]
    return r"$0<\alpha<\dfrac\pi2$ で $\tan\alpha=%s$ のとき、$\sin2\alpha,\ \cos2\alpha$ の値を求めよ。"%L(t),st,r"\sin2\alpha=%s,\ \cos2\alpha=%s"%(L(s2),L(c2))
o=[b8(t) for t in [2,3,R(1,2),R(3,4),R(5,12)]]
build(Z,CH,"tanα から sin2α・cos2α",o,"<p>$\\sin2\\alpha=2\\sin\\alpha\\cos\\alpha$ の分母を $1=\\sin^2+\\cos^2$ で割ると、$\\tan\\alpha$ だけの式になる。</p>","sin も cos も出さず、tan だけで押し通す。",8)
# 9 合成して方程式
def b9(a,b,c):
    # a sin th + b cos th = c on [0,2pi)
    r=sp.sqrt(a*a+b*b); al=sp.atan2(b,a)
    sols=[]
    for n in range(0,3600):
        t=n*math.pi/1800
        pass
    sol=sp.nsolve if False else None
    af,bf,cf_=float(a),float(b),float(c); rf=math.hypot(af,bf); alf=math.atan2(bf,af)
    base=math.asin(cf_/rf); roots=sorted({round(((base-alf)%(2*math.pi)),9),round(((math.pi-base-alf)%(2*math.pi)),9)})
    roots=[t for t in roots if t<2*math.pi-1e-9]
    assert all(abs(af*math.sin(t)+bf*math.cos(t)-cf_)<1e-6 for t in roots)
    ang=lambda t:"%d^\\circ"%round(math.degrees(t))
    vals=[round(math.degrees(t)) for t in roots]
    st=[("合成","<p>"+D(r"%s\sin\theta+%s\cos\theta=%s\sin\left(\theta+%s\right)"%(L(a),L(b),L(sp.simplify(r)),ang(float(al))))),
        ("方程式","<p>"+D(r"%s\sin\left(\theta+%s\right)=%s\ \Longrightarrow\ \sin\left(\theta+%s\right)=%s"%(L(sp.simplify(r)),ang(float(al)),L(c),ang(float(al)),L(sp.nsimplify(c/r))))),
        ("解",D(r"\theta=%s"%(r",\ ".join("%d^\\circ"%v for v in vals))))]
    return r"$0^\circ\leqq\theta<360^\circ$ のとき、方程式 $%s\sin\theta+%s\cos\theta=%s$ を解け。"%(L(a),L(b),L(c)),st,r"\theta=%s"%(r",\ ".join("%d^\\circ"%v for v in vals))
o=[b9(*v) for v in [(1,sp.sqrt(3),1),(sp.sqrt(3),1,sp.sqrt(3)),(1,1,1),(1,-1,1),(sp.sqrt(3),-1,1)]]
build(Z,CH,"合成を使った方程式（度数法）",o,"<p>$a\\sin\\theta+b\\cos\\theta=r\\sin(\\theta+\\alpha)$（$r=\\sqrt{a^2+b^2}$）に合成して、1つの $\\sin$ の方程式に。範囲を $\\theta+\\alpha$ に移して解を拾う。</p>","2つの波を1つの波にまとめれば、あとは基本の方程式。",9)
# 10 α+β の決定
def b10(ta,tb):
    ta,tb=R(ta),R(tb); t=(ta+tb)/(1-ta*tb)
    al=math.atan(float(ta));be=math.atan(float(tb)); s=al+be
    assert abs(math.tan(s)-float(t))<1e-9
    st=[("加法定理","<p>"+D(r"\tan(\alpha+\beta)=\dfrac{%s+%s}{1-%s\cdot%s}=%s"%(L(ta),L(tb),L(ta),L(tb),L(t)))),
        ("範囲","<p>"+I(r"\tan\alpha>0,\ \tan\beta>0")+" より "+I(r"0<\alpha,\beta<\dfrac\pi2")+"、"+I(r"0<\alpha+\beta<\pi")+"。</p>"),
        ("決定","<p>"+I(r"\tan(\alpha+\beta)=%s"%L(t))+(" より "+I(r"\alpha+\beta=\dfrac{\pi}{4}") if t==1 else (" より "+I(r"\alpha+\beta=\dfrac{3\pi}{4}") if t==-1 else ""))+"。</p>")]
    return r"$0<\alpha<\dfrac\pi2,\ 0<\beta<\dfrac\pi2$ で $\tan\alpha=%s,\ \tan\beta=%s$ のとき、$\alpha+\beta$ の値を求めよ。"%(L(ta),L(tb)),st,(r"\dfrac{\pi}{4}" if t==1 else r"\dfrac{3\pi}{4}")
o=[b10(*v) for v in [(R(1,2),R(1,3)),(2,3),(R(1,3),R(1,2)),(3,2),(R(1,4),R(3,5))]]
build(Z,CH,"tanα, tanβ から α+β を決める",o,"<p>$\\tan(\\alpha+\\beta)$ を計算し、<b>範囲を確認</b>して角を1つに決める。$0<\\alpha+\\beta<\\pi$ なら $\\tan$ が $1$ で $\\dfrac\\pi4$、$-1$ で $\\dfrac{3\\pi}4$。</p>","tan の値だけでなく、角の範囲もセットで判断する。",10)
XU=finishx(Z,CH)
