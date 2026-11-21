# -*- coding: utf-8 -*-
from bh import *
Z=U_(); CH=[]
R=sp.Rational
# 6 否定
def b6(a):
    # すべての実数x について x^2 + a x + 1 > 0  (|a|<2 で真)。否定は ある x で ≤0。 判定: 真偽
    true=abs(a)<2; neg_true=not true
    st=[("否定をつくる","<p>「すべての "+I("x")+" について "+I("P")+"」の否定は「ある "+I("x")+" について "+I(r"P\text{でない}")+"」。</p>"+D(r"\text{否定：ある実数 }x\text{ について }x^2%sx+1\leqq0"%("%+d"%a if a not in(1,-1) else ("+" if a==1 else "-")))),
        ("判別式で真偽を調べる","<p>"+I(r"x^2%sx+1>0"%("%+d"%a if a not in(1,-1) else ("+" if a==1 else "-")))+" がつねに成り立つ条件は 判別式 "+I(r"D=%d^2-4=%d"%(a,a*a-4))+" が負。</p>"+D(r"D=%d\ %s\ 0"%(a*a-4,"<" if a*a-4<0 else (r"=" if a*a-4==0 else ">")))),
        ("結論","<p>"+("元の命題は真、否定は偽。" if true else "元の命題は偽、否定は真（"+I(r"D\geqq0")+" なので "+I(r"x^2+ax+1\leqq0")+" となる "+I("x")+" がある）。")+"</p>")]
    return r"命題「すべての実数 $x$ について $x^2%sx+1>0$」の否定を述べ、元の命題と否定の真偽を答えよ。"%("%+d"%a if a not in(1,-1) else ("+" if a==1 else "-")),st,("元の命題：真、否定：偽" if true else "元の命題：偽、否定：真")
o=[b6(v) for v in [1,3,-2,-1,4]]
build(Z,CH,"全称命題の否定と真偽",o,r"<p>「すべての $x$ で」の否定は「ある $x$ で…でない」。$>$ の否定は $\leqq$。2次式が常に正になるかは<b>判別式</b>で調べる。</p>","「全員そう」の否定は「ひとりでも違う人がいる」。",6)
# 7 逆裏対偶
def b7(k):
    # x^2 = k^2 ⇒ x = k  (偽) 
    st=[("命題 $p\\Rightarrow q$","<p>"+I(r"p:x^2=%d,\ \ q:x=%d"%(k*k,k))+"。</p>"),
        ("真偽","<p>"+I("x=-%d"%k)+" のとき "+I("p")+" は真、"+I("q")+" は偽。反例があるので <b>偽</b>。</p>"),
        ("逆・裏・対偶",D(r"\text{逆 }q\Rightarrow p:\ x=%d\Rightarrow x^2=%d\ \ (\text{真})"%(k,k*k))+D(r"\text{裏 }\overline p\Rightarrow\overline q:\ x^2\neq%d\Rightarrow x\neq%d\ \ (\text{真})"%(k*k,k))+D(r"\text{対偶 }\overline q\Rightarrow\overline p:\ x\neq%d\Rightarrow x^2\neq%d\ \ (\text{偽})"%(k,k*k)))]
    return r"命題「$x^2=%d$ ならば $x=%d$」の逆・裏・対偶をつくり、それぞれの真偽を答えよ。"%(k*k,k),st,"元：偽、逆：真、裏：真、対偶：偽"
o=[b7(v) for v in [2,3,4,5,6]]
build(Z,CH,"逆・裏・対偶と真偽",o,r"<p>$p\Rightarrow q$ に対して 逆は $q\Rightarrow p$、裏は $\overline p\Rightarrow\overline q$、対偶は $\overline q\Rightarrow\overline p$。<b>元と対偶の真偽は一致</b>、逆と裏も一致する。</p>","元と対偶はセット、逆と裏もセット。反例1つで偽。",7)
# 8 背理法 √p+√q
def b8(p,q):
    pq=p*q; assert int(pq**.5)**2!=pq
    st=[("有理数と仮定","<p>"+I(r"\sqrt{%d}+\sqrt{%d}=r"%(p,q))+"（"+I("r")+" は有理数）とする。</p>"),
        ("両辺を2乗","<p>左辺を展開する。</p>"+D(r"(\sqrt{%d}+\sqrt{%d})^2=%d+2\sqrt{%d}\sqrt{%d}+%d=%d+2\sqrt{%d}"%(p,q,p,p,q,q,p+q,pq))+"<p>これが "+I("r^2")+" に等しい。</p>"+D(r"%d+2\sqrt{%d}=r^2"%(p+q,pq))+D(r"2\sqrt{%d}=r^2-%d"%(pq,p+q))+D(r"\sqrt{%d}=\dfrac{r^2-%d}{2}"%(pq,p+q))),
        ("矛盾","<p>右辺は有理数。ところが "+I(r"\sqrt{%d}"%pq)+" は無理数（"+I("%d"%pq)+" は平方数でない）。矛盾。</p>"),
        ("結論","<p>よって "+I(r"\sqrt{%d}+\sqrt{%d}"%(p,q))+" は無理数。</p>")]
    return r"$\sqrt{%d}+\sqrt{%d}$ が無理数であることを、背理法で証明せよ。ただし $\sqrt{%d}$ が無理数であることは使ってよい。"%(p,q,pq),st,r"\text{無理数である}"
o=[b8(*v) for v in [(2,3),(2,5),(3,5),(2,7),(3,7)]]
build(Z,CH,"背理法（√p+√q は無理数）",o,r"<p>結論を否定して「有理数 $r$」と仮定し、<b>2乗して $\sqrt{pq}$ を $r$ で表す</b>。右辺は有理数、左辺は無理数となって矛盾。</p>","仮定が正しいと、ありえない結論にぶつかる。だから仮定が誤り。",8)
# 9 対偶で倍数
def b9(p):
    st=[("対偶をつくる","<p>"+I(r"n^2\text{が%dの倍数}\Rightarrow n\text{が%dの倍数}"%(p,p))+" の対偶：</p>"+D(r"n\text{が%dの倍数でない}\Rightarrow n^2\text{が%dの倍数でない}"%(p,p))),
        ("余りで場合分け","<p>"+I(r"n=%dk+r\ (1\leqq r\leqq %d)"%(p,p-1))+" とおく。</p>"+D(r"n^2=(%dk+r)^2=%dk^2+2\cdot%dk\cdot r+r^2=%dk(%dk+2r)+r^2"%(p,p*p,p,p,p)+r"\ \Rightarrow\ n^2\ \text{を}%d\text{でわった余りは }r^2\text{の余り}"%p)),
        ("$r^2$ は $%d$ の倍数でない"%p,"<p>"+I("%d"%p)+" は素数で "+I(r"1\leqq r\leqq%d"%(p-1))+" なので、"+I("r^2")+" は "+I("%d"%p)+" の倍数でない。実際に調べると</p>"+wtable([I("r")]+[I(str(r_)) for r_ in range(1,p)],[[I("r^2")]+[I(str(r_*r_)) for r_ in range(1,p)],["%dでわった余り"%p]+[I(str(r_*r_%p)) for r_ in range(1,p)]])+"<p>余りはどれも 0 でない。</p>"),
        ("結論","<p>対偶が真なので、もとの命題も真。</p>")]
    return r"整数 $n$ について、「$n^2$ が $%d$ の倍数ならば $n$ は $%d$ の倍数である」ことを、対偶を利用して証明せよ。"%(p,p),st,r"\text{証明終}"
o=[b9(v) for v in [5,7,3,11,13]]
build(Z,CH,"対偶を使った整数の証明（p の倍数）",o,r"<p>直接示しにくいときは<b>対偶</b>。「$n$ が $p$ の倍数でない $\Rightarrow$ $n^2$ が $p$ の倍数でない」を、$n=pk+r\ (1\leqq r<p)$ で示す。素数なので $r^2$ は $p$ の倍数でない。</p>","結論の反対から出発して、仮定の反対へ着く。",9)
# 10 十分条件の連鎖
def b10(a,b,c):
    # p: |x|<a, q: x<b (b>=a?), r: x^2<c^2 ...
    st=[("集合で表す","<p>"+I(r"p:-%d<x<%d"%(a,a))+"、"+I(r"q:x<%d"%b)+"、"+I(r"r:-%d<x<%d"%(c,c))+"。</p>"),
        ("包含関係","<p>"+I(r"p\Rightarrow q")+" は "+I(r"P\subset Q")+"。"+I(r"(-%d,%d)\subset(-\infty,%d)"%(a,a,b))+"。右端どうしを比べると "+I(r"%d\leqq %d"%(a,b))+(" なので成り立つ。" if a<=b else " ではないので成り立たない。")+"</p><p>同じように "+I(r"r\Rightarrow p")+" は "+I(r"(-%d,%d)\subset(-%d,%d)"%(c,c,a,a))+"、右端 "+I(r"%d\leqq %d"%(c,a))+(" で成り立つ。" if c<=a else " ではなく成り立たない。")+"</p>"),
        ("判定","<p>"+I("p\\Rightarrow q")+(" は真。" if a<=b else " は偽。")+I(r"r\Rightarrow p")+(" は真" if c<=a else " は偽")+"、"+I(r"p\Rightarrow r")+(" は真。" if a<=c else " は偽。")+"</p>")]
    ans=("rはpの十分条件" if c<=a else "")+("、" if c<=a and a<=b else "")+("pはqの十分条件" if a<=b else "")
    return r"実数 $x$ についての条件 $p:|x|<%d$、$q:x<%d$、$r:|x|<%d$ について、$p$ は $q$ の何条件か、$r$ は $p$ の何条件かを答えよ。"%(a,b,c),st,("pはqの十分条件" if a<=b else "pはqの十分条件でない")+"、"+("rはpの十分条件（pはrの必要条件）" if c<a else "rはpの必要条件（十分でない）")
o=[b10(*v) for v in [(3,5,2),(2,4,1),(4,6,3),(3,7,1),(5,8,2)]]
build(Z,CH,"範囲で判定する十分・必要条件",o,r"<p>条件を<b>数直線上の範囲</b>で表し、<b>$P\subset Q$ なら $p\Rightarrow q$</b>（$p$ は $q$ の十分条件）。範囲の包含を図で確認する。</p>","狭い範囲は十分、広い範囲は必要。",10)
XU=finishx(Z,CH)
