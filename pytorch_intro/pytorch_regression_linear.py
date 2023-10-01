import torch
from torch import nn

class LinearRegressionModel(nn.Module):
    def __init__(self):
        super().__init__()
        
        # TODO: initialize learnable parameters to use in forward pass
        self.weight = None
        self.bias = None
        
    def forward(self, x : torch.Tensor) -> torch.Tensor:
        # TODO: implement forward pass (linear equation)
        
        return x

# instantiate pytorch model
model = LinearRegressionModel()

# initializing sample training data
x_train = torch.rand((30, 1), dtype=torch.float) * 10
y_train = 4.5 * x_train + 2.7

# TODO: experiment with hyperparameters on training
num_epochs = 40
learning_rate = 0.001

# TODO: initialize loss function and optimizer

for epoch in range(num_epochs):
    for iter in range(len(x_train)):
        # TODO: forward pass of the network
        
        # TODO: compute the loss
        
        # TODO: reset gradient of parameters in network
        
        # TODO: backwards pass of the network
        
        # TODO: gradient descent step with optimizer
        
        pass
    
    slope = float(model.weight[0])
    intercept = float(model.bias[0])
    
    print(f'Epoch {epoch+1}: {slope:.3f}x + {intercept:.3f}')
    