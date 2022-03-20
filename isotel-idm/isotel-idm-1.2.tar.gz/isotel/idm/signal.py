"""ISOTEL IDM Base Representation of Signals and their Generators

Structure:
 - values is an array of measurement values
 - signal is a dict sorted by channel each having a pair of lists: y and x values
 - stream is a tuple of individual measurements from multiple multi-channel signals
 - channel refers to a measurement input by name

"""
from math import *
import re
import time

try:
    if get_ipython:
        from ipywidgets import interact, IntSlider, ToggleButton
        from bokeh.io import push_notebook, show, output_notebook
        from bokeh.plotting import figure
        from bokeh.models import Range1d
except:
    pass

try:
    # Needed by signal2spectrum
    from scipy.fftpack import fft
except:
    pass

try:
    # Needed by SNR
    import scipy.optimize
    import numpy as np
except:
    pass

try:
    import pyqtgraph as pg
except:
    pass

def search_edge(values, threshold, hysteresis=0, edge='rising', start_idx=0):
    state = None
    oldstate = None
    thr_low = threshold - hysteresis
    thr_high= threshold + hysteresis

    for i,v in enumerate(values):
        if v < thr_low:
            state = 0
        elif v > thr_high:
            state = 1

        if oldstate != None and state != None and i >= start_idx:
            if edge == 'rising' or edge == 'any':
                if oldstate < state:
                    return i
            if edge == 'falling' or edge == 'any':
                if oldstate > state:
                    return i

        oldstate = state

    return None

def tofloat(values, index):
    if index:
        return float(values[index])
    return float('nan')

def get_stream_bychannel(header, name):
    for i,s in enumerate(header):
        for j,ch in enumerate(s[1]):
            if ch.startswith(name):
                return lambda s: s[i][1][j]

def replace_channels2streams(header, expr):
    expr_out = expr
    for token in re.findall(r"[A-Z]+\d*", expr): # Assumes channel names to be uppercase followed by optional numbers
        for i,s in enumerate(header):
            for j,ch in enumerate(s[1]):
                if ch.startswith(token):
                    expr_out = expr_out.replace(token, 's['+str(i)+"][1]["+str(j)+"]")
    return expr_out

def trigger(stream, cond, precond=None, P=50, N=50, single_shot=False, post_delay=0):
    try:
        hdr = next(stream)
        yield hdr

        precond_triggered = False
        triggered = False
        prebuf = [[]]*P
        prebuf_wi = 0
        prebuf_size = 0
        N_preset = N
        trigger_ts = 0

        exec('global trigger_cond; trigger_cond = lambda s:' + replace_channels2streams(hdr, cond))
        if precond:
            exec('global pretrigger_cond; pretrigger_cond = lambda s:' + replace_channels2streams(hdr, precond))
        else:
            precond_triggered = True

        for s in stream:
            if not triggered and prebuf_size >= P:
                ts = time.time()
                if ts > trigger_ts:
                    if precond and not precond_triggered:
                        if pretrigger_cond(s) > 0:
                            precond_triggered = True

                    if precond_triggered > 0 and trigger_cond(s) > 0:
                        triggered = True
                        trigger_ts = ts + post_delay
                        if P >= 0:
                            for __ in range(P):
                                if prebuf[prebuf_wi] != []:
                                    yield prebuf[prebuf_wi]
                                prebuf_wi = (prebuf_wi+1) % P

            if triggered:
                N -= 1
                if N >= 0:
                    yield s
                elif not single_shot:
                    precond_triggered = False
                    triggered = False
                    N = N_preset
                else:
                    return

            # Prebuffer keeps filling for subsequent shots
            if P > 0:
                prebuf[prebuf_wi] = s
                prebuf_wi = (prebuf_wi+1) % P
                prebuf_size += 1
    finally:
        stream.close()

def addmath(stream, name, expr, remove_NaN=True):
    try:
        hdr = next(stream)
        yield hdr + ( ('t [s]', (name,)), )

        exec('global math_expr; math_expr = lambda s:' + replace_channels2streams(hdr, expr))
        for s in stream:
            t = None
            for st in s:
                if st[0] != None:
                    t = st[0]
                    break
            if t:
                try:
                    result = math_expr(s)
                    if (remove_NaN == True and result == result) or remove_NaN == False:
                        yield s + ( (t, (result,)), )
                except:
                    pass
    finally:
        stream.close()

def merge(*streams):
    try:
        for s in zip(*streams):
            merged = ()
            for t in s:
                for c in t:
                    merged += (c,)
            yield merged
    finally:
        for s in streams:
            s.close()

def mergeNsync(*streams):
    try:
        ss = [s for s in streams]

        # Merge Header
        v = [next(s) for s in ss]
        merged = ()
        for t in v:
            for c in t:
                merged += (c,)
        yield merged

        # Sync and Merge Readings
        v = [next(s) for s in ss]
        loop = True
        while loop:
            t_min = v[0][0][0]
            for t in v:
                t_min = t[0][0] if t[0][0] < t_min else t_min

            merged = ()
            for i,t in enumerate(v):
                used = False
                for c in t:
                    if c[0] != None and c[0] <= t_min:
                        merged += (c,)
                        used = True
                    else:
                        merged += ((None, (None,)),)
                if used:
                    try:
                        v[i] = next(ss[i])
                    except:
                        loop = False
            yield merged
    finally:
        for s in streams:
            s.close()

def replay(stream):
    for s in stream:
        yield s

def to_tsv(stream):
    def convert(num):
        if num != None and num == num:
            return str(num)
        return ''

    def make_tsv_line(tup):
        line = ''
        for s in tup:
            line += convert(s[0]) + '\t'
            for y in s[1]:
                line += convert(y) + '\t'
        return line

    try:
        for s in stream:
            yield make_tsv_line(s)
    finally:
        stream.close()

def stream2signal(stream, split=None, relative_time=False, incremental=False):
    try:
        header = next(stream)
        i = 0
        out = None
        for src in stream:
            i += 1
            if i == 1:
                out = {}
                x_ref = 0
                for s in header:
                    for a in s[1]:
                        if a != None:
                            out[str(a)] = dict({'y': [], 'x': []})

            # Collect values, for each stream in src
            for s,h in zip(src, header):
                for a,v in zip(h[1],s[1]):
                    if s[0] != None:
                        out[str(a)]['y'] += [ v ]
                        if relative_time and i == 1:
                            x_ref = s[0]

                        out[str(a)]['x'] += [ s[0] - x_ref ]

            if i == split:
                yield out
                out = None
                i = 0
            elif incremental:
                yield out

        # Flush remaining
        if out != None:
            yield out
    finally:
        stream.close()

def rms(y, ac=False):
    if ac:
        return rms(np.array(y) - np.mean(y))
    return np.sqrt( np.mean(np.array(y)**2) )

def snr_dB(signal, noise):
    return 20*log10(rms(signal) / rms(noise))

def sinad_dB(signal):
    """
    Calculates SINAD by fitting a single ideal tone sine to the signal
    to be subtracted from the actual signal.

    :param signal: a signal dict providing x and y arrays
    :returns: SNR in dB and frequency
    """
    def sine_fitter(x, y):
        def sinfun(t, A, w, p, c):
            return A * np.sin(w*t + p) + c

        ff = np.fft.fftfreq(len(x), (x[1]-x[0]))
        Fyy = abs(np.fft.fft(y))
        guess_freq = abs(ff[np.argmax(Fyy[1:])+1])
        guess_amp = np.std(y) * 2.**0.5
        guess_offset = np.mean(y)
        guess = np.array([guess_amp, 2.*np.pi*guess_freq, 0., guess_offset])
        popt, pcov = scipy.optimize.curve_fit(sinfun, x, y, p0=guess)
        A, w, p, c = popt
        return sinfun(x, A, w, p, c), w/(2.*np.pi), abs(A)

    x = np.array(signal['x'])
    y = np.array(signal['y'])
    y_ideal, f, A = sine_fitter(x, y)
    return snr_dB(y, y - y_ideal), f, A

def enob(sinad):
    return (sinad - 1.76) / 6.02

def blackmanharris(N, sym, a):
    k = np.linspace(0,len(a)-1,len(a))
    w = np.zeros(N)
    M = N-1 if sym else N
    for i in range(N):
        w[i] = np.sum( a * np.cos(2*np.pi*k*i/M) )
    return w

def blackmanharris3(N, sym=True):
    BLACKMANHARRIS_3TH = [0.42,  -0.5, 0.08]
    return blackmanharris(N, sym, BLACKMANHARRIS_3TH)

def blackmanharris4(N, sym=True):
    # https://liquidsdr.org/doc/windowing/
    BLACKMANHARRIS_4TH = [0.35875, -0.48829, 0.14128, -0.01168]
    return blackmanharris(N, sym, BLACKMANHARRIS_4TH)

def blackmanharris7(N, sym=True):
    # https://dsp.stackexchange.com/questions/51095/seven-term-blackman-harris-window
    BLACKMANHARRIS_7TH = [0.27105140069342, -0.43329793923448, 0.21812299954311,
        -0.06592544638803, 0.01081174209837, -0.00077658482522, 0.00001388721735]
    return blackmanharris(N, sym, BLACKMANHARRIS_7TH)

def tospectrum(signal, log_ref=1, log_unit='dB', start_fi=0, window=blackmanharris3):
    try:
        Nw = None
        for shot in signal:
            fft_shot = {}
            for s in shot:
                N = len(shot[s]['y'])
                if Nw != N:
                    w = window(N, False) if window else 1
                    w = w/rms(w)
                    Nw = N
                Y = [20*log10(2*abs(i+1e-99)/log_ref/N) for i in fft(w*shot[s]['y'])]
                dT = (shot[s]['x'][-1] - shot[s]['x'][0]) / (N-1)
                X = [i / ((N-2)*dT) for i in range(N//2)]
                fft_shot[s.replace('[', '['+log_unit)] = { 'y': Y[start_fi:N//2], 'x' : X[start_fi:] }

            yield fft_shot

    except KeyboardInterrupt:
        pass
    finally:
        signal.close()

    return fft_shot


DISPLAY_MODE_AVG = 'avg'
DISPLAY_MODE_PEAK = 'peak'
SCOPE_CH_COLORS = ['darkorange', 'darkmagenta', 'darkcyan', 'darkred', 'darkgreen', 'red', 'blue', 'brown']

def scope(signal, width=700, height=400, title="Unnamed",
          colors = SCOPE_CH_COLORS, y_range = None,
          x_label = 't [s]', skip=0, post_func=None, display_mode=None, avg_k=0.5):
    
    assert(avg_k<=1)
    try:
        get_ipython
        output_notebook()
    except:
        print('Runs inside jupyter with bokeh plots only')
        return

    def plot_lines(plot, shot):
        lines  = []
        for i, l in enumerate(shot):
            lines += [ plot.line(x = shot[l]['x'], y = shot[l]['y'], color = colors[i], legend = l) if colors[i] else None ]

        return lines

    def plot_setup():
        plot = figure(title=title, x_axis_label=x_label,
                #y_axis_label=   Common unit on Y axis can cause many issues, it's been added to the legent
                plot_width=width, plot_height=height, background_fill_color='white', border_fill_color='white',
                tools="pan,crosshair,box_zoom,reset,save,wheel_zoom,hover")

        plot.xgrid.grid_line_color = 'lightgray'
        plot.ygrid.grid_line_color = 'lightgray'
        if y_range:
            plot.y_range = Range1d(y_range[0], y_range[1])

        return plot

    plot = plot_setup()
    shot = last_valid_shot = None
    plot_handle = None

    try:
        i = 0
        valid = True
        for shot in signal:
            if plot_handle == None:
                lines = plot_lines(plot, shot)
                last_valid_shot = shot
                plot_handle = show(plot, notebook_handle=True)
            else:
                i += 1
                if i > skip:
                    for i, l in enumerate(shot):
                        if lines[i]:
                            # Only update screen with the same number of samples
                            if len(lines[i].data_source.data['y']) == len(shot[l]['y']):
                                valid = True
                                if display_mode == 'avg':
                                    avg = [a*(1-avg_k)+b*avg_k for a,b in zip(lines[i].data_source.data['y'],shot[l]['y'])]
                                    lines[i].data_source.data['y'] = avg
                                    shot[l]['y'] = avg
                                elif display_mode == 'peak':
                                    peak = [max(a,b) for a,b in zip(lines[i].data_source.data['y'],shot[l]['y'])]
                                    lines[i].data_source.data['y'] = peak
                                    shot[l]['y'] = peak
                                else:
                                    lines[i].data_source.data = shot[l]
                            else:
                                valid = False

                    push_notebook(handle=plot_handle)
                    i = 0

            if valid:
                last_valid_shot = shot
                if post_func:
                    post_func(shot)

    except KeyboardInterrupt:
        pass
    finally:
        signal.close()

    return last_valid_shot


def qscope(signal, width=700, height=400, title="Unnamed",
          colors = SCOPE_CH_COLORS,
          y_range = None, x_label = 't [s]', skip=0, post_func=None, display_mode=None, avg_k=0.5, chain=False):

    assert(avg_k<=1)

    def plot_lines(plot, shot):
        lines  = []
        for i, l in enumerate(shot):
            lines += [ plot.line(x = shot[l]['x'], y = shot[l]['y'], color = colors[i], legend = l) if colors[i] else None ]

        return lines

    def plot_setup():
        qp = pg.plot(title=title)
        qp.setLabel('bottom', text = x_label.split('[')[0], units = x_label.split('[')[1].split(']')[0])
        qp.showGrid(True,True,0.7)
        qp.showButtons()
        qp.addLegend(offset=(-5,5))
        return qp
    
    qp = plot_setup()
    shot = last_shot = None
    pen = [pg.mkPen(pg.QtGui.QColor(color)) for color in colors]

    try:
        i = 0
        valid = True
        legend = True
        for shot in signal:
            i += 1
            if i > skip:
                for i, l in enumerate(shot):
                    if last_shot:
                        # Only update screen with the same number of samples
                        if len(last_shot[l]['y']) == len(shot[l]['y']):
                            valid = True
                            if display_mode == 'avg':
                                avg = [a*(1-avg_k)+b*avg_k for a,b in zip(last_shot[l]['y'],shot[l]['y'])]
                                shot[l]['y'] = avg
                            elif display_mode == 'peak':
                                peak = [max(a,b) for a,b in zip(last_shot[l]['y'],shot[l]['y'])]
                                shot[l]['y'] = peak
                        else:
                            valid = False

                    if valid:
                        qp.plot(shot[l]['x'], shot[l]['y'], pen = pen[i], name = l if legend else None, clear=i==0 )

                i = 0
                legend = False

            if valid:
                last_shot = shot
                if post_func:
                    post_func(shot)

            pg.QtGui.QApplication.processEvents()

            if chain:
                yield shot

    except KeyboardInterrupt:
        pass
    finally:
        signal.close()

    if not chain:
        yield last_shot
