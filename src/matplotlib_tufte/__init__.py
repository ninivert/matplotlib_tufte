from enum import Enum
import warnings
import matplotlib.axes
import matplotlib.pyplot as plt  # needs this to access fontManager

__all__ = ['setup', 'breathe', 'data_lim', 'despine']

def setup():
	import pathlib
	pathbase = pathlib.Path(__file__).parent

	try:
		# Attempt to import standard TeX font
		for fontpath in (pathbase / 'newcomputermodern/otf').glob('*.otf'):
			matplotlib.font_manager.fontManager.addfont(str(fontpath))  # matplotlib doesn't like non-string paths
		for fontpath in (pathbase / 'lm2.004otf').glob('*.otf'):
			matplotlib.font_manager.fontManager.addfont(str(fontpath))  # matplotlib doesn't like non-string paths
	except Exception as e:
		warnings.warn(f'could not setup fonts : {e}')

	plt.style.use(pathbase / 'tufte.mplstyle')

class AxisWhich(Enum):
	X = 'x'
	Y = 'y'
	BOTH = 'both'

def breathe(ax: matplotlib.axes.Axes | None = None, which = AxisWhich.BOTH, pad_frac: float = 0.04):
	"""Add some space between the axes and the spines

	Parameters
	----------
	ax : matplotlib.axes.Axes or None
		axes to use, if set to ``None`` then ``plt.gca()`` is used
	which : str or AxisWhich, optional
		which axis to apply the spacing on, by default AxisWhich.BOTH
	pad_frac : float, optional
		space to add between the plot and the axis, as a fraction of the data span, by default 0.04
	"""

	if ax is None:
		ax = plt.gca()
	
	if not isinstance(which, AxisWhich):
		which = AxisWhich(which)

	if which is AxisWhich.X or which is AxisWhich.BOTH:
		limy = ax.get_ylim()
		span = limy[1] - limy[0]
		m0 = limy[0] - span*pad_frac
		ax.spines.bottom.set_position(('data', m0))

	if which is AxisWhich.Y or which is AxisWhich.BOTH:
		limx = ax.get_xlim()
		span = limx[1] - limx[0]
		m0 = limx[0] - span*pad_frac
		ax.spines.left.set_position(('data', m0))

def data_lim(ax: matplotlib.axes.Axes | None = None, which = AxisWhich.BOTH):
	"""Sets the axis to use the limits of the data

	Parameters
	----------
	ax : matplotlib.axes.Axes or None
		axes to use, if set to ``None`` then ``plt.gca()`` is used
	which : str or AxisWhich, optional
		which axis to apply the spacing on, by default AxisWhich.BOTH
	"""

	if ax is None:
		ax = plt.gca()

	if not isinstance(which, AxisWhich):
		which = AxisWhich(which)

	if which is AxisWhich.X or which is AxisWhich.BOTH:
		ax.set_xlim((ax.dataLim.xmin, ax.dataLim.xmax))

	if which is AxisWhich.Y or which is AxisWhich.BOTH:
		ax.set_ylim((ax.dataLim.ymin, ax.dataLim.ymax))

def despine(ax: matplotlib.axes.Axes | None = None, which = AxisWhich.BOTH):
	"""Remove the top and right spine
	
	Parameters
	----------
	ax : matplotlib.axes.Axes or None
		axes to use, if set to ``None`` then ``plt.gca()`` is used
	which : str or AxisWhich, optional
		which axis to despine, by default AxisWhich.BOTH
	"""

	if ax is None:
		ax = plt.gca()

	if not isinstance(which, AxisWhich):
		which = AxisWhich(which)

	if which is AxisWhich.X or which is AxisWhich.BOTH:
		ax.spines.top.set_visible(False)

	if which is AxisWhich.Y or which is AxisWhich.BOTH:
		ax.spines.right.set_visible(False)

def line_guide(ax: matplotlib.axes.Axes, pad: float, plot_kwargs: dict = {}):
	# TODO
	# trace a spaced line between points
	raise NotImplementedError()