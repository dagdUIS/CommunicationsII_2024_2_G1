import numpy as np
from gnuradio import gr


class blk(gr.sync_block):  
    """vector averager. N is the lengh of the vector"""

    def __init__(self, N=1024):
        gr.sync_block.__init__(
            self,
            name='e_vec_averager_ff',   
            in_sig=[(np.float32,N)],
            out_sig=[(np.float32,N)]
        )
        self.N = N
        self.rows_counter=0
        self.sum=0

    def work(self, input_items, output_items):
        x=input_items[0]
        y=output_items[0]
        self.sum += np.sum(x, axis=0)
        self.rows_counter += len(x)
        y[:]=self.sum/self.rows_counter
        return len(output_items[0])
