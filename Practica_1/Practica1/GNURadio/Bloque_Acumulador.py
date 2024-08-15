"""
Embedded Python Blocks:

LAB_2 --> Practica_1 --> Bloque Acumulador
"""

import numpy as np
from gnuradio import gr
class blk (gr. sync_block ):
	def __init__ ( self ) : # only default arguments here
		gr. sync_block . __init__ (
		self ,
		name =’e_Acum ’, # will show up in GRC
		in_sig =[ np. float32 ],
		out_sig =[ np. float32 ]
	)
	def work (self , input_items , output_items ):
		x = input_items [0] # Senial de entrada .
		y0 = output_items [0] # Senial acumulada
		y0 [:] = np. cumsum (x)
		return len (y)
