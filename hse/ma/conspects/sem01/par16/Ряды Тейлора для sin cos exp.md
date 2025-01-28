# $\sin x / \cos x$

$\forall x \in \mathbb{R},\ \forall n:|\sin ^{(n)}(x)|=|\sin \left( x+\frac{\pi}{2}n \right)|\leq 1\stackrel{\text{Сл}}{\implies}\lim\limits_{ n \to +\infty }(T_{n,0}f(x))=\sin x\ \forall x$

$$
\lim\limits_{ n \to +\infty} \underbrace{ \left( \sum\limits_{k=0}^{n} \frac{(-1)^{k}x^{2k+1}}{(2k+1)!} \right) }_{ \text{част. сумма ряда} } =\sin x\implies \sin x=\sum\limits _{n=0}^{+\infty} \frac{(-1)^{n}x^{2n+1}}{(2n+1)!}\ \forall x \in \mathbb{R}
$$
$$
\cos x=\sum\limits_{n=0}^{+\infty} \frac{(-1)^{n}x^{2n}}{(2n)!}
$$
# exp

$f(x)=e^{x}$

Рассмотрим $x\leq b: |e^{x}|\leq e^{b}=k\stackrel{\text{Сл}}{\implies}T_{n,x_{0}}f(x)\stackrel{n \to +\infty}{\to}e^{x}$

$\lim\limits_{ n \to +\infty } \sum\limits_{k=0}^{n} \frac{x^{k}}{k!}=e^{x}\ \forall x \leq b\implies \sum\limits_{n=0}^{+\infty} \frac{x^{n}}{n!}=e^{x}\ \forall x \in \mathbb{R}$

