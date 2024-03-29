# SAN-FAPL
This repository contains the source code for our paper: "Feedback-efficient Active Preference Learning for Socially Aware Robot Navigation", accepted to IROS-2022.
For more details, please refer to [our project website](https://sites.google.com/view/san-fapl).


## Abstract
Socially aware robot navigation, where a robot is required to optimize its trajectory to maintain comfortable and compliant spatial interactions with humans in addition to reaching its goal without collisions, is a fundamental yet challenging task in the context of human-robot interaction. While existing learning-based methods have achieved better performance than the preceding model-based ones, they still have drawbacks: reinforcement learning depends on the handcrafted reward that is unlikely to effectively quantify broad social compliance, and can lead to reward exploitation problems; meanwhile, inverse reinforcement learning suffers from the need for expensive human demonstrations. In this paper, we propose a feedback-efficient active preference learning approach, FAPL, that distills human comfort and expectation into a reward model to guide the robot agent to explore latent aspects of social compliance. We further introduce hybrid experience learning to improve the efficiency of human feedback and samples, and evaluate benefits of robot behaviors learned from FAPL through extensive simulation experiments and a user study (N=10) employing a physical robot to navigate with human subjects in real-world scenarios.


## Overview Architecture for FAPL
<div align=center>
<img src="/figures/architecture.png" width="800" />
</div>  



## Set Up
1. Install the required python package
```
pip install -r requirements.txt
```

2. Install [Human-in-Loop RL](https://github.com/rll-research/BPref) environment

3. Install [Python-RVO2](https://github.com/sybrenstuvel/Python-RVO2) library

4. Install Environment and Navigation into pip
```
pip install -e .
```


## Run the code
0. Develop expert demonstrations in hybrid experience learning.
```
python demonstration_api.py --vis
```

1. Train a policy with preference learning. 
```
python train_FAPL.py 
```

2. Test a policy.
```
python test_FAPL.py
```

3. Plot training curves.
```
python plot.py
```

(The code was tested in Ubuntu 18.04 with Python 3.6.)

## Simulation Environment

The simulation environment is a 22 m × 20 m two-dimensional space, and the yellow circle indicates the robot. The blue dotted line illustrates the robot FoV, humans that can be detected by the robot are green circles while those out of robot view are red circles. The red star is the robot goal, and the orientation and number of each agent are presented as a red arrow and a black number respectively.

<div align=center>
<img src="/figures/environment.jpg" width="300" />
</div>  

## Learning Curve

<div align=center>
<img src="/figures/curve_sr.png" width="450" /> <img src="/figures/curve_df.png" width="450" />
</div>  

## Citation
If you find the code or the paper useful for your research, please cite our paper:
```
@article{wang2022feedback,
  title={Feedback-efficient Active Preference Learning for Socially Aware Robot Navigation},
  author={Wang, Ruiqi and Wang, Weizheng and Min, Byung-Cheol},
  journal={arXiv preprint arXiv:2201.00469},
  year={2022}
}
```

## Acknowledgement

Contributors:  
[Weizheng Wang](https://github.com/WzWang-Robot/FAPL); [Ruiqi Wang](https://github.com/R7-Robot?tab=repositories).

Part of the code is based on the following repositories:  

[CrowdNav](https://github.com/vita-epfl/CrowdNav); [DSRNN_CrowdNav](https://github.com/Shuijing725/CrowdNav_DSRNN); and [B_Pref](https://github.com/rll-research/B_Pref).





