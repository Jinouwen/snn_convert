import numpy as np
import configparser
import os


class Partitioner(object):
    def __init__(self, config_filename):
        self.config = configparser.ConfigParser()
        self.config_filename = os.path.join(os.path.dirname(os.path.abspath(__file__)), config_filename)
        self.config.read(self.config_filename)
        print('find config file' + self.config_filename)
        print(list(self.config.items()))
        self.core_size = self.config.getint('machine', 'core_size')

    def run(self):
        data_num = self.config.getint('data', 'file_num')
        connections = {}
        data_dirname = os.path.join(os.path.dirname(self.config_filename), self.config.get('data', 'dir_path'))
        for i in range(data_num):
            data_filename = os.path.join(data_dirname, '{:0>4d}data_ij.npz'.format(i))
            print("processing " + data_filename)
            a = np.load(data_filename)['arr_0']
            a = a // self.core_size
            for (u, v) in a:
                if (u, v) in connections:
                    connections[(u, v)] += 1
                else:
                    connections[(u, v)] = int(1)
        print('saving')
        output_dirname = os.path.join(os.path.dirname(self.config_filename), self.config.get('output', 'dir_path'))
        file_ij = os.path.join(output_dirname, 'dataij.bin')
        file_w = os.path.join(output_dirname, 'dataw.bin')
        output_data_ij = np.array(list(connections.keys()), dtype=np.intc)
        output_data_w = np.array(list(connections.values()), dtype=np.intc)
        print(output_data_ij.shape)
        output_data_ij.tofile(file_ij)
        output_data_w.tofile(file_w)


if __name__ == '__main__':
    p = Partitioner('partition_config.ini')
    p.run()
