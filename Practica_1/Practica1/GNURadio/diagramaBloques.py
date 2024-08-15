#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Practica_1
# GNU Radio version: 3.9.8.0

from distutils.version import StrictVersion

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print("Warning: failed to XInitThreads()")

from PyQt5 import Qt
from gnuradio import qtgui
import sip
from gnuradio import blocks
from gnuradio import gr
from gnuradio.filter import firdes
from gnuradio.fft import window
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
import diagramaBloques_epy_block_1 as epy_block_1  # embedded python block



from gnuradio import qtgui

class diagramaBloques(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Practica_1", catch_exceptions=True)
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Practica_1")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "diagramaBloques")

        try:
            if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
                self.restoreGeometry(self.settings.value("geometry").toByteArray())
            else:
                self.restoreGeometry(self.settings.value("geometry"))
        except:
            pass

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 32000

        ##################################################
        # Blocks
        ##################################################
        self.epy_block_1 = epy_block_1.blk()
        self.blocks_vector_source_x_0 = blocks.vector_source_f((1, 2, -1), True, 1, [])
        self.RMS = qtgui.number_sink(
            gr.sizeof_float,
            0,
            qtgui.NUM_GRAPH_HORIZ,
            1,
            None # parent
        )
        self.RMS.set_update_time(0.10)
        self.RMS.set_title("")

        labels = ['', '', '', '', '',
            '', '', '', '', '']
        units = ['', '', '', '', '',
            '', '', '', '', '']
        colors = [("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"),
            ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black")]
        factor = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]

        for i in range(1):
            self.RMS.set_min(i, -1)
            self.RMS.set_max(i, 1)
            self.RMS.set_color(i, colors[i][0], colors[i][1])
            if len(labels[i]) == 0:
                self.RMS.set_label(i, "Data {0}".format(i))
            else:
                self.RMS.set_label(i, labels[i])
            self.RMS.set_unit(i, units[i])
            self.RMS.set_factor(i, factor[i])

        self.RMS.enable_autoscale(False)
        self._RMS_win = sip.wrapinstance(self.RMS.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._RMS_win)
        self.Potencia_Promedio = qtgui.number_sink(
            gr.sizeof_float,
            0,
            qtgui.NUM_GRAPH_HORIZ,
            1,
            None # parent
        )
        self.Potencia_Promedio.set_update_time(0.10)
        self.Potencia_Promedio.set_title("")

        labels = ['', '', '', '', '',
            '', '', '', '', '']
        units = ['', '', '', '', '',
            '', '', '', '', '']
        colors = [("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"),
            ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black")]
        factor = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]

        for i in range(1):
            self.Potencia_Promedio.set_min(i, -1)
            self.Potencia_Promedio.set_max(i, 1)
            self.Potencia_Promedio.set_color(i, colors[i][0], colors[i][1])
            if len(labels[i]) == 0:
                self.Potencia_Promedio.set_label(i, "Data {0}".format(i))
            else:
                self.Potencia_Promedio.set_label(i, labels[i])
            self.Potencia_Promedio.set_unit(i, units[i])
            self.Potencia_Promedio.set_factor(i, factor[i])

        self.Potencia_Promedio.enable_autoscale(False)
        self._Potencia_Promedio_win = sip.wrapinstance(self.Potencia_Promedio.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._Potencia_Promedio_win)
        self.Media_Cuadratica = qtgui.number_sink(
            gr.sizeof_float,
            0,
            qtgui.NUM_GRAPH_HORIZ,
            1,
            None # parent
        )
        self.Media_Cuadratica.set_update_time(0.10)
        self.Media_Cuadratica.set_title("")

        labels = ['', '', '', '', '',
            '', '', '', '', '']
        units = ['', '', '', '', '',
            '', '', '', '', '']
        colors = [("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"),
            ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black")]
        factor = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]

        for i in range(1):
            self.Media_Cuadratica.set_min(i, -1)
            self.Media_Cuadratica.set_max(i, 1)
            self.Media_Cuadratica.set_color(i, colors[i][0], colors[i][1])
            if len(labels[i]) == 0:
                self.Media_Cuadratica.set_label(i, "Data {0}".format(i))
            else:
                self.Media_Cuadratica.set_label(i, labels[i])
            self.Media_Cuadratica.set_unit(i, units[i])
            self.Media_Cuadratica.set_factor(i, factor[i])

        self.Media_Cuadratica.enable_autoscale(False)
        self._Media_Cuadratica_win = sip.wrapinstance(self.Media_Cuadratica.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._Media_Cuadratica_win)
        self.Media = qtgui.number_sink(
            gr.sizeof_float,
            0,
            qtgui.NUM_GRAPH_HORIZ,
            1,
            None # parent
        )
        self.Media.set_update_time(0.10)
        self.Media.set_title("")

        labels = ['', '', '', '', '',
            '', '', '', '', '']
        units = ['', '', '', '', '',
            '', '', '', '', '']
        colors = [("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"),
            ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black")]
        factor = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]

        for i in range(1):
            self.Media.set_min(i, -1)
            self.Media.set_max(i, 1)
            self.Media.set_color(i, colors[i][0], colors[i][1])
            if len(labels[i]) == 0:
                self.Media.set_label(i, "Data {0}".format(i))
            else:
                self.Media.set_label(i, labels[i])
            self.Media.set_unit(i, units[i])
            self.Media.set_factor(i, factor[i])

        self.Media.enable_autoscale(False)
        self._Media_win = sip.wrapinstance(self.Media.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._Media_win)
        self.Desviacion_Estandar = qtgui.number_sink(
            gr.sizeof_float,
            0,
            qtgui.NUM_GRAPH_HORIZ,
            1,
            None # parent
        )
        self.Desviacion_Estandar.set_update_time(0.10)
        self.Desviacion_Estandar.set_title("")

        labels = ['', '', '', '', '',
            '', '', '', '', '']
        units = ['', '', '', '', '',
            '', '', '', '', '']
        colors = [("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"),
            ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black")]
        factor = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]

        for i in range(1):
            self.Desviacion_Estandar.set_min(i, -1)
            self.Desviacion_Estandar.set_max(i, 2)
            self.Desviacion_Estandar.set_color(i, colors[i][0], colors[i][1])
            if len(labels[i]) == 0:
                self.Desviacion_Estandar.set_label(i, "Data {0}".format(i))
            else:
                self.Desviacion_Estandar.set_label(i, labels[i])
            self.Desviacion_Estandar.set_unit(i, units[i])
            self.Desviacion_Estandar.set_factor(i, factor[i])

        self.Desviacion_Estandar.enable_autoscale(False)
        self._Desviacion_Estandar_win = sip.wrapinstance(self.Desviacion_Estandar.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._Desviacion_Estandar_win)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_vector_source_x_0, 0), (self.epy_block_1, 0))
        self.connect((self.epy_block_1, 4), (self.Desviacion_Estandar, 0))
        self.connect((self.epy_block_1, 0), (self.Media, 0))
        self.connect((self.epy_block_1, 1), (self.Media_Cuadratica, 0))
        self.connect((self.epy_block_1, 3), (self.Potencia_Promedio, 0))
        self.connect((self.epy_block_1, 2), (self.RMS, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "diagramaBloques")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate




def main(top_block_cls=diagramaBloques, options=None):

    if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()

    tb.start()

    tb.show()

    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()

        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    qapp.exec_()

if __name__ == '__main__':
    main()
