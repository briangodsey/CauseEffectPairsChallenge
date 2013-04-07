import data_io
import numpy as np
import pylab as pl

def main():
    train = data_io.read_train_pairs()
    target = data_io.read_train_target()
    
    ## for row in train.iloc[0:4].iterrows():
    for ind in train.index[0:20]:
        pl.scatter( train['A'][ind],
                    train['B'][ind],
                    marker=".")
        pl.show()
        

if __name__=="__main__":
    main()
