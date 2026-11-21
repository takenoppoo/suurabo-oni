# -*- coding: utf-8 -*-
from bh import *
from d_2_5_1 import gplane,curve,mark
from gq import *
Z=U_(); CH=[]
R=sp.Rational; _c=[0]
def Q(a,b,c): return a*x**2+b*x+c
# 6 x軸との交点の距離から
def b6(p,q,a):
    f=a*(x-p)*(x-q); e=sp.expand(f); ln=abs(p-q)
    st=[("$x$ 軸との交点を文字で","<p>2点 "+I("(%d,0),(%d,0)"%(p,q))+" を通るので "+I(r"y=a(x-%s)(x-%s)"%(L(p),L(q)))+" とおける。</p>"),
        ("もう1点を代入","<p>"+I("(0,%s)"%L(f.subs(x,0)))+" を通るので</p>"+D(r"%s=a(%s)(%s)\ \Rightarrow\ a=%s"%(L(f.subs(x,0)),L(-p),L(-q),L(a)))),
        ("展開",D(r"y=%s(x-%s)(x-%s)=%s"%(L(a),L(p),L(q),L(e))))]
    vx,vy=vtx(a,*[e.coeff(x,1),e.coeff(x,0)]) if False else (sp.Rational(p+q,2),f.subs(x,sp.Rational(p+q,2)))
    fg=quadfig("x131_6_%d_%d_%d"%(p,q,a),[(f,"#b81f36")],[(p,0,"(%d, 0)"%p),(q,0,"(%d, 0)"%q),(0,f.subs(x,0),"(0, %s)"%f.subs(x,0)),(vx,vy,"")],axis=vx)
    st[0]=(st[0][0],st[0][1]+fg)
    return r"放物線が $x$ 軸と $(%d,0),\ (%d,0)$ で交わり、点 $(0,%s)$ を通るとき、この放物線の方程式を $y=ax^2+bx+c$ の形で求めよ。"%(p,q,L(f.subs(x,0))),st,r"y=%s"%L(e)
o=[b6(*v) for v in [(1,3,2),(-1,2,3),(2,5,-1),(-2,3,1),(1,-4,2)]]
build(Z,CH,"x軸との交点から2次関数を決める",o,r"<p>$x$ 軸との交点が $\alpha,\beta$ なら $y=a(x-\alpha)(x-\beta)$ とおける。残る $a$ は<b>もう1点</b>を代入して決める。</p>","通る場所が分かっているときは、その形から作る（交点→因数分解の形）。",6)
# 7 x軸から切り取る線分の長さ
def b7(k,ln):
    # y = x^2 - 2 k x + c   x軸から切り取る長さ ln → c = k^2 - (ln/2)^2
    c=k**2-R(ln,2)**2; f=x**2-2*k*x+c
    xs=sp.solve(f,x); assert abs(xs[0]-xs[1])==ln
    st=[("平方完成","<p>"+I(r"y=x^2-%sx+c=(x-%s)^2-%s^2+c"%(L(2*k),L(k),L(k)))+"。軸は "+I("x=%s"%L(k))+"。</p>"),
        ("交点の位置","<p>軸について対称なので、2交点は "+I("x=%s\\pm\\dfrac{%d}{2}"%(L(k),ln))+"。</p>"),
        ("$c$ を決める","<p>"+I("x=%s+\\dfrac{%d}{2}=%s"%(L(k),ln,L(k+R(ln,2))))+" で "+I("y=0")+"。</p>"+D(r"\left(\dfrac{%d}{2}\right)^2-%s^2+c=0\ \Rightarrow\ c=%s"%(ln,L(k),L(c))))]
    fg=quadfig("x131_7_%d_%d"%(k,ln),[(f,"#b81f36")],[(k-R(ln,2),0,"(%s, 0)"%L(k-R(ln,2))),(k+R(ln,2),0,"(%s, 0)"%L(k+R(ln,2))),(k,c-k*k,"")],axis=k)
    st[0]=(st[0][0],st[0][1]+fg)
    return r"放物線 $y=x^2-%sx+c$ が $x$ 軸から切り取る線分の長さが $%d$ になるように、定数 $c$ の値を定めよ。"%(L(2*k),ln),st,r"c=%s"%L(c)
o=[b7(*v) for v in [(2,6),(3,4),(1,2),(2,3),(3,8)]]
build(Z,CH,"x軸から切り取る線分の長さ",o,r"<p>放物線は軸について対称。2交点は<b>軸から等距離（左右に長さの半分ずつ）</b>。交点の1つの座標を $y=0$ に代入して定数を決める。</p>","軸を中心にした左右対称。半分ずつ考える。",7)
# 8 平行移動・対称移動で通る点
def b8(a,b,c,p,q):
    f=Q(a,b,c); g=sp.expand(f.subs(x,x-p)+q)  # 平行移動 (p,q)
    # y軸対称:
    h=sp.expand(g.subs(x,-x))
    st=[("平行移動","<p>"+I("x")+" 方向に "+I(str(p))+"、"+I("y")+" 方向に "+I(str(q))+" 移動：</p>"+D(r"y-%s=%s"%(L(q),L(f.subs(x,x-p))) if False else r"y=%s"%L(g))),
        ("$y$ 軸に関して対称移動","<p>"+I("x")+" を "+I("-x")+" におきかえる。</p>"+D(r"y=%s"%L(h))),
        ("頂点の移り変わり","<p>頂点 "+I(L(sp.Point(*[R(-b,2*a),f.subs(x,R(-b,2*a))]).args[0]) if False else "(%s,\\ %s)"%(L(R(-b,2*a)),L(f.subs(x,R(-b,2*a)))))+" は平行移動で "+I("(%s,\\ %s)"%(L(R(-b,2*a)+p),L(f.subs(x,R(-b,2*a))+q)))+"、対称移動で "+I("(%s,\\ %s)"%(L(-(R(-b,2*a)+p)),L(f.subs(x,R(-b,2*a))+q)))+"。</p>")]
    v0=(R(-b,2*a),f.subs(x,R(-b,2*a))); v1=(v0[0]+p,v0[1]+q); v2=(-v1[0],v1[1])
    fg=quadfig("x131_8_%d_%d_%d_%d_%d"%(a,b+9,c+9,p+9,q+9),[(f,"#999999"),(g,"#1f6fb8"),(h,"#b81f36")],[(v0[0],v0[1],"元"),(v1[0],v1[1],"平行移動"),(v2[0],v2[1],"対称移動")])
    st[0]=(st[0][0],st[0][1]+"<p>灰色が元の放物線、青が平行移動後、赤が最後の放物線（点は頂点）。</p>"+fg)
    return r"放物線 $y=%s$ を $x$ 軸方向に $%d$、$y$ 軸方向に $%d$ だけ平行移動し、さらに $y$ 軸に関して対称移動した放物線の方程式を求めよ。"%(L(f),p,q),st,r"y=%s"%L(h)
o=[b8(*v) for v in [(1,2,3,2,1),(2,-4,1,3,-2),(1,-6,5,1,4),(-1,2,0,2,3),(2,4,-1,-1,2)]]
build(Z,CH,"平行移動と対称移動の合成",o,r"<p>順番どおりに変換する。<b>平行移動</b>は $x\to x-p,\ y\to y-q$、<b>$y$ 軸対称</b>は $x\to-x$。頂点の動きで検算する。</p>","1つずつ動かす。順番を入れ替えると結果が変わる。",8)
# 9 係数の符号
def b9(a,b,c):
    f=Q(a,b,c); D_=b*b-4*a*c
    st=[("開き方・軸・切片から符号","<p>"+("下に凸なので " if a>0 else "上に凸なので ")+I("a%s0"%(">" if a>0 else "<"))+"。切片 "+I("c=%s"%L(c))+" より "+I("c%s0"%(">" if c>0 else ("<" if c<0 else "=")))+"。</p>"),
        ("軸の位置から $b$","<p>軸 "+I(r"x=-\dfrac{b}{2a}=%s"%L(R(-b,2*a)))+" は"+("右側" if R(-b,2*a)>0 else "左側")+"。"+I("a%s0"%(">" if a>0 else "<"))+" なので "+I("b%s0"%(">" if b>0 else ("<" if b<0 else "=")))+"。</p>"),
        ("判別式から","<p>"+I("x")+" 軸との交点が"+("2個" if D_>0 else ("1個" if D_==0 else "0個"))+"なので "+I("b^2-4ac%s0"%(">" if D_>0 else ("=" if D_==0 else "<")))+"。</p>")]
    ax_=R(-b,2*a); rts=sp.solve(f,x) if D_>=0 else []
    fg=quadfig("x131_9_%d_%d_%d"%(a+9,b+9,c+9),[(f,"#b81f36")],[(0,c,"(0, %s)"%L(c)),(ax_,f.subs(x,ax_),"")]+[(r_,0,"") for r_ in rts if r_.is_real],axis=ax_)
    st[0]=(st[0][0],st[0][1]+"<p>グラフの形：点線が軸、赤い曲線が放物線。</p>"+fg)
    sg=lambda v:("正" if v>0 else ("負" if v<0 else "0"))
    return r"$y=%s$ のグラフについて、$a,\ b,\ c,\ b^2-4ac$ の符号をそれぞれ答えよ。"%L(f),st,"a:%s, b:%s, c:%s, b^2-4ac:%s"%(sg(a),sg(b),sg(c),sg(D_))
o=[b9(*v) for v in [(1,-4,3),(-1,2,3),(2,4,1),(-2,-4,-3),(1,4,4)]]
build(Z,CH,"グラフから係数・判別式の符号を読む",o,r"<p>$a$：開く向き、$c$：$y$ 切片、$b$：軸 $-\dfrac b{2a}$ の位置と $a$ の符号、$b^2-4ac$：$x$ 軸との共有点の数。<b>1つずつ</b>順に決める。</p>","グラフの特徴をチェックリストのように1つずつ読み取る。",9)
# 10 放物線と直線の共有点
def b10(k):
    # y = x^2 - 2x + 3 と y = k x ... discriminant
    f=x**2-2*x+3; eq=sp.expand(f-k*x); D_=sp.discriminant(eq,x)
    ks=sp.solve(sp.Eq(D_,0),k) if False else None
    kk=sp.Symbol('kk'); eqk=x**2-(2+kk)*x+3; Dk=sp.discriminant(eqk,x); sol=sp.solve(Dk,kk)
    st=[("共有点の方程式","<p>"+I("x^2-2x+3=kx")+" より</p>"+D(r"x^2-(2+k)x+3=0")),
        ("判別式",D(r"D=(2+k)^2-12=k^2+4k-8")),
        ("接する条件","<p>"+I("D=0")+" より</p>"+D(r"k=%s"%(r",\ ".join(L(s_) for s_ in sol))))]
    return r"放物線 $y=x^2-2x+3$ と直線 $y=kx$ が接するような定数 $k$ の値を求めよ。",st,r"k=%s"%(r",\ ".join(L(s_) for s_ in sol))
def b10b(c0,m0):
    # y=x^2+c0 と y= m x: x^2 - m x + c0=0, 接する m^2=4 c0
    kk=sp.Symbol('kk'); Dk=sp.discriminant(x**2-kk*x+c0,x); sol=sp.solve(Dk,kk)
    st=[("共有点の方程式","<p>"+I("x^2+%d=kx"%c0)+" より</p>"+D(r"x^2-kx+%d=0"%c0)),
        ("判別式","<p>接する $\\iff$ 重解 $\\iff D=0$。</p>"+D(r"D=k^2-%d=0"%(4*c0))),
        ("解く",D(r"k=%s"%(r",\ ".join(L(s_) for s_ in sol)))+"<p>接点の "+I("x")+" は重解 "+I(r"x=\dfrac k2")+"。</p>"+D(r"k=%s\ \Rightarrow\ \text{接点 }(%s,\ %s)"%(L(sol[1]),L(sol[1]/2),L(sol[1]**2/2*0+(sol[1]/2)**2+c0))+r"\quad k=%s\ \Rightarrow\ \text{接点 }(%s,\ %s)"%(L(sol[0]),L(sol[0]/2),L((sol[0]/2)**2+c0))))]
    kv=[sol[0],sol[1]]
    fg=quadfig("x131_10_%d"%c0,[(x**2+c0,"#b81f36")]+[(kk_*x,"#1f6fb8") for kk_ in kv],[(kk_/2,(kk_/2)**2+c0,"") for kk_ in kv])
    st[0]=(st[0][0],st[0][1]+"<p>赤が放物線、青い直線が接する2本の直線（点が接点）。</p>"+fg)
    return r"放物線 $y=x^2+%d$ と直線 $y=kx$ が接するような定数 $k$ の値と、そのときの接点を求めよ。"%c0,st,r"k=%s,\ \text{接点 }(%s,\ %s);\ k=%s,\ \text{接点 }(%s,\ %s)"%(L(sol[1]),L(sol[1]/2),L((sol[1]/2)**2+c0),L(sol[0]),L(sol[0]/2),L((sol[0]/2)**2+c0))
o=[b10b(c0,0) for c0 in [4,9,1,16,25]]
build(Z,CH,"放物線と直線が接する条件",o,r"<p>$y$ を消去して $x$ の2次方程式にし、<b>判別式 $D=0$</b>（重解）を条件にする。接点の $x$ は重解 $x=-\dfrac b{2a}$。</p>","接する＝2点が1点に重なる。重解のサイン $D=0$。",10)
XU=finishx(Z,CH)
