$$
a= \underline{\lim}x_{n} \Leftrightarrow \begin{cases}
\forall \varepsilon>0\ \exists N\ \forall n \geq N: x_{n} >a-\varepsilon\\
\forall \varepsilon>0\ \forall N\ \exists n\geq N: x_{n}<a+\varepsilon
\end{cases}
$$

$$
b= \overline{\lim}x_{n} \Leftrightarrow \begin{cases}
\forall \varepsilon>0\ \exists N\ \forall n \geq N: x_{n} <b+\varepsilon\ (1)\\
\forall \varepsilon>0\ \forall N\ \exists n\geq N: x_{n}>b-\varepsilon\ (2)
\end{cases}
$$

# Д-во

$b = \lim\limits_{ n \to +\infty} z_{n}$
$z_{n} = \sup\{ x_{n}, x_{n+1},\dots \}$

## 1. $\impliedby$

(1): $\forall \varepsilon>0 \exists N\ \forall n\geq N: z_{n}\leq b+\varepsilon$
(2): в любом хвосте есть эл-т больше $b-\varepsilon \implies \forall n: z_{n}>b-\varepsilon$

НСНМ $b-\varepsilon < z_{n} \leq b+\varepsilon \implies \lim\limits_{ n \to +\infty} z_{n} = b$

## 2. $\implies$

$\forall \varepsilon>0\ \exists N\ \forall n\geq N: b-\varepsilon<z_{n}\leq b+\varepsilon$

