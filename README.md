# Cayley Digraph Diameters

Code accompanying the paper "Measures of information spread in digraphs" 
by Gregory C Magda, Jonathan Rubin, Sabrina Streipert,
Cameron Watt, Abhiram Kumar (University of Pittsburgh).

## Usage
Run `compute_table1.py` to reproduce Table 1 from the paper.

## Requirements
Install dependencies with:
pip install -r requirements.txt

## Algorithm
The algorithm used to compute the diameters uses lemma 2 which states if two initially active sets $X$ and $Y$ of a Cayley graph are in the same orbit, then $d(X,t) = d(Y,t)$ for a fixed threshold $t$. Therefore, we do not need to compute the diameter of all possible starting positions. We only need to compute the diameter for a single representative element from each orbit. For example, suppose we want to compute the $d_{st}$ diameters when $s = 2$. Instead of computing the diameter of all ${7 \choose 2} = 21$ starting sets, we can identify the three distinct orbits given by
    $\hspace{0.5cm}\textrm{orbit 1:} \{(1, a), (a, a^2), (a^2, a^3), (a^3, a^4), (a^4, a^5), (a^5, a^6), (a^6, a)\}$
    $\hspace{0.5cm}\textrm{orbit 2:} \{(1, a^2), (a, a^3), (a^2, a^4), (a^3, a^5), (a^4, a^6), (a^5, 1), (a^6, a)\}$
    $\hspace{0.5cm}\textrm{orbit 3:} \{(1, a^3), (a, a^4), (a^2, a^5), (a^3, a^6), (a^4, 1), (a^5, a), (a^6, a^2)\}$\
and compute the diameter for a single element from each orbit say $(1,a)$, $(1,a^2)$, and $(1,a^3)$. In order to compute the orbit representatives, we iterate over all possible starting positions of a given cardinality $s$. For a given subset $S$, if $S$ is in an existing orbit, we continue to the next possible starting subset. If $S$ is not in an existing orbit, then we construct the orbit by repeatedly multiplying $S$ by a generator of our group, namely $a$. i.e. The orbit of $S$ is given by $Orb(S) = \{S, aS, a^2S,...,a^6S\}$. We remark that code uses the additive notation for $C_7$ with elements $\{0,1,...,6\}$ as opposed to the multiplicative notation which uses $\{1,a,...,a^6\}$.
