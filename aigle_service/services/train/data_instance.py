import pandas as pd
from .tools import load_data


def singleton(class_):
    instances = {}

    def getInstance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]
    return getInstance


@singleton
class DataInstance():
    data = None
    y = None
    y_label = None
    data_test = None
    y_labeltest = None

    data_true = None

    data_false = None

    data_true_sample = None

    data_false_sample = None

    data_train = None

    y_train = None

    has_done_preprocess = False

    def __init__(self):
        self.data, self.y, self.y_label, self.data_test, self.y_labeltest = self.load_data()

    def load_data(self):
        return load_data()

    """ Getter and Setter """

    def get_data(self):
        return self.data

    def get_y(self):
        return self.y

    def get_y_label(self):
        return self.y_label

    def get_data_test(self):
        return self.data_test

    def get_y_labeltest(self):
        return self.y_labeltest

    def get_data_true(self):
        return self.data_true

    def get_data_false(self):
        return self.data_false

    def get_data_true_sample(self):
        return self.data_true_sample

    def get_data_false_sample(self):
        return self.data_false_sample

    def get_data_train(self):
        return self.data_train

    def get_y_train(self):
        return self.y_train

    def set_data(self, data):
        self.data = data

    def set_y(self, y):
        self.y = y

    def set_y_label(self, y_label):
        self.y_label = y_label

    def set_data_test(self, data_test):
        self.data_test = data_test

    def set_y_labeltest(self, y_labeltest):
        self.y_labeltest = y_labeltest

    def set_data_true(self, data_true):
        self.data_true = data_true

    def set_data_false(self, data_false):
        self.data_false = data_false

    def set_data_true_sample(self, data_true_sample):
        self.data_true_sample = data_true_sample

    def set_data_false_sample(self, data_false_sample):
        self.data_false_sample = data_false_sample

    def set_data_train(self, data_train):
        self.data_train = data_train

    def set_y_train(self, y_train):
        self.y_train = y_train

    def set_has_done_preprocess(self, has_done_preprocess):
        self.has_done_preprocess = has_done_preprocess
