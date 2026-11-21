# -*- coding: utf-8 -*-
from bh import *
import statistics as stt
Z=U_(); CH=[]
R=sp.Rational
def quart(d):
    d=sorted(d); n=len(d)
    med=lambda a:(a[len(a)//2] if len(a)%2 else R(a[len(a)//2-1]+a[len(a)//2],2))
    lo=d[:n//2]; hi=d[(n+1)//2:]
    return med(lo),med(d),med(hi)
# 6 平均を目標にする
def b6(n,m,tgt):
    xneed=tgt*(n+1)-n*m
    st=[("合計を使う","<p>"+I("n=%d"%n)+" 個の平均が "+I(str(m))+" なので、合計は "+I(r"%d\times%d=%d"%(n,m,n*m))+"。</p>"),
        ("追加後の式","<p>新しいデータ "+I("x")+" を加えた "+I(str(n+1))+" 個の平均を "+I(str(tgt))+" にする。</p>"+D(r"\dfrac{%d+x}{%d}=%d"%(n*m,n+1,tgt))),
        ("解く",D(r"%d+x=%d\ \Rightarrow\ x=%d"%(n*m,tgt*(n+1),xneed)))]
    return r"%d個のデータの平均値が $%d$ であった。新しいデータを1つ加えて、平均値を $%d$ にしたい。加えるデータの値を求めよ。"%(n,m,tgt),st,str(xneed)
o=[b6(*v) for v in [(9,52,55),(14,68,70),(19,45,48),(24,60,64),(11,73,75)]]
build(Z,CH,"平均値を目標にするために加えるデータ",o,r"<p>平均値 $\times$ 個数 $=$ <b>合計</b>。追加後の「合計 ÷ 個数」が目標になる方程式を立てる。</p>","合計に注目すれば、平均の問題は足し算と割り算だけ。",6)
# 7 仮平均
def b7(base,ds):
    d=[base+t for t in ds]; mean=R(sum(d),len(d)); mm=base+R(sum(ds),len(ds)); assert mean==mm
    st=[("仮平均を決める","<p>データが "+I(str(base))+" に近いので、仮平均を "+I(str(base))+" とし、<b>差</b> "+I("d=x-%d"%base)+" を求める。</p>"+D(r"d:\ %s"%(r",\ ".join(str(t) for t in ds)))),
        ("差の平均",D(r"\dfrac{%s}{%d}=%s"%("+".join("(%d)"%t if t<0 else str(t) for t in ds),len(ds),L(R(sum(ds),len(ds)))))),
        ("もとの平均","<p>平均 "+I(r"=%d+%s"%(base,L(R(sum(ds),len(ds)))))+"。</p>"+D(r"\bar x=%s"%L(mean)))]
    return r"次の %d 個のデータの平均値を、仮平均を使って求めよ。 $$%s$$"%(len(d),r",\ ".join(str(v) for v in d)),st,L(mean)
o=[b7(*v) for v in [(1000,[3,-4,7,2,-1,6]),(2000,[12,-8,5,-3,9,-5,2]),(500,[-6,4,9,-2,7]),(3000,[15,-10,5,0,-5,20]),(800,[-3,8,-6,5,2,-1,4,3])]]
build(Z,CH,"仮平均を使った平均の計算",o,r"<p>データが近い値のときは、<b>基準にする値を引いた差</b>の平均を出し、後でその基準をもどして足す。$\bar x=a+\overline{(x-a)}$。</p>","大きな数をそのまま足さず、基準からのずれだけを集計する。",7)
# 8 四分位数
def b8(d):
    q1,q2,q3=quart(d); ds=sorted(d); n=len(ds)
    st=[("小さい順に並べる","<p>"+I(r"%s"%(r",\ ".join(str(v) for v in ds)))+"（"+I("n=%d"%n)+"）。</p>"),
        ("中央値（第2四分位数）","<p>"+("データの数が奇数なので、中央の値 " if n%2 else "データの数が偶数なので、中央2つの平均 ")+I(r"Q_2=%s"%L(q2))+"。</p>"),
        ("前半・後半に分ける","<p>"+("中央の値を除いて、" if n%2 else "")+"前半 "+I(r"%s"%(r",\ ".join(str(v) for v in ds[:n//2])))+"、後半 "+I(r"%s"%(r",\ ".join(str(v) for v in ds[(n+1)//2:])))+"。</p>"+D(r"Q_1=%s,\qquad Q_3=%s"%(L(q1),L(q3))))
        ,("四分位範囲",D(r"Q_3-Q_1=%s"%L(q3-q1)))]
    return r"次のデータの第1・第2・第3四分位数と四分位範囲を求めよ。 $$%s$$"%(r",\ ".join(str(v) for v in d)),st,r"Q_1=%s,\ Q_2=%s,\ Q_3=%s,\ \text{四分位範囲 }%s"%(L(q1),L(q2),L(q3),L(q3-q1))
o=[b8(d) for d in [[12,5,9,20,15,7,3,18,10],[8,14,3,21,6,17,11,9,25,13],[30,22,41,19,35,27,48,24],[7,12,5,9,16,11,20,8,14,6,18],[50,62,44,58,71,49,66,55,60,53,47,64]]]
build(Z,CH,"四分位数（奇数個・偶数個）",o,r"<p>小さい順に並べ、<b>中央値で前半・後半に分ける</b>。データの数が奇数のときは、中央値を前半・後半のどちらにも含めない。前半の中央値が $Q_1$、後半の中央値が $Q_3$。</p>","まず並べる。半分に分ける。それぞれの真ん中を見る。",8)
# 9 未知数が2つ
def b9(base,m,lo_,hi_):
    # sorted 7 data: base list with a and b unknown in ranges, mean m
    fixed=base; S=7*m-sum(fixed); sols=[(a,b) for a in range(lo_[0],lo_[1]+1) for b in range(hi_[0],hi_[1]+1) if a+b==S]
    assert sols
    st=[("合計の式","<p>7個の平均が "+I(str(m))+" なので合計は "+I(str(7*m))+"。</p>"+D(r"%s+a+b=%d\ \Rightarrow\ a+b=%d"%("+".join(str(v) for v in fixed),7*m,S))),
        ("範囲の条件","<p>小さい順に並んでいるので "+I(r"%d\leqq a\leqq %d,\ \ %d\leqq b\leqq %d"%(lo_[0],lo_[1],hi_[0],hi_[1]))+"。</p>"),
        ("整数の組",D(r"(a,\ b)=%s"%(r",\ ".join("(%d,%d)"%p for p in sols))))]
    return r"7個のデータ $%d,\ a,\ %d,\ %d,\ b,\ %d,\ %d$ は小さい順に並んでいて、平均値が $%d$ である。$%d\leqq a\leqq %d$、$%d\leqq b\leqq %d$ をみたす整数 $a,\ b$ の組をすべて求めよ。"%(base[0],base[1],base[2],base[3],base[4],m,lo_[0],lo_[1],hi_[0],hi_[1]),st,r"(a,b)=%s"%(r",\ ".join("(%d,%d)"%p for p in sols))
o=[b9(*v) for v in [([4,6,8,11,12],8,(4,6),(8,11)),([3,5,7,10,13],7,(3,5),(7,10)),([2,6,9,12,14],8,(2,6),(9,12)),([5,8,10,13,16],10,(5,8),(10,13)),([1,4,6,9,11],6,(1,4),(6,9))]]
build(Z,CH,"平均と範囲から未知のデータを決める",o,r"<p>平均から<b>合計の式</b>を作る。並び順から決まる<b>範囲</b>を整数でしらみつぶしに調べる。</p>","式が1本で未知数が2つのとき、範囲が残りの条件になる。",9)
# 10 度数分布表で平均の範囲
def b10(cls,freq):
    n=sum(freq); mid=[R(a+b,2) for a,b in cls]; mean=sum(f*m for f,m in zip(freq,mid))/n
    lo=R(sum(f*a for f,(a,b) in zip(freq,cls)),n); hi=R(sum(f*b for f,(a,b) in zip(freq,cls)),n)
    hdr="".join("<th>%s以上%s未満</th>"%(a,b) for a,b in cls)+"<th>計</th>"
    row="".join("<td>%d</td>"%f for f in freq)+"<td>%d</td>"%n
    tbl='<table class="tbl"><tr>%s</tr><tr>%s</tr></table>'%(hdr,row)
    st=[("階級値で近似","<p>各階級の真ん中の値（階級値）が全員の値だとみなす。</p>"+D(r"\bar x\fallingdotseq\dfrac{%s}{%d}=%s"%("+".join("%s\\times%d"%(L(m),f) for m,f in zip(mid,freq)),n,L(mean)))),
        ("最小の場合","<p>全員が階級の<b>下限</b>の値のとき最小。</p>"+D(r"\dfrac{%s}{%d}=%s"%("+".join("%d\\times%d"%(a,f) for (a,b),f in zip(cls,freq)),n,L(lo)))),
        ("最大の場合","<p>全員が階級の<b>上限</b>に限りなく近いとき（未満なので届かない）。</p>"+D(r"\dfrac{%s}{%d}=%s"%("+".join("%d\\times%d"%(b,f) for (a,b),f in zip(cls,freq)),n,L(hi)))+"<p>実際の平均は "+I(r"%s\leqq \bar x<%s"%(L(lo),L(hi)))+"。</p>")]
    return r"次の度数分布表のデータの平均値を、階級値を使って求めよ。また、実際の平均値がとりうる範囲を求めよ。"+tbl,st,r"\text{階級値による平均 }%s,\ \ %s\leqq\bar x<%s"%(L(mean),L(lo),L(hi))
o=[b10(*v) for v in [([(0,10),(10,20),(20,30),(30,40)],[3,8,6,3]),([(10,20),(20,30),(30,40),(40,50)],[2,5,9,4]),([(0,20),(20,40),(40,60),(60,80)],[4,10,5,1]),([(50,60),(60,70),(70,80),(80,90)],[5,6,6,3]),([(0,5),(5,10),(10,15),(15,20)],[6,9,3,2])]]
build(Z,CH,"度数分布表から平均値の範囲を求める",o,r"<p>階級値 $=\dfrac{\text{下限}+\text{上限}}2$。実際の値は階級の中で動くので、<b>全員が下限のとき最小、上限のとき最大</b>。「未満」の上限には届かない。</p>","まとめた情報から、実際の値の幅を見積もる。",10)
XU=finishx(Z,CH)
