# Information spreading on a network

This project investigates the Networkx package for the purposes of simulating information spreding on a complex network. The code loads network, calculates its basic characteristics, then runs SIR model on top of the network and visualises the outputs. 

## Susceptible-Infected-Recovered (SIR) model

The SIR model is implementated from ndlib package. It assumes that suspective node becomes infected with probability beta if connected to an infected node. It then can become recovered with probability gamma. For more information follow [documentation](https://ndlib.readthedocs.io/en/latest/reference/models/epidemics/SIR.html).

For the SIR dynamics simulation we use the [ego-Facebook dataset](http://snap.stanford.edu/data/ego-Facebook.html) (a short version).
For the visualisation of the information spreading on network, a small Watts-Strogatz graph is used.

## Repository structure

The main file is main.ipynb; it gives an overview of the project. 
To run script locally, first call `pip3 install -r requirements.txt` to download required dependencies, then run jupyter notebook (Visit [Jupyter website](https://jupyter.org/try) for more information). 


