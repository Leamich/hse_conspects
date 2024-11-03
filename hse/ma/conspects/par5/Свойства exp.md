1. $\exp(1) = e, \exp(0)=1$
2. $a\leq b \implies \exp(a)\leq \exp(b)$
> [!info]- Док-во
> $$
> \begin{gathered}
> 1+\frac{a}{n}\leq 1+\frac{b}{n} \text{ (НСНМ обе части >0)}\\
> \left( 1+\frac{a}{n} \right)^{n}\leq \left( 1+\frac{b}{n} \right)^{n}\\
> \exp(a)\leq \exp(b)\text{ (пред. переход в нер-ве)}
> \end{gathered}
> $$
3. $\exp(a)>0\ \forall a\in \mathbb{R}$
> [!info]- Док-во
> НСНМ $\left( 1+\frac{a}{n} \right)^{n}>0$
4. $\exp(a)\exp(-a)\leq 1$
> [!info]- Док-во
> $$
> \left( 1+\frac{a}{n} \right)^{n}\left( 1+\frac{-a}{n} \right)^{n}=\left( 1-\frac{a^{2}}{n^{2}} \right)^{n}\leq1
> $$
> $$
> \exp(a)\exp(-a)\leq 1
> $$
5. $\exp(a)\geq 1+a\quad \forall a\in \mathbb{R}$
> [!info]- Док-во
> $$
> \begin{gathered}
> \left( 1+\frac{a}{n} \right)^{n} \stackrel{Н.Б.}{\geq} 1+n\cdot \frac{a}{n}=1+a;\quad n>-a\\
> \downarrow n\to +\infty\\
> \exp(a)\geq 1+a
> \end{gathered}
> $$
6. $\exp(a)\leq \frac{1}{1-a}$ для $a < 1$
> [!info]- Док-во
> $\exp(a)\exp(-a)\leq 1 \Leftrightarrow \exp(a) \leq \frac{1}{\exp(-a)} \stackrel{\text{св-во 5}}\leq \frac{1}{1-a}$
7. $\forall n \in \mathbb{N}: \left( 1+\frac{1}{n} \right)^{n}<e<\left( 1+\frac{1}{n} \right)^{n+1}$
> [!info]- Док-во
> $$
> \begin{cases}
> z_{n}\text{ стр. убыв.}\\
> \lim\limits_{ n \to +\infty} z_n=e 
> \end{cases}
> $$
> fix $n$:
> $$
> \begin{array}{c}
> e\leq\left( 1+\frac{1}{n+1} \right)^{n+2} < \left( 1+\frac{1}{n} \right)^{n+1}\\
> e< \left( 1+\frac{1}{n} \right)^{n+1}
> \end{array}
> $$
 