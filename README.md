# Image Classification using Convolutional Neural Networks

CNNs use a variation of multilayer perceptrons designed to require minimal preprocessing. They are also known as shift invariant or space invariant artificial neural networks (SIANN), based on their shared-weights architecture and translation invariance characteristics.

Convolutional networks were inspired by biological processes in which the connectivity pattern between neurons is inspired by the organization of the animal visual cortex. Individual cortical neurons respond to stimuli only in a restricted region of the visual field known as the receptive field. The receptive fields of different neurons partially overlap such that they cover the entire visual field.

CNNs use relatively little pre-processing compared to other image classification algorithms. This means that the network learns the filters that in traditional algorithms were hand-engineered. This independence from prior knowledge and human effort in feature design is a major advantage.

This project contains a feedforward CNN implemented using Keras, trained for classifying handwritten digits using MNIST dataset. The architecture yields an impressive accuracy of 99.9% after 25 epochs which stands better than the human vision and most conventional industry-standard classification models.

### References

http://cs231n.github.io/convolutional-networks/
https://en.wikipedia.org/wiki/Convolutional_neural_network
http://ufldl.stanford.edu/tutorial/supervised/ConvolutionalNeuralNetwork/
