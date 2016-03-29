# 6.1 Introduction
> the different situations to which the network is applied all share the same general structure — all patients can be described by the same set of attributes, only the attributes’ values differ across patients. We call this type of model **_variable-based_**, since the focus of the representation is a set of random variables.

- Dynamic Bayesian Network

# 6.2 Temporal Models
隨時間改變的一組變數 $\{X^{(t)}_i\}$ 代表了在時間$t$的狀態，現在$X_i$就變成了一個template variable。

## 6.2.1 Basic Assumptions
### 將時間軸離散化
各時間點之間的間隔
$$\Delta$$
for example,
$$\Delta=1sec$$
所以原來的distribution可以分解成
$$P(X^{(0:T)})=P(X^{(0)})\prod_{t=0}^{T-1}P(X^{(t+1)}|X^{(0:t)})$$

### Markov Assumption
$\forall t\geq0$,
$$(X^{(t+1)}\perp X^{(0:t-1)}|X^{(t)})$$
此假設讓我們可以把distribution寫成串狀,
$$\cdots\rightarrow X^{(t-1)}\rightarrow X^{(t)}\rightarrow X^{(t+1)}\rightarrow \cdots$$
而在此假設下，原本的distribution可改寫成
$$P(X^{(0:T)})=P(X^{(0)})\prod_{t=0}^{T-1}P(X^{(t+1)}|X^{(t)})$$
現實中很少會出現完全符合Markov assumption的分佈，我們必須考慮所觀察的分佈是否夠接近此假設。

### Stationary System
$\forall t\geq0$,
$$P(X^{(t+1)}=\xi'|X^{(t)}=\xi)=P(X'=\xi'|X=\xi)$$
這代表不論在任何時間點上，擁有相同狀況($\xi'$ 和 $\xi$)的機率是一樣的。
我們稱$P(X'|X)$ 分佈為transition model。

## 6.2.2 Dynamic Bayesian Network
現在我們知道temporal model可用很多個transition model構成，我們開始談論transition model的細節。
 - 2-times-slice Bayesian network(2-TBN): $P(X'|X_I)$, that is, conditional Bayesian network over $X'$ given interface variables $X_I$, and $X', X_I \subset X$。

 ![2-TBN](./img/2TBN.png)
 - interface variable $X_I$: variables whose values at time $t$ have direct effect to time $t+1$; parents of $X'$

2-TBN寫成conditional distribution，
 $$P(X'|X_I)=\prod_{i=1}^nP(X'_i|Pa_{X'_i})$$
舉例來說，上圖的分佈寫成，
$$P(W',\cdots,F',O'|W,\cdots,F)$$
$$=P(W'|W)P(V'|W,V)P(L'|V,L)P(F'|W,F)P(O'|L',F')$$
對於每個node $X'_i$來說$P(X'_i|Pa_{X'_i})$ 是它的template factor。

再來是討論整個network
- inter-time-slice edge: 不同時間點的連結
- intra-time-slice edge: 相同時間點內的連結

被inter-time-slice連結的兩個node $X\rightarrow X'$，我們稱作persistence variables  

> **Definition** A dynamic Bayesian network (DBN) is a pair $<B_0,B_{\rightarrow}>$, where $B_0$ is a Bayesian network over $X^{(0)}$, representing the initial distribution over states, and $B_{\rightarrow}$ is a 2-TBN for the process. For any desired time span $T \geq 0$, the distribution over $X^{(0:T)}$ is defined as a unrolled Bayesian network, where, for any $i=1,\ldots,n$:
> - the structure and CPDs of $X_i^{(0)}$ are the same as those for $X_i$ in $B_0$
> - the structure and CPDs of $X_i^{(t)}$ for $t>0$ are the same as those $X'_i$ in $B_{\rightarrow}$
