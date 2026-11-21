# -*- coding: utf-8 -*-
from bh import *
import math
Z=U_(); CH=[]; R=sp.Rational; s=sp.sqrt; _c=[0]
def cube_fig(name,secpts=None,sec_lab=None,w=44):
    def fn(ax):
        # oblique projection
        def P(x,y,z): return (x+0.5*y, z+0.35*y)
        V={(i,j,k):P(i,j,k) for i in (0,1) for j in (0,1) for k in (0,1)}
        edges=[(a,b) for a in V for b in V if a<b and sum(abs(a[t]-b[t]) for t in range(3))==1]
        for a,b in edges:
            hidden=(a[1]==1 and b[1]==1 and (a[0]==0 or a[2]==0) and False)
            ls="--" if (a[1]==1 and b[1]==1 and a[0]==0 and b[0]==0) or (a[0]==0 and a[1]==1 and b[0]==0 and b[1]==1) or (a[1]==1 and b[1]==1 and a[2]==0 and b[2]==0) else "-"
            ax.plot([V[a][0],V[b][0]],[V[a][1],V[b][1]],color="#555",lw=1.3,ls=ls)
        if secpts:
            pts=[P(*p) for p in secpts]; ax.fill([p[0] for p in pts],[p[1] for p in pts],color="#f4b6bf",alpha=.7)
            q=pts+[pts[0]]; ax.plot([p[0] for p in q],[p[1] for p in q],color="#b81f36",lw=2)
        lab={(0,0,0):"A",(1,0,0):"B",(1,1,0):"C",(0,1,0):"D",(0,0,1):"E",(1,0,1):"F",(1,1,1):"G",(0,1,1):"H"}
        for k,v in lab.items():
            x_,y_=V[k]; ax.text(x_+(-.12 if k[0]==0 else .12),y_+(.1 if k[2] else -.12),v,fontsize=11,ha="center",va="center")
        ax.set_aspect("equal"); ax.axis("off")
    make_fig(name,fn,size=(3.6,3.2)); return img(name,w)
# 6 オイラー（正多面体）
def b6(p,q,name):
    # 各面 p角形, 各頂点に q 面: pF=2E=qV, V-E+F=2
    F_,E_,V_=sp.symbols('F E V'); sol=sp.solve([p*F_-2*E_,q*V_-2*E_,V_-E_+F_-2],[F_,E_,V_],dict=True)[0]
    f,e,v=sol[F_],sol[E_],sol[V_]
    st=[("辺の数と面・頂点の数","<p>各面は "+I(str(p))+" 角形。辺は2つの面に共有されるので、面の辺の数の合計は辺の数の2倍。</p>"+D(r"%dF=2E"%p)+"<p>各頂点には "+I(str(q))+" 本の辺が集まる。辺は2つの頂点をもつので</p>"+D(r"%dV=2E"%q)),
        ("オイラーの多面体定理","<p>"+I("V-E+F=2")+" に "+I(r"F=\dfrac{2E}{%d},\ V=\dfrac{2E}{%d}"%(p,q))+" を代入。</p>"+D(r"\dfrac{2E}{%d}-E+\dfrac{2E}{%d}=2\ \Rightarrow\ E=%d"%(q,p,e))),
        ("面と頂点",D(r"F=%d,\qquad V=%d"%(f,v)))]
    return r"すべての面が合同な正%d角形で、各頂点にちょうど %d 個の面が集まる凸多面体（%s）の面・辺・頂点の数を求めよ。"%(p,q,name),st,r"F=%d,\ E=%d,\ V=%d"%(f,e,v)
o=[b6(*v) for v in [(5,3,"正十二面体"),(3,3,"正四面体"),(4,3,"正六面体"),(3,4,"正八面体"),(3,5,"正二十面体")]]
build(Z,CH,"正多面体の面・辺・頂点の数（オイラーの定理）",o,r"<p>$pF=2E$、$qV=2E$、$V-E+F=2$ の連立。<b>辺は2つの面・2つの頂点に共有される</b>ことから、$F,V$ を $E$ で表す。</p>","辺は2回数えられている。割る2を忘れない。",6)
# 7 立方体の切断（正六角形）
def b7(a):
    S=R(3,4)*3**0*0
    sd=a*s(2)/2; Hx=R(3,2)*s(3)*sd**2
    pts=[(1,.5,0),(1,1,.5),(.5,1,1),(0,.5,1),(0,0,.5),(.5,0,0)]
    # verify planar & regular: compute 3D
    P=np.array(pts,float); d=[np.linalg.norm(P[i]-P[(i+1)%6]) for i in range(6)]; assert np.allclose(d,d[0])
    fig=cube_fig("ax13c%d"%a,pts,None)
    st=[("切断面の形","<p>1辺 "+I(str(a))+" の立方体を、辺の中点6つを通る平面で切る。切り口の各辺は面の対角線の半分なので、等しい長さ。</p>"+fig),
        ("辺の長さ",D(r"\text{1辺}=\dfrac12\cdot%s=%s"%(L(a*s(2)),L(sd)))),
        ("面積","<p>切り口は<b>正六角形</b>（1辺 "+I(L(sd))+"）。正三角形6個分。</p>"+D(r"S=6\cdot\dfrac{\sqrt3}{4}\left(%s\right)^2=%s"%(L(sd),L(Hx))))]
    return r"1辺の長さが $%d$ の立方体 $ABCD\text{-}EFGH$ を、辺 $BC,\ CG,\ GH,\ HE,\ EA,\ AB$ の中点を通る平面で切る。切り口の面積を求めよ。"%a,st,L(Hx)
o=[b7(a) for a in [4,6,2,8,10]]
build(Z,CH,"立方体の切断面（正六角形）",o,r"<p>切り口の各辺は面の対角線の半分で、すべて等しい長さ。<b>正六角形</b>は正三角形6個。面積 $=\dfrac{3\sqrt3}{2}\ell^2$。</p>","切り口を平面図形として取り出して、知っている図形に直す。",7)
# 8 正四角錐の二面角
def b8(a,h):
    t=R(2*h,a); th=sp.atan(t); sl=sp.sqrt(h*h+R(a*a,4)); cosv=sp.simplify(R(a,2)/sl)
    # 数値: 二面角
    ang=math.degrees(math.atan(2*h/a))
    def fn(ax):
        ax.plot([-a/2,a/2,0,-a/2],[0,0,h,0],color="#333",lw=1.8); ax.plot([0,0],[0,h],color="#888",ls="--",lw=1.2)
        ax.text(0,-.12*h,"M",ha="center",fontsize=11); ax.text(a/2,-.12*h,"N",ha="center",fontsize=11); ax.text(0,h*1.03,"O",ha="center",fontsize=11)
        ax.text(a/4+.05*a,h*.3,"θ",fontsize=11,color="#b81f36"); ax.text(.05,h/2,"h",fontsize=11); ax.text(a/4,-.12*h,"a/2",fontsize=10,ha="center")
        ax.set_aspect("equal"); ax.axis("off"); ax.set_xlim(-a/2-.3,a/2+.5)
    make_fig("ax13p%d_%d"%(a,h),fn,size=(3.2,2.8)); fig=img("ax13p%d_%d"%(a,h),42)
    st=[("断面を考える","<p>底面の辺の中点 "+I("M")+" と頂点 "+I("O")+" を通り、底面の辺に垂直な平面で切る。側面と底面のなす角 "+I(r"\theta")+" は、この断面の底角。</p>"+fig),
        ("$\\tan\\theta$","<p>底面の中心から辺の中点までは "+I(r"\dfrac a2=%s"%L(R(a,2)))+"、高さ "+I("h=%d"%h)+"。</p>"+D(r"\tan\theta=\dfrac{h}{a/2}=\dfrac{%d}{%s}=%s"%(h,L(R(a,2)),L(t)))),
        ("斜面の高さ・余弦",D(r"OM'=\sqrt{h^2+(a/2)^2}=%s,\qquad \cos\theta=\dfrac{a/2}{OM'}=%s"%(L(sl),L(cosv))))]
    return r"底面が1辺 $%d$ の正方形で、高さが $%d$ の正四角すいがある。側面と底面のなす角を $\theta$ とするとき、$\tan\theta$ と $\cos\theta$ を求めよ。"%(a,h),st,r"\tan\theta=%s,\ \cos\theta=%s"%(L(t),L(cosv))
o=[b8(*v) for v in [(6,4),(8,3),(10,12),(6,3),(12,8)]]
build(Z,CH,"正四角すいの側面と底面のなす角",o,r"<p>二面角は<b>交線に垂直な平面</b>で切った断面で測る。底辺の中点と頂点を通る断面で、底面の中心から辺の中点まで $\dfrac a2$、高さ $h$ の直角三角形を考える。</p>","立体の角は、断面を取り出して平面の角にする。",8)
# 9 正四面体のねじれの位置にある2直線のなす角
def b9(a,i):
    V={'A':np.array([0,0,math.sqrt(6)/3*a]),'B':np.array([a/math.sqrt(3),0,0]),'C':np.array([-a/(2*math.sqrt(3)),a/2,0]),'D':np.array([-a/(2*math.sqrt(3)),-a/2,0])}
    cfg=[("A","BC","B","CD"),("A","BC","B","AD"),("A","AB","C","AD"),("A","AB","C","CD"),("A","BD","B","AC")]
    v1,e1,v2,e2=cfg[i]
    M=(V[e1[0]]+V[e1[1]])/2; N=(V[e2[0]]+V[e2[1]])/2
    u=M-V[v1]; w=N-V[v2]; cs=abs(u@w)/np.linalg.norm(u)/np.linalg.norm(w)
    fr=sp.nsimplify(round(cs,9),[sp.sqrt(3)],tolerance=1e-7)
    assert abs(float(fr)-cs)<1e-6
    st=[("辺の中点","<p>"+I("M")+" は辺 "+I(e1)+" の中点、"+I("N")+" は辺 "+I(e2)+" の中点。2直線 "+I(v1+"M")+"、"+I(v2+"N")+" はねじれの位置にある。</p>"),
        ("平行移動して三角形をつくる","<p>どちらかを<b>平行移動</b>して、1つの三角形の2辺にする。中点連結定理を使って長さを求め、<b>余弦定理</b>を使う。1辺 "+I(str(a))+"、正三角形の中線は "+I(r"\sqrt3\cdot%s/2"%("%d"%a))+"。</p>"),
        ("$\\cos\\theta$",D(r"\cos\theta=%s"%L(fr))+"<p>（なす角 "+I(r"0^\circ<\theta\leqq90^\circ")+" なので正の値で答える）。</p>")]
    return r"1辺の長さが $%d$ の正四面体 $ABCD$ で、辺 $%s$ の中点を $M$、辺 $%s$ の中点を $N$ とする。直線 $%sM$ と直線 $%sN$ のなす角を $\theta\ (0^\circ<\theta\leqq90^\circ)$ とするとき、$\cos\theta$ を求めよ。"%(a,e1,e2,v1,v2),st,L(fr)
o=[b9(4,i) for i in range(5)]
build(Z,CH,"正四面体のねじれの位置にある2直線のなす角",o,r"<p>ねじれの位置の2直線のなす角は、<b>一方を平行移動</b>して交わらせた角。中点連結定理で平行な線分をつくり、三角形の<b>余弦定理</b>で $\cos\theta$ を出す。</p>","ずらして交わらせてから角を測る。",9)
# 10 内分の作図
def b10(m,n):
    tot=m+n
    def fn(ax):
        ax.plot([0,6],[0,0],color="#333",lw=2); ax.plot([0,3.5*0.8],[0,2.5*0.8],color="#333",lw=1.5)
        import numpy as np_
        ux=np_.array([3.5,2.5])/np_.linalg.norm([3.5,2.5])*0.9
        pts=[ux*k for k in range(tot+1)]
        for i,pp in enumerate(pts): ax.plot(pp[0],pp[1],"o",ms=4,color="#555")
        Bq=pts[-1]; ax.plot([Bq[0],6],[Bq[1],0],color="#b81f36",lw=1.6)
        for k in (m,):
            pk=pts[k]; ax.plot([pk[0],6*k/tot*0+ (6*k/tot)],[pk[1],0],color="#b81f36",lw=1.6,ls="--")
        ax.text(-.2,-.3,"A",fontsize=11); ax.text(6.05,-.3,"B",fontsize=11); ax.text(6*m/tot,-.4,"P",fontsize=11,color="#b81f36",ha="center"); ax.text(Bq[0]+.1,Bq[1]+.1,"C",fontsize=11)
        ax.set_aspect("equal"); ax.axis("off"); ax.set_xlim(-.5,6.5)
    make_fig("ax13d%d_%d"%(m,n),fn,size=(4,2.6)); fig=img("ax13d%d_%d"%(m,n),52)
    st=[("補助線","<p>"+I("A")+" から別の半直線を引き、等間隔に "+I(str(tot))+" 個の点をとる（"+I(r"A\to C")+"）。</p>"+fig),
        ("平行線を引く","<p>"+I("C")+" と "+I("B")+" を結び、"+I("A")+" から数えて "+I(str(m))+" 番目の点を通って "+I("CB")+" に平行な直線を引く。</p>"),
        ("理由","<p>平行線と線分の比の定理より "+I(r"AP:PB=%d:%d"%(m,n))+"。</p>"+D(r"AP:PB=%d:%d"%(m,n)))]
    return r"線分 $AB$ を $%d:%d$ に内分する点 $P$ の作図の手順を述べ、その作図が正しい理由を説明せよ。"%(m,n),st,r"\text{平行線と比の定理より }AP:PB=%d:%d"%(m,n)
o=[b10(*v) for v in [(2,3),(3,2),(1,4),(3,4),(2,5)]]
build(Z,CH,"線分を m:n に内分する作図",o,r"<p>$A$ から任意の半直線を引いて<b>等間隔に $m+n$ 個</b>の点をとり、最後の点と $B$ を結ぶ。$m$ 番目の点から<b>それと平行</b>に線を引く。理由は平行線と線分の比の定理。</p>","目盛りのついた別の定規を借りて、平行線で写し取る。",10)
XU=finishx(Z,CH)
