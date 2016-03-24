# Soundness and Completeness

> In brief:
> - Soundness means that you cannot prove anything that's wrong.
> - Completeness means that you can prove anything that's right.

d-separation無法保證BN中的active trial，在P分佈下不是independent:
 - $X\rightarrow Y$ over BN $G$, but $X\perp Y$ on distribution $P$


> Completeness
>  - If (X ⊥ Y | Z) in all distributions P that factorize over G, then d-sepG(X;Y | Z). And the contrapositive: If X and Y are not d-separated given Z in G, then X and Y are dependent in some distribution P that factorizes over G.

 解釋：
  - 在所有可以被G表示的分佈{P}裡, 如果X和Y都是獨立的, 則X和Y是d-sep。
  - 反過來說, 如果X和Y不是d-sep, 則存在一些被G表示的分佈中, X和Y是相關的。

  整體來說, d-separation沒辦法完全推論distribution的相依狀況

>   **Theorem 3.5** For almost all distributions P that factorize over G, that is, for all distributions except for a set of measure zero in the space of CPD parameterizations, we have that I(P\) = I(G)

Measure Zero (?)
