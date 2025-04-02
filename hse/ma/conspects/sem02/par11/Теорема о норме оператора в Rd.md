$A:\mathbb{R}^{m}\to \mathbb{R}^n$ — [[hse/ma/conspects/sem02/par11/Линейный оператор|ЛО]]

$$||A||^{2}\leq \sum\limits_{j=1}^{m}\sum\limits_{k=1}^{n}a_{jk}^{2}$$
## Следствие

$A:\mathbb{R}^{m}\to \mathbb{R}^{n}$ — ЛО $\implies A$ — [[Ограниченный оператор|огр. опер.]]
## Док-во

$x=\sum\limits_{k=1}^{m}x_ke_{k}$

$$
\begin{gathered}
||Ax||=\left| \left|  A\left( \sum\limits_{k=1}^{m}x_{k}e_{k} \right) \right|  \right|\leq \sum\limits_{k=1}^{m}||x_{k}Ae_{k}||=\sum\limits_{k=1}^{m}|x_{k}|\cdot ||Ae_{k}||\stackrel{\text{К-Б}}\leq\\
\leq \left( \sum\limits x_{k}^{2} \right)^{1/2}\cdot\left( \sum\limits_{k=1}^{m} ||Ae_{k}||^{2} \right)^{1/2}
\end{gathered}
$$

Для $||x||<1$ первый сомножитель $\leq 1$
$$
||Ax||^{2}\leq ||Ae_{k}||^{2}
$$
$$
||Ae_{k}||^{2}=\sum\limits_{j=1}^{n}a^{2}_{jk}
$$