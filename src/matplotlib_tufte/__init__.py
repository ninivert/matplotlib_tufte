from enum import Enum
import warnings
import matplotlib.axes
import matplotlib.pyplot as plt  # needs this to access fontManager

__all__ = ['setup', 'breathe', 'data_lim']

def setup():
	import pathlib
	pathbase = pathlib.Path(__file__).parent

	try:
		# Attempt to import standard TeX font
		for fontpath in (pathbase / 'lm2.004otf').glob('*.otf'):
			matplotlib.font_manager.fontManager.addfont(str(fontpath))  # matplotlib doesn't like non-string paths
	except Exception as e:
		warnings.warn(f'could not setup fonts : {e}')

	plt.style.use(pathbase / 'tufte.mplstyle')

class AxisWhich(Enum):
	X = 'x'
	Y = 'y'
	BOTH = 'both'

def breathe(ax: matplotlib.axes.Axes, which = AxisWhich.BOTH, pad_frac_start = 0.04, pad_frac_end = 0.04):
	"""Add some space between the axes and the spines

	Parameters
	----------
	ax : matplotlib.axes.Axes
	which : str or AxisWhich, optional
		which axis to apply the spacing on, by default AxisWhich.BOTH
	pad_frac_start : float, optional
		space to add to the start of the axis, as a fraction of the data span, by default 0.04
	pad_frac_end : float, optional
		space to add to the end of the axis, as a fraction of the data span, by default 0.04
	"""
	
	if not isinstance(which, AxisWhich):
		which = AxisWhich(which)

	if which is AxisWhich.X or which is AxisWhich.BOTH:
		limx = ax.get_xlim()
		ax.spines['bottom'].set_bounds(limx[0], limx[1])
		span = limx[1] - limx[0]
		m0 = limx[0] - span*pad_frac_start
		m1 = limx[1] + span*pad_frac_end
		ax.set_xlim((m0, m1))

	if which is AxisWhich.Y or which is AxisWhich.BOTH:
		limy = ax.get_ylim()
		ax.spines['left'].set_bounds(limy[0], limy[1])
		span = limy[1] - limy[0]
		m0 = limy[0] - span*pad_frac_start
		m1 = limy[1] + span*pad_frac_end
		ax.set_ylim((m0, m1))

def data_lim(ax: matplotlib.axes.Axes, which = AxisWhich.BOTH):
	"""Sets the axis to use the limits of the data

	Parameters
	----------
	ax : matplotlib.axes.Axes
	which : str or AxisWhich, optional
		which axis to apply the spacing on, by default AxisWhich.BOTH
	"""
	if not isinstance(which, AxisWhich):
		which = AxisWhich(which)

	if which is AxisWhich.X or which is AxisWhich.BOTH:
		ax.set_xlim((ax.dataLim.xmin, ax.dataLim.xmax))

	if which is AxisWhich.Y or which is AxisWhich.BOTH:
		ax.set_ylim((ax.dataLim.ymin, ax.dataLim.ymax))

def line_guide(ax: matplotlib.axes.Axes, pad: float, plot_kwargs: dict = {}):
	# TODO
	# trace a spaced line between points
	raise NotImplementedError()