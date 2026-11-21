# -*- coding: utf-8 -*-
from bh import *
import math
Z=U_(); CH=[]; R=sp.Rational
def Phi(z): return 0.5*(1+math.erf(z/math.sqrt(2)))
def f4(v): return "%.4f"%v
# 6 母平均の信頼区間
def b6(n,xb,sg,z95=1.96):
    se=sg/math.sqrt(n); lo=xb-z95*se; hi=xb+z95*se
    st=[("標準誤差","<p>"+D(r"\dfrac{\sigma}{\sqrt n}=\dfrac{%g}{\sqrt{%d}}=%.3f"%(sg,n,se))),
        ("95% 信頼区間","<p>"+D(r"\overline X\pm1.96\cdot\dfrac{\sigma}{\sqrt n}=%g\pm1.96\times%.3f"%(xb,se))),
        ("区間",D(r"%.2f\leqq m\leqq%.2f"%(lo,hi)))]
    return r"母標準偏差 $%g$ の母集団から大きさ $%d$ の標本を抽出したところ、標本平均が $%g$ であった。母平均 $m$ に対する信頼度 $95\%%$ の信頼区間を求めよ。"%(sg,n,xb),st,r"%.2f\leqq m\leqq%.2f"%(lo,hi)
o=[b6(*v) for v in [(100,52,10),(64,170,16),(225,30,12),(36,75,9),(400,48,20)]]
build(Z,CH,"母平均の95%信頼区間",o,"<p>信頼度95%の区間は $\\overline X-1.96\\dfrac\\sigma{\\sqrt n}\\leqq m\\leqq\\overline X+1.96\\dfrac\\sigma{\\sqrt n}$。</p>","測った平均を中心に、誤差の幅だけ左右に。",6)
# 7 信頼区間の幅から n
def b7(sg,w):
    # width 2*1.96*sg/sqrt(n) <= w  -> n >= (2*1.96*sg/w)^2
    n0=(2*1.96*sg/w)**2; n=math.ceil(n0)
    st=[("区間の幅","<p>"+D(r"2\times1.96\times\dfrac{%d}{\sqrt n}\leqq%g"%(sg,w))),
        ("解く","<p>"+D(r"\sqrt n\geqq\dfrac{2\times1.96\times%d}{%g}=%.2f\ \Rightarrow\ n\geqq%.1f"%(sg,w,2*1.96*sg/w,n0))),
        ("最小の $n$","<p>整数で "+I("n=%d"%n)+"。</p>")]
    return r"母標準偏差 $%d$ の母集団から標本を抽出し、母平均に対する信頼度 $95\%%$ の信頼区間の幅を $%g$ 以下にしたい。標本の大きさ $n$ は最低いくつ必要か。"%(sg,w),st,"n=%d"%n
o=[b7(*v) for v in [(10,4),(8,2),(15,5),(20,6),(12,3)]]
build(Z,CH,"信頼区間の幅から必要な標本の大きさ",o,"<p>区間の幅は $2\\times1.96\\dfrac{\\sigma}{\\sqrt n}$。これが指定以下になる $n$ を求め、<b>切り上げ</b>る。</p>","精度を2倍にするには標本を4倍に。",7)
# 8 母比率
def b8(n,x):
    p=x/n; se=math.sqrt(p*(1-p)/n); lo=p-1.96*se; hi=p+1.96*se
    st=[("標本比率","<p>"+I(r"\hat p=\dfrac{%d}{%d}=%.3f"%(x,n,p))+"。</p>"),
        ("標準誤差","<p>"+D(r"\sqrt{\dfrac{\hat p(1-\hat p)}{n}}=\sqrt{\dfrac{%.3f\times%.3f}{%d}}=%.4f"%(p,1-p,n,se))),
        ("区間",D(r"%.3f\leqq p\leqq%.3f"%(lo,hi)))]
    return r"ある製品 $%d$ 個を調べたところ不良品が $%d$ 個あった。不良品の母比率 $p$ に対する信頼度 $95\%%$ の信頼区間を求めよ。"%(n,x),st,r"%.3f\leqq p\leqq%.3f"%(lo,hi)
o=[b8(*v) for v in [(400,60),(900,180),(625,125),(1600,320),(2500,400)]]
build(Z,CH,"母比率の95%信頼区間",o,"<p>標本比率 $\\hat p=\\dfrac xn$、区間は $\\hat p\\pm1.96\\sqrt{\\dfrac{\\hat p(1-\\hat p)}{n}}$。</p>","割合の推定も、平均の推定と同じ作り方。",8)
# 9 仮説検定（さいころ）
def b9(n,k):
    p=1/6; mu=n*p; sg=math.sqrt(n*p*(1-p)); z=(k-mu)/sg; rej=abs(z)>1.96
    st=[("仮説","<p>帰無仮説 "+I(r"H_0:\ p=\dfrac16")+"（偏りがない）、対立仮説 "+I(r"H_1:\ p\neq\dfrac16")+"。有意水準5%（両側）。</p>"),
        ("検定統計量","<p>"+I("X\\sim N(%.1f,\\ %.2f^2)"%(mu,sg**2))+" で近似。</p>"+D(r"Z=\dfrac{%d-%.1f}{%.3f}=%.2f"%(k,mu,sg,z))),
        ("判断","<p>"+I("|Z|=%.2f"%abs(z))+(" > 1.96 なので "+I("H_0")+" を<b>棄却</b>する。偏りがあるといえる。" if rej else " ≤ 1.96 なので "+I("H_0")+" は<b>棄却できない</b>。偏りがあるとはいえない。")+"</p>")]
    return r"さいころを $%d$ 回投げたところ、1の目が $%d$ 回出た。このさいころは1の目が出やすいといえるか。有意水準 $5\%%$（両側検定）で判断せよ。"%(n,k),st,(r"\text{棄却する（偏りがある）}" if rej else r"\text{棄却できない}")
o=[b9(*v) for v in [(600,120),(300,60),(720,150),(180,38),(1200,230)]]
build(Z,CH,"仮説検定（さいころの偏り）",o,"<p>帰無仮説 $H_0$ を立て、標準化した値 $Z$ が<b>棄却域</b>（両側5%なら $|Z|>1.96$）に入るか判断。入れば棄却、入らなければ「棄却できない」（偏りがないと証明したわけではない）。</p>","偶然では起きにくいほどの偏りか、を確かめる。",9)
# 10 片側検定
def b10(n,x,p0):
    p=x/n; z=(p-p0)/math.sqrt(p0*(1-p0)/n); rej=z>1.64
    st=[("仮説","<p>"+I("H_0:\\ p=%g"%p0)+"、"+I("H_1:\\ p>%g"%p0)+"。有意水準5%（片側）。</p>"),
        ("検定統計量","<p>"+D(r"Z=\dfrac{\hat p-p_0}{\sqrt{p_0(1-p_0)/n}}=\dfrac{%.3f-%g}{\sqrt{%g\times%g/%d}}=%.2f"%(p,p0,p0,1-p0,n,z))),
        ("判断","<p>"+I("Z=%.2f"%z)+(" > 1.64 なので棄却。" if rej else " ≤ 1.64 なので棄却できない。")+"</p>")]
    return r"ある薬の治癒率は従来 $%g$ とされていた。新しい薬を $%d$ 人に投与したところ $%d$ 人が治癒した。新薬の治癒率は従来より高いといえるか。有意水準 $5\%%$（片側）で判断せよ（$P(Z\geqq1.64)=0.05$）。"%(p0,n,x),st,(r"\text{棄却（高いといえる）}" if rej else r"\text{棄却できない}")
o=[b10(*v) for v in [(400,180,0.4),(400,170,0.4),(900,360,0.35),(625,300,0.45),(100,45,0.4)]]
build(Z,CH,"仮説検定（母比率・片側検定）",o,"<p>「高いか」を調べるので<b>片側検定</b>（棄却域は $Z>1.64$）。標準化 $Z=\\dfrac{\\hat p-p_0}{\\sqrt{p_0(1-p_0)/n}}$ を計算して比べる。</p>","基準より大きく外れているか、片方向だけを見る。",10)
XU=finishx(Z,CH)
