import network
import mnist_loader

training_data, validation_data, test_data = mnist_loader.load_data_wrapper()
net_size = [31266, 120, 1]
net = network.Network(net_size)

training_data[0][0].shape

eta = 0.25
epochs = 300
mini_batch_size = 10

print "eta: " + str(eta) + " epochs " + str(epochs) + " mini batch size: " + str(mini_batch_size) + " layers: " + str(net_size)
net.SGD(training_data, epochs, mini_batch_size, eta, test_data=test_data)

#validation
print "Validation: " + str(net.evaluate(validation_data)) + "/" + str(len(validation_data))
print "eta: " + str(eta) + " epochs " + str(epochs) + " mini batch size: " + str(mini_batch_size)+ " layers: " + str(net_size)