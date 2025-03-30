Число $e$ — иррац.

## Док-во

Пусть $e= \frac{m}{n},\ m,n\in \mathbb{N},\ n\geq2\ (\text{тк } 2<e<3)$

$$
\underbrace{ e^{x} }_{ \text{пусть }x=1 }=\sum\limits_{k=0}^{n} \frac{x^{k}}{k!}+\frac{e^{c}}{(n+1)!}x^{n+1}\text{ (c между x=1 и }x_{0}=0)
$$
$$
\begin{gathered}
\frac{m}{n}=e=1+\frac{1}{1!}+\frac{1}{2!}+\dots+\frac{1}{n!}+\frac{e^{c}}{(n+1)!}\quad|\cdot n!\text{ (0<c<1)}\\
\underbrace{ m\cdot(n-1)! }_{ \in \mathbb{N} }=\underbrace{ n!+n!+ \frac{n!}{2!}+ \frac{n!}{3!}+\dots+ \frac{n!}{n!} }_{  \in \mathbb{N} }+ \frac{e^{c}}{n+1}\implies\\
\implies \frac{e^{c}}{n+1} \in \mathbb{N}\implies \frac{e^{c}}{n+1}\geq 1
\end{gathered}
$$
$$
1\leq\frac{e^{c}}{n+1}< \frac{e}{n+1}< \frac{3}{\underbrace{ n+1 }_{  \geq 3 }}
$$
(получ. пр-чие)