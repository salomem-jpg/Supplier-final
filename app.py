"""Supplier Capability Hub — self-contained Streamlit demonstration.

Contains fictional supplier scenarios, synthetic questionnaire and method notes.
Requires only Streamlit and pandas. See README before publishing.
"""
from __future__ import annotations
import base64 as _hub_b64
import hashlib as _hub_hashlib
import io as _hub_io
import os as _hub_os
from pathlib import Path as _HubPath
import sys as _hub_sys
import tempfile as _hub_tempfile
import zipfile as _hub_zipfile

_BUNDLE_B85 = (
    'P)h>@6aWAK2ms17X<ZVW0NbP(006c|000R9003ofXK8L_E^v9hTkme;Mw0*Tr|5WbA(^2SduFnmlZQEY9VPMY#xt;;ECN9gD5_;KqDT!%$<`VM_Tzm%9B_'
    'Bfb8oUwa=)tn!zLwroV&vfFtXI_uCA`G|5ZFZJp8aOWhjc-EK74Ks`YA>rLq)Byox7jmeyM_l}TEqMJ{B1i#a`UmSrN%SL<3#<2n{;C8}*+&t;t^y@P`fr'
    'L1JRk(I!Z*u+_iS#m1ks*+W;lzA=Ud}^T{-Qp>>%aU~#*BGdJ2bYDA_q8nZI1|faDl>YXRrt(BGLQ3HDR`BEfhC8BhX=E=Sc>s@wytre@mQqGRZ-Gzc~L9'
    'S2YM(eR$KeM+L*7uRz+^Umr}u7#q~T(CkEID{8SI>?JCW0&G=cqJvg{}|NbVT89uN`GvE;PK#d~XNI&SU;u42H`1b7PETWlTdPF`?q%+|=zrXa77?c`UQc'
    'in>kr(vRisAWzkXa=K%|19kyB=IeG@+Lj@wD=Ng1m2aDdXw521R|DC&d(4N8Y-g9ewQu!NJAl&EV?i!R5`x`^$ac(!8eI%+=Mr1may<&xJvzOtCzTd!RDb'
    '6)TzVED3XYN6Z&_UH~o;W3!0Q+&>WbcYbvNG%wDgEUjuEz<S@NNqq%0Wa+mT0E6qFaH3!K90qKjCTX0FKdxm(C(7frlrK8f)!=$?c6I*49;g#cpD*KbF(%'
    'fJ%Vho{h(EqR|I;35RbJf9vUnlK%OY942-5Y<+4qBM5s9I9F{P`TZAD$Cx3>`F&&8@t3lJ#%tMo$e+cdt-i%PlzejBgw#IF2Y)Nz^>r2ylu`P#kkKzL^?z'
    'hWliDpd=y=<K$X5-XBoxlC(<vRq}7h1}U-vQ9HX8P9*lJ@Fo;+@$gjBj*{=3B{b0La||tGY~QNMh6E|ITN#dz4Y%xe2v#x9UTXXBkFRizR<r-Gy@H5|30u'
    'orGys9#fHQyo>cxOcy}UCzGB_8iK2~?Bn_2U$@@gEYT^GJXKOhq%c2Z#wk!SZJut%_cl;~p8}Md5V+twV$_hyI_0y^@@vDbF=?V$}%fYPybf<XmFcXKb%Q'
    'fA~iT5Z#@O#pwHyBdzNGbXx&icr+h<@~LW$k;jG>`KHYabrfnO9XbWKzv|!XgO73?LV@oA0f_JIOpx0TSD-#zj7^)1~C^)w;rkgULn~&@#UFkHck}`zK+p'
    'A>{;VRq095su~`TzQE@Rf4)}Zw*VBW)ebV=EyE8Krb$uNRrIjv@5}?zEv#wgSl+K>Srf7NXI;h{nb}_?#>`miXHjI%&lD5_Ps0{@!K30DSb}U!52Fg(GAg'
    '|dU3led^m188gzp!tqh_``^cXi7x#!{$F9<J-T<U8W&(qs^XA%vyX8lgQUy)>yeT(xojN2C06*>%dvI5RAL{^k!=t2SGC1T=*bW*Y*t;m?+*cbvW^H~bPO'
    '{7qYI?j5$1Gt`%BaR{nw0B<}z`a}^(Ff-xglcCEAE>>EhV&}Na!f=UDyk7ghjO7Fr6tbrXfK8=ox4crVN8A(>8C8c^i0$94D6X@;AGGU7w$MRMGo<sup$$'
    'aI3uZ1M7{j*^C^TL(~`8tNPe^-<&-L4WxZT!Z-h3e#u9*tX`hxcv*p;`608Vi020XQxQaJmPU7TMSxnan5QTPx(ZH%1MhiGhSdBvzOMF?cDqJnb8^G~O-n'
    '#<@{no6F!7+0(bGAZwxETFEV5m8P5Kxk(_U__6dbRU_@gJGhYE0izWY2SC0Q0<J!Ky6M%2vx54ULP1L4_tky>%z0;NM$k8Vui<9n@$7#o;&F6}E|mYHT=y'
    'JQMI>Gh?dkC^m>!pw-4sA)UVq2(-hd#u8|H$xJ2?=<eob919p?_p!Fh&c<4Pjkb#j2YqHs);oxYQjLU&V~Tujits7eb;A`+Q)TzHh{NQA`G+H;CP;cL?fU'
    '9*59r8z>U-C94FCLfAF!vAhR7K(bl?N2NT4W{_9~a`n`4)cYdB+5FL1Xp#Mr;fo4)oVAhWKcDyli0a`F|Q0IRvE3-x=7Do*;s8cShZ7+R#!-3JTIwig!2p'
    'tz3AJB0%4G69{}xeg0lP_h>9B5}MI4i4H<Z`Ua~Srsp0Au;N51)iiCZ4@nQ>;?X|->6H?CONr!Pn@|csp8!eNV{-b*n^qpMi(>U@|GW*@@-bK!M7s1IojA'
    'W_ERxGE{LK}iO`BR<hYCj#-145$K;B#$im2Oi6!ntl`bjFBo%J}Knp@>fuD*g%XNlb@if~i)jv%uMO27@?_CYfzWqgf_x?)!@Y9cHm*Q&h^TpsVo*}d%gR'
    ')K@J-Z%=FU9v~H$M!n1b%)yxI7<Nu}X?^3i)@%b%jF~<=A@1A3#nLTP@@BHT;F~Z4ueUk$0x`010z*KI2AsEOHHQ2aa<*MGWO*@kDcZv<jVH<5`^4MOnes'
    '3k@`OAlMQ&L+l?Yv)l}VF~{s0MAkuIPXJ5<r5QPXp&DVm6yBCaRgKw+q>qq%Ka&1t=!;dT{73!_9e>VoImjEK4K1e{yQnQn=omuw1eJXW_t~J<Ku9bC|5!'
    '&E4_+R_iSBzhu5(T5ZR+*4ied6wWl6S{ZUJjPltn^P_IaZmletV5So;|6Y@n3LmyHhT>;whmz`jKEPstg0Ix1-cGlu0fi}7io>~3XL3z_O-nI`T|AnG^A&'
    'OR5eR4YAH<k|LAIjy-cCJKC8PBXc0w>^r-+0ZHiWm`Mf@lE6+a~`h-_aQuM`gAl18*YwIDK7OMM+S*Wh5%cF!4-(mm2~HOXob#v361oPO$N%!qk)|uN{Q>'
    'JO`$bpxk`$4P6Dd+)CVhYDdAemCIE2sp7L0oAYhN<U-g8g=0xUl2CtUFqb2byt3V2`vv_rCvvQaR_YjD|xqw#UsFO~z1f`}bWyYRIn1TQ5=)?ryNd*bRf5'
    '$B`IT$Y-j)LG+6zke}4CH~9q@7y1rY3p^f^g`d_HZztK==4a6+|Bx__R+sY&ID6DjX79o>EBJMEqI>GqgT=xM{wY_UZ4em>t2ORdrukhH9PGu8k*e0n{O%'
    'r7mz4ppFH>zal*Id5_?WH{zA>U(?3G&-#oMpRFsPiOV1-3tnH00G50!-}}>G@WIn*yyFIUP|MiPhcCV;LyvbL3E(fp<(b^X44$y?`uyiHaMih{AYg?Hxs9'
    '@TIhn?y?E6PRuM1!lVlbV0xU6BHuUF?=DyZBvCf{isBS76kIlD;+s18cQI9Hp1kwX$^y5gblok4!T;~cE`<GM=Om7q)=e}j_uy+4v+(*Xv;uIp`8%cVHC2'
    '_v3#j!9Rt!T@vm=i*#lDL)@|xCe%Cm?&%riznEUZYpuFgHYFL4-VebWC877HXQqmFuXZd@Bo5m4!voyq&&w+=_<vw<{n2uo2m79FdFvXj+~?w5!Y}6n`eR'
    '_SrSL|5ylC-`5YJ+K%qHlq({P5<~HK9g?1-Sc)1)aBkyOMtDjKTe_2>ho&B5tb$Fz`BIS@*O&FlH5yzq}1ea-5QKoY^`t<$`eAw6%YgFg4@?<Ac=59=qZG'
    '~MvYVV8bAji!dz9pgzr~(`T)&MxSf{YAIU9rLIiF5K?juZ#Lju&a7Esv8gW$jKDW2#6@^^v52*+}!4vRLA-C>NAu>=}1Y3$|hlEuIwkjM-CA+{gn)FGo$z'
    '(7NmNJc>^G-PEYh{L_wCb=J5YuI`Czi^;E&nedY{;d{VLf~z_qaOe$)mLi4&u9bw|JQNnX@?DKH<8{yUx;ay^_&<!{_o$EG8r(Z{E*7D8uEHp%2o?$hTWy'
    '(=+*zjOK%5*XBY>Tgzj1QkBt7GFT15|9qklqueRZreM*Hd3q#snUo@M?$!Ls`>`1`h+wTsyLcZm38#-c-{YX-tz9$T`OwE0z_T~~6nz&7lRwE}$(nL31ey'
    'TkU$&@+A<<lg%Zj&MszZ<V_QuT78_s)*nOR%+kx->WGTY2&!=)?YPSFPzMM<BC>I_TIgUg{GSF!^g#44uMpMUv!c>d!8**#IJRc%gz!Ft;6YEfS<UbOIV+'
    '&;9cR8!jV|XFYSh*&Q^hQ5s#BQ`}e>7=bnhWYH~6iiv7N!SnN<NPIMItyw$~uDHb=Js?VcbumI8Vw?qnle&3PWpkd^g^$`@smg>2xfTglhYHxejxI8?rwS'
    'Zbsopb!btxPrNP>LwgmJU~cYNt^(Ybhn-TFx(T?7`QFDTDCnB>1NF1TGBz;>n5p$A%`lf;Hej*hGW;4m6j03CGV>Nz6sj^3-OBWX`Cr8!@wl-WlVnO_hk@'
    'J~N79h4^Q0DljzWx74v6L*o#wL(Z?C5TvZA;AFOi$UU8A?ma>>D>9hb^{PFZk*cK}lRIc6Vm#UMIe)-2ilaiIfE=w?jp5P|c)ijS8p)=KqRsmnUB02v`zc'
    '@Kz*e2xbM3uiXx9%noH&i3CH<CqQR8C;B|J7c@peF#T9;jduOvm4zN#aKCqYAS6^MsA1-#>Yq<cdcc3jovrH<R`p!_bfKSJ6<!Ho27#_!YFG#%KfhuVwu!'
    'em`iKSh*A5tXGZyjLgT*FoEV0&1F=T%EUNdjDgnJhq4`N!qV}ZGzm7(MMy`PZ10*pgyBv&BUvfaqZ2(*raw!Zx|o__4w!?k46t~!bdOsXfo^^Bh)$xD;_-'
    'fd~g@QANT|$e3B-iA7!zmx+SRURCv6{R?=NzVam(;HkHU#?&VGk4uee3LUWyrd_19tm}7LwMCsOk%L&Go+MVTgodR}~f*0UC`YcjUcB5?8Woezs2vAMc1w'
    'YwEYRw`{C~Zrq*ts-tTgI#TK7<(deI3yxQ}wy88M3*jo%uKf#p_rWynFL{Kfd&jZ!4mCuRP(sVw`Q2<WxugR97Qb<KZ6Xar`<6-v$j&s0-SQ2Ujx)&eK@v'
    'n{0`Zq9&7HQF0WjYlvD`66(M*;z{AhHH9!Z&anUcuZ~9{Dd2mDa{L?SV_jyEWd!`dkUlGY2K&+r8c8?BaNj?=2P!JB&`BpuKqktR!B<GLLTRedwBP6(K0G'
    '}9zEtyY6I^!5t2_2FSnz=W=pp|6=O24b;T*p>_R^-<)NzYdeU#=s>Ic(8toLee(~Xi&b<n@pQ$Eod8gkAdUk_duPh{rx;b(LD67HkQqw-KGXR>57N#n``>'
    'F-MnJvI(HZ%!!yE9P;&^|@U8vDFEoE5GqwTu!;YLHFCF`3A@1FDl{bC=a3Q$ENfbI06L%NB->aX5N&_;jLBeI*n7Jc}SeHtseJA{jhgDd&EOfYiN5?M%og'
    'wf=;MSXz<gO7d)D5qe+5N$jg;|@G5@cPIZEk8|!omv+9Y%wxG-oue8VQCXM?~V6mqFs?97g>In;KDXFtCt(H##vJ(IyXaD+f2erci*pQA01HVoH)h(kVm|'
    'K9OO@6(pG3tN^aW9qEk4$-;JE#&`xURHwoy1_WHFb-8gtMi36(Ai)%ofcNK(jOA9*Kk0rZO0d6<BpnNl%{M6PJbRj)0p<lWekHrzWVGrgx|$KxR*}=G}bD'
    'Ed*MAm=&9_jo49#fAqDMEAa+jY|C7WDM_fR$P0zn`?Y|gwQ{ycU;?TPdfXkdmD*)Aj6FO24iEJ;DhQ7upUK2(Zg*M}hvVWNn%$quZS%&QD^?vl9<vc=S1A'
    'fru0^*X&AB4579SA{Ab2Vtl;B=D>!y{RW{)F#8@3CtC(hyH&>9&hbKG`4FQ!WS(a}_}KsQSAn^J~Bg~Ux(f%S5wSc!adUS_gzb<vas=z)!_dxzZ=`?E=wK'
    '5pPu<Ox@`Jduqvi%#KQDE|f?AEQM~TD2-jZ3W%)KE;+)&;z4!=UM1+ZHo9#=bDIP(`um_T_*8_XL628r2-7EzE#~ZFn>>J&%I@NQ@3nt^Q1p>@ab<<nSH?'
    '}QAb6Z$_@c+%B2?WfBn1en6B0dmlvIaF0XNZV^QzqA0EZu|K(rX%u2N5$xThwY_LZgpDRaPmCu!p>+@=-h6Vw|%2&SkM_qI4!^`qct*8w>Q;dTH@yhE7m2'
    'q~5jpHA@>gZg)1qcyXj09k{Q&8Kfqcu(GZZ91aDS2E<)V@;}!=hqt6_XcoUSw0?qcQ@TJ9Q>EPrwSqoS#;jPU=u+A(`ViU<049TbomBp{pHLobz0y$Fa{T'
    'rD~v+ccZmD=%`5|9qnc_&nnzxhRwlz4=N%Y=0_)VffsBi9;oCx-IBsE$+#J1a#g?^*VL1#avXGr#X?`4x=CnDfCY9+2MU?q&g&z!t3?8v+^$WQ+<JDLm{Y'
    '5?GfB#mmC2Sfb<l^E)YA_24ODVRYA^Ub0s>3H4P6~P;58*4h#^vFQ5J&P9urcn5$EIHmDhJfrc=g~OzzS3yW00QURB17tG68#<FqtLeODY+>gXmd&Nsf}X'
    '`EGyzWDp!{^Kw66vm)c>k-fo{{(L?q~{mvJ&YDK+a+XY{bde6x>#pZrTT5x4ttlzZ)3MXEdgzK6|^<qtJ;KFiSLqT9R@qSCd#dk@FyfK6?q-EpPFxuCUK='
    '&Fd>*^QhnV_0Ea(7*q`cmIU@GTLpskmokr@WxS*+HecMM*kNhN^wkw!~tnaIAHf5*;_2V~AE@>P}K{;+O0goaA<h1hI#vcM|B6HiA>K<O5_(xDnTpQd##e'
    'Wmmzg*t@Fu1um7w<3s{EHXr-i$~iq&qc6y6YfPTj7*^%v|2_0V}@=rUv96Y*O4Y&UUL(e61W@njbCYvM9IwCJeP}z}&~&eT*fzKN~;k1CTnW<M(NPZz|=A'
    'zW7Pd)Li*}l*a?pL_mF9n)3MQ69q#3@=nFS8g$R7*~&a4wNlTytE=LKnQABjCmQF3-)GQ@s!_UC?||X`m{Nzn;>V&)Z&QjDRTGRyT@dWZWk>ooA`6zA1|<'
    '|2Y=Q3iH6(Cf4q}T(U1oHA^Td#YpDJ028WP!B91O=;C&gZtv15A?Zn)B-h|>ehFYQfh_R}WCz7f!_Fm$rcP1Y2A4UIvrhDzp)sp@HxpWvOGq%V>FCUkDg{'
    'A27ZS?l*7{6#AXYi0}=)C577=5L%VbxSEbbEA!sC{08b>YV~klg|E~IB%FnNrx>i;F@GLH(6M+fmLrO#x^|X`i<7tca5}qMTXwb8do{=_`Ika3I^@_aA3H'
    '5aB+ms)h#W47VRrIa-89K3eUl667(*tW>mv!<NqAM_RJR4&Z9kyG2B;K9d*hO&E(zk;L~$=;|+H%h~HEqpF3Vt<8)8fj5cR_35v9>k-q14HFH{<+QAkNF^'
    '7H@b^Ae|1WDqj-%0rFiMNFG<A&EYnobb1_b%<zVHcZGWZP3!Lpv+CuU{f%O`n0=N#OPh=&DW7S5V3I<!|9}@IM#hUG}k}z00w#hU^G_TVw9xc=93~o1*#N'
    '68R3)*THk_wln=rGu^ca&n<b|EHOpb=ca$vOmA74=hpn*!AhH==cfNbXJDBXyOwgq6Rlm<tuU?Xp?DX)VX3jRzKP!QKtn@aoG~aIJZ0os;`B*r(AG-5&Zp'
    'kz)95Qa#_aMs-Vu-X;TxC=-@1IMr(jMC*<Y8h+*Y5M+Uc7&8vU8~0pUsIRI=5Z6c4=cQE+c$&oi&lJX!c_lUlt7(cjrkt$zLr`L9bcny4v;U=ptE*uGwFW'
    'w0TeCYE^+b=`g^EHISPQz^{kSKOYamUmgG{z6Jf)9biRXr$bYp6%st`@7*oM`!fSw@32^!&wWFSiMWHoc&N-zQ1wW;(7-!Hmxr)lP|Gp&k5Y8nbIi0-)cc'
    'jrAZUU$PG9)A1h~@DoI3Sn2k;pVY(NIlrSFjPPJ5BNH%_*PWg@fTE!Sr=n}H(b=2{OjeMSW^UaGjjh_sRl&4I-77N7WS6ytQZkz5P=M;kHcyC~mh_U$R>-'
    'U$sD^4YR)2V8WV;~1krIX($pRSjyiVzBdZ%)Qv9UqU6kB^_*>YS)VFV7Pz)<q#QYTnS0O)``F%cv98&BvP;^HoRLbG>M-=I_U+iP-gnL&`xj{gf@$+S;aA'
    'twF_Fw@dt4+L}%atkum1`zivRm#FrjX}z~@khHtyk9r@yL|^Bpw`jc5Cn(Ww%xg$t7ru-XtrS*M%XC6f?(c4#q8Ejkqkgw|u;+{mL%ye}=Dk{cl2XQH(S&'
    '*in(peNY3&O*e#a)aVZ%Mj?OpWs9?%ymlc0Nd6wsI&gy;n?fa3JX@K~E6Y|x|#9v1zL8|>5WI?%WAy#{5i$A#90HteND_d2(4FjILoYl=Hc-}cPj`!xG;^'
    'YD4|!BakAh7<!nYhifGZ#E5Bb@1O%O9KQH0000809Z6>UAy)P<Twrh06QT701N;C0C#V4Yjbd6V`VOIdA(WNa^lDtzUL`AY$bv!48|UNyfTp39%jdtnX$|'
    'E?q-Xks77i)v5>TC3CvPdrSb~NW8^;fd6a#Ue19J#VS9FyT*Mbx>i+vbA6xZ${WcX+L>bS5IAT2V8JAK>xx^Y<h%gbUWV1MB_j!_pfk@dEPxv$lgKWb-<k'
    'NPocJIZhU`w8*!4nH4^F<g;ManY~ZkXIe*+OK2r*H?6FA{+tAdhDZJM2CXpe5Olxsb#|#Di3{Ywuzf#Tm<`0KR3+q$0vsz&jV3BWXGMG3Q}03p_0Yc6gq}'
    ';7351BuV2H58JhRy<VH8@sdp@vpmaFF`2MnnZ#)Z&Ok~XmbIE$^WtP<pBLFOw9kK*aisAiJX=6ei{uus#c2`Eg9z+OHmubyFYbqZ+HQb!5Q1>C4W-B7N;I'
    '17gs0F(?Q;0}>cgjtyFd1i+uhpz)y>`Te)9hM<FMbL^Bu?M8F%mx%9to+$TsofG+8iXzXsD5Pl3#2qsc@Fjau**aE5T7-r8Zzec7n60<O6~$;4CE5Rn)AK'
    '{W3>c{V#ZbDGWCyPHoJ*PkaJFD{24@B3Tl!f~DVO4DqbOQ=IiMhMiC({e7cf1AdB?vdsX<VI#<$-Kh50CEM8J0bB3dV>89R*AA8%4v6J2@d~s`w{<#cOY7'
    '0_*0a>55f@s1$QjmWC8C{E|-Wn2}MiM^2m?LH8bHYqBxA_8<xS{L<(T-DB$|X98O6gA%E|*G!bI|io@L!a&__@<@j(=CNn+_g?7tq)57^gaJ@DQ<Fz6ub3'
    'j2AKKTz^RADcWli(i!xfYPZi}TReVr;AiNRTwn=L=>7$_s>SF}aAnN2w`fDO8)M92gcnnhV0dtKC0bd^4QfeEV>9^9hz7X@a+D5T`*F{3QHRVT5HVxC9R3'
    'y<){eAC}?oAgZq-t~4N<^F-m8atX~K9>gjjPK7;nhXt`F9Yh%^JW>G+8PY6-zp{0ZEtu9W4~tXp<2+?E@D&(3-a=TR7x@x438EE}iArI<@B)eR_VCR*LPl'
    '$`B?3`qF$F0}2}46qe4dIuv997JJVhlEPuqCPy+^!GH)OX^0qeB$T(<8-ikt*c_y@8T*z!cx@>Mb)unreUTMSG|B13?)IE1$x<Oy_YQIBi2nlEN75^EE=j'
    'i#%Rqyn~%RNiX)LL~HHf_LPUIbAyAro};Ag)q6s)JXZ-;6kpv40-g}Sq2g|pX=-kt`H2LZyv}A!7Zr;q4JYR<2GeiI*D8aG*ksXlWviV@!Ib@jz(Nzl=jt'
    'HmTt<;RUZ+;GsTNq6i=Q=GS+z5Bx0DRaoU2b<@&K%LCOQ<wQ{TBn5qP2v#DU+pa1f=6Jlpdayd=QEY+Asx7T0w`X~Pdx~a(4LPV^q40U4g8Oacrk>6Ogx>'
    'nIXict_vWWHSTbkoqvY_TL2v*5{4MT7_s8tsqLk%QbSoUtl$DV&)N+gEqj55v3b3#DKS(1s(WnWQLb7-VCGY(<RA{z&Um(;GdGn+oG2VYK83pQ!+Iku@Hh'
    'WI9p`nMWh@VqJ9mp@<q9bF)Lw7Kf@p1wvI|4%JCht@~Ob5P$Eud2Su4^ZHGnE?fia28Z>i(nK<tBPsNqZzJv8!gsX8pcN>1?j5#IULN@vECa==4cYRbAvf'
    'q3_4wuSi>$+^AOL&ML|R24U*YdkP|AM>YCL7@XxDIDZN8Rc=sT`?XgN9oLpryrG$%vH66&?W4y}T?$|_a~j%%M<j^@g7_5YSr^5qs1?~L1eNZS+CChA!l^'
    'wKh}VqEqyiq}zp)Oc*IjAyl0%D1#XLB&hzILNp!y$VW^eHl{{X%GtSs;lN6CPje|*xg>i<hb=HHvNz<r#@#-?$f9{)<L)k=8OLUbH(D%P#=`IBfdmfZHoY'
    'O@kDE{$Lda<F)8#vi0eum7O+k0_~Y07Mmp~3_2lAdX+5IiTwGo`<I*{twcw9b$OWC>YD(^7ON-(vA(1WMEQHH(SG%g_$Z%C;Xfx35W{dv?m$FqAnNgPGnu'
    'k`!iFFnshgZgHcDkp?9hJjnkwf=%U(6lS6A?#y!_s`32Hv@CU*z62Vsimosk*Ia38x4J^Z_V-lN7?MP>?njCezI%@XNY+Z@Mn(gw&xx(o6yrXs>{pEBTL5'
    'j*gi@6vb@Di8a+f=|KlE7gmcZ1<z4WrC@cc+3O$wV!2W|fo1EMiXM7JA&S0EQq?vRnaUOCS(0b{k@hm>Ibe6+MN4vI<URpdFD)5~*XaD;nWRRWqr-6veUu'
    'g+8g*y&Ev@g^zy8U#8i@{}U42*JQ5--{;y}sk?xi+l!G2Z!DrN|7<ODukeY<PwB@k-vodkm;4XBBZ`>IdT1*m9SR24Frfrljqt)@1HN_b5Jxc2J4-ZdTry'
    'FX4~H6dS1ohGaHU#3_Crqc}_w?+Yr25?k_$+%RDg0-AM$K)w5;hQ^h#qMd@rDJMfc~L^o(W@w5Ls0XKJ#YUcOJZ22($Ti-&BA4<-G{vjs+BY|9=XTAz${K'
    '$SK2ZCW_-dmuR48<-FA1j>zt@6^D@92Q&nqe#M_qjn~s$Aw`n;xK}AYezT(&nFj<+--D!S-W9NgKGEz0YkV5@{&!bodx^FL12}UGJ(&QNE)FPUf+hyxnQq'
    'IuZI!$!RpT*kw5>4zKeBs8UAh_fk>P|!5-<&g*Yy=2pwg7XM<SE8M_%~nk)Nk*%u8O4bU^RwKz<8ExA2#Zk^@nYbhn`-u(#%GVn!P6TxayV$FWP5gqi=4o'
    '24niRU(;v(KqgS2O1fic;%<2H?g#e%=8k>%_S3~@b~pU)diedzDFP!T_czM@78RrHby?2P>L=cx8%ePg7FOVhClETDEJcQFyeBl>tUzvw$}<c3qnOZMqck'
    'DXPIFI_bYSFYQBm?CC9PEYTTK&bAB|r$pU@rCYneio6!;DgDKRA}CS^5@e|Y%xu^4VOnidlhag7?1OF{hwvXLx`Nb)PmX7$pnKxf+^)pxqYWLpzypziB#w'
    'AuPGhuicY(p*>-pt_(A`}$s_PZvjfE1LSLNge%CjZg(wgDx_-+MIJrfsWJua~wpCnbXVCK`-+MTX4~skLr{r>PTz74i?o${T9irP723%LW#|<kG0<G`o5u'
    'Ffi`H6?NFvmL>-WEbW)>Svl=;y5y$j_MbA^^EDQ#{smAy;s#7*2e5%ZuwUXKCfc^ZJzq2hCl@01Pv-LVaqbWbBWIC!eSjeJp&=F!!QTrShk?)r*X$*?ZG6'
    'DZT_}owTC;N=r0%J?bbbl(UFr5V6<CpkNpYdjS#`;pwC08JqN|>Hl4jOi=NbEY75kRXrSFk|K&0YrwE3&CB{h9N=kc}?TIg%<}fqM%Gw-H%IAnF933#2to'
    'QtYeodDmb9bT6~a9LMSX=H1QJ!w<JZbvHfe(Ju=*#*Dg%>Uc+19Q2UKINklFQe^$Qx~Roo7G$9q6xaDGb!aOSQ`P23MT3H_^<=ie|7q-Rw%b`8Wp4K*dFp'
    'iACnrqb+#cjX>jM34c<#kvoVs5fogAON`TBgxpAOc6pDo<44-b<kyr=UZa^K*%x~D%+xKCNwJ!D63lBeCSEjD6`-fFuwhz<|m`e&!-MD<`TFfwHB+mpldP'
    '-N&S4<y~;;&{7zB$gUT20sb6+a+X+u4Y%S9iNsAoPj<_Dxjk(Q1`3=I>_S0JqFDAlqyzwFpaY;Ub;ZdWE=)Q`^uk+6Y<sxVFA8Yg2;SY2yuG)_Up4ZSX_u'
    'S-frm{ajqsB_p4cVb~ZaJ^l$_%DOFgaDffe1Duq}1GTJi5YP+Qp8uE=h3&qnpnkFp>y&bGmywXnr4}r1acF&i<rp?nmCG+etb^^xub2bRd^4dMF@W7@e6V'
    'ovE9xK*3Qi@ik3&LxJ&`gMmD_r|<ZWuW{{4HSp0`L{B`{GoTD$}+OgYC9z+}&;#Bb3rT<B~CrN!}iv9iQ>4O5Z3h|F9Hj=ya_m9?0bl-b3ZGJN)%JIwE=<'
    '6>GH~!3}zTuwq__Y==P9Zd@PSe|vlT@p^d2t}bpbF0VgcKm35M=9044yW!RK{q@afc6oO_eBbNfID)r3cr_HU-b*ZY_*T6HtMrjA2c5{Syu`OTvIO&B-7M'
    'W$NB~?>Klls^9gPO)brOhI5sW;zPC5DVl@9`xmwU+z&eC8$7ik3}j$iG4DR})LHmZk|g7%m(?q46gT&xdn(|Br0*eQW(3F>)LZqZl)k5de23%r8Lex?*pi'
    'N5EIM5enUApH5S{~(-La>kvmICWd?quFlxD;TYXFzV+h->5Dt!KOT<4yZ(G4LLD8U!q`Cvp5=Dlpk<m+oCa0vq@Q`;ZH};{i*2E?G-hR4E6%DbgAm_*k*U'
    'Of-?HX<31m~Iwx&*WiD~BsRliBrK9!UW}nQMsXAmmG+`!HJos&8ca=B>w)ul{?#p%u8py-JwvZEs#Cy@=0r(pvmjbTTKoyW0KKv*$N{M%-s2@P6$LC+DLW'
    'I0gAfZ$(i^itTUcdbOM3$J*cPrIL>Z6+4R;}zT@tzKiJWbW{ax8LH$D_jI<z!}~6liZS)nH5qzZDKu4`MmgS+O*>Qad?^o}FM|%eDUEgE>=wforn|jMhtZ'
    'jOwa{la;`s$|v-p3;r3A9eLnu*8v3bCAd}J6>SJrzRsyYXJwcM<|7kaGG8XD-D;UJJq)I)x*)S7t#Uond3iKl)AvVxT+vov{;O_VH6ae)F9<Y_!j1mUSR4'
    'TQAPMMO8Jy233(8mdy`%aqbYQiA15ir?1QY-O00;o!0BKz<vL9Yo3;+Q7SO5SN0001FVRT_HV_|b;b6<01Wn?aDb8l|lTy1aMHWL2cUqLKdAi;U>R&V=~+'
    '?T}hwK-fI*LHdr^oj*n;(A$2qDoSBHbMXU4XO9FB(J@RMO=WQYf>VI!<mP}(L?_F9YSB=KZHg!7`;HFHz)7jk5B$Ho=mLKQC1P-h^VSpGQ<L%apF@!S&WW'
    'Zl(3k@QWQ_hZK9t%`9y`J@l{dovow}`tEzq^Ji_s|s1d}MjH`;O-3a>|8rNQzoL*fK{nXpo=L8FaSSpiLBDO{{<trK!<d@<g$xuXyL~90(Vj)pLpwpmekF'
    '9=(Zt0Dd^&C@ZE@H9Vgj*yxoTXPA)%2RP2w6vy$wakh9Zlg!8dGSV#z@dl**gN=Qn>+XP{@Q(^8AtFkjip|F(JV+z*2W+Pwd%v;*Bk@l;t+gM)rn8OsO<t'
    '0lbag;TWqi7aHVL5>7EZ`KvC0vR8IqtA0Dx@7L}~|NJd~m)y{R#6DTxKnrV1)I3X`lAUTL#KjhdL?rcLfRZ2%b>#L1^0$6S#*#(^37H1lBV^fQJ$&^3@(t'
    'R+Y%{(^pkkPXSV)dxLIQMrdW?J$hQ%PRaH2Z7taMy|dbQOrq>_g8GnUE{bb}ilUl9hfmu42Q2wqvnOcJ3QJjMz3mD0$k1jpKjl-31WF_4hsC>f^-N<thft'
    'J19|oCT?`IvKA+c8h2PB{w7j^QlZT1S`?nDpmgW^s?p|Wx=ee@POj0m<cMDIML1SXk4%`Rb6*fuW5|4`S?<Fa|Pptzb$*B|CQY*OG*4qOnn?e_2jRMS`D<'
    'XW=xmQYvm#pGHVXX9sRGY^_h@M&?4bdX?EJ|P1nM7-4NBA)mBL|zkh-3wpzx*tk#;eR8tsqtlUzxw4QPfMyes?<imM20UO5YXBcYcjH+X|tW&yKvg?L+RW'
    'Xe~ik1qICP_#MU*6I%7j*QIWFD?e6&w?0O^oio;NygRQk~D5VwVrFtbXdXS3~0faw}~Ws+k?_aU!*kECs#+xzsQhJBE<k^9{Jck`rij4G+1^hrk<DUoihH'
    'f*)xj!1M1)bpz%ZktJA(OtpWVvKSCHP`*<jYNdmSC=aC~()dA@3kj5&5K`k~@c+M{x_o0Su2C*yr3%1q!T2(R9KGD+&XK`wl!kzz0TN&%m{T^YSu{AXwr1'
    'C>6>jL&MwiZx>Rz;5VQ|cB!2$eG4vrWP09`V`_X{kc#Y*!xgl`xqDu7ia1nUH#3#i~}q9;qY{b#w(MG=*eUJ`5GD>AJtn^^yIwoagv_zLE>g!+cnG+uZQI'
    '@P!+&>PCLg|nIl8iMb^`lkUAmcoz#fWzP8P%VxL4VgqMqUH~gKT?_~Db*~fG1j`yMQuf<x@bEOG}M6o%ug!dEL5Sq4`#n1BY?CFNlg4}ShTT7c^!qDYve`'
    'VJ7T3O>dysfZIQLAMK+VXH0L);OSPKD0{HRt@~4x_x5te|Zw<;F<uCks)IFy2G_I{znbO+_lKY8TiVBq?k{d$zn4EEK?Rm_YGBe;rd1X1E#@dy|2tLk{=u'
    '74108qYa?p+=#={QG)6GbfcOh-r0D`NszBg*=6IIjR0^D81%>9ke~R+H*w%mO?rOFISv@z?m4kkVx8D>~w7TnUi}J(U~%QX65b^N9>>+br9MAP;)0E2inA'
    'rG*}YmS~)^RG_z2Y=Qnoa8UKNW+7l#n$*>*0xD$|pk59kAC#1klw)K0I(WRu{A_dv!41S_c)ivUPRL-D0L9f@oyM@R%7$x=3MXE!ws%MHhQK<{l1l7dsMG'
    'EnsCD8>X=GkRHz~g%+q#Mr<odM&W!6<dJRMuscrtI;b%8Q_Z#|l?3Hn*T_KpNJjbM^NkqK9E{<H6`N%Y^;o><QJGcS5xe;vRu!;}q8T6Qu0JDH{cclT1e='
    'rQ_v*3^i?GaYg`_qlO}7~o#(apui0p;T{c)MiBo@5Q^Q;nH{Im>VL;!Vo#Ei7A3urU+tp2x33AAdV>-aZM4#>k!0!YC)!^2x1DZTBZQ2WeT#|rXZ_r3bNX'
    '^DS|kLxUcP+B8X?o)R=;-wkgPJ&rQ+D!Vp26i7A4Zf~<}y$m*C9vpS~4td1$j>P$@$#1v$8Oo>??Q({)vl$h1E41svpHboFqVpi9bnAJ4}SzS|NR@W3{bx'
    'lE5*A!&+OhH!9l$g~sC1&+ZiCI0@kj%4Z3bJ~p#H^kv$m*Gbtez>zI-MBeHPc~{wei6^z!EP-j1#e8ihJ-yRqM*T{MXZye~%{<dzS$F4mt@aj?v{teftg3'
    '#a2iX-J!ppmLKWs-;2*!SmU5p#Mg_2_!Nh7i`IC>^D&4P?rZ)*9)SSxIN>n{4G5NU82_4alzo!_gf;}rG5M4cQ8-F4uNb-w>Z@iTt+xoHnA{dE6?9gN3eM'
    'Lm6*MM7Abg8?(8Ft8jGak4ueF<0urI&0;_{4+_u#j#aVS~|t_`!oLcqARFf0zYFHxM^RnBe6Ng|-zEhS-qU@~CVw?ytRTF({Df)jxP5~!C5JeqMGk9L}Ba'
    '!;W_9E){D^W9~(mg4fFhm0JmrzInERh+YzD1g3-d8CS6gwi-7vYJ6PY4`J6ogIFwW$nRlt!uoE;99TmX1LDoA-K*u2(F&j!El{<UF25R>m#>%edJchJB-}'
    'wK9=0-Ok2pUHO=m@Tbng)^wv|>!)A5uem3i3vKO1xx}VKz?Zaku_G7c|D7S^pn){4$)2z0G&3egTfx%%44*ddYno|J*8f|kvF#M^35j_L9MTNyb@1wS!5s'
    'j>E99FB9!|HaCSl??FDpFFC^6<fWn~}hZHA1n$#v!0>jt#w})fN(G7dNnl71vD<v%Voc?4E_Wog8)n4~7kH*xwa7td|mYTBG0ftnQs;up+SdnrtvYmV!##'
    'h?QV1Ypy*v6xOz{N&q{!>&2r3)q}e}faZ00-`0SA+XL#{8F1Y0fPH%d>U=ujxCcbFPWshT=zKBUxa|RPt&>;v1Uf%}N_BYO1LB(PKDEvtomSCQcxN}Oate'
    'KJAWG!u80!tzLyi-Fh^Y$WFCe-n;%;u`Z5+V<K!@!9ZsS#A<($B719aeXoMcCGBwndgsO2$Ztnwj6ekE^7?c;seRQH@JUQ;gQIKi;<&Jqavh}qowK_##j&'
    'JRU8K%GM?PnY#1SY~6#>PfI{%QIzroF0B%%dWhxpB|n){`7G3d`@;i_#bB<!MZpl;wabf8HODo+f9WOr=RrJC55fkPLAal3<Jn=D6&vJG%V9>%5Dk1hGKG'
    ')?XnSvnNvBBuFT3=)pPCaugaRhwh|hm5$4;6CQhci2ZQHNbTBx}WqiGJ!QELCXWElBS@b1Mtlp$aTQ<hj1HnBh6UXb#m{{&!8Izp@xh)A3XP<;gmUy{0Vb'
    'YT;DUcUw0kPk8?)PN(yl-~IFFTf}J@xJZ`-f&mT)QnZGM#s1MlMP;=j4|0>+BS-@*k9hsi+R~=J<QxVcu_*7jeE}UZitr9pJcJ+e+PkXwG@aj$)5bTROzi'
    '&%Z1#=|C!c0n5NN#H&z+K?#OONVxsV2RaV!dokR&4>`7RaNpK|ecJ=}?F=~I?ttU=1|0Wvz`kb#>U=)nxCg{FXFyzYtO3Vu57@Uepw0)xHD^Fva|XmUXFy'
    'zY28`DZIlpjd-|pn8=ligXpu3w9{0Z|F%dSx2EPO~h@c1+AO3^t<(p3n1r#tz;6P3B)ET%qE+@A=ZB0U*FKfA;wzgkXj=CTx?fbK&w&Z#zjCMa4l%!BrPV'
    '15S-lCaSk%UcH9&jhx*Dubc3t18_nxA}I}XZgldX_^FaEy>uD6r6V^1<$Ft-X|4!T)WWj*nSw%>i$$<ZKM%S5|vF*`*E<2q<Q~QKn3hlHQ6cGfK&!2S+bJ'
    '~{1B^#^o3k`(=dy=ty)HVjl*z-{p<4HzphN+E2J&}%t}E*nQ}D~!dK)fb&(E%I%r;zJMuZ)P*EfbLAWYO2zzG6Yga#ZCJJjeQ{@Hj6D10rX@8<{?mhGd!L'
    'CH1ZTBP!=Y5I7MPHuKzK>hAcr3MQGUUC1_oNM{d!-GXufwyNJyq85pNz(`1O?^4>oisu?bUEsf4q5Q#?YBRC}XJLa*TuDVW=QOap_;}69rX?vHapceckK-'
    'UBa+^<sBef*t(GSrwiSOgd^Ym_CHWd0|XQR000O8yBld;A0_U+egXgh4F>=K6#xJLWMOn+FJxtHZ(nm`Z*paGE^2dcZq1ZIZrd;rMfW+y!0T8LMOkhVc;U'
    'E4S4|qAK)NevX&e)kD1oHh20?({p*QSFI-~_lqEd9*jV*qP^JgAE^l||(tI&!<STVbX7h02I>Q?7S>)EGPH?_g}u9c+)^Q`Ovt;~V_{`qSGxoE^rmeM|hF'
    'b0jOP+6#i)$#}IYYp@^{kIzSGPkl;q6E`6O({`>$x#U{Ycsp-Tys%+Q?^pIg#xQu8LNfG;s%lxR;Zt(db$C=D)5M9-S}0yLSx0Ql;+@GT&zkIh2K$aSyHK'
    'CZ+MgiDw?hH+|lAt3H|M>#yx7kbqzdX-Trr>71eTG-PJ%9v_u0^(PYwqqh`>8&<ID=axbyy2dq$-R-^MZ5v*NRIQxN-PYwrFal;A)g1ibKXi{0!M><8o;K'
    'MzE$fcp@2p(D*m7bK4<oK|pOL)i_XfzF>qQ+b!0t`07VI#z~rtYaCacn&Rp$a&NBf{PNXX*x(yRHM$k0ku%GcB8jrm(fUJcGb8$hD-7q=;q&<<*gy^+-)0'
    'oA=v~_w((Sc^tE|Nb;I_q|3{*kdTl>NiT3Oq`i>(Ba2>Gc%gse_EePjLgIz27kGFi^)9Rz7G8MQ3t3=$y9{b<Lfg&Bwx4CggK0O;)<w|^ua^T>ciTsTmAn'
    'Cqk72PPy%VfBgvG|NMuW1hg)yzM!Y4{PQ5F*=n<&dr>6pc1X2}o{4=%zpW6{+VnU5ELgIGEyHcY~r2Y0ldOxER#h53rd#Mm$_JfwWe*HxIWEX)@h!%C+4O'
    '2d4`VZO34E1K>vtkQq88k3mhpvzYr!s7o^zSw|!moFCPD;+aSB7S1#zG@e*7k>ayO9KQH000080N?;=T|(fE+EN1m03rwg01*HH0AyiwVJ~BHX>?_BX<;s'
    '7b9RkYO>f*b5WVMD5PN7ZashuNJ#RJ%5THSVxapmyMyrV_QX#2b%fG&FNYR#^V4Z_)S)%5B%$t$%Ej6tlG`q&>0oT;A<HX**+MYKbrZfdoH&bLsF{(hi%~'
    '$nFOM`ap>i%Zy5*r?MqNq%--5!70se`u@%BwN>b}~r~e5d5iQsA%6tL?=Jw4ENc;WR7bUB@jsL(S$L4c^5RGE|(p4!Go!DugWS8%xU6H<MQbQBqw23G`#)'
    'Km%Tgf_`}d{i`0vvuRwb{OAn+ivV5(!7z2?)cYxc<bb;aqtIUcn6w3cgS#;)AE4Osfx;}PS0_;a@dj_+>s)#T{XQlr<Jbcn<)Giij)GV)j&{!SSER&%8wL'
    'f&d6=*W7mN0Ip2fdDLF3EPu%)b#ry|hOoygjJ(oUBiXGb8}&h<d$5gV1r^v+wq7aGqfE@er$yghHOMF&&(rHZ){!rikt$3%k~G{|Q%-=rg2Arv?PL2ZL;p'
    'y|-^Jv5hSjHFWz#|mJ`G9(VFR2424FLC)iQpgR`R?(dyYfChD9#h~ZKSh|ql7<6_J&8i|5QHao9B@FOFMq>^+zUxVzLU$$OtzJ#uuJ$UkBib`u{!o_CH^Q'
    'W@x;7SZcw1354X9<QNsWsarF|357r;^E2c~$P*+Z3OsaIWhyuf<XRYsQfk4q)IeFt#f{SEsa~xj3MB(2)_-WsdQ;DcWa8+Wgn$?WPDT*7}2@GgGn@zxDa_'
    'w32XY`bs6cGk*elr9x6HJm!%@V{KJtfYf-<pwzl|3MEU^<q0ponqTKhMM8FTw8~E-}7rTOlF^7ty5=Z{-P;Vl4ek6#rE5maQ$&>{`qOexZB*=&(zA9+mHE'
    'a_f@Zoi|@80!l(&+b%g58t*uUX<YczsA2BUAB6VdP^?`ay=!GO*xcH@r2&a$k(PBPuotIb7v^SG2Q1vhlg&pF!<{S}gVn(BwiJYq2z!kqE+eO9BcZCnTVd'
    'I_9CHG9mnYEw^U|{H{W|vB_B+gvj~}1XkG!5ot3`aQpH8fBeLym550`JIAYYw8zFt<Gj8v<~x&)fdb!q#<=OC5&P)P^wItc#s#}-*cpCjMbtoYO;U-7Z#B'
    'a8n5P)h>@6aWAK2mn|#X<b(=EL~a$001H=000*N003lRbYU-PZggdGc4cmKX>V?GE^2dcZq-`Na@#f#zUL`0K8F*@f2pgJq^Pc&I`LR;ddOrt5V@34g8+j'
    'c$x5d)eTP0w?|qa$Nq0d~lqQs9Urgm-St7v&u-|_B2Y!6P*dO@E*pcEH9DUD@F0a`zx_*B<I(k{$h>dVy1gD$*<6i%yx{*OV<4V|!?%WuNB=;(wu}mi*rB'
    'G9*Q)YdhO96((Jm;}+OU6~g+{|b{o#ozD!Y10QgqtPF`cYV?jflBqc`Y{P7OK%O7YV2sezT4{Z|R}8qtOksvCbi>Mj1%K&@j6Ht2XzvCZTXQb5Krb#iW=R'
    'oRt0h55ozkLgADKEO0{;3KUMG41D$iFS9x7A;opk)oK!vko2o}cTuO)tu7`y<3iz$kKs37=^uq}pUMF|&yAjQ8J?BWTW3(}9M)z>J&A-n=rN@o8w<!l*{F'
    'CB_lR=-eEBteL!V_r*;?H(828npABXAK86P`u009H*2+oz*8Suntodq~I=0MDJ4AwRwd*dfk#4DqSB+NlF?Om)h)UOm7t}EGxa=pm5fIe;?=vytNjc)Za2'
    '6jDo^QxJzXN|zVK@B+6fWwO_@J!-b6lpEMi6BpeB$#ov%A#@^kBzprrnAG3Mu_ib1|V9ZypoN~I-e{LoVh3M19~^U9<rPphdj`TiTJXevZuW*$c_}M0&pD'
    'ai?Gth1xRthv?S6AvbdCw*wB2;YU$}#Gi8mQ8lGiP({v%+tl}!pf=CL5TXd`fcOTe!C9^fWPus_Ppn-N-E}8Ua@yA@iq7m|wZIBO%m{E!`k~SOE!V@$CTZ'
    'v;6NVNf`@T<l^tg~FgLjnE73z;;*J}$URK{pr>?QG@zR}uceS$)<%${)0xYc?Fc8ejEqnt&Y~_Xa1u!D(-B)*HNTMEEC-N@5nDDFdd+!lZ$71kTDU-z&Y4'
    'kW69axcB5&$DMBXzrX&*f9C~Q`w*S2o^1`)^X;e(p37J3rFNYCl0oJT-v;aHZb0e66mS|7K*SjnA2=MPQZF_@4j#9Ty}&cOkF<fXNOi83(E_m~`8qvt!oE'
    'HLXekWS<PH>Hi)9U*J#Pf}x_%ZjRX5X#4fq;}y$OLi2ZIhd3nQ=&a^$QVL$9_js-n113FM#xYGFgEmvYJMOfS^o$J_7P2ljHr`hc+#V;Hc}^;ILV&3wHxx'
    'aKOQ3KT>Irzvxq;jD<l8h6)eTf*N+RTL*-l_J+w^1&Cm7wtniM*rt=n{URiZpLq)0OWX0&oNJMw>%EpPD1F6kW2(BrA7)zDR2wa=$;q~51cZp9wUAe>;`a'
    '>vKaQN(C7ZDw*AQ3?X(Z=l}gbaQWv4bph{%yw%)~QZ+N<mwMFfU6;Dl2#;pZcxMXz1Rx5=W)f(s(7aM6i)TnsnDG6ScL!qHn&6NVTqAZ><t4A%8?4bBvHS'
    'iUhiFIO%`eGOxSiPlZH-eo_te4f-;WOF8h&x<-LTRtggHsg>h5Jx1J%Ra`h9{o8bzfUW)*`Nkex+iBj0=24_TvYEyAYw+QCpf?qX&VU_p&sFmHd@~2vyWv'
    '4i3Jv)jd9#<hn1cpoPbjAupSt9(H#W#AWVV`S2hJeakeoGuPcg>efilQq)ot$lZ&J*K01CHkoT>%dPQH5*t-_HbcsdgU}O%j19kf>Ary&u%i<;e9jbn#=m'
    'fbwG3ilH=7NQFoC;OW3v=PPT$(1$+AJxe73aJNkh;mu753sYb1Pst`WY32+pUl83-zSWss&2leo}{q3wV6ymT%5^K~fEZOsf$+c$&DYqlzRmROSI`8FdsZ'
    'Zv{{Um_7pFTd{iOHs_;qhq%epG&X5EXFMBc|~(&b}KA-l*)%-z)k=kF%h-JH!649@MAN;a;dbm_5;D$0T{rD-OMy7@xaD8#DdF^R27c*3Ep6YdY(vOXJ`b'
    '5=OT$JAsd09atq6yMfrP08!JsJ5!U#e9`E5r>Vw0^@rhS4ova*oMb|w)0GD6H{I|kLZSQ%VoJ~-k-PVKIQmrEgoANvYxZCMO2`4LxxK9Mhx8%uH$o87K4%'
    '4EqzN+(RW95RUQcoy&Xe{{lo^hE{QfojTKzj|H`pwnw{kRd*Zm(>cHlK8iX9Q!aV^5gDmZPpZv=`^l<fkzYo2n*ok2{@{^|X%qFTIU3tw)|oA3)}I06n(;'
    '`1)rC*#weg6QRc9z1ySueak^+C8R#1h6jwWW&ZYi(Lt|0t<gNexZd1rtCDg$LMb!xLJTHpWHxm>6&-qv9_Sl*2cdh>{^3?%n2AS%p<j%A&X6e7!PxblNpI'
    'Ng4NrFW<|;B%AH?v0SaqNo-cG>6POEVAHRnQ>2Cx(N;?yjzdpGMD8t$F;Ji)wQA%qk<Xl5=Y8?w~~cC>EZeHe}Jt}gp`BQ|Wy8jd>$)wTISo1{K2Ug7t|*'
    'N-ZLsPT_y5Z{-*JBhe$W?MYo`W8d&0w|G0MY6nj6{+$D``!E+&aI*R+%K5D`1C(eO9KQH0000809Z6>T@XyB6k!Pf03t8|03ZMW0AyiwVJ~lHW@%$-VQgP'
    '<b!BsOX>V?BVQF$@E^2dcZnaw5ZXCH0ec!Jj^ppS|TXSh$5(I%g@*)BpuWfnr66Aryu9>05CfmG>JiAz6pYj38exbi)tH|!2maH^d>FF0i8cnn7u&PegDe'
    '~v<7&~z$SOF)0Vkg&c-u!s;@x#lH*Z+9U-v9Xe=HvAbZ{NPW{_vW8{q;BI_S$d3OTj(|a9$eio-u7a!%vx6uceS&u^R~mXvcCR0{-Gpp3zHI+)44h1eH5{'
    '(?9Ve#(s`J@t-os&!*4nKNVkrB73g5hm-i}FV7x%V)pG5H=!(*1j{rpx*nZ(JnH06U5_q09<`u&+?TB^*&pDG#9h*x7aH#V*s)^v?TSkiw72_?ht4|8xW1'
    '|$#Gn6)+i!6v^Y^va{)Y$7n<X6x`XVj*PI0Xf1mikqOI~sz{r;r+X2~}cIyxxTeCFYcr$_(B9pg<LK+dMKNntRCSPlg(SJrEn)(CL!uZMM|Qo(sNTkc?Kr'
    '3YKt^K#m;DHlgZ@X|tUtJreA0f#OYMhmGB&YeUk6#IO~C3-;t0m(yrGjn1Kc~H;`)T{&4<&i;MI|l1DEw#I6u&7pH1#lNE0^}*R5inUTweN*x-hpL$I)aC'
    'Io=aK^$p;f}?Hx0gnH^X!3t$ej!dMEw)gHsqd5%m)F^4bhg=f))XL@|+SYDKqP-3L<Txv`UhEU{M5&~Eo0?c+sVNx-v1%Au*i?OT=$7}?@2z<R1=oR=JWJ'
    'w$l7xKm^T2uq%E^z?G+6Dv6dA1HdG+EaN*Q+i<n9j$*RVRv-?v@x~C*iKm2LdfM1rjl46%rs|yy3qE&q0e`zIxTg2h+vzV~(s=M#SP3S5O#yEaneJTsy-W'
    '@CRP+g{YGivd0kpo$IjX0>hz(^)8hOw!|W0jq2|)f>&UCwdt;^IpEqADl&aqUG)UkNe^cu0=qJh9Ouv+hPH`Y{L`AS*_Oc*+ua#^%LE~_y`Xe5#QDfRS{d'
    '&ZXb_lE5;Mgo$_tKGZc38a3oNq~n7z7%S7%+2E=GieNtId#Dnu!h4s{h5l?4Xiu4jy$ccHi(*)b&&9Jyl$6UreEnj?)dP7MUI0tTTlMX7-D$D7`Db=k$+v'
    '(u451zi`OLvcdVF6p_{<k`IP6i3?I|J2V@%P!)cO~;KlO81G>6AY}4r3J9rmfqOZ`c!;J4bY}n5n6Up_G~t?gG>o%6V{&CdD3#0JY`8-diTWYv+N@2*?eR'
    'uxZ^tKHlIX3rY^^(8r13?_!_On8ubYg*Pf~*$6!@7d$eJAAGo4AjzH1=MydA+w6(O(PfCt9?n%<8;)5utS7^Gvs@A%}0%(>U)BflYVR;#yY9Ts>x@hu;Fm'
    '=|~o*688W@pE?zG*KtDp8|x(+gr`6x+_p4RM;e(_mfI%~)G$J)VMYu;`hcA32_^F@7R=aFEE>$(H6xnIV*++BsP0%r1^>JB2>*m5k3H1_Adnq2Od4SIHxZ'
    '+4_2-Q{K!jj~!bL_h6e}f$|n~?w*too%&^ddTgUn2Ad+biPc7v=E9{P6moFr41Ns3GM^qfim)h@X`xm>g4W7aoZL}g^^|#1rzn}vj=lf5%fZGvS?_x;9kP'
    '@|%Oy!*VU2T>b<m<xktvu4i<0@HrTYpLu44Dm>2J)2rm({G_Jz@t*skaGGKapsno)3UuON>N3E-bOx@fo>nJ<owB~`i<HO>4IGo=U`Y01|U3m4+(o+3^gT'
    'pb2Wl6f`;6dFk+&(Ii~Qr)o?rx?Sm!4Qn|C2ZKJ^#EH}#lcc!el`XeGy_xKSl^ni5)B9y@{~1A_>oX?gT=@Ed<+;;lQcBAfai7t2myVA1yH)}!*;MKf`hf'
    'k{9=^wLi;9EENtvYSnNl-rh9{h$NX{x_Tsv(b5u;M2_BjWB>AHWt2n$ItSuIg7V{6_uy=qsCZKU7DkiDJlZLD`_E9iNhm#LFC>K_7NQc>OY<pTXSZXY$Bf'
    'ufAFshKmP?#E?ne`zrl(_?oyawc(5?d{N4-Hk~tc8=`21}5|Y$PXfg%;>&O+05&d)Csgrc5IDX<EHgdMxH6Afa>0!yFX}j0m`D9vcQubMRJ&DV+@w;9yO%'
    'Sd8SJCdPuNR-U3N_Q6eu*{(ODc|mh7J6NAAvXPLjXe=Cc%E4+2SWvZ-s|IT&hX*T`#o0Kl(43{L6?~DkhNLqI>S}_{BPYb;=ba%&r!Nc^FN^b$oPxg+8&G'
    '$@35v(I0F!0|rZlRG#B^j<lBGF)p!QD_mYwAAXkXCWidY(j+T0}V{ePStHDi}lf~r+10C|)=smKo2G>gkIP<%3y@;x0o#N00c=yHl<Tbkg-?&hGD`%j8GH'
    'BELp1{Q-=l6|i9DmkO+X{2+g$k<LI3(zr<p;M(TE4d{?7_4iu=@@Vt7QoC8MO8E1mfL$*OiJ`ziIvB<=6@b|F<9SZvtxrw=gIM&LhER??h2@mg5F@RKpYt'
    ')VOopn;X)^ykKrT|I?l($sV#kYvqYdkwTH^|32n!wG@Ypr);!r_3{+K~R|D?{<&#Fs(iY7KHc?1oYd2W@WRJE6*DZn~qi%3z<lbr&`GlNG<;w(jkMm4)Sk'
    'M(fUi#)d7IVu`yVUcbuTvCdXJcYZ<ES`grtycOaJwhFt6M^C;P~4oIL28_c0MMw2Pa<#@lB-R_!=t0ugO2%V{?NAQg$&Ws<tCA%YyQR5aNkhN-as}=k)*H'
    'WYMXTvdb~ytUzO{6Zy|2fm&ZXX-+!R%@achn)Ng}jv^>j2g{|i(=pL0j6b5pwKWApLXY%Xrw_U>I2e8{?QA+Ggj?9RC!konsMU_6lKa!FrirD|Dp<O;{3N'
    'Z^zFv%_{095^c#nMg_1FJqhfAhZ4qwp4k&Ue`m{GUvP@S%l^hDytegM_MyQ}a2%vPvAZ`of^|J-VGr_&Yl({znI9wgjxb$cb9P+Vdc6nCy=DtrI+-~V~};'
    '?;{KMqgRR7Q;ducN2?5q3=Upv7$GAUqX5Ziu~AS?eMGhE%rN*n=OH(Xim~B5h^Mgv475fXqk??OG2R<CZxet>~_9joyFC~Hr~ak3N2K7kQ%<{37^9T9AEa'
    '<cyQkU%d!c2p=g=$oF$-X|FMq8PNg0rr6{7$BD#Q0Blnf)LU&8T8N<B3&ab(Qr#Z<!wCTHFeg{xX0|XQR000O8STt!}=HyKrumb=9#t#4h8~^|SWMOn+FJ'
    'fhGV`yz*a%*35Wpia=a${&NYIARH?N?2Y+cprr@2?p6EEU;JQJ}f)A%_BK3N$&i2!etp$JW#osc=ZI-J-v%_x`fZ=);z6q`(I0`mzVZ7AZ>e=FNLE{%`~E'
    'r+few<QA`B@$T2R_3fe>mNI3Jy81(Kg>xd~8UFbj$a}psnYIWm<|aD8ooPFdJe_5<Ii|D2(`LdgF~y+Uybrm-Om^C&wu>oaAI{y2yYK4T+xo@#({4##HbU'
    '`!3eqfDRzCDs6Pg*KA-+1qd<gCg+$EZm8#|LQ<dc_9>t>xy*UVpk8p7}*-0A7XJ*>!PL2W#A-h>Q-G{r5p^7tu#ub?#)G6oYY0^0^%@f6lzf&*vB@4-iAk'
    'a+Dz*R2WApzna3Jcd?#NN7t+y6579EVcN}49<|5;BY4~-JY#;-VZr>`_s=q-oN?n{p(-eFJ`y=RXq+Sm#*`KNuunGrL4hi2_Jxh^~E8>DoVJ9GdOGoVx`|'
    'P^mL$u+@x66O;>V{U$H=rV4MSPXqEZ1$nO3ZWI~rk=6X(?vX!=)`xqpuSiA(+p;aoDhEdqV3WNzvm9Q*3iYy@)KcJF~2zA1C!cT>gY)VpKi-{zWMj!iGlr'
    'JBP^6>lP&3r|#`V3rn!QF)y+?O2N*o)=SR&YG~>;$7klH^L5H%`h#bS+vyu(8!w@v$PZ+2o=8wPNCuwd5QuW0ueZ+Rag6OH@tiGg``8p;uG?$|&#q-UWom'
    'sV>BpY|+3NI13z;96ZFdslYZStWkuOB>RR-8Wh$;?ofCUUD#-BBj)zR%3nqA<3nA#$-zukcfx@XrX7fF<wgi>gbfB-$u^!id}EYQwRd5Tg7yH5SCsb4OKD'
    '?@EM@d1%ASrs3wx}76|u)%Ed}6;&GTLuCSe1HwUh()-FlQs1>*_rC*#c3H$SvZkcQw#naB%5PSNw#^!<CJvmr(VPg^yi!rI$qToDaR^v3U*xPni`_(NAaH'
    'a>-yutOt6dz@?kiB+x+TQ6f#Nl$d?sMd34m}xDP#MlpHP9~HKNNZi}@ytj(x_dtb@D(-x?S<ywVM|g;8f#2nFx{V?e^&qb<eP{$Q_pBkCk-M|?q$qnS!cO'
    'rsF!hkCoLZ@6J;2}o!a`<L~cDw?aORlw4Im1sjU1zNff7MXF_a6;(#o;dLgKZVLudW%4h#*Mrr624SPcGo_>PwB1;4IQDUV(2H75bYxHHFx$TL-D>=6&76'
    'MuQKu{belmp`ww#ffId3{x(-+cTRP)h>@6aWAK2ms&!X<Y?BM`4l#007Al000;O003lRbYU-ZZf|#HY+-9<Uu|z=Yc6VYZ*J9B-*4hZ5Pr{JG2$5{LXx|t'
    '_e2~wL6;Z`N!zHctc^XvtE_i@yK6Xly8pei3j{-`q2wy{ULwUF&(H7sX83Xh(8yJajUS<L+YdfMKe~B<Kgv$~_!O8BV9KHp95wJ1rRA2R0VY#Wj|TOGS+1'
    'l3Gm|z$%abN#Oy^4Szc7U-r6I*!HJUDpQKe4MP@v!GUwSaQ9}I4K;V>TdMjzwbZq&UBZ^P)$n^)ft!r@Q-AsGZ=omu!x_vXHP*Xu{GUJb(=|6+9A8&qA8*'
    '`M>|7FDj&`{MsrUd23hO}Y$k`>pV|R=a(?2vfC@EcdPKTEPqqG$!0ohagaSp(HiXtUl5x=IzUP;l2q!b7Q$2uPhQ(N~>q?<rV6j$=T{%s&dAqkJY@WIOXP'
    '<9xk(YPBaZIVIoekKuJSPyu(pJxiR4f6+{8#EXla6hW823$YsgxEPfJf>_I}qwMtj5T+G;%dCum!j>wBZSO$hdtF%m9sUWz-4={H-cBw!in1oVJQ1d5_X='
    'CB`>q|uiY621!pWu37O2(GwNOcKLpU>hVv1IW>r;^$e*T%*LGbWyK6zRg|{J3I6aJ8A3#R)4|LZ#CC<954UEf7DITw@w<Gkv#anv`18m}7w~jZ-#rfI92E'
    'Dhek|lz#f_HBq8yOzu1w%WUaBZ}fyHjn!m6LC`qiI7Qu}CQ@}dwX71p&|GOZt}*kN>UNsYJ!!(l>Ds`&k60?}!8&?~?ykeTUI0e2!eq)4^Z8g3GOPk3wrB'
    'B533`_wV4f%ueC`XDEqXn_D$L`2oZF3x6OZy(O(kkiFc*s;L!Cs|2tuZ0V_ZWV0Rj_ds!bXYjvRbJNil1JbVWcxl9Mq*SX6n=t#em(^FrGx7lcfz*mz$Lq'
    ';XSjGY8a^`{ZBhI;vDxs}WK7D~Uv>MkH<t^C>6z-(`;70!A}qF|Uz`2&Y@sVW6n`bh|hN2Z+NZru5W$04UcPFZt$~+C<L;dt4WQEi!S<$61|51T-xg(R?n'
    'j<P$ui8!d3s1LMc#fL3Zx{x>UwEQQ#u4I5TlDBsyz9L~;mX@iUQHg$-ojbzVLH?N&qaMpz2JJSMxI5-UMCj|GBO_@$9;fWF@F>MdR2TPt43293us<lGkzh'
    '}O`4o+%_A1Q4!%2-3d{K`M{D!8XzOofi9cr@GSf5>I9$jNIk^#>@?M=l(ocU%S}8f9Kb`XM?BINzRdz=_-6fY;}zyIKAIyq?qNdvp5yWEZDT-o1^{SFBiE'
    '+x{Y|q4Wh&`ogXE_um<%m$5#T%pnU<j_ESo$?YW>;7Jperb<5p8*9XU7ki&@?u*uJe(N5%)lX~4ea$qjN4TQhzSr6RPdj}lw+~tDqw=w3UE@(;Vm00JiQB'
    '=ONglS-BWf&(CMC^;MJ?wC>-={gcq}E#(RQvZDcyJfpPjy8Q6~T!rvJ@W4<}9m67<aTO|8>`;F#8WXUA&)+4-U9l2K*;KsJQ1*6McnHr#fo*mG5fp9`Vrc'
    'a74seb{?1pC!fGAg%iifAsZlP)h*<6ay3h000O8$~0+R5}W|rq!<7IwnhK|2><{90000000000q=5hc003ofXK8L_E^v8JO928D0~7!N00;nBG-+MC_6g)'
    'T4gdf<Apigj00000000000001_fy)>G0C#V4Yjbd6V`VOIc~DCM0u%!j000080N?;=T`jU7URMkN0Qy(}02BZK00000000000HlE}CjbCsVRT_HV_|b;b6'
    '<01Wn?aDb8l`?O928D0~7!N00;oP8);o1CGNd`0ssIF2LJ#S00000000000001_fwnUM0AyiwVJ~E5ZEs(5V{dY0b1rIgZ*EXa0Rj{Q6aWAK2ms&!X<b6#'
    'joMNJ001Hg000pH0000000000005+cXEp!;WMOn+FJp3PbY*gBVJ>5Hc2G+J0u%!j0000809Z6>T~{nDU0MeK03s*=02crN00000000000HlHFIRF4;VRT'
    '_HX>N37a&~2IbZKvHb1rIgZ*EXa0Rj{Q6aWAK2mn|#X<ZOZrW9cb001H|001BW0000000000005+ccR>IEWMOn+FK=dMX=7<&Y+rG8Wpi|CZ*Fd3X>w&QY'
    'IARHP)h*<6ay3h000O8STt!}=HyKrumb=9#t#4h8~^|S0000000000q=6Po003lRbYU-IWo~0=ZDDe2Uvg!0Wnpq-XfA4VZ*EXa0Rj{Q6aWAK2ms&!X<Y?'
    'BM`4l#007Al000;O0000000000005+c08an_WMOn+FLQ2hcV=v1Yh_<;Z)0mNYIARHP)h{{000002>=NISONe5$Ws6S000'
)
_BUNDLE_DIGEST = "46d1d3786372ecbdd63e1b921282af2956f27791bc5673daf9d09111b45517ee"
_archive_bytes = _hub_b64.b85decode(_BUNDLE_B85)
if _hub_hashlib.sha256(_archive_bytes).hexdigest() != _BUNDLE_DIGEST:
    raise RuntimeError('Bundled demonstration data integrity check failed.')
_hub_dir = _HubPath(_hub_tempfile.gettempdir()) / ('supplier_capability_hub_' + _BUNDLE_DIGEST[:12])
_hub_dir.mkdir(parents=True,exist_ok=True)
with _hub_zipfile.ZipFile(_hub_io.BytesIO(_archive_bytes)) as _archive:
    for _name in _archive.namelist():
        if _name.startswith('/') or '..' in _HubPath(_name).parts:
            raise RuntimeError('Unexpected demonstration asset path')
        _out = _hub_dir / _name
        _out.parent.mkdir(parents=True,exist_ok=True)
        _payload = _archive.read(_name)
        if not _out.exists() or _out.read_bytes() != _payload:
            _out.write_bytes(_payload)
if str(_hub_dir) not in _hub_sys.path:
    _hub_sys.path.insert(0,str(_hub_dir))

"""Supplier Capability Hub — internal supplier-development workspace.

All cases and criterion ratings are explicitly synthetic; calculations are shared
with the optional Microsoft Copilot Studio API bridge in api/service.py.
"""

import copy
import html
import json
from pathlib import Path

import pandas as pd
import streamlit as st

import engine as E
import workspace as W

st.set_page_config(
    page_title='Supplier Capability Hub | Supplier development',
    page_icon='🟣', layout='wide', initial_sidebar_state='collapsed',
)

BASE=Path(__file__).resolve().parent
H=lambda v:html.escape(str(v),quote=True)
MONEY=lambda v:f'€{v/1_000_000:,.2f}m' if abs(v)>=100_000 else f'€{v:,.0f}'
NAMES={r['code']:r['name'] for r in E.CRITERIA}
NAV=[
    ('Overview','Overview'),
    ('Supplier assessment','Supplier assessment'),
    ('Compare suppliers','Compare suppliers'),
    ('Intervention planner','Intervention planner'),
    ('Investment case','Investment case'),
    ('Eight-stage delivery','Eight-stage delivery'),
    ('Supplier questionnaire','Supplier questionnaire'),
    ('Research library','Research library'),
    ('Data & Snowflake','Data & Snowflake'),
    ('Microsoft Copilot','Microsoft Copilot'),
    ('Briefing & export','Briefing & export'),
]

if 'cases' not in st.session_state:st.session_state.cases=E.new_cases()
if 'scores' not in st.session_state:st.session_state.scores=W.new_scores()
if 'active_case' not in st.session_state:st.session_state.active_case=next(iter(st.session_state.cases))
if 'nav' not in st.session_state:st.session_state.nav='Overview'
if 'chat' not in st.session_state:st.session_state.chat={}
if 'compare_ids' not in st.session_state:st.session_state.compare_ids=list(st.session_state.cases)[:3]

st.markdown(r'''<style>
:root{--purple:#4B197E;--violet:#7133A3;--plum:#29103D;--ink:#25183B;--sub:#657083;--border:#E5E1ED;--surface:#F8F7FB;--accent:#06A9B9;--mint:#E9F7F5;--warning:#A86A16;--success:#14775C;--danger:#AA4D4B;--r:12px}
html,.stApp{color-scheme:light!important;background:#fff!important;color:var(--ink)!important}
.stApp [data-testid="stAppViewContainer"],.stApp [data-testid="stMain"],.stApp [data-testid="stMainBlockContainer"]{background:#fff!important;color:var(--ink)!important}
.stApp [data-testid="stAppViewContainer"] *, .stApp p,.stApp span,.stApp label{font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Arial,sans-serif}
.stApp h1,.stApp h2,.stApp h3,.stApp h4{font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Arial,sans-serif!important;letter-spacing:-.035em;color:var(--ink)!important}
.stApp h2{font-size:1.55rem!important}.stApp h3{font-size:1.12rem!important}
[data-testid="stHeader"]{background:#fff!important}#MainMenu,footer{visibility:hidden}
.block-container{max-width:1290px!important;padding:1.15rem 2rem 3rem!important}
[data-testid="stSidebar"], [data-testid="stSidebarCollapsedControl"]{display:none!important}
.stApp [data-testid="stWidgetLabel"] p{color:#3A2D4B!important;font-size:.82rem!important;font-weight:650}
.stApp [data-testid="stTextInput"] input,.stApp [data-testid="stNumberInput"] input,.stApp textarea,.stApp [data-baseweb="select"]>div{color:#291B42!important;background:#fff!important;border-color:#D9D4E4!important}
.stApp [data-testid="stMarkdownContainer"] a{color:var(--purple)!important}
.stApp [data-testid="stMarkdownContainer"] p,.stApp [data-testid="stMarkdownContainer"] li{color:#4A4657}
.stApp [data-testid="stDataFrame"],.stApp [data-testid="stDataEditor"]{border:1px solid var(--border);border-radius:9px;overflow:hidden}
.stApp [data-testid="stButton"] button[kind="primary"], .stApp [data-testid="stFormSubmitButton"] button[kind="primary"],.stApp [data-testid="stDownloadButton"] button[kind="primary"]{background:var(--purple)!important;color:#fff!important;border:1px solid var(--purple)!important;font-weight:650;border-radius:7px!important}
.stApp [data-testid="stButton"] button[kind="primary"] *, .stApp [data-testid="stFormSubmitButton"] button[kind="primary"] *{color:#fff!important}
.stApp [data-testid="stButton"] button[kind="secondary"],.stApp [data-testid="stDownloadButton"] button[kind="secondary"]{background:#fff!important;color:var(--purple)!important;border:1px solid #CCC5DA!important;border-radius:7px!important;font-weight:600}
.stApp button:hover{border-color:var(--purple)!important}
.hub-brand{display:flex;justify-content:space-between;align-items:center;gap:15px;padding:9px 0 15px;border-bottom:1px solid #ECE7F1}
.hub-lockup{display:flex;align-items:center;gap:12px}.hub-logo{width:37px;height:37px;border-radius:7px;background:linear-gradient(145deg,#50208B,#8B4DC1);position:relative;flex:none}
.hub-logo:before,.hub-logo:after{content:"";position:absolute;width:5px;height:22px;left:13px;top:8px;background:#fff;transform:skewX(-23deg)}.hub-logo:after{left:22px;background:#30DDCF}
.hub-brand strong{display:block;font-size:1.12rem;letter-spacing:-.04em;color:var(--ink);line-height:1.1}.hub-brand span{display:block;color:#706482;font-size:.65rem;letter-spacing:.14em;font-weight:750;margin-top:4px}
.hub-environment{font-size:.68rem;font-weight:800;letter-spacing:.11em;border:1px solid #DDD3E9;border-radius:5px;padding:6px 9px;color:#64408E;white-space:nowrap}
[class*="st-key-hub_nav_"] button{font-size:.81rem!important;min-height:41px!important;border-radius:5px!important;border:1px solid transparent!important;background:#fff!important;color:#554A67!important;box-shadow:none!important;padding:7px 8px!important}
[class*="st-key-hub_nav_"] button:hover{background:#F4EFFA!important;color:var(--purple)!important}
[class*="st-key-hub_nav_"] button[kind="primary"]{background:#F3EBFA!important;border:1px solid #E2D1EF!important;color:var(--purple)!important;font-weight:800!important}
.hub-divider{height:1px;background:#ECE7F1;margin:5px 0 16px}
.hub-hero{background:linear-gradient(110deg,#261044 0%,#4A1B77 56%,#7543A5 100%);border-radius:12px;padding:38px 46px;display:flex;align-items:center;justify-content:space-between;gap:20px;color:#fff;margin:5px 0 21px;position:relative;overflow:hidden}
.hub-hero:after{content:"";position:absolute;right:-90px;top:-135px;width:370px;height:370px;border:45px solid rgba(255,255,255,.07);border-radius:50%}
.hub-hero>div{position:relative;z-index:1}
.hub-hero .eyebrow{font-size:.66rem;color:#56E6DA;font-weight:800;letter-spacing:.18em}
.hub-hero h1{font-size:clamp(2.1rem,4.1vw,3.4rem)!important;color:#fff!important;margin:12px 0 13px!important;max-width:630px;line-height:1.04;font-weight:760}
.hub-hero p{font-size:1rem;line-height:1.6;color:#E0D6EB!important;max-width:595px;margin:0}
.hero-domain-mini{display:grid;grid-template-columns:repeat(3,1fr);gap:6px;min-width:260px;max-width:300px;border:1px solid #ffffff38;background:#ffffff10;backdrop-filter:blur(9px);border-radius:10px;padding:15px}
.hero-domain-mini>div{background:#ffffff16;border-radius:6px;padding:13px 8px;text-align:center;color:white!important}
.hero-domain-mini b{font-size:1.35rem;color:#fff}.hero-domain-mini small{display:block;font-size:.61rem;color:#EAE0F1}
.hub-context{display:flex;flex-wrap:wrap;align-items:center;gap:10px;margin:2px 0 22px;padding:12px 16px;border:1px solid var(--border);border-radius:9px;background:#FCFBFE;color:var(--sub);font-size:.8rem}
.hub-context strong{color:var(--ink);font-size:.96rem}.hub-context span{background:#EEE6F6;color:#61368D;padding:4px 10px;border-radius:4px;font-weight:650;font-size:.72rem}
.hub-context .warning{background:#FFF2E5;color:#975D17}
.page-head{margin:14px 0 19px}.page-head h2{margin:7px 0!important;font-size:1.74rem!important}.page-head p{color:#697081!important;margin:0!important;font-size:.89rem;line-height:1.6;max-width:950px}
.section-kicker{color:var(--purple);text-transform:uppercase;font-size:.67rem;font-weight:800;letter-spacing:.13em}
.section-title{font-size:1.08rem;font-weight:770;color:var(--ink);margin:19px 0 12px;letter-spacing:-.02em}
.card,.tile,.domain-panel,.gate,.data-step,.insight{border:1px solid var(--border);background:#fff;border-radius:10px;margin:0 0 12px;box-shadow:0 2px 11px rgba(36,20,55,.025)}
.card{padding:20px 22px;min-height:124px}.card .head{color:#6D458D;font-size:.67rem;text-transform:uppercase;letter-spacing:.12em;font-weight:800;margin-bottom:11px}.card h3{margin:0 0 9px!important;font-size:1.12rem!important}.card p{font-size:.87rem;line-height:1.6;color:#686476!important;margin:0}.card .foot{font-size:.75rem;color:#867E92;margin-top:12px}
.tile{padding:17px 19px;min-height:109px}.tile .label{font-size:.75rem;font-weight:660;color:#766D80}.tile .value{font-size:1.78rem;font-weight:770;color:#301C49;letter-spacing:-.055em;margin:8px 0 2px}.tile .note{font-size:.72rem;color:#817A8D}
.chip{display:inline-flex;gap:5px;padding:4px 9px;border-radius:5px;font-size:.72rem;font-weight:720;background:#F1EAF8;color:#62358D}.chip.warn{background:#FFF2E4;color:#9A621C}.chip.green{background:#E4F5ED;color:#177A57}.chip.coral{background:#FEF0ED;color:#B04F4C}.chip.purple{background:#F1EAF8;color:#63358D}
.stage-rail{display:grid;grid-template-columns:repeat(8,minmax(0,1fr));gap:8px;margin:15px 0 19px}.stage-chip{min-width:0;min-height:88px;background:#FCFBFD;border:1px solid var(--border);border-radius:8px;padding:12px 9px}.stage-chip .num{font-size:.65rem;font-weight:750;color:#978EA1}.stage-chip .name{font-size:.69rem;font-weight:650;line-height:1.3;color:#443954;margin-top:9px}.stage-chip.done{background:#EBF6F3;border-color:#C9E9DD}.stage-chip.active{background:#F2EBF9;border-color:#CBB2E5}.stage-chip.active .num{color:var(--purple)}
.domain-panel{padding:18px 20px;min-height:147px;border-top:4px solid #A38AB7}.domain-panel.a{border-top-color:#5D2A92}.domain-panel.b{border-top-color:#8B61BE}.domain-panel.c{border-top-color:#09A5B4}.domain-panel .tag{font-size:.66rem;font-weight:700;letter-spacing:.1em;color:#80768E}.domain-panel h3{font-size:.97rem!important;margin:9px 0!important}.domain-panel .score{font-size:1.6rem;font-weight:800;color:var(--ink)}.domain-panel .msg{font-size:.73rem;color:#817987;margin-top:7px}
.progress-track{height:6px;background:#EEE8F3;border-radius:8px;overflow:hidden;margin-top:11px}.progress-fill{height:100%;background:#7550AA}
.insight{display:flex;align-items:center;justify-content:space-between;padding:15px 17px}.insight .name{color:var(--ink);font-size:.83rem;font-weight:700}.insight .desc{color:#7E738C;font-size:.74rem;margin-top:4px}.insight .rating{font-size:1.05rem;font-weight:800;color:#5F348A;white-space:nowrap}.insight.low .rating{color:#BA5F43}
.gate{padding:16px 14px;min-height:119px;border-top:3px solid #D9B0A8}.gate.ok{border-top-color:#1B927C}.gate .num{font-size:.64rem;color:#82778D;font-weight:800}.gate .name{font-weight:740;color:var(--ink);font-size:.88rem;margin-top:9px}.gate .status{font-size:.72rem;color:#786E81;margin-top:9px}
.data-step{padding:20px;min-height:132px}.data-step .index{font-size:.67rem;letter-spacing:.11em;color:#714BA0;font-weight:800}.data-step h3{font-size:1rem!important;margin:11px 0 7px!important}.data-step p{color:#6F687C!important;font-size:.76rem!important}
.note-box,.notice{padding:15px 19px;border-radius:8px;background:#F8F5FC;border:1px solid #E6DDF0;color:#5F4E6D;font-size:.82rem;line-height:1.6;margin:8px 0 15px}
.note-box b,.notice b{color:#3E2363}
.chat-panel{padding:15px;border:1px solid var(--border);border-radius:9px;background:#fff}
.hub-footer{color:#8B8294;font-size:.73rem;padding:24px 0;margin-top:40px;border-top:1px solid var(--border)}
@media(max-width:980px){.hero-domain-mini{display:none}.stage-rail{grid-template-columns:repeat(4,1fr)}.block-container{padding:1rem 1.1rem 3rem!important}}
@media(max-width:640px){.hub-brand{align-items:flex-start}.hub-environment{display:none}.hub-hero{padding:28px 22px}.hub-hero h1{font-size:2rem!important}.stage-rail{grid-template-columns:repeat(2,1fr)}.block-container{padding:.8rem .8rem 3rem!important}}
</style>''',unsafe_allow_html=True)


def card(label,title,body,footer=''):
    st.markdown(f'<div class="card"><div class="head">{H(label)}</div><h3>{H(title)}</h3><p>{H(body)}</p>'+ (f'<div class="foot">{H(footer)}</div>' if footer else '')+'</div>',unsafe_allow_html=True)


def tile(label,value,note=''):
    st.markdown(f'<div class="tile"><div class="label">{H(label)}</div><div class="value">{H(value)}</div><div class="note">{H(note)}</div></div>',unsafe_allow_html=True)


def heading(label,title,desc=''):
    st.markdown(f'<div class="page-head"><div class="section-kicker">{H(label)}</div><h2>{H(title)}</h2><p>{H(desc)}</p></div>',unsafe_allow_html=True)


def title_line(text):
    st.markdown(f'<div class="section-title">{H(text)}</div>',unsafe_allow_html=True)


def chip(text,style=''):
    return f'<span class="chip {style}">{H(text)}</span>'


def save(changes):
    if E.revise_case(case(),changes):
        st.toast('Saved. Relevant reviews were reopened when assumptions changed.')
    else:st.toast('No changes detected')


def save_diagnosis(criteria,gap,evidence,verified,approved):
    # Update supporting inputs first, then record the assessor attestation.
    # A material evidence edit invalidates all *old* attestations.
    E.revise_case(case(),{'criteria':criteria,'gap':gap,'evidence':evidence})
    E.revise_case(case(),{'evidence_verified':bool(verified),'diagnosis_approved':bool(approved) and bool(verified)})
    st.toast('Diagnosis saved. Review required for any changed downstream decisions.')


def save_shortlist(selected,reviewed):
    E.revise_case(case(),{'selected':list(selected)})
    E.revise_case(case(),{'solution_approved':bool(selected) and bool(reviewed)})
    st.toast('Shortlist recorded; subsequent stage decisions may require review.')


def case():return st.session_state.cases[st.session_state.active_case]
def score():return st.session_state.scores.get(st.session_state.active_case,{})


def gate_ui(v):
    cols=st.columns(4)
    for idx,(col,g) in enumerate(zip(cols,v['gates']),1):
        with col:
            st.markdown(f'<div class="gate {"ok" if g["passed"] else "no"}"><div class="num">GATE {idx:02d}</div><div class="name">{H(g["name"])}</div><div class="status">{H("Satisfied in scenario" if g["passed"] else "Open / not satisfied")}</div></div>',unsafe_allow_html=True)


def domain_ui(scores):
    prof=W.case_profile(case(),scores)
    cols=st.columns(3)
    for col,dom in zip(cols,prof['domains']):
        with col:
            pct=round(dom['coverage']*100)
            name=W.DOMAIN_LABELS[dom['domain']]
            val=f"{dom['average']:.2f}" if dom['average'] is not None else '—'
            st.markdown(f'<div class="domain-panel {dom["domain"].lower()}"><div class="tag">DOMAIN {dom["domain"]} · {dom["measured"]}/{dom["total"]} assessed</div><h3>{H(name)}</h3><div class="score">{val}<span style="font-size:.8rem;color:#8BA0A5"> / 5</span></div><div class="progress-track"><div class="progress-fill" style="width:{pct}%"></div></div><div class="msg">{H(dom["signal"])} · {pct}% evidence coverage</div></div>',unsafe_allow_html=True)


def insights(items,kind,limit=4):
    if not items:
        st.caption('No assessed criteria in this group.')
    for row in items[:limit]:
        st.markdown(f'<div class="insight {"low" if kind=="low" else ""}"><div><div class="name">{H(row["code"])} · {H(row["name"])}</div><div class="desc">{H("Capability improvement area" if kind=="low" else "Demonstrated in the synthetic scenario")}</div></div><span class="rating">{row["score"]:.1f} / 5</span></div>',unsafe_allow_html=True)


def reset_case():
    cid=st.session_state.active_case
    seed=next((x for x in E.CASES if x['id']==cid),None)
    if not seed:
        st.warning('Imported case has no original scenario.')
        return
    st.session_state.cases[cid]=copy.deepcopy(seed)
    st.session_state.scores[cid]=copy.deepcopy(W.SCORES['assessments'][cid])
    st.rerun()

# Corporate navigation. Streamlit remains the Python application behind the interface.
st.markdown('''<div class="hub-brand"><div class="hub-lockup"><div class="hub-logo"></div><div><strong>Supplier Capability Hub</strong><span>SUPPLIER DEVELOPMENT / WORKSPACE</span></div></div><div class="hub-environment">SYNTHETIC EVALUATION DATA</div></div>''',unsafe_allow_html=True)
primary_nav=[('Overview','Overview'),('Assessment','Supplier assessment'),('Compare','Compare suppliers'),
             ('Interventions','Intervention planner'),('Business case','Investment case'),('Delivery','Eight-stage delivery')]
other_nav=['Supplier questionnaire','Research library','Data & Snowflake','Microsoft Copilot','Briefing & export']
navcols=st.columns([1,1.1,.9,1.24,1.2,1,.95],gap='small')
for ix,(label,destination) in enumerate(primary_nav):
    with navcols[ix]:
        if st.button(label,key=f'hub_nav_{ix}',use_container_width=True,type='primary' if st.session_state.nav==destination else 'secondary'):
            st.session_state.nav=destination
            st.rerun()
with navcols[6]:
    with st.popover('More tools',use_container_width=True):
        for ix,destination in enumerate(other_nav):
            if st.button(destination,key=f'hub_other_{ix}',use_container_width=True):
                st.session_state.nav=destination
                st.rerun()
st.markdown('<div class="hub-divider"></div>',unsafe_allow_html=True)
cols=st.columns([2.3,1,1],gap='medium')
keys=list(st.session_state.cases)
with cols[0]:
    selected=st.selectbox('Active supplier',keys,format_func=lambda k:st.session_state.cases[k]['name'],
            index=keys.index(st.session_state.active_case),key='hub_supplier_selection')
    if selected!=st.session_state.active_case:
        st.session_state.active_case=selected
        st.rerun()
with cols[1]:
    current=case()
    st.caption('Supplier reference')
    st.markdown(f'<div style="font-size:.87rem;color:#49335F;font-weight:700;padding:3px 0">{H(current["id"])}</div>',unsafe_allow_html=True)
with cols[2]:
    st.caption('Engagement progress')
    st.progress(min(current.get('completed_stage',0)/8,1.0),text=f"Stage {current.get('completed_stage',0)} of 8 recorded")

c=case();s=score();v=E.calc(c);profile=W.case_profile(c,s)
if st.session_state.nav=='Overview':
    st.markdown('''<div class="hub-hero"><div><div class="eyebrow">SUPPLIER DEVELOPMENT · INTERNAL WORKSPACE</div><h1>Supplier capability management</h1><p>Review capability assessments, select improvement support, evaluate the investment case and record stage decisions.</p></div><div class="hero-domain-mini"><div><b>A</b><small>Readiness</small></div><div><b>B</b><small>Production</small></div><div><b>C</b><small>Resilience</small></div></div></div>''',unsafe_allow_html=True)
st.markdown(f'<div class="hub-context"><strong>{H(c["name"])}</strong> <span>{H(c.get("type",""))} supplier</span> <span>Stage {min(c.get("completed_stage",0)+1,8)} / 8</span> <span class="warning">{H(W.short_status(c))}</span> <div style="margin-left:auto">{H(c.get("country",""))}</div></div>',unsafe_allow_html=True)
nav=st.session_state.nav

# ——— 01 / THE COMMAND CENTER —————————————————————————————————————————
if nav=='Overview':
    heading('Current supplier','Assessment and decision status',
            'The selected supplier record is used across assessment, interventions, feasibility and delivery.')
    cols=st.columns(4)
    with cols[0]:tile('Supplier cases',str(len(st.session_state.cases)),'Two existing and two new in the seed scenarios')
    with cols[1]:tile('Assessment coverage',f"{profile['coverage']:.0%}",'Share of 16 capabilities scored in demo')
    with cols[2]:tile('Expected net value',MONEY(v['net']),'Siemens scenario · before discounting')
    with cols[3]:tile('Intervention candidates',str(len(E.recommendations(c,30))),'Matches to case criteria; review required')

    left,right=st.columns([1.3,1],gap='large')
    with left:
        title_line('Business requirement')
        card('01 / BUSINESS NEED','What the supplier must deliver',c.get('objective') or 'Objective not defined',c.get('trigger',''))
        card('02 / ROOT CAPABILITY GAP','Why intervention may be needed',c.get('gap') or 'Assessment not recorded',f"Gap criteria: {', '.join(c.get('criteria',[])) or 'pending'}")
    with right:
        title_line('Decision pulse')
        card('04 / FEASIBILITY',W.short_status(c),
             'All four feasibility gates must be checked, then reviewed by a responsible manager.',
             f"{sum(g['passed'] for g in v['gates'])}/4 gates satisfied in current scenario")
        card('NEXT STEP',f"Stage {min(c.get('completed_stage',0)+1,8)} · {E.STAGES[min(c.get('completed_stage',0),7)]}",
             W.STAGE_OUTCOMES[min(c.get('completed_stage',0),7)],'The application never auto-approves a stage.')

    title_line('Capability picture')
    domain_ui(s)
    a,b=st.columns(2,gap='large')
    with a:
        title_line('Capability strengths')
        insights(profile['strengths'],'high',3)
    with b:
        title_line('Gaps to resolve')
        insights(profile['weaknesses'],'low',3)
    title_line('Engagement progress')
    rail=[]
    for i,name in enumerate(E.STAGES,1):
        state='done' if i<=c.get('completed_stage',0) else ('active' if i==min(c.get('completed_stage',0)+1,8) else '')
        rail.append(f'<div class="stage-chip {state}"><div class="num">{i:02d} / {"DONE" if state=="done" else ("NEXT" if state=="active" else "OPEN")}</div><div class="name">{H(name)}</div></div>')
    st.markdown('<div class="stage-rail">'+''.join(rail)+'</div>',unsafe_allow_html=True)
    title_line('Investment gates')
    gate_ui(v)
    st.markdown('<div class="note-box">A green benchmark score (≥3.1) is only a reference signal. The Siemens decision still depends on evidence, a relevant intervention, the four Stage 4 gates, supplier economics and human approval.</div>',unsafe_allow_html=True)


# ——— 02 / CAPABILITY ASSESSMENT —————————————————————————————————————————
elif nav=='Supplier assessment':
    heading('Assessment','Capability assessment',
            'Sixteen project criteria across three domains. These 1–5 ratings are synthetic illustrations; questionnaire scores are separate and not automatically converted.')
    domain_ui(s)
    tabs=st.tabs(['Strengths & weaknesses','Edit assessment matrix','Evidence & risk signals'])
    with tabs[0]:
        a,b=st.columns(2,gap='large')
        with a:
            title_line('Strongest capabilities')
            insights(profile['strengths'],'high',7)
        with b:
            title_line('Improvement priorities')
            insights(profile['weaknesses'],'low',7)
        st.caption('Scores ≥3.1 are shown as at/above the reference benchmark; scores below are improvement flags. None of these are an award decision.')
    with tabs[1]:
        st.markdown('<div class="note-box">Edit the fictional 1–5 assessment scores below to demonstrate how a new diagnosis changes comparison. A changed score reopens previous diagnosis and approval status.</div>',unsafe_allow_html=True)
        rows=[]
        for crit in E.CRITERIA:
            key=crit['code']
            rows.append({'Domain':key[0], 'Code':key,'Criterion':crit['name'],'Demo score':s.get(key),'Definition':crit['definition']})
        df=pd.DataFrame(rows)
        edited=st.data_editor(df,use_container_width=True,hide_index=True,num_rows='fixed',key=f'editor_{c["id"]}',
            disabled=['Domain','Code','Criterion','Definition'],column_config={'Demo score':st.column_config.NumberColumn('Demo score (1–5)',min_value=1,max_value=5,step=.1,format='%.1f'), 'Definition':st.column_config.TextColumn(width='large')})
        if st.button('Save assessment ratings',type='primary'):
            try:
                newvals={r['Code']:W.normalize_score(r['Demo score']) if pd.notna(r['Demo score']) else None for _,r in edited.iterrows()}
                if newvals!=s:
                    st.session_state.scores[c['id']]=newvals
                    E.revise_case(c,{'diagnosis_approved':False,'evidence_verified':False,'solution_approved':False,'finance':{'sponsor_review':'Pending'}})
                    st.success('Assessment updated. Prior assessment and investment approvals require revalidation.')
                    st.rerun()
                else:st.info('No score changes.')
            except ValueError as ex:st.error(str(ex))
        st.download_button('Download assessment CSV',pd.DataFrame(rows).to_csv(index=False),'supplier_assessment.csv','text/csv')
    with tabs[2]:
        a,b=st.columns([1.1,1],gap='large')
        with a:
            title_line('Evidence completeness')
            st.metric('Assessed criteria',f"{16-len(profile['missing'])} / 16")
            st.write('Unassessed criteria:',', '.join(profile['missing']) or 'None')
            st.markdown('**Recorded gap evidence**')
            st.write(c.get('evidence') or 'No evidence narrative recorded.')
        with b:
            title_line('Signals to investigate')
            for item in W.risk_notes(c,s):st.markdown(f'- {H(item)}')
            st.caption('Scenario signal only. Actual risks require verified, authorized supplier records.')


# ——— 03 / SIDE-BY-SIDE COMPARISON ————————————————————————————————————
elif nav=='Compare suppliers':
    heading('Supplier comparison','Compare up to three suppliers',
            'Select two or three fictional supplier scenarios. Missing scores remain blank; the 3.1 reference does not imply qualification or a GO decision.')
    pool=list(st.session_state.cases)
    ids=st.multiselect('Suppliers to compare',pool,default=[x for x in st.session_state.compare_ids if x in pool][:3],
                       format_func=lambda k:st.session_state.cases[k]['name'],max_selections=3)
    st.session_state.compare_ids=ids
    if len(ids)<2:
        st.info('Choose at least two suppliers to view the comparison.')
    else:
        chosen=[st.session_state.cases[x] for x in ids]
        cols=st.columns(len(chosen),gap='medium')
        for col,item in zip(cols,chosen):
            pr=W.case_profile(item,st.session_state.scores.get(item['id'],{}))
            gates=E.calc(item)
            with col:
                card('SUPPLIER',item['name'],item.get('gap','')[:170],f"{item.get('type','')} · {item.get('country','')}")
                a,b=st.columns(2)
                a.metric('Assessed',f"{pr['coverage']:.0%}")
                b.metric('Critical gaps',str(len(pr['weaknesses'])))
                st.caption(f"Decision: {W.short_status(item)}")
                st.caption('Strongest: '+', '.join(x['code'] for x in pr['strengths'][:3]))
                st.caption('Weakest: '+', '.join(x['code'] for x in pr['weaknesses'][:3]))
        title_line('Domain profile')
        drows=[]
        for prefix in 'ABC':
            row={'Domain':f'{prefix} · {W.DOMAIN_LABELS[prefix]}'}
            for item in chosen:
                summ=W.domain_summary(st.session_state.scores.get(item['id'],{}),prefix)
                row[item['name']]=f"{summ['average']:.2f} / 5 · {summ['measured']}/{summ['total']}" if summ['average'] is not None else 'No evidence'
            drows.append(row)
        st.dataframe(pd.DataFrame(drows),use_container_width=True,hide_index=True)
        title_line('Full 16-criterion comparison')
        rows=W.compare_rows(chosen,st.session_state.scores)
        view=pd.DataFrame(rows)
        fmt={k['name']:'{:.1f}' for k in chosen}
        def heat_cell(val):
            if not isinstance(val,(float,int)) or pd.isna(val):return 'background-color:#F1F4F5;color:#778C93'
            return 'background-color:#DFF4EC;color:#236C57;font-weight:750' if val>=W.BENCHMARK else 'background-color:#FFF0E9;color:#AD6649;font-weight:750'
        style=view.style.format(fmt,na_rep='—').map(heat_cell,subset=[r['name'] for r in chosen])
        st.dataframe(style,use_container_width=True,hide_index=True,height=680)
        st.markdown('<div class="note-box">Mint = synthetic rating ≥3.1. Peach = below 3.1. Grey = not assessed. A high average does not override a critical gap, evidence requirement or feasibility gate.</div>',unsafe_allow_html=True)
        title_line('Which case needs what kind of intervention?')
        for item in chosen:
            picks=E.recommendations(item,3)
            st.markdown(f"**{item['name']}** — "+('; '.join(f"{p['name']} ({', '.join(p['matched'])})" for p in picks) if picks else 'No case-specific matches yet'))


# ——— 04 / INTERVENTION DESIGN ———————————————————————————————————————
elif nav=='Intervention planner':
    heading('Step 3 · intervention design','Intervention selection',
            'Research-linked candidates are ranked by criterion fit, then reviewed for scope, evidence, supplier context and feasibility. They are not Siemens-approved interventions.')
    st.markdown(f'<div class="note-box"><b>Gap to solve:</b> {H(c.get("gap") or "Not recorded")}<br><b>Criteria:</b> {H(", ".join(c.get("criteria",[])) or "None selected")}</div>',unsafe_allow_html=True)
    items=E.recommendations(c,30)
    if not items:
        st.info('No matching interventions. Add relevant criteria in the eight-stage diagnosis first.')
    else:
        left,right=st.columns([1.4,.75],gap='large')
        with left:
            title_line('Recommended intervention candidates')
            for idx,item in enumerate(items[:9],1):
                st.markdown(f'<div class="card"><div class="head">MATCH {idx:02d} · {H(item["id"])} · {H(item["evidence_status"])}</div><h3>{H(item["name"])}</h3><p>{H(item["mechanism"])}</p><div class="foot">Matched criteria: {H(", ".join(item["matched"]))} · Research reference: {H(item["reference"])}</div></div>',unsafe_allow_html=True)
                with st.expander('Scope and evidence limitations',expanded=False):
                    st.write('Scope / boundary:',item.get('boundary','No boundary recorded'))
                    st.write('Screening:',item.get('evidence_status','Unknown'))
                    st.write('Approval status:',item.get('approval','Unreviewed'))
        with right:
            title_line('Shortlist and route for approval')
            options=[r['id'] for r in items]
            default=[x for x in c.get('selected',[]) if x in options]
            with st.form('intervention_shortlist'):
                selected=st.multiselect('Chosen interventions',options,default=default,
                    format_func=lambda x: next((r['name']+' · '+x for r in items if r['id']==x),x))
                reviewed=st.checkbox('I have reviewed the fit, evidence and limitations',value=c.get('solution_approved',False))
                if st.form_submit_button('Save intervention shortlist',type='primary'):
                    save_shortlist(selected,reviewed)
                    st.rerun()
            st.markdown('<div class="notice">The coordinator may suggest options, but the supplier team confirms the final shortlist. A benchmark lead is not evidence that the intervention will work for this supplier.</div>',unsafe_allow_html=True)
            title_line('Three domain specialists')
            for a in E.specialist_analysis(c):
                st.markdown(f"**{a['code']} — {a['name']}**")
                st.caption(', '.join(a['criteria']) if a['active'] else 'Not invoked for this gap')


# ——— 05 / INVESTMENT CASE ————————————————————————————————————————————
elif nav=='Investment case':
    heading('Step 4 · feasibility','Siemens and supplier business cases',
            'Model Siemens value, supplier incentives and four decision gates. Probabilities are explicit assumptions; the numbers are not approved forecasts.')
    a,b,d,e=st.columns(4)
    with a:tile('Success probability',f"{v['probability']:.0%}",'Technical × on-time × sustained')
    with b:tile('Expected gross benefit',MONEY(v['expected_gain']),'Before Siemens support costs')
    with d:tile('Siemens expected net',MONEY(v['net']),'Expected benefit − intervention cost')
    with e:tile('Supplier balance',MONEY(v['supplier_balance']),'Supplier benefits − CapEx and OpEx')
    title_line('Four feasibility gates')
    gate_ui(v)
    with st.expander('Edit scenario economics and feasibility assumptions',expanded=True):
        with st.form('finance_form'):
            f=c.get('finance',{})
            x1,x2,x3=st.columns(3)
            gain=x1.number_input('Potential benefit (€)',min_value=0.0,value=float(f.get('gain',0)),step=100_000.0,format='%.0f')
            pt=x2.slider('Technical closure likelihood',0,100,int(float(f.get('p_technical',0))*100),1)/100
            po=x3.slider('On-time likelihood',0,100,int(float(f.get('p_on_time',0))*100),1)/100
            y1,y2,y3=st.columns(3)
            ps=y1.slider('Sustainment likelihood',0,100,int(float(f.get('p_sustain',0))*100),1)/100
            tech=y2.checkbox('Technically feasible (assessor judgement)',value=bool(f.get('tech_ok',False)))
            timing=y3.checkbox('Timeline and resources feasible',value=bool(f.get('timing_ok',False)))
            st.markdown('**Siemens intervention cost components**')
            k1,k2,k3,k4,k5=st.columns(5)
            experts=k1.number_input('Experts (€)',min_value=0.0,value=float(f.get('cost_experts',0)),step=50_000.0)
            travel=k2.number_input('Travel (€)',min_value=0.0,value=float(f.get('cost_travel',0)),step=10_000.0)
            testing=k3.number_input('Testing (€)',min_value=0.0,value=float(f.get('cost_testing',0)),step=10_000.0)
            tooling=k4.number_input('Tooling (€)',min_value=0.0,value=float(f.get('cost_tooling',0)),step=50_000.0)
            incentives=k5.number_input('Incentives (€)',min_value=0.0,value=float(f.get('cost_incentives',0)),step=50_000.0)
            st.markdown('**Supplier economics and willingness**')
            z1,z2,z3=st.columns(3)
            capex=z1.number_input('Supplier CapEx (€)',min_value=0.0,value=float(f.get('supplier_capex',0)),step=50_000.0)
            opex=z2.number_input('Supplier OpEx (€)',min_value=0.0,value=float(f.get('supplier_opex',0)),step=50_000.0)
            contribution=z3.number_input('Supplier contribution / support (€)',min_value=0.0,value=float(f.get('supplier_contribution',0)),step=50_000.0)
            z4,z5,z6=st.columns(3)
            retained=z4.number_input('Retained savings (€)',min_value=0.0,value=float(f.get('retained_savings',0)),step=50_000.0)
            relief=z5.number_input('Productivity ask relief (€)',min_value=0.0,value=float(f.get('productivity_relief',0)),step=50_000.0)
            upside=z6.number_input('Other-customer upside (€)',min_value=0.0,value=float(f.get('other_customer_upside',0)),step=50_000.0)
            willing_options=['Unknown','No','Yes with conditions','Yes']
            willingness=st.selectbox('Supplier willingness',willing_options,index=willing_options.index(f.get('supplier_willing','Unknown')) if f.get('supplier_willing') in willing_options else 0)
            mechanism=st.text_input('Supplier incentive mechanism',value=f.get('mechanism',''))
            if st.form_submit_button('Recalculate business case',type='primary'):
                save({'finance':{
                    'gain':gain,'p_technical':pt,'p_on_time':po,'p_sustain':ps,'tech_ok':tech,'timing_ok':timing,
                    'cost_experts':experts,'cost_travel':travel,'cost_testing':testing,'cost_tooling':tooling,'cost_incentives':incentives,
                    'supplier_capex':capex,'supplier_opex':opex,'supplier_contribution':contribution,
                    'retained_savings':retained,'productivity_relief':relief,'other_customer_upside':upside,
                    'supplier_willing':willingness,'mechanism':mechanism}})
                st.rerun()
    title_line('Scenario sensitivity')
    f=c.get('finance',{})
    rates=[.3,.4,.5,.6,.7,.8,.9]
    vals=[f.get('gain',0)*p-v['total_cost'] for p in rates]
    st.line_chart(pd.DataFrame({'Success probability':[f'{p:.0%}' for p in rates], 'Net value (€)':vals}).set_index('Success probability'),height=230,use_container_width=True)
    st.caption('Sensitivity varies the total success probability only. The nominal scenario probability is the product of the three entered assumptions.')
    cols=st.columns([1,1],gap='large')
    with cols[0]:
        title_line('Siemens value calculation')
        st.latex(r'\text{Expected net} = \text{Potential gain}\times(P_T P_O P_S)-\text{Siemens costs}')
        st.write(f"{MONEY(v['gross_gain'])} × {v['probability']:.1%} − {MONEY(v['total_cost'])} = **{MONEY(v['net'])}**")
    with cols[1]:
        title_line('Supplier-side value calculation')
        st.latex(r'\text{Balance} = \text{Support} + \text{Retained value} - \text{CapEx} - \text{OpEx}')
        st.write(f"Benefits {MONEY(v['supplier_value'])} − costs {MONEY(v['supplier_cost'])} = **{MONEY(v['supplier_balance'])}**")
    title_line('Open review points')
    if v['blockers']:
        for item in v['blockers']:st.markdown('- '+item)
    else:st.success('All model checks pass. A responsible manager still needs to confirm the approval.')
    decision_options=['Pending','Approved in simulated scenario','Not approved']
    with st.form('sponsor_form'):
        choice=st.selectbox('Recorded scenario decision (human review simulation)',decision_options,
            index=decision_options.index(f.get('sponsor_review','Pending')) if f.get('sponsor_review','Pending') in decision_options else 0)
        approved=st.form_submit_button('Record reviewer decision',type='primary')
        if approved:
            if choice=='Approved in simulated scenario' and v['blockers']:
                st.error('Resolve the open gates and reviews before recording a GO.')
            else:
                save({'finance':{'sponsor_review':choice}})
                st.rerun()
    st.markdown('<div class="notice">Economic figures are undiscounted, scenario-only assumptions. Supplier benefit streams may overlap. A positive model result does not award volume, approve spending or bypass procurement governance.</div>',unsafe_allow_html=True)


# ——— 06 / ALL EIGHT STAGES ———————————————————————————————————————————
elif nav=='Eight-stage delivery':
    heading('Engagement delivery','Eight-stage process',
            'Navigate through stages 1–8. Inputs, approvals and evidence are recorded in the current session; the rules block skipped stages.')
    rail=[]
    for i,name in enumerate(E.STAGES,1):
        state='done' if i<=c.get('completed_stage',0) else ('active' if i==min(c.get('completed_stage',0)+1,8) else '')
        rail.append(f'<div class="stage-chip {state}"><div class="num">{i:02d}</div><div class="name">{H(name)}</div></div>')
    st.markdown('<div class="stage-rail">'+''.join(rail)+'</div>',unsafe_allow_html=True)
    n=st.selectbox('Open stage',list(range(1,9)),index=min(c.get('completed_stage',0),7),format_func=lambda i:f'{i:02d} · {E.STAGES[i-1]}')
    title_line(W.STAGE_OUTCOMES[n-1])
    if n==1:
        with st.form('stage1'):
            a,b=st.columns(2)
            name=a.text_input('Supplier name',value=c.get('name',''))
            owner=b.text_input('Siemens engagement owner',value=c.get('owner',''))
            trigger=st.text_area('Business trigger',value=c.get('trigger',''))
            objective=st.text_area('Measurable business objective',value=c.get('objective',''))
            a,b=st.columns(2)
            date=a.text_input('Need-by date (YYYY-MM-DD)',value=c.get('need_date',''))
            country=b.text_input('Country',value=c.get('country',''))
            if st.form_submit_button('Save business need',type='primary'):
                save({'name':name,'owner':owner,'trigger':trigger,'objective':objective,'need_date':date,'country':country});st.rerun()
    elif n==2:
        with st.form('stage2'):
            crit=st.multiselect('Relevant capability criteria',list(NAMES),default=c.get('criteria',[]),format_func=lambda k:f'{k} · {NAMES[k]}')
            gap=st.text_area('Capability gap',value=c.get('gap',''))
            evidence=st.text_area('Baseline and evidence trail',value=c.get('evidence',''),height=130)
            verified=st.checkbox('Assessor has checked the evidence',value=c.get('evidence_verified',False))
            approved=st.checkbox('Assessor approves this diagnosis',value=c.get('diagnosis_approved',False))
            if st.form_submit_button('Save diagnosis',type='primary'):
                save_diagnosis(crit,gap,evidence,verified,approved);st.rerun()
        if c.get('data_snapshot'):
            with st.expander('Attached synthetic data snapshot'):st.json(c['data_snapshot'])
        if st.button('Pull matching mock Snowflake record (resets diagnosis)'):
            try:E.attach_synthetic_snapshot(c);st.rerun()
            except ValueError as ex:st.error(str(ex))
    elif n==3:
        items=E.recommendations(c,30)
        eligible=[x['id'] for x in items]
        with st.form('stage3'):
            chosen=st.multiselect('Evidence-matched intervention shortlist',eligible,default=[x for x in c.get('selected',[]) if x in eligible],format_func=lambda x:next((i['name'] for i in items if i['id']==x),x))
            approved=st.checkbox('Human reviewed the solution fit and evidence boundaries',value=c.get('solution_approved',False))
            if st.form_submit_button('Save solution selection',type='primary'):
                save_shortlist(chosen,approved);st.rerun()
        st.caption('For full evidence and alternative recommendations, open Intervention planner.')
    elif n==4:
        gate_ui(E.calc(c))
        st.write('Current disposition:',W.short_status(c))
        st.caption('Change assumptions and record the scenario decision in Investment case.')
        if st.button('Open the investment case',type='primary'):
            st.session_state.nav='Investment case';st.rerun()
    elif n==5:
        data=c.get('commitments',{})
        with st.form('stage5'):
            a,b=st.columns(2)
            se=a.text_input('Siemens owner',value=data.get('siemens_owner',''))
            su=b.text_input('Supplier owner',value=data.get('supplier_owner',''))
            milestone=st.text_area('Agreed scope / first milestone',value=data.get('milestone',''))
            a,b=st.columns(2)
            sa=a.checkbox('Simulated Siemens approval',value=data.get('siemens_approved',False))
            sb=b.checkbox('Simulated supplier approval',value=data.get('supplier_approved',False))
            if st.form_submit_button('Save mutual commitments',type='primary'):
                save({'commitments':{'siemens_owner':se,'supplier_owner':su,'milestone':milestone,'siemens_approved':sa,'supplier_approved':sb}});st.rerun()
    elif n==6:
        st.caption('Record implementation tasks with completion evidence. Every action must be complete before Stage 6 can be recorded.')
        tasks=pd.DataFrame(c.get('actions',[]))
        for key in ('task','owner','due','status','evidence'):
            if key not in tasks.columns:tasks[key]=''
        tasks=tasks[['task','owner','due','status','evidence']]
        edited=st.data_editor(tasks,hide_index=True,num_rows='dynamic',use_container_width=True,key=f'tasks_{c["id"]}',
            column_config={'status':st.column_config.SelectboxColumn('Status',options=['Not started','In progress','Done'])})
        if st.button('Save implementation actions',type='primary'):
            actions=[{k:str(val).strip() for k,val in row.items()} for row in edited.fillna('').to_dict('records') if str(row.get('task','')).strip()]
            save({'actions':actions});st.rerun()
    elif n==7:
        data=c.get('verification',{})
        with st.form('stage7'):
            metric=st.text_input('Verified outcome metric',value=data.get('metric',''))
            a,b,d=st.columns(3)
            baseline=a.number_input('Baseline',value=float(data.get('baseline',0)))
            target=b.number_input('Target',value=float(data.get('target',0)))
            actual=d.number_input('Actual',value=float(data.get('actual',0)))
            evidence=st.text_area('Measured evidence',value=data.get('evidence',''))
            verifier=st.text_input('Independent reviewer',value=data.get('verifier',''))
            sustained=st.checkbox('Improvement is sustained',value=data.get('sustained',False))
            if st.form_submit_button('Save verification',type='primary'):
                save({'verification':{'metric':metric,'baseline':baseline,'target':target,'actual':actual,
                    'evidence':evidence,'verifier':verifier,'sustained':sustained}});st.rerun()
    elif n==8:
        data=c.get('closure',{})
        with st.form('stage8'):
            owner=st.text_input('Handover owner',value=data.get('owner',''))
            followup=st.text_area('Monitoring cadence and follow-up trigger',value=data.get('followup',''))
            lessons=st.text_area('Lessons to retain',value=data.get('lessons',''))
            approver=st.text_input('Human closure reviewer',value=data.get('approved_by',''))
            if st.form_submit_button('Save closure',type='primary'):
                save({'closure':{'owner':owner,'followup':followup,'lessons':lessons,'approved_by':approver}});st.rerun()
    ok,reason=E.stage_check(c,n)
    st.markdown(f'<div class="note-box"><b>{"Ready to record" if ok else "Stage gate open"}:</b> {H(reason)}</div>',unsafe_allow_html=True)
    if n==c.get('completed_stage',0)+1:
        if st.button(f'Record Stage {n} completion',type='primary',disabled=not ok):
            try:E.complete_stage_local(c,n);st.success('Stage completion recorded.');st.rerun()
            except ValueError as ex:st.error(str(ex))
    elif n<=c.get('completed_stage',0):
        st.caption('This stage was already recorded in the fictional scenario. Editing material inputs can reopen later stages.')
    else:st.info(f"Complete Stage {c.get('completed_stage',0)+1} before recording Stage {n}.")


# ——— 07 / QUESTIONNAIRE —————————————————————————————————————————————
elif nav=='Supplier questionnaire':
    heading('Illustrative survey','Supplier questionnaire · 55 rated questions',
            'This public demonstration uses 55 newly written example questions. The official Siemens supplier questionnaire is not included. Survey responses do not automatically determine the 16 capability ratings.')
    questions=E.SURVEY['ratedQuestions']
    responses=c.get('survey',{})
    rated=[responses.get(f"Q{q['id']}",{}).get('rating') for q in questions]
    a,b,d=st.columns(3)
    with a:tile('Rated questions',str(sum(r is not None for r in rated))+' / 55','Unanswered questions remain unrated')
    with b:tile('Survey categories',str(len({q['section'] for q in questions})),'Different from the A/B/C capability domains')
    with d:tile('Scoring relationship','Not automatic','Survey and project criteria are distinct')
    sections=list(dict.fromkeys(q['section'] for q in questions))
    sec=st.selectbox('Questionnaire section',sections)
    sec_q=[q for q in questions if q['section']==sec]
    with st.form('survey_section'):
        answers={}
        for q in sec_q:
            key=f"Q{q['id']}";existing=responses.get(key,{})
            st.markdown(f"**Q{q['id']}** · {q['text']}")
            a,b=st.columns([1,2])
            current=existing.get('rating')
            values=['Not rated','1','2','3','4','5']
            rating=a.selectbox('Illustrative rating',values,index=values.index(str(current)) if str(current) in values else 0,key=f'question_{c["id"]}_{key}')
            evidence=b.text_input('Assessment evidence note',value=existing.get('evidence',''),key=f'question_e_{c["id"]}_{key}')
            answers[key]={'rating':int(rating) if rating!='Not rated' else None,'evidence':evidence}
            st.divider()
        if st.form_submit_button('Save questionnaire section',type='primary'):
            save({'survey':answers});st.rerun()
    st.caption('A supplier self-report should be independently checked before it supports a capability score or intervention decision.')


# ——— 08 / RESEARCH LIBRARY ——————————————————————————————————————————
elif nav=='Research library':
    heading('Research methods','Intervention library and source review',
            'The public demonstration contains method examples and intervention leads. Original case evidence must be verified in the approved research library before operational use.')
    a,b,d=st.columns(3)
    with a:tile('Candidate interventions',str(len(E.INTERVENTIONS)),'Working candidate library; not approved')
    with b:tile('Method categories',str(len(E.RESEARCH)),'Industrials · aerospace · semiconductors · automotive')
    with d:tile('Coverage framework','A / B / C','16 capability criteria')
    tabs=st.tabs(['Intervention catalog','Search benchmark research','Evidence rules'])
    with tabs[0]:
        selected_domain=st.selectbox('Filter intervention domain',['All','A','B','C'])
        filtered=[r for r in E.INTERVENTIONS if selected_domain=='All' or selected_domain in r['domain']]
        st.dataframe(pd.DataFrame([{'Intervention':r['name'],'Domains':', '.join(r['domain']),
                                   'Criteria':r['criteria'],'Evidence screen':r['evidence_status'],'Source':r['reference'],
                                   'Limitation':r.get('boundary','')} for r in filtered]),hide_index=True,use_container_width=True,height=470)
    with tabs[1]:
        query=st.text_input('Search benchmark notes',placeholder='e.g. capacity, ramp up, supplier training, resilience')
        if query:
            results=E.search_research(query,limit=10)
            if not results:st.info('No matching excerpts found. Try a broader keyword.')
            for row in results:
                st.markdown(f'<div class="card"><div class="head">{H(row["sector"])} · {H(row["title"])}</div><h3>{H(row["section"])}</h3><p>{H(row["quote"])}</p><div class="foot">Synthetic method example; not a verified company case.</div></div>',unsafe_allow_html=True)
        else:st.info('Search is local keyword retrieval of synthetic method notes—not a live internet or Copilot search.')
    with tabs[2]:
        st.markdown('''- **KEEP:** scoped evidence supports investigating the mechanism for a defined use case.
- **INVESTIGATE:** plausible mechanism but evidence, scope or applicability remains unclear.
- **REJECT:** insufficient relevance or support for recommendation.

The intervention catalog contains research leads, **not** Siemens-approved supplier improvement packages. The case-specific match is a transparent criterion rule, not a causal or statistically validated prediction.''')
        st.markdown('<div class="notice">Project research excerpts and questionnaire wording may be subject to reuse restrictions. Confirm permission before committing these materials to a public repository or external hosted application.</div>',unsafe_allow_html=True)


# ——— 09 / SNOWFLAKE & PROVENANCE ———————————————————————————————————————
elif nav=='Data & Snowflake':
    heading('Data architecture','Know what every recommendation is based on',
            'A transparent explanation of the project datasets, how the mock Snowflake views join to a supplier, and what IT must do before any production connection.')
    flow=[('01','Supplier inputs','55-question instrument, assessment evidence, approval records'),
          ('02','Snowflake views','Risk, performance, evaluation and relationship management'),
          ('03','Decision engine','16 criteria, three specialists, evidence matches, four gates'),
          ('04','User interfaces','Streamlit demonstration and future Copilot Studio tools')]
    cols=st.columns(4)
    for col,(num,title,desc) in zip(cols,flow):
        with col:st.markdown(f'<div class="data-step"><div class="index">DATA FLOW · {num}</div><h3>{H(title)}</h3><p>{H(desc)}</p></div>',unsafe_allow_html=True)
    title_line('Data register')
    dataset_rows=[
        ['Supplier scenarios',f'{len(E.CASES)} fictional cases','Synthetic','Business need, gaps, stage history and economic assumptions'],
        ['Capability rubric',f'{len(E.CRITERIA)} criteria','Project methodology','A:5, B:7, C:4; not identical to questionnaire sections'],
        ['Demo assessment scores','16 scores × 4 cases, some missing','Synthetic','Side-by-side comparison; reference line 3.1, never auto-approval'],
        ['Supplier questionnaire',f"{len(E.SURVEY['ratedQuestions'])} rated questions",'Synthetic instrument','Newly written questions; responses fictional; mapping illustrative'],
        ['Intervention catalog',f'{len(E.INTERVENTIONS)} records','Working candidate catalog','Potential mechanisms; original evidence requires separate verification'],
        ['Benchmark research',f'{len(E.RESEARCH)} sector documents','Synthetic method notes','Illustrative text for demo search; not evidence'],
        ['Snowflake view snapshot',f"{len(E.MOCK['sources'])} views × {len(E.MOCK['suppliers'])} suppliers",'Synthetic / mock','A demonstration of the four-source join; no database connection'],
    ]
    st.dataframe(pd.DataFrame(dataset_rows,columns=['Dataset','Scale','Data status','Role in decision']),hide_index=True,use_container_width=True)
    title_line('Four Snowflake subject areas')
    descriptions={
        'SUPPLIER_RISK_MANAGEMENT':'Dependencies, continuity flags and potential disruptions. Helps prioritize resilience and investigate exposure.',
        'SUPPLIER_PERFORMANCE_MANAGEMENT':'OTD, yield, current vs required capacity and lead time. Helps establish performance baselines.',
        'SUPPLIER_EVALUATION':'Supplier assessment status, gap codes and reviewer notes. Helps validate diagnosis and identify missing evidence.',
        'SUPPLIER_RELATIONSHIP_MANAGEMENT':'Supplier owner, forecasting status, willingness and commercial context. Helps evaluate feasibility and incentives.'
    }
    cols=st.columns(2)
    for idx,name in enumerate(E.MOCK['sources']):
        with cols[idx%2]:card(f'PROPOSED READ-ONLY VIEW {idx+1:02d}',name.replace('SUPPLIER_','').replace('_',' ').title(),descriptions.get(name,''),'Joined on an approved supplier ID in a real implementation')
    title_line('Current supplier · synthetic Snowflake preview')
    record=W.snapshot_metrics(c)
    if record:
        tabs=st.tabs(['Risk','Performance','Evaluation','Relationship'])
        for tab,(k,label) in zip(tabs,[('risk','Risk'),('performance','Performance'),('evaluation','Evaluation'),('relationship_mgmt','Relationship')]):
            with tab:
                data=record.get(k,{})
                for key,val in data.items():
                    st.markdown(f"**{key.replace('_',' ').capitalize()}**: {val if val is not None else 'Not supplied'}")
        st.caption('These entries are hard-coded mock data from snowflake_mock.json, not fetched from a Siemens account.')
    else:st.info('No corresponding mock record for this imported case.')
    title_line('What a real connection requires')
    st.markdown('''1. Siemens approves four supplier-scoped **read-only Snowflake views**, with confirmed schema and data ownership.
2. IT configures identity, network access, role-based permissions, row-level supplier restrictions and audit logging.
3. The API service retrieves permitted records by supplier ID. Missing fields remain explicitly missing.
4. Evidence is presented for supplier-development review; changes to diagnosis or economics invalidate previous scenario approvals.
5. Copilot Studio invokes the approved tools. It does not receive unrestricted database access or decide supplier awards.''')
    st.markdown('<div class="notice">Live status: <b>not connected to Siemens Snowflake.</b> Mock records are synthetic. The included SQL view contract and adapter are proposals for Siemens IT review, not approved schemas.</div>',unsafe_allow_html=True)


# ——— 10 / COPILOT STUDIO —————————————————————————————————————————————
elif nav=='Microsoft Copilot':
    heading('Microsoft Copilot Studio','Copilot integration requirements',
            'Streamlit is the evaluation screen. For Siemens users, the intended interface is a Copilot Studio coordinator and three domain specialists calling the shared Python API.')
    title_line('Architecture and status')
    cols=st.columns(4)
    steps=[('01','Employee asks Copilot','Describe the supplier need and select an approved supplier ID.'),
           ('02','Coordinator scopes','Calls the A, B and C specialists only where the evidence warrants.'),
           ('03','API evaluates','Validated tool inputs invoke the same deterministic decision engine.'),
           ('04','Human decides','The agent returns sources, gates, blockers and next actions for approval.')]
    for col,(num,title,desc) in zip(cols,steps):
        with col:st.markdown(f'<div class="data-step"><div class="index">COPILOT FLOW · {num}</div><h3>{H(title)}</h3><p>{H(desc)}</p></div>',unsafe_allow_html=True)
    a,b=st.columns([1.1,1],gap='large')
    with a:
        title_line('Three specialist responsibilities')
        for code,label in W.DOMAIN_LABELS.items():
            card('DOMAIN '+code,label,W.DOMAIN_EXPLAINERS[code],
                 'Inputs: approved criteria, permitted supplier evidence and scoped intervention records')
    with b:
        title_line('Integration readiness')
        for label,detail in [
            ('Shared business engine','Implemented and tested locally'),
            ('Authenticated FastAPI bridge','Tested in full-source package; not deployed'),
            ('API specification and agent instructions','Included in full-source technical package'),
            ('Copilot Studio connected agent','Not connected; needs Siemens tenant'),
            ('Live Snowflake data','Not connected; needs approved views'),
            ('Enterprise identity / audit controls','Requires Siemens IT implementation')]:
            st.markdown(f'<div class="insight"><div><div class="name">{H(label)}</div><div class="desc">{H(detail)}</div></div></div>',unsafe_allow_html=True)
    with st.expander('API tool contract · example inputs and responses'):
        st.code('''POST /v1/solutions     {"case_id":"DEMO-EX-001"}
POST /v1/feasibility   {"case_id":"DEMO-EX-001"}
POST /v1/data-preview  {"case_id":"DEMO-EX-001"}
POST /v1/questions     {"case_id":"DEMO-EX-001","question":"What blocks Stage 4?"}
Header: X-API-Key: <server-managed-demo-secret>''',language='text')
        st.caption('For enterprise use, replace demo API-key authentication with Siemens-approved identity and authorization controls.')
    title_line('Ask the grounded decision assistant')
    st.caption('This embedded preview is rule-based. It is not a live Copilot or a hosted LLM. It shows grounded answers and model outputs for the selected synthetic case.')
    conversation=st.session_state.chat.setdefault(c['id'],[])
    with st.container(border=True):
        for turn in conversation[-10:]:
            with st.chat_message(turn['role']):st.markdown(turn['content'])
        q=st.chat_input('Try: Which interventions fit? What blocks Stage 4? Why would a new supplier invest?')
        if q:
            conversation.append({'role':'user','content':q})
            ans=E.bounded_copilot(c,q)
            conversation.append({'role':'assistant','content':ans['answer']})
            st.rerun()
    st.markdown('<div class="notice">This package is Copilot-connectable, but no Siemens tenant, credentials, production API, Microsoft 365 channel or Snowflake data connection has been configured.</div>',unsafe_allow_html=True)


# ——— 11 / STAKEHOLDER BRIEF + EXPORT —————————————————————————————————
elif nav=='Briefing & export':
    heading('Export','Decision brief and case records',
            'Produce a printable stakeholder brief from the current synthetic scenario. Export case and score records for future demonstration sessions.')
    a,b=st.columns([1.2,.8],gap='large')
    with a:
        title_line('Executive readout')
        card('BUSINESS PROBLEM',c['name'],c.get('trigger',''),c.get('objective',''))
        card('CAPABILITY CONSTRAINT','What the assessment indicates',c.get('gap',''),
             f"{len(profile['weaknesses'])} assessed criteria below the 3.1 reference · {len(profile['missing'])} missing")
        picks=E.recommendations(c,4)
        card('INTERVENTION DIRECTION','What to investigate',', '.join(x['name'] for x in picks) or 'No matching candidates','Research leads; subject to evidence and owner review')
        gate_ui(v)
        st.write('**Siemens scenario net value:**',MONEY(v['net']))
        st.write('**Supplier-side balance:**',MONEY(v['supplier_balance']))
        st.write('**Current decision:**',W.short_status(c))
    with b:
        title_line('Download and reset')
        brief=W.briefing_html(c,s)
        st.download_button('Download stakeholder brief (HTML)',brief,file_name=f'{c["id"]}_decision_brief.html',mime='text/html',type='primary',use_container_width=True)
        st.caption('Open the HTML in your browser and use Print → Save as PDF if needed.')
        st.download_button('Export current supplier case (JSON)',json.dumps(c,indent=2,ensure_ascii=False),file_name=f'{c["id"]}_case.json',mime='application/json',use_container_width=True)
        st.download_button('Export assessment ratings (JSON)',json.dumps({'case_id':c['id'],'scores':s,'data_status':'synthetic'},indent=2),file_name=f'{c["id"]}_ratings.json',mime='application/json',use_container_width=True)
        st.markdown('<div class="note-box">This workbench stores edits in your current Streamlit session only. Export the records you want to retain before closing the tab.</div>',unsafe_allow_html=True)
        uploaded=st.file_uploader('Import a previously exported case JSON',type=['json'])
        if uploaded and st.button('Import as unverified scenario'):
            try:
                raw=json.load(uploaded)
                validated=E.clean_imported_case(raw)
                st.session_state.cases[validated['id']]=validated
                st.session_state.scores.setdefault(validated['id'],{r['code']:None for r in E.CRITERIA})
                st.session_state.active_case=validated['id']
                st.success('Imported. Evidence and approvals require review.');st.rerun()
            except (ValueError,TypeError,KeyError,json.JSONDecodeError) as ex:st.error('Invalid case JSON: '+str(ex))
        if c['id'] in W.SCORES['assessments']:
            if st.button('Reset this supplier to original demo scenario',use_container_width=True):reset_case()

st.markdown('<div style="height:34px"></div><div style="border-top:1px solid #E5E1ED;padding:13px 3px;font-size:.72rem;color:#8B8294">SUPPLIER CAPABILITY HUB · SYNTHETIC DEMONSTRATION &nbsp;·&nbsp; Synthetic evaluation records &nbsp;·&nbsp; Siemens production integration pending approval</div>',unsafe_allow_html=True)
