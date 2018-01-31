# Gradient Based Representational Similarity Analysis
# Created by Muhammad Yousefnezhad
# iBRAIN, College of Computer Science and Technology
# Nanjing University of Aeronautics and Astronautics
# Example
# rsa = DeepRSA()
# beta, eps, weight, bias, loss = rsa.fit(data, design)
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

class DeepRSA:
    def __init__(self, layers=[10,10], n_iter = 1000, learning_rate=0.001, loss_norm = 'euclidean', activation = 'relu', batch_size = 50, report_step=300, verbose=True, CPU=False):
        self.loss_norm      = loss_norm  # 'euclidean', 2, np.inf
        self.activation     = str.lower(activation) # 'relu', 'sigmoid', 'tanh'
        self.learning_rate  = learning_rate
        self.n_iter         = n_iter
        self.batch_size     = batch_size
        self.report_step    = report_step
        self.Layers         = layers
        self.verbose        = verbose
        self.Beta           = None
        self.Eps            = None
        self.Weights        = None
        self.Biases         = None
        self.loss_vec       = None
        self.CPU            = CPU


    def fit(self, data_vals, design_vals, sess=None):
        import tensorflow as tf
        import numpy as np
        import os
        from Network.MLP import MLP
        # RSA Parameters
        F = tf.placeholder("float", [None, np.shape(data_vals)[1]])
        D = tf.placeholder(shape=[None, np.shape(design_vals)[1]], dtype=tf.float32)
        Beta = tf.Variable(tf.random_normal(shape=[np.shape(design_vals)[1], self.Layers[-1]]))
        Eps  = tf.Variable(tf.random_normal(shape=[1, self.Layers[-1]]))
        # Kernel Optimization
        MappedF = tf.placeholder("float", [None, self.Layers[-1]])
        mlp = MLP()
        kernelmapping = mlp.multilayer_perceptron(F, LayerShape=self.Layers, Activation=self.activation)
        kernel_loss = tf.reduce_mean(tf.square(kernelmapping - tf.matmul(D, Beta)))
        kernel_train = tf.train.AdamOptimizer(learning_rate=self.learning_rate).minimize(kernel_loss)
        # RSA optimization
        rsa_loss = tf.square(tf.norm(MappedF - tf.add(tf.matmul(D, Beta), Eps), ord=self.loss_norm))
        rsa_train = tf.train.GradientDescentOptimizer(learning_rate=self.learning_rate).minimize(rsa_loss)
        # Performance Estimation mean((F - D * Beta)**2) / n
        perf  = tf.divide(tf.reduce_mean(tf.square(MappedF - tf.matmul(D, Beta))), tf.constant(np.shape(data_vals)[0],dtype=tf.float32))
        if self.CPU:
            os.environ['CUDA_VISIBLE_DEVICES'] = '-1'
            print("Switch to CPU env ...")

        if sess is None:
            sess = tf.Session()
        sess.run(tf.global_variables_initializer())
        if self.verbose:
            print("Before Mapping, MSE:   {:20.10f}".format(sess.run(perf, {D: design_vals, MappedF: sess.run(kernelmapping, {F:data_vals})})))
        # Training loop
        self.loss_vec = list()
        for i in range(self.n_iter):
            rand_index = np.random.choice(len(design_vals), size=self.batch_size)
            rand_design = design_vals[rand_index]
            rand_data = sess.run(kernelmapping, {F:data_vals[rand_index]})
            sess.run(rsa_train, {D: rand_design, MappedF: rand_data})
            temp_loss = sess.run(rsa_loss, feed_dict={D: rand_design, MappedF: rand_data})
            self.loss_vec.append(temp_loss)
            if self.verbose:
                if (i == 0) or ((i+1)%self.report_step == 0) or (i == self.n_iter - 1):
                    print('It: {:9d} of {:9d} \t Loss: {:20.10f}'.format(i + 1, self.n_iter, temp_loss))
            sess.run([kernel_train, kernel_loss, kernelmapping], {D: rand_design, F: data_vals[rand_index]})
        Fhat = sess.run(kernelmapping, {F:data_vals})
        MSE = sess.run(perf, {D: design_vals, MappedF: Fhat})
        if self.verbose:
            print("After Mapping, MSE:    {:20.10f}".format(MSE))
        # Final Results
        self.Beta                   = sess.run(Beta)
        self.Eps                    = sess.run(Eps)
        self.Weights, self.Biases   = mlp.return_values(sess)
        sess.close()
        return self.Beta, self.Eps, self.Weights, self.Biases, self.loss_vec, MSE