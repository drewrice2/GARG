import random
import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Conv1D, MaxPooling1D
from keras.layers import LocallyConnected1D, LocallyConnected2D
from datetime import datetime

# --------------------------------------------------
# -                                                -
# -  GAR.py                                        -
# -        contains the core functionality of GAR  -
# -                                                -
# --------------------------------------------------

# TODO: support more stuff

class Genome:

    def __init__(self, net_must_start_with=[], net_must_end_with=[], dimensionality=2,
        min_depth=2, max_depth=7): # input params
        self.net_must_start_with = net_must_start_with
        self.net_must_end_with = net_must_end_with
        self.dimensionality = dimensionality
        self.min_depth = min_depth
        self.max_depth = max_depth
        self.model = Sequential() # only supporting Sequential models initially
        self.architecture = []
        # network variable initializations
        self.node_range = [16,32,64,128,256]
        self.conv_filter_range = [16,32,64,128,256]
        self.dropout_range = [0.1,0.25,0.5]
        self.pool_or_kernel_range_2D = [(2,2),(3,3),(4,4)]
        self.pool_or_kernel_range_1D = [2,3,4,6]
        self.activation_funcs = ['relu']


        def typecheck_and_error_handle():
            # !
            if self.dimensionality != 2:
                msg = "Only supporting 2D convolutional nets at this time. Change parameter `dimensionality`."
                raise ValueError(msg)
            # initial type checking
            if type(self.dimensionality) != int:
                msg = "Parameter `dimensionality` must be of type <class 'int'>. Found %s" % (type(self.dimensionality))
                raise TypeError(msg)
            if type(self.min_depth) != int:
                msg = "Parameter `min_depth` must be of type <class 'int'>. Found %s" % (type(self.min_depth))
                raise TypeError(msg)
            if type(self.max_depth) != int:
                msg = "Parameter `max_depth` must be of type <class 'int'>. Found %s" % (type(self.max_depth))
                raise TypeError(msg)
            if type(self.net_must_start_with) != list:
                msg = "Parameter `net_must_start_with` must be of type <class 'list'>. Found %s" % (type(self.net_must_start_with))
                raise TypeError(msg)
            if type(self.net_must_end_with) != list:
                msg = "Parameter `net_must_end_with` must be of type <class 'list'>. Found %s" % (type(self.net_must_end_with))
                raise TypeError(msg)
            if self.max_depth < self.min_depth:
                msg = "Parameter `max_depth` must be greater than or equal to `min_depth`."
                raise ValueError(msg)
            if (len(self.net_must_start_with) >= self.max_depth) or (len(self.net_must_end_with) >= self.max_depth):
                msg = "Net size too bit for max_depth. Check parameters: `max_depth`, `net_must_start_with`, `net_must_end_with`."
                raise ValueError(msg)
        # run typechecking
        typecheck_and_error_handle()


    # ~ OUTLINE ~
    # based on 'layer' parameter, check for relevant variables (first requires 'input_layer')
    # for what's left off, randomization
    #       if 'key' in dict.keys(): blah
    # dictionary
    # while True:
    #   model.add

    def randomize_layers():
        '''
        # Randomize layers until self.max_depth is reached.
        '''
        while len(self.model.layers) < self.max_depth:
            pass
        pass

    def add_layer_dict_to_model():
        '''
        # Receives a one-layer dictionary. Interprets and adds to self.model.
            Writes to self.architecture list.
        '''
        pass

    def add_from_list(self, list_of_layers):
        '''
        # Input: list_of_layers to run through self.interpret_layer_dict
        '''
        for layer_dictionary in list_of_layers:
            pass

    def clear_memory():
        pass

    def interpret_layer_dict(self, layer_dictionary):
        '''
        # Interprets a single-layer dictionary.

        # Returns: dictionary of 'layer_name':'parameters'
            where the 'parameters' dict is fed directly into a Keras layer object

        # TODO: support Conv1D, LocallyConnected1D, LocallyConnected2D
        '''
        # dictionary for parameter pass
        keras_layer_parameters = {}

        # fundamental parameter checking
        if 'layer_name' in layer_dictionary.keys():
            layer_dictionary['layer_name'] = layer_dictionary['layer_name'].lower()
        else:
            msg = "Each layer requires supported a `layer_name`."
            raise ValueError(msg)
        # check for parameter 'input_shape'
        if len(self.model.layers) == 0:
            if 'input_shape' in layer_dictionary.keys():
                keras_layer_parameters['input_shape'] = layer_dictionary['input_shape']
            else:
                msg = "First model layer requires parameter `input_shape`."
                raise ValueError(msg)

        # Dense layer
        if layer_dictionary['layer_name'] == 'dense':
            if 'units' in layer_dictionary.keys():
                keras_layer_parameters['units'] = layer_dictionary['units']
            else:
                keras_layer_parameters['units'] = random.choice(self.node_range)
            if 'activation' in layer_dictionary.keys():
                keras_layer_parameters['activation'] = layer_dictionary['activation']
            else:
                keras_layer_parameters['activation'] = random.choice(self.activation_funcs)
        # Dropout
        if layer_dictionary['layer_name'] == 'dropout':
            if 'rate' in layer_dictionary.keys():
                keras_layer_parameters['rate'] = layer_dictionary['rate']
            else:
                keras_layer_parameters['rate'] = random.choice(self.dropout_range)
        # Conv2D
        if layer_dictionary['layer_name'] == 'conv2d':
            if 'filters' in layer_dictionary.keys():
                keras_layer_parameters['filters'] = layer_dictionary['filters']
            else:
                keras_layer_parameters['filters'] = random.choice(self.conv_filter_range)
            if 'kernel_size' in layer_dictionary.keys():
                keras_layer_parameters['kernel_size'] = layer_dictionary['kernel_size']
            else:
                keras_layer_parameters['kernel_size'] = random.choice(self.pool_or_kernel_range_2D)
            if 'activation' in layer_dictionary.keys():
                keras_layer_parameters['activation'] = layer_dictionary['activation']
            else:
                keras_layer_parameters['activation'] = random.choice(self.activation_funcs)
            conv_filter_range
        # MaxPooling2D
        if layer_dictionary['layer_name'] == 'maxpooling2d':
            if 'pool_size' in layer_dictionary.keys():
                keras_layer_parameters['pool_size'] = layer_dictionary['pool_size']
            else:
                keras_layer_parameters['pool_size'] = random.choice(self.kernel_or_pool_size_2d)
        # Layer invalid
        else:
            msg = 'Could not find `%s` in supported layers. \n\tError occurred at: %s' % \
                (layer_dictionary['layer_name'], datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC'))
            raise ValueError(msg)

        return {layer_dictionary['layer_name']:keras_layer_parameters}

if __name__ == '__main__':
    x = Genome('b','b',dimensionality=2, min_depth=4,max_depth=4)

# def layer_add(layer_name,
#         node_range=[16,32,64,128,256], \
#         dropout_range=[0.1,0.25,0.5], \
#         pool_or_kernel_range_2D=[(2,2),(3,3),(4,4)], \
#         pool_or_kernel_range_1D=[2,3,4,6], \
#         activation_funcs=['relu']):
#     '''
#     # Generate a layer from a given layer name.
#
#     # Supported layers:
#         Dense, Dropout, Flatten, Conv2D, MaxPooling2D, LocallyConnected2D
#
#         Future layers:
#             MaxPooling1D, Conv1D, LocallyConnected1D, BatchNormalization
#
#     # Raises:
#         ValueError, if 'layer_name' is not recognized
#
#     # Returns: layer object.
#
#     # TODO! accept 'parameters' dictionary with 'layer_name','num_nodes','activation_func'
#     '''
#     # random selections done upfront
#     layer_name = layer_name.lower()
#     node_size = random.choice(node_range)
#     activation = random.choice(activation_funcs)
#     kernel_or_pool_size_2d = random.choice(pool_or_kernel_range_2D)
#     kernel_or_pool_size_1d = random.choice(pool_or_kernel_range_1D)
#
#     if layer_name == 'dense':
#         layer = Dense(units=node_size, activation=activation)
#     elif layer_name == 'dropout':
#         layer = Dropout(random.choice(dropout_range))
#     elif layer_name == 'flatten':
#         layer = Flatten()
#     elif layer_name == 'conv1d':
#         model.add(Conv1D(filters=node_size, kernel_size=kernel_or_pool_size_1d, activation=activation))
#     elif layer_name == 'conv2d':
#         layer = Conv2D(filters=node_size, kernel_size=kernel_or_pool_size_2d, activation=activation)
#     elif layer_name == 'maxpooling1d':
#         layer = MaxPooling1D(pool_size=pool_or_kernel_range_1D)
#     elif layer_name == 'maxpooling2d':
#         layer = MaxPooling2D(pool_size=pool_or_kernel_range_2D)
#     elif layer_name == 'locallyconnected1d':
#         layer = LocallyConnected1D(filters=node_size, kernel_size=pool_or_kernel_range_1D, activation=activation)
#     elif layer_name == 'locallyconnected2d':
#         layer = LocallyConnected2D(filters=node_size, kernel_size=pool_or_kernel_range_2D, activation=activation)
#     else: # layer unrecognized and not added
#         msg = 'Could not find "%s" in supported layers. \n\tError occurred at: %s' % \
#             (layer_name, datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC'))
#         raise ValueError(msg)
#     return layer
#
# def add_from_list(model, layer_list, model_architecture_list):
#     '''
#     # Recevies a list and adds the given layers to the model.
#
#     # Returns: model architecture list.
#     '''
#     for layer_name in layer_list:
#         try:
#             layer_to_add = layer_add(layer_name)
#             model_architecture_list.append(layer_name)
#             model.add(layer_to_add)
#         except ValueError as e:
#             pass
#     return model_architecture_list
#
# def generate_genome(model, dimensionality, min_depth=2, max_depth=7, net_must_start_with=[], net_must_end_with=[]):
#     '''
#     # Generate basic genome from given dimension, parameters.
#
#     # TODO:
#         add ability to specify layer-specific parameters on opening and closing, i.e. node_size
#
#     # Raises:
#         ValueError, if 'min_depth' and 'max_depth' are incorrectly sized
#         TypeError, if 'net_must_start_with' & 'net_must_end_with' are not lists
#     '''
#     # ERROR HANDLING !
#     # check depth args
#     if min_depth >= max_depth:
#         msg = 'Minimum depth variable "%i" needs to be bigger than max_depth variable "%i".\n\tError occurred at: %s' % \
#             (min_depth, max_depth, datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC'))
#         raise ValueError(msg)
#     # check net_must_start_with & net_must_end_with data types
#     if type(net_must_start_with) != list:
#         msg = 'Argument "net_must_start_with" must be a list.\n\tError occurred at: %s' % \
#             (datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC'))
#         raise TypeError(msg)
#     if type(net_must_end_with) != list:
#         msg = 'Argument "net_must_end_with" must be a list.\n\tError occurred at: %s' % \
#             (datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC'))
#         raise TypeError(msg)
#
#     # check dimensionality, define universe of available functions
#     # TODO: infer from input dimensions
#     if dimensionality == 2:
#         available_funcs = ['conv2d','dense','dropout','maxpooling2d'] # ,'locallyconnected2d']
#     elif dimensionality == 1:
#         # available_funcs = ['dense','dropout','conv1d','maxpooling1d','locallyconnected1d']
#         # only supporting 2 dimensional data at this point
#         msg = 'Not supporting 1D...Only supporting 2 dimensional data at this point.'
#         raise ValueError(msg)
#     else:
#         msg = 'Dimensionality must be "1" or "2".\n\tError occurred at: %s' % \
#             (datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC'))
#         raise ValueError(msg)
#     # generate architecture
#     model_architecture = []
#     net_size = random.randint(min_depth, max_depth)
#     # add must_start_with
#     model_architecture = add_from_list(model, net_must_start_with, model_architecture)
#     for _ in range(net_size): # being done one layer at a time to only generate working nets
#         while True:
#             layer = np.random.choice(available_funcs, 1, p=[0.35,0.35,0.1,0.2])[0]
#             try:
#                 layer_to_add = layer_add(layer)
#                 model_architecture.append(layer)
#                 model.add(layer_to_add)
#                 break
#             except ValueError as e:
#                 pass
#     # add must_end_with
#     model_architecture = add_from_list(model, net_must_end_with, model_architecture)
#     return model_architecture
