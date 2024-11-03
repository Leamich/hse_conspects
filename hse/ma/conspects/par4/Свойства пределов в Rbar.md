1. Предел единств.
2. все св-ва про добавить/убрать/переставить конечное число эл-тов
3. $\begin{cases}\forall n: x_{n}\leq y_{n}\\ \lim\limits_{ n \to +\infty} x_n=+\infty\end{cases}\implies \lim\limits_{ n \to +\infty} y_n=+\infty$
4. $\begin{cases}\forall n: x_{n}\geq y_{n}\\ \lim\limits_{ n \to +\infty} x_n=-\infty\end{cases}\implies \lim\limits_{ n \to +\infty} y_n=-\infty$
>[!info]- Доказательство
> $$
> \lim\limits_{ n \to +\infty} x_{n}=-\infty \Leftrightarrow \forall E\in \mathbb{R}\ \exists N\ \forall n\geq N: 
> \begin{cases}
> x_{n}<E\\
> y_{n} \leq x_{n} < E
> \end{cases} \implies$$
> $$\implies y_{n}<E \xLeftrightarrow{def} \lim\limits_{ n \to +\infty} y_n=-\infty 
> $$
5. [[Теорема об арифметических действиях с пределами в Rbar]]