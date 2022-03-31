import numpy as np


class TwoLayerPerceptron:
    def __init__(self, input_size, hidden_size, output_size, activation, error_function):
        self.hidden_weights = np.random.uniform(size=(input_size, hidden_size))
        self.hidden_bias = np.random.uniform(size=(1, hidden_size))

        self.output_weights = np.random.uniform(size=(hidden_size, output_size))
        self.output_bias = np.random.uniform(size=(1, output_size))

        self.activation = activation
        self.error_function = error_function

    def forward_pass(self, input):
        hidden_layer_out = np.dot(input, self.hidden_weights) + self.hidden_bias
        hidden_layer_out = self.activation(hidden_layer_out)

        output_layer_out = np.dot(hidden_layer_out, self.output_weights) + self.hidden_bias
        output_layer_out = self.activation(output_layer_out)

        return output_layer_out