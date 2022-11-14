# Required Environment:
The environment below was used for this code:

- Python Version: 3.9.6 (pygame does not install on 3.11 yet)
- Python libraries: pip install -r requirements.txt
- Other libraries:
  - graphviz:
  ```
  sudo apt-get install graphviz libgraphviz-dev
  ```
  - pygame:
  ```
  sudo apt-get install git python3-dev python3-setuptools python3-numpy python3-opengl \
    libsdl-image1.2-dev libsdl-mixer1.2-dev libsdl-ttf2.0-dev libsmpeg-dev \
    libsdl1.2-dev libportmidi-dev libswscale-dev libavformat-dev libavcodec-dev \
    libtiff5-dev libx11-6 libx11-dev fluid-soundfont-gm timgm6mb-soundfont \
    xfonts-base xfonts-100dpi xfonts-75dpi xfonts-cyrillic fontconfig fonts-freefont-ttf libfreetype6-dev
  ```

# Folders
## Reference
Code snippets in Jupyter

## 01_Simple_GP
- `GP_HowTo.ipynb`: How to use the DEAP library for Simple GP
- `Simple_GP.py`: Full GP for simple problems:
  - Symbolic Regression
  - Fibonacci (using Symbolic Regression)
  - Binary Parity

## 02_PoleBalancing -- Simple GP for OpenAI Gym
- `PoleBalance_GP.py`: Evolve Simple GP for CartPole-v1
- `PoleBalance_GPView.py`: View one solution
- `MountainCar_GP.py`: Evolve Simple GP controller for MountainCar-v1
- `MountainCar_GPView.py`: View one solution

## 03_Neat -- neat-python examples
For now this directory is the same as the example folder of neat-python repository. Use the following in class:

- `single-pole-balancing`: Single pole balancing, self-simulator version.
- `single-pole-balancing-openai`: SPB, using the OpenAI simulator
- `picture2d`: Simple version of picture evolution using CPPNs

## 04_SoftRobots -- TODO

## DEAP Examples
Examples from DEAP repository -- Will remove later
