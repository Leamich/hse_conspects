$\lim\limits_{ n \to +\infty} x_n=\lim\limits_{ n \to +\infty} z_n=a$

$\forall n \in \mathbb{N}: x_{n}\leq y_{n}\leq z_{n}\implies \exists \lim\limits_{ n \to +\infty} y_{n}=a$

**Rem**. можно ослабить НСНМ $x_{n}\leq y_{n}\leq z_{n}$
## Док-во

Докажем, что $\forall\varepsilon>0\ \exists N\ \forall n\geq N: |y_{n}-a|<\varepsilon$.

fix $\varepsilon>0$, тогда по [[Лемма о двух сходящихся последовательностях|лемме]] $\exists N\ \forall n\geq N \begin{cases}|x_{n}-a|<\varepsilon\\|z_{n}-a|<\varepsilon\end{cases}\ (*)$

из $(*) \Leftrightarrow \begin{cases}a-\varepsilon<x_{n}<a+\varepsilon\\a-\varepsilon<z_{n}<a+\varepsilon\end{cases}$

Тогда 

$$
\begin{gathered}
a-\varepsilon<x_{n}\leq y_{n}\leq z_{n}<a+\varepsilon\\
a-\varepsilon<y_{n}<a+\varepsilon
\end{gathered}
$$

Следовательно $|y_{n}-a|<\varepsilon$.

Тогда $\lim\limits_{ n \to +\infty} y_{n}=a$

**чтд**

