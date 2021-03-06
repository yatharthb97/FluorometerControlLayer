# -*- coding: utf-8 -*-


# GUI → Checked

from pyqtgraph.Qt import QtGui, QtCore
import pyqtgraph as pg
from collections import deque


import os

def GenerateGUI(sub_plots=4, maxlen=100):
	"""
	Generates and returns a dictionary collection of Graphing GUI resources.
	Only generates individual plots as of now.
	"""

	this_title = "Fluorimeter Reading Display"
	x_label = "X axis →"
	x_units = "time (s)"
	y_label = "Y axis →"
	y_units = "intensity"

	app = QtGui.QApplication([])
	
	
	window = pg.GraphicsLayoutWidget(show=True, title=this_title)
	window.resize(1440,720)
	window.setWindowTitle(this_title)

	# icon
	icon_path = os.path.join(".", "control_layer", "icon.png")
	icon = QtGui.QIcon(str(icon_path))
	window.setWindowIcon(icon)
	
	# Enable antialiasing for prettier plots
	pg.setConfigOptions(antialias=True, useOpenGL=True)


	# Create plots
	canvases = []
	curves = []
	data = []
	times = []

	def table_condition(pt, total_plots):

		#if total_plots == 4:
		#	return pt % 2 == 0
		#else:
		return (pt == total_plots/2)

	for pt in range(1, sub_plots+1):
		canvas = window.addPlot(title=f"Sample - {pt}")
		canvases.append(canvas)
		if table_condition(pt, sub_plots):
			window.nextRow()
		datum = deque(maxlen=maxlen)
		time = deque(maxlen=maxlen) 
		datum.append(0.0)
		time.append(0.0)

		canvas.setLabel('left', y_label, y_units)
		canvas.setLabel('bottom', x_label, x_units)
		canvas.setPos(time[0], datum[0])

		curve = canvas.plot(symbolBrush='c', symbolSize=4)
		curves.append(curve)
		data.append(datum)
		times.append(time)
 

	return {"app": app, "window": window, "canvases": canvases, "curves": curves, "data" : data, "time": times}