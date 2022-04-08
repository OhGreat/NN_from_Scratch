# Neural Network from scratch
Small library of neural networks created from scratch with python and numpy. <br/>
Created to learn in depth about gradient descent and backpropagation. <br/>
The networks are then tested by teaching them to emulate the XOR logic gate.

## Installation
Python 3 and numpy >=1.19 are required

## Usage
To run a single experiment use the file XOR_experiment.py
``` 
python XOR_experiment.py
```

To run a multiple experiments and get a plot of the results use the file experiments.py
``` 
python experiments.py
```

## Observations
It interesting to note that when running the network with only two hidden nodes (which is the minimum requirement to emulate the XOR logic gate), the network sometimes fails to learn to simulate XOR. <br/>
An example of this behaviour can be seen when running experiments with np.random.seed(0). In general, this is the result of bad weight initialization and the more neurons we add to the hidden layer, the harder it is for weight inintialization to influence the learning of the model.<br/>
An example of the explained behaviour can be seen on the image below.
![Screenshot](results/losses.png)

The labels represent the parameters of the experiments:<br/>
<ul>
  <li>hn : denotes the hidden nodels in the hidden layer of the network.</li>
  <li>lr : denotes the learning rate used during training. </li>
  <li>working: is a boolean value representing if the network learnt to simulate the XOR logic gate properly.</li>
</ul>


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Future Work
- Implement multiple layers in the network.
