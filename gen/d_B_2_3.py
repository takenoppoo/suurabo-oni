# -*- coding: utf-8 -*-
from bh import *
Z=U_(); CH=[]
R=sp.Rational
def dec(q,nd=2): return ("%."+str(nd)+"f")%float(q)
# 例題1 母平均の信頼区間
def b1(xb,s,n):
    se=R(s)/sp.sqrt(n); assert se.is_rational; w=R(196,100)*se
    st=[("標本平均の標準偏差","<p>標本の大きさ "+I("n=%d"%n)+" は十分大きいので、母標準偏差を "+I(r"\sigma=%d"%s)+" として</p>"+D(r"\dfrac{\sigma}{\sqrt n}=\dfrac{%d}{\sqrt{%d}}=%s"%(s,n,L(se)))),
        ("信頼区間の公式","<p>母平均 $m$ の信頼度95%の信頼区間：</p>"+D(r"\left[\overline X-1.96\cdot\dfrac{\sigma}{\sqrt n},\ \ \overline X+1.96\cdot\dfrac{\sigma}{\sqrt n}\right]")),
        ("値を代入する",D(r"1.96\times%s=%s"%(L(se),dec(w,2)))+D(r"%s-%s=%s,\quad %s+%s=%s"%(dec(xb),dec(w,2),dec(xb-w,2),dec(xb),dec(w,2),dec(xb+w,2))))]
    return r"母標準偏差 $%d$ の母集団から大きさ $%d$ の標本を無作為に抽出したところ、標本平均は $%s$ であった。母平均 $m$ に対する信頼度 $95\%%$ の信頼区間を求めよ。"%(s,n,dec(xb)),st,r"%s\leqq m\leqq %s"%(dec(xb-w,2),dec(xb+w,2))
V_=[(50,20,100),(120,15,36),(75,24,64),(200,30,100),(36,5,25)]
o=[b1(*v) for v in V_]
build(Z,CH,"母平均の信頼区間",o,r"<p>信頼度95%：$\left[\overline X-1.96\dfrac{\sigma}{\sqrt n},\ \overline X+1.96\dfrac{\sigma}{\sqrt n}\right]$。$\sigma$ が不明でも $n$ が大きければ標本標準偏差で代用する。</p>","標本平均を中心に、$1.96$ 標準偏差ぶんの幅をとる網を投げて、母平均を捕まえる。",1)
# 例題2 母比率
def b2(n,cnt):
    ph=R(cnt,n); se2=ph*(1-ph)/n; se=sp.sqrt(se2); assert se.is_rational; w=R(196,100)*se
    st=[("標本比率","<p>"+I(r"p_0=\dfrac{%d}{%d}=%s"%(cnt,n,dec(ph)))+"。</p>"),
        ("標準誤差",D(r"\sqrt{\dfrac{p_0(1-p_0)}{n}}=\sqrt{\dfrac{%s\times%s}{%d}}=%s"%(dec(ph),dec(1-ph),n,dec(se,4)))),
        ("信頼区間","<p>母比率 $p$ の信頼度95%の信頼区間：</p>"+D(r"p_0\pm1.96\sqrt{\dfrac{p_0(1-p_0)}{n}}"+r"=%s\pm%s"%(dec(ph),dec(w,4)))+D(r"%s\leqq p\leqq %s"%(dec(ph-w,4),dec(ph+w,4))))]
    return r"ある製品を $%d$ 個調べたところ、不良品が $%d$ 個あった。この製品全体の不良品の割合 $p$ に対する信頼度 $95\%%$ の信頼区間を求めよ。"%(n,cnt),st,r"%s\leqq p\leqq %s"%(dec(ph-w,4),dec(ph+w,4))
V_=[(400,200),(400,80),(900,90),(2500,2000),(100,50)]
o=[b2(*v) for v in V_]
build(Z,CH,"母比率の信頼区間",o,r"<p>標本比率 $p_0$、標本の大きさ $n$ のとき、母比率 $p$ の信頼度95%の信頼区間は $$p_0-1.96\sqrt{\frac{p_0(1-p_0)}{n}}\leqq p\leqq p_0+1.96\sqrt{\frac{p_0(1-p_0)}{n}}$$</p>","アンケートの「支持率 $\\pm$ 誤差」と同じ。標本が大きいほど誤差の幅は小さい。",2)
# 例題3 標本の大きさ
def b3(s,L_):
    s=R(s); L_=R(L_); nmin=(R(392,100)*s/L_)**2; assert nmin.is_integer or True
    import math
    nn=int(math.ceil(float(nmin)))
    st=[("信頼区間の幅","<p>信頼度95%の区間の幅は "+I(r"2\times1.96\times\dfrac{\sigma}{\sqrt n}")+"。</p>"+D(r"2\times1.96\times\dfrac{%s}{\sqrt n}\leqq %s"%(L(s),dec(L_) if False else dec(L_,2)))),
        ("$\\sqrt n$ について解く",D(r"\sqrt n\geqq\dfrac{3.92\times%s}{%s}=%s"%(L(s),dec(L_,2),L(R(392,100)*s/L_)))),
        ("$n$ を求める",D(r"n\geqq\left(%s\right)^2=%s"%(L(R(392,100)*s/L_),L(nmin)))+"<p>よって最小の $n$ は "+I(str(nn))+"。</p>")]
    return r"母標準偏差 $%s$ の母集団から標本を抽出して、母平均に対する信頼度 $95\%%$ の信頼区間の幅（長さ）を $%s$ 以下にしたい。標本の大きさ $n$ を最小いくつにすればよいか。"%(L(s),dec(L_,2)),st,"n=%d"%nn
V_=[(10,3.92),(10,1.96),(5,1.96),(20,7.84),(15,2.94)]
o=[b3(s,R(str(l))) for s,l in V_]
build(Z,CH,"信頼区間の幅と標本の大きさ",o,r"<p>信頼区間の幅は $2\times1.96\dfrac{\sigma}{\sqrt n}$。幅 $\leqq L$ から $\sqrt n$ について解き、2乗して $n$ の範囲を出す。<b>整数に切り上げる</b>。</p>","精度を2倍にしたければ、標本は4倍必要。$n$ が $\\sqrt n$ で効いてくる。",3)
# 例題4 仮説検定 p=1/2
def b4(n,k):
    m=R(n,2); s=sp.sqrt(R(n,4)); assert s.is_rational; z=(k-m)/s; rej=abs(z)>R(196,100)
    st=[("仮説を立てる","<p>帰無仮説 "+I(r"H_0:\ p=\dfrac12")+"（コインは正しく作られている）、対立仮説 "+I(r"H_1:\ p\neq\dfrac12")+"。有意水準は $5\\%$。</p>"),
        ("$H_0$ のもとでの分布","<p>表の回数 "+I("X")+" は "+I(r"B\left(%d,\ \dfrac12\right)"%n)+"。正規分布で近似。</p>"+D(r"m=%d\times\dfrac12=%s,\quad \sigma=\sqrt{%d\times\dfrac12\times\dfrac12}=%s"%(n,L(m),n,L(s)))),
        ("棄却域と検定統計量","<p>有意水準5%の棄却域は "+I(r"|Z|\geqq1.96")+"。</p>"+D(r"Z=\dfrac{%d-%s}{%s}=%s"%(k,L(m),L(s),L(z)))),
        ("判断","<p>"+I(r"|Z|=%s"%L(abs(z)))+(" $>1.96$ なので棄却域に入る。<b>$H_0$ を棄却</b>し、コインは正しく作られていないと判断する。" if rej else " $<1.96$ なので棄却域に入らない。<b>$H_0$ は棄却できない</b>。コインが正しく作られていないとはいえない。")+"</p>")]
    return r"1枚のコインを $%d$ 回投げたところ、表が $%d$ 回出た。このコインは正しく作られている（表の出る確率が $\dfrac12$）といえるか。有意水準 $5\%%$ で検定せよ。"%(n,k),st,("棄却される（正しく作られているとはいえない）" if rej else "棄却されない（正しくないとはいえない）")
V_=[(100,62),(400,220),(100,56),(900,435),(400,176)]
o=[b4(*v) for v in V_]
build(Z,CH,"仮説検定（コインの偏り）",o,r"<p>①帰無仮説 $H_0$ を立てる ②$H_0$ のもとで $X$ の分布（正規近似）③<b>棄却域</b>（有意水準5%なら $|Z|\geqq1.96$）を決める ④$Z$ を計算し、棄却域に入れば $H_0$ を棄却。入らなければ「棄却できない」（$H_0$ が正しいとは言い切れない）。</p>","「偶然ではめったに起こらないほど極端か？」を5%の物差しで判断する。",4)
# 例題5 一般の母比率
def b5(n,p0,k):
    p0=R(p0); m=n*p0; s=sp.sqrt(n*p0*(1-p0)); assert s.is_rational; z=(k-m)/s; rej=abs(z)>R(196,100)
    st=[("仮説を立てる","<p>"+I(r"H_0:\ p=%s"%L(p0))+"（従来と変わらない）、"+I(r"H_1:\ p\neq%s"%L(p0))+"。有意水準 $5\\%$。</p>"),
        ("$H_0$ のもとでの分布","<p>"+I(r"X\sim B(%d,\ %s)"%(n,L(p0)))+" を正規分布で近似。</p>"+D(r"m=%d\times%s=%s,\quad \sigma=\sqrt{%d\times%s\times%s}=%s"%(n,L(p0),L(m),n,L(p0),L(1-p0),L(s)))),
        ("検定統計量",D(r"Z=\dfrac{%d-%s}{%s}=%s"%(k,L(m),L(s),L(z)))),
        ("判断","<p>棄却域 "+I(r"|Z|\geqq1.96")+"。"+I(r"|Z|=%s"%L(abs(z)))+(" $>1.96$ なので <b>$H_0$ を棄却</b>。割合は変わったと判断できる。" if rej else " $<1.96$ なので <b>$H_0$ は棄却できない</b>。変わったとはいえない。")+"</p>")]
    return r"ある病気の治癒率は従来 $%s$ であった。新薬を $%d$ 人に使ったところ $%d$ 人が治癒した。新薬で治癒率が変わったといえるか。有意水準 $5\%%$ で検定せよ。"%(L(p0),n,k),st,("変わったといえる（棄却）" if rej else "変わったとはいえない（棄却されない）")
V_=[(400,R(1,5),100),(400,R(1,5),92),(900,R(1,10),110),(900,R(1,10),100),(100,R(1,5),29)]
o=[b5(*v) for v in V_]
build(Z,CH,"仮説検定（母比率）",o,r"<p>$H_0:\ p=p_0$ のもとで $X\sim B(n,p_0)$、$m=np_0$、$\sigma=\sqrt{np_0(1-p_0)}$。$Z=\dfrac{X-m}{\sigma}$ が $|Z|\geqq1.96$ なら棄却。</p>","「従来どおり」と仮定したとき、観測された結果がどれほど珍しいかを $Z$ で測る。",5)
UNIT=finish(Z,CH,1,2,"統計的な推測","推定と仮説検定","信頼区間、標本の大きさ、仮説検定まで、統計的推測の手順を問う難問に挑みます。",subject="B")
