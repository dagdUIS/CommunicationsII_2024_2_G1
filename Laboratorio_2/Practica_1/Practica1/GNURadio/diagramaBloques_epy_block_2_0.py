"""
Embedded Python Blocks:

Bloque Diferenciador
"""

import numpy as np
from gnuradio import gr
class blk (gr. sync_block ):
	def __init__ ( self ) : # only default arguments here
		gr. sync_block . __init__ (
			self ,
			name ="e_Diff", # will show up in GRC
			in_sig =[ np. float32 ],
			out_sig =[ np. float32 ]
		)
		self . acum_anterior = 0
	def work (self , input_items , output_items ):
		x = input_items [0] # Senial de entrada .
		y0 = output_items [0] # Senial acumulada diferencial
		N = len (x)
		diff = np. cumsum (x) - self . acum_anterior
		self . acum_anterior = diff [N -1]
		y0 [:] = diff
		# y0 [:] = len(y0)
		return len (y0)
