1. $\lim\limits_{ x \to 0 }(1+x)^{1/x}=e$ (второй замечательный предел)
2. $\lim\limits_{ x \to +\infty }\left( 1+\frac{1}{x} \right)^{x}=\lim\limits_{ x \to -\infty }\left( 1+\frac{1}{x} \right)^{x}=e$
# Док-во
## Пункт 1

$$
\left( 1+\frac{1}{x} \right)^{1/x}\stackrel{\text{def}}{=}\underbrace{ \exp }_{ \text{непр} }\underbrace{\left(  \frac{1}{x}\ln(1+x)  \right)}_{ \to 1\text{ при } x\to 0 }
$$
$$
\lim\limits_{ x \to 0 } \exp\left( \frac{1}{x}\ln(1+x) \right)=\exp\left( \lim\limits_{ x \to 0 } \frac{\ln(1+x)}{x} \right)=\exp(1)=e
$$
## Пункт 2

$$
\left( 1+\frac{1}{x} \right)^{x}\stackrel{\left[ y=\frac{1}{x} \right]}{=}(1+y)^{1/y} \stackrel{y\to 0+}{\to}e
$$
>[!note] Почему можно заменять переменные при подсчёте пределов? Из определения по Гейне.
$$
\begin{gathered}
x\to +\infty\implies y\to 0+\\
x\to -\infty\implies y\to 0-
\end{gathered}
$$
