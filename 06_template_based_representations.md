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
