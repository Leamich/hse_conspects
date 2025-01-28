$x^{n}-1$
* в $\mathbb{C}: x^{n}-1=\prod\limits_{a_{i}\in \mu_{n}}(x-a_{i})$
* в $\mathbb{R}: (x^{n}-1)=(x-1)(x+1)\prod\limits_{k=0}^{n-1}\left( x^{2}-2\cos \frac{2\pi k}{n} + 1 \right)$
* в $\mathbb{Q}: x^{n}-1=\prod\limits_{d|n}\Phi_{d}(x)$, $\Phi_{d}(x)=\prod\limits_{\varepsilon \in \mu_{n},\ ord(\varepsilon)=d}(x-\varepsilon)$ — круговой многочлен (с целыми коэффициентами).

1. $\Phi_{d}\in \mathbb{Z}[x]$
2. $\Phi_{d}$ — неразл. в $\mathbb{Q}[x]$
# Док-во
(2) не оч. просто
## (1)

(ММИ по $d$)

$\Phi_{n}=\frac{x^{n}-1}{\underbrace{ \prod\limits_{d|n,\ d<n}\Phi_{d} }_{ \in \mathbb{Z}[x]\text{ (по И.п.)} }}\in \mathbb{Z}[x]$
