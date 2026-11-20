# -*- coding: utf-8 -*-
# 整式の割り算・分数式（数学II いろいろな式）
from bh import *
Z=U_()
def poly_(cs): return sum(c_*x**(len(cs)-1-i) for i,c_ in enumerate(cs))
def qr(Q,rem): return r"\text{商 }"+L(Q)+r",\quad \text{余り }"+L(rem)
def divpart(A,B):
    h,Q,rem=divtext(A,B)
    return h,Q,rem
CH=[]  # (問題, 解答HTML, 答, k)
def pack(k,prob,steps,ans):  # 練習・章末用
    return prob,flat(steps),ans

# ===== 例題1 整式の割り算 =====
def b1(A,B):
    h,Q,rem=divtext(A,B)
    steps=[("商を1項ずつ立てて引く","<p>最高次の項どうしを割って商の項を決め、（割る式）×（商の項）を引く。余りの次数が割る式より小さくなるまで繰り返す。</p>"+h),
           ("商と余りを読む",D(qr(Q,rem))),
           ("確かめ",D(r"\begin{aligned}&"+P(B)+P(Q)+"+"+P(rem)+r"\\ &="+L(sp.expand(A))+r"\end{aligned}"))]
    assert sp.expand(B*Q+rem-A)==0
    return r"整式 $"+L(A)+r"$ を $"+L(B)+r"$ で割ったときの商と余りを求めよ。",steps,qr(Q,rem)
V1=[(poly_([6,-1,-7,5,-2]),poly_([2,1,-3])),(poly_([4,0,-5,3,1]),poly_([2,-1,1])),(poly_([3,-2,-4,1,6]),poly_([3,1,-2])),(poly_([2,5,-1,-3,4]),poly_([1,2,-1])),(poly_([5,-3,0,2,-7]),poly_([5,2,-1]))]
o=[b1(*v) for v in V1]
Z.ex("整式の割り算（筆算）",o[0][0],
 r"<p>整式の割り算は<b>数の筆算と同じ</b>。降べきの順に並べ、最高次の項どうしを割って商の項を決め、割る式を掛けて引く。余りの次数が割る式の次数より小さくなるまで繰り返す。</p>$$A=BQ+R\quad(R\text{ の次数}<B\text{ の次数})$$",
 "割り算は「何回引けるか」の繰り返し。まず一番大きい次数の項だけを見て、1回ぶん引く。",
 o[0][1],o[0][2],[z[0] for z in o[1:4]],[(flat(z[1]),z[2]) for z in o[1:4]])
CH.append((o[4][0],flat(o[4][1]),o[4][2],1))

# ===== 例題2 割り算の関係式（逆算・因数で割った余り） =====
def b2(al,be,Q,u,v):
    B=sp.expand((x-al)*(x-be)); Rm=u*x+v; Pp=sp.expand(B*Q+Rm); rem=Rm.subs(x,al)
    steps=[("割り算の関係式を書く","$$P(x)=(\\text{割る式})\\times(\\text{商})+(\\text{余り})$$"+D(r"P(x)="+P(B)+P(Q)+"+"+P(Rm))),
           ("展開して $P(x)$ を求める",D(r"P(x)="+L(Pp))),
           ("割る式を因数分解する",D(L(B)+"="+facs(sorted([al,be],reverse=True)))+"<p>よって "+I("P(x)=("+L(x-al)+")\\{("+L(x-be)+")("+L(Q)+")\\}+("+L(Rm)+")")+"。</p>"),
           (f"余りを {L(x-al)} で割る",f"<p>"+I(L(x-al))+r" で割ったとき、商のかたまりの部分は割り切れる。残る "+I(L(Rm))+" を "+I(L(x-al))+" で割った余りが答え。</p>"+D(L(Rm)+"="+L(u)+P(x-al)+"+"+L(sp.expand(u*al+v))+r"\ \Rightarrow\ \text{余り }"+L(rem)))]
    assert sp.rem(Pp,x-al,x)==rem
    prob=r"整式 $P(x)$ を $"+L(B)+r"$ で割ると、商が $"+L(Q)+r"$、余りが $"+L(Rm)+r"$ である。(1) $P(x)$ を求めよ。(2) $P(x)$ を $"+L(x-al)+r"$ で割った余りを求めよ。"
    return prob,steps,r"P(x)="+L(Pp)+r",\quad \text{余り }"+L(rem)
V2=[(1,-2,2*x-1,3,4),(2,-1,x+3,2,-5),(3,1,3*x-2,-1,6),(-1,4,x-4,4,1),(2,-3,2*x+5,-3,2)]
o=[b2(*v) for v in V2]
Z.ex("割り算の関係式から元の式を求める",o[0][0],
 r"<p>割り算の結果は必ず<b>関係式</b> $$P(x)=B(x)\,Q(x)+R(x)$$ で書ける。逆に商・余りがわかっていれば右辺を展開して $P(x)$ が出る。また、割る式 $B$ が $(x-\alpha)(x-\beta)$ と因数分解できるなら、$x-\alpha$ で割ったときの余りは、余り $R$ を $x-\alpha$ で割った余りに等しい。</p>",
 "割り算は「かけ算＋たし算」に書き直せる。逆算するときは、かけて、たすだけ。",
 o[0][1],o[0][2],[z[0] for z in o[1:4]],[(flat(z[1]),z[2]) for z in o[1:4]])
CH.append((o[4][0],flat(o[4][1]),o[4][2],2))

# ===== 例題3 分数式の加減 =====
def b3(al,be,n1,n2):
    n3=-n1*(al-be); D1=x-al; D2=x-be; DD=sp.expand(D1*D2)
    E=n1/D1+n2/D2+n3/DD; res=sp.cancel(sp.together(E)); num0=sp.expand(n1*D2+n2*D1+n3)
    assert sp.expand(num0-sp.expand(sp.cancel(E*DD)))==0 and sp.factor(num0).has(D1)
    steps=[("分母を因数分解して通分する","<p>"+I(L(DD)+"="+P(D1)+P(D2))+" なので、共通分母は "+I(P(D1)+P(D2))+"。</p>"+D(sgn_terms([(n1,D1),(n2,D2),(n3,DD)])+"="+fr(L(n1)+P(D2)+("+" if n2>0 else "")+L(n2)+P(D1)+("+" if n3>0 else "")+L(n3),P(D1)+P(D2)))),
           ("分子を展開して整理する",D(fr(L(n1*D2)+(("+" if n2>0 else "")+L(n2*D1))+(("+" if n3>0 else "")+L(n3)),P(D1)+P(D2))+"="+fr(L(num0),P(D1)+P(D2)))),
           ("分子を因数分解して約分する",D(fr(L(num0),P(D1)+P(D2))+"="+fr(L(sp.factor(num0)),P(D1)+P(D2))+"="+fr(L(res.as_numer_denom()[0]),L(res.as_numer_denom()[1]))))]
    prob=r"次の計算をして、できるだけ簡単な分数式で答えよ。 $$"+sgn_terms([(n1,D1),(n2,D2),(n3,DD)])+"$$"
    nu,de=res.as_numer_denom()
    return prob,steps,fr(L(nu),L(de))
V3=[(1,-2,2,3),(2,-1,3,-1),(-3,1,1,4),(3,-2,-2,5),(-1,2,4,-3)]
o=[b3(*v) for v in V3]
Z.ex("分数式の加減（通分して約分）",o[0][0],
 r"<p>分数式の足し算・引き算は<b>分数と同じ</b>。①分母を因数分解 ②最小公倍数で通分 ③分子を展開して整理 ④分子を因数分解して約分、の順に進める。</p>",
 "通分は「全員の分母をそろえて同じ大きさのピザにする」こと。そろえてから、ピースの数（分子）を足す。",
 o[0][1],o[0][2],[z[0] for z in o[1:4]],[(flat(z[1]),z[2]) for z in o[1:4]])
CH.append((o[4][0],flat(o[4][1]),o[4][2],3))

# ===== 例題4 分数式の乗除 =====
def b4(an,ad,bn,bd):
    A_=prod_(an)/prod_(ad); B_=prod_(bn)/prod_(bd); res=sp.cancel(A_/B_)
    steps=[("各式を因数分解する",D(fr(L(sp.expand(prod_(an))),L(sp.expand(prod_(ad))))+"="+fr(facs(an),facs(ad))+r"\qquad "+fr(L(sp.expand(prod_(bn))),L(sp.expand(prod_(bd))))+"="+fr(facs(bn),facs(bd)))),
           ("割り算を、逆数の掛け算に直す",D(fr(facs(an),facs(ad))+r"\times"+fr(facs(bd),facs(bn)))),
           ("約分する","<p>分子と分母に共通な因数を消す。</p>"+D(L(sp.factor(res))+"="+fr(L(res.as_numer_denom()[0]),L(res.as_numer_denom()[1]))))]
    prob=r"次の計算をせよ。 $$"+fr(L(sp.expand(prod_(an))),L(sp.expand(prod_(ad))))+r"\div"+fr(L(sp.expand(prod_(bn))),L(sp.expand(prod_(bd))))+"$$"
    nu,de=res.as_numer_denom()
    return prob,steps,fr(L(sp.factor(nu)),L(sp.factor(de)))
V4=[([3,-2],[-2,1],[3,-1],[-2,-2]),([4,1],[1,-3],[4,-2],[-3,-3]),([2,-5],[-1,5],[2,3],[5,5]),([-4,3],[3,-1],[-4,1],[-1,-1]),([1,6],[-2,6],[1,-5],[-2,-2])]
o=[b4(*v) for v in V4]
Z.ex("分数式の乗除（因数分解して約分）",o[0][0],
 r"<p>分数式の掛け算・割り算は、まず<b>すべての分子・分母を因数分解</b>する。割り算は<b>逆数</b>を掛ける形に直し、共通因数を約分する。展開してから約分しようとしないのがコツ。</p>",
 "約分できるのは「かたまり（因数）」どうし。足し算でつながった項は消せない。必ず因数分解してから消す。",
 o[0][1],o[0][2],[z[0] for z in o[1:4]],[(flat(z[1]),z[2]) for z in o[1:4]])
CH.append((o[4][0],flat(o[4][1]),o[4][2],4))

# ===== 例題5 部分分数と和 =====
def b5(d,mm):
    terms=[(1,sp.expand((x+i*d)*(x+(i+1)*d))) for i in range(mm)]
    E=sum(1/tt[1] for tt in terms); res=sp.cancel(sp.together(E)); assert sp.simplify(res-mm/(x*(x+mm*d)))==0
    A_=x+0*d
    tex_terms="+".join(fr(1,"("+L(x+i*d)+")("+L(x+(i+1)*d)+")") if i>0 else fr(1,"x("+L(x+d)+")") for i in range(mm))
    parts="+".join(r"\dfrac1{"+str(d)+r"}\left("+fr(1,L(x+i*d) if i>0 else "x")+"-"+fr(1,L(x+(i+1)*d))+r"\right)" for i in range(mm))
    steps=[("1項ずつ部分分数に分ける","<p>公式 "+I(r"\dfrac1{A(A+d)}=\dfrac1d\left(\dfrac1A-\dfrac1{A+d}\right)")+" を使う。（確かめ："+I(r"\dfrac1A-\dfrac1{A+d}=\dfrac{d}{A(A+d)}")+"）</p>"+D(parts)),
           ("途中の項が消える","<p>前の項の「"+I("-")+"」と次の項の「"+I("+")+"」が打ち消し合う。残るのは最初と最後だけ。</p>"+D(r"\dfrac1{"+str(d)+r"}\left("+fr(1,"x")+"-"+fr(1,L(x+mm*d))+r"\right)")),
           ("通分してまとめる",D(r"\dfrac1{"+str(d)+r"}\cdot"+fr(L(x+mm*d)+"-x",f"x({L(x+mm*d)})")+"="+r"\dfrac1{"+str(d)+r"}\cdot"+fr(str(mm*d),f"x({L(x+mm*d)})")+"="+fr(str(mm),f"x({L(x+mm*d)})")))]
    prob=r"次の和を計算せよ。 $$"+tex_terms+"$$"
    return prob,steps,fr(str(mm),f"x({L(x+mm*d)})")
V5=[(2,3),(1,4),(3,3),(2,5),(4,3)]
o=[b5(*v) for v in V5]
Z.ex("部分分数に分けて和を求める",o[0][0],
 r"<p>分母が連続した形 $A(A+d)$ の和は<b>部分分数</b>に分けると、途中の項が打ち消し合う。$$\dfrac1{A(A+d)}=\dfrac1d\left(\dfrac1A-\dfrac1{A+d}\right)$$</p>",
 "ドミノ倒しのように、前の項の後ろと次の項の前が打ち消し合い、両端だけが残る。",
 o[0][1],o[0][2],[z[0] for z in o[1:4]],[(flat(z[1]),z[2]) for z in o[1:4]])
CH.append((o[4][0],flat(o[4][1]),o[4][2],5))
for p_,b_,a_,k_ in CH: Z.ch(p_,b_,a_,k_)
UNIT=Z.unit(0,0,"いろいろな式","整式の割り算・分数式","整式の筆算、割り算の関係式、分数式の加減乗除、部分分数による和まで、計算の精度が問われる難問に挑みます。",subject="2")
