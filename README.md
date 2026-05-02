https://github.com/dancegolga/fixed-spectral-projection-riemann./blob/main/docs/%D1%84%D0%B8%D0%BD%D0%B0%D0%BB.pdf

https://doi.org/10.5281/zenodo.19970767

# Fixed spectral projection of the Riemann frequency γ₁ as a low-dimensional model of prime deviation macrodynamics

**Author:** Olga Sheveleva  
**Contact:** [dancegolga@gmail.com]  
**Field:** Mathematical Physics / Computational Genomics  
**Keywords:** Riemann Zeta Function, Prime-counting function, Spectral Analysis, Genomic Signal Processing

---

## 1. Overview
This repository contains the numerical analysis suite and visualization tools used to evaluate the stability of a low-dimensional logarithmic oscillatory approximation of the prime-counting deviation function $\Delta(x) = \pi(x) - Li(x)$.

The study introduces a fixed spectral probe $\gamma_1$ (the first non-trivial Riemann zero frequency) and tests its alignment with:
1. Out-of-sample prime deviation dynamics up to $10^{20}$.
2. Spectral profiles of human genomic sequences (notably locus 13q14.11).

## 2. Repository Structure
*   `main.py`: The primary Python script for statistical simulation and figure generation.
*   `README.md`: Project documentation and metadata.
*   `figures/`: Directory where generated high-resolution (600 DPI) plots are saved.

## 3. Mathematical Model
The model $\Phi(x)$ implemented in this code follows:
$$\Phi(x) = \frac{\sqrt{x}}{\ln x} \cos(\gamma_1 \ln \ln x + \theta)$$
Where $u = \ln \ln x$ provides phase linearization in log-log space.

## 4. Installation & Requirements
To reproduce the analysis, ensure you have Python 3.8+ installed. The following libraries are required:
* `numpy` (Numerical computing)
* `matplotlib` (Publication-grade visualization)
* `scipy` (Statistical distributions)

Install dependencies via pip:
```bash

pip install numpy matplotlib scipy
5. UsageExecute the following command in your terminal to generate the results:Bashpython main.py
6. Statistical ValidationSignificance is assessed against constrained surrogate ensembles.Fig 1: Displays the separation of the phase stability metric $S(x)$ between the model and null-hypothesis surrogates.Fig 2: Illustrates the spectral deviation in genomic locus 13q14.11 relative to the FDR (False Discovery Rate) threshold.7. License & CitationThis code is provided under the MIT License.If you use this model or code in your research, please cite:Sheveleva, O. (2026). Fixed spectral projection of the Riemann frequency γ₁ as a low-dimensional model of prime deviation macrodynamics.Note: This study adheres to a strict preregistration protocol. All parameters were fixed prior to out-of-sample evaluation.

## Acknowledgments. The author would like to thank Gemini AI (Google) for support in Python scripting and technical documentation formatting. 
