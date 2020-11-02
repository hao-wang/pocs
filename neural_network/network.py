import numpy as np
import random


def logistic_sigmoid(z):
    return 1/(np.exp(-z)+1)


class Network:
    def __init__(self, sizes):
        self.n_layers = len(sizes)
        self.sizes = sizes
        self.weights = [np.random.randn(m, n) for (m, n) in zip(sizes[1:], sizes[:-1])]
        self.biases = [np.random.randn(m, 1) for m in sizes[1:]]

    def feed_forward(self, x):
        for weight, bias in zip(self.weights, self.biases):
            x = logistic_sigmoid(np.dot(weight, x) + bias)

        return x

    def SGD(self, training_data, epochs, mini_batch_size, eta, test_data=None):
        if test_data:
            n_test = len(test_data)

        n = len(training_data)
        for epoch in range(epochs):
            data = random.shuffle(training_data)
            batches = [data[i: i+mini_batch_size] for i in range(0, n, mini_batch_size)]

            for batch in batches:
                self.update_by_batch(batch, eta)

            if test_data:
                print("Epoch {0}: {1}/{2}".format(epoch, self.evaluate(test_data).sum(), n_test))
            else:
                print("Epoch {} complete.".format(epoch))

    def update_by_batch(self, batch, eta):
        nabla_b = [np.zeros(b.shape) for b in self.biases]
        nabla_w = [np.zeros(w.shape) for w in self.weights]
        for x, y in batch:
            d_nabla_b, d_nabla_w = self.backprop(x, y)
            nabla_b = [nb+dnb for (nb, dnb) in zip(nabla_b, d_nabla_b)]
            nabla_w = [nw+dnw for (nw, dnw) in zip(nabla_w, d_nabla_w)]

        self.weights = [w - (eta/len(batch))*nw for (w, nw) in zip(self.weights, nabla_w)]
        self.biases = [b - (eta/len(batch))*nb for (b, nb) in zip(self.biases, nabla_b)]

    def backprop(self, x, y):
        return [1]*(self.n_layers-1), [1]*(self.n_layers-1)

    def evaluate(self, test_data):
        test_result = [np.argmax(self.feed_forward(x), y) for (x, y) in test_data]
        return np.array([(x == y) for (x, y) in test_result])
