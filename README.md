# Accelerated Affine-Invariant Convergence Rates of the Frank-Wolfe Algorithm with Open-Loop Step-Sizes
## References

Code for the paper:

[Wirth, E., Pena, J., and Pokutta, S. (2023b). Accelerated affine-invariant convergence rates of the Frank-Wolfe
algorithm with open-loop step-sizes. arXiv preprint arXiv:2310.04096.](https://arxiv.org/abs/2310.04096)

This project is an extension of the previously published Git repository
[open_loop_fw](https://github.com/ZIB-IOL/open_loop_fw), which contains the code to the following paper:

Wirth, E., Pokutta, S., and Kerdreux, T. (2023). Acceleration of Frank-Wolfe Algorithms with Open-Loop Step-Sizes. 
In Proceedings of AISTATS.


## Installation guide

Download the repository and store it in your preferred location, say ~/tmp.

Open your terminal and navigate to ~/tmp.

Run the command:
```shell script
$ conda env create --file environment.yml
```

This will create the conda environment affine_invariant_open_loop_fw.

Activate the conda environment with:
```shell script
$ conda activate affine_invariant_open_loop_fw
```
Navigate to ~/tmp

To perform the experiments in the paper:

```python3 script
>>> python3 -m experiments.ablation_study_l
```
```python3 script
>>> python3 -m experiments.collaborative_filtering
```
```python3 script
>>> python3 -m experiments.gaps_growth
```
```python3 script
>>> python3 -m experiments.logistic_regression
```
```python3 script
>>> python3 -m experiments.polytope_ls_ol
```
```python3 script
>>> python3 -m experiments.polytope
```
```python3 script
>>> python3 -m experiments.regression
```
```python3 script
>>> python3 -m experiments.strong_growth
```
```python3 script
>>> python3 -m experiments.weak_boundary_growth
```

The experiments are then stored in ~/tmp/experiments/figures.


Some referees were interested in seeing the effects of higher dimensions on the experiments. No surprises occurred. 
For completeness, the additional experiments can be run in the same way as the experiments for the main paper:
```python3 script
>>> python3 -m experiments.referee_ablation_study_l
```
```python3 script
>>> python3 -m experiments.referee_polytope_ls_ol
```