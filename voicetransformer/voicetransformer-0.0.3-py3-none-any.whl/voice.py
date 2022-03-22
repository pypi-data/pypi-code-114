#!/usr/bin/env python3
# coding: utf-8

"""
This is a simple wrapper around pyWorld based on the `vt_server_module_world <https://github.com/egaudrain/VTServer/blob/master/src/vt_server_module_world.py>`_,
also offering a command line interface.

Use it as a command line tool, or as a module using the `process_world` function.

~~~~~~~~~~~~~~

voicetransformer, a simple wrapper for pyworld
Copyright (C) 2022 Etienne Gaudrain

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

import logging

LOG = logging.getLogger('voice.py')
LOG.setLevel('DEBUG')

import time, os, re, pickle, hashlib

import numpy as np
import scipy.interpolate as spi

import pyworld
import soundfile as sf

RE = dict()
RE['f0'] = re.compile(r"([*+-~]?)\s*((?:[0-9]+(?:\.[0-9]*)?|\.[0-9]+)(?:[eE][-+]?[0-9]+)?)\s*(Hz|st)?")
RE['vtl'] = re.compile(r"([*+-]?)\s*((?:[0-9]+(?:\.[0-9]*)?|\.[0-9]+)(?:[eE][-+]?[0-9]+)?)\s*(st)?")
RE['duration'] = re.compile(r"([*+-~]?)\s*((?:[0-9]+(?:\.[0-9]*)?|\.[0-9]+)(?:[eE][-+]?[0-9]+)?)\s*(s)?")

def check_arguments(mo, purpose):
    """
    Receives an :mod:`re` match object from parsing module arguments and do some basic checking.

    :param mo: The argument to parse.
    :type mo:  re.Match
    :param purpose: Purpose is `'f0'`, `'vtl'` or `'duration'`.

    :return: A tuple of the form ``(args_ok, args)``: ``args_ok`` is True or False depending on whether
             the argument is fine or not. ``args`` contains a dictionary with the parsed out argument:

                `v`
                    is the value as a float.

                `u`
                    is the unit for offsets, or None for ratios.

                `~`
                    if ``True``, then it denotes an absolute (average) value instead of an offset.

    """

    if mo is None:
        return False, "Not a valid argument."

    s, v, unit = mo.groups()

    if s=='*':
        if unit!=None:
            return False, "If a ratio is given (*), no unit should be given (got '%s')." % (unit)

        try:
            v_f = float(v)
        except ValueError:
            return False, "Could not parse value '%s'" % (v)

        return True, {'v': v_f, 'u': None, '~': False, '=': False} # r for ratio

    if s=='~':
        if purpose=='f0' and unit!='Hz':
            return False, "If an average is given, the unit has to be 'Hz' (got '%s')." % unit
        elif purpose=='duration' and unit!='s':
            return False, "If fixed duration is given, the unit has to be 's' (got '%s')." % unit

        try:
            v_f = float(v)
        except ValueError:
            return False, "Could not parse value '%s'" % (v)

        return True, {'v': v_f, 'u': unit, '~': True, '=': False} # r for ratio
    else:
        if unit==None:
            return False, "If an offset value is given ({}), a unit has to be given.".format(s+v)

        try:
            v_f = float(s+v)
        except ValueError:
            return False, "Could not parse value '%s'" % (s+v)

        return True, {'v': v_f, 'u': unit, '~': False, '=': False} # o for offset


def parse_arguments(m):
    for k in ['f0', 'vtl', 'duration']:
        if k not in m:
            m[k] = None
        else:
            if isinstance(m[k], dict):
                if 'u' in m[k] and 'v' in m[k] and '~' in m[k] and '=' in m[k]:
                    continue
                else:
                    raise ValueError("[world] '%s' was passed as dictionary but it doesn't have the right keys..." % k)
            elif m[k] is None:
                continue
            else:
                args_ok, args = check_arguments(RE[k].match(m[k]), k)
                if not args_ok:
                    raise ValueError("[world] Error while parsing argument %s (%s): %s" % (k, m[k], args))
                else:
                    m[k] = args

    return m

def world_analysis_f0(x, fs, frame_period):
    _f0, t = pyworld.dio(x, fs, frame_period=frame_period)
    f0 = pyworld.stonemask(x, _f0, t, fs)

    return t, f0

def world_analysis_arr(x, fs, frame_period=None):

    if frame_period is None:
        frame_period = pyworld.default_frame_period

    t, f0 = world_analysis_f0(x, fs, frame_period)
    sp = pyworld.cheaptrick(x, f0, t, fs)
    ap = pyworld.d4c(x, f0, t, fs)

    return f0, t, sp, ap

def world_analysis(in_filename, cachefolder=None, frame_period=None):

    dat_folder = os.path.dirname(in_filename)
    if cachefolder is not None:
        dat_folder = os.path.join(cachefolder, hashlib.blake2s(dat_folder.encode('utf-8'), digest_size=6).hexdigest())
        if not os.path.exists(dat_folder):
            os.makedirs(dat_folder)

    dat_filename = os.path.join(dat_folder, os.path.splitext(os.path.basename(in_filename))[0] + '.world')

    if frame_period is None:
        frame_period = pyworld.default_frame_period

    try:
        # The file already exists so we just load it
        t1 = time.time()
        tp1 = time.process_time()

        dat = pickle.load(open(dat_filename, "rb"))

        # No need to update because cache is set to None
        #vsct.update_job_file(dat_filename)

        # We could check some things here like the file and the World version, but it should
        # be builtin the file signature.
        #f0, sp, ap, fs, rms_x, sp_interp, ap_interp = dat['f0'], dat['sp'], dat['ap'], dat['fs'], dat['rms'], dat['sp_interp'], dat['ap_interp']
        f0, sp, ap, fs, t, rms_x = dat['f0'], dat['sp'], dat['ap'], dat['fs'], dat['t'], dat['rms']

        if 'frame_period' in dat and frame_period != dat['frame_period']:
            raise Exception("The frame period in the pickled file does not match that of the version of pyworld. We regenerate it.")

        t2 = time.time()
        tp2 = time.process_time()
        LOG.info("[world (v%s)] Loaded f0, sp and ap from '%s' in %.2f ms (%.2f ms of processing time)" % (pyworld.__version__, dat_filename, (t2-t1)*1e3, (tp2-tp1)*1e3))

        # used_files.append(dat_filename)

    except:
        t1 = time.time()
        tp1 = time.process_time()
        x, fs = sf.read(in_filename)
        if len(x.shape)>1:
            x = np.mean(x, axis=1)
        rms_x = rms(x)

        f0, t, sp, ap = world_analysis_arr(x, fs, frame_period=frame_period)
        #return f0, sp, ap
        #f0, sp, ap = pyworld.wav2world(x, fs)

        # Note: I thought of keeping the interpolant in the pickle file, but it
        # makes it way too big and the processing gain is relatively small

        pickle.dump({'f0': f0, 'sp': sp, 'ap': ap, 'fs': fs, 'rms': rms_x, 't': t, 'file': in_filename, 'world_version': pyworld.__version__, 'frame_period': frame_period}, open(dat_filename, 'wb'))
        #vsct.job_file(dat_filename, [in_filename], None)

        t2 = time.time()
        tp2 = time.process_time()
        LOG.info("[world (v%s)] Extracted f0, sp and ap from '%s' in %.2f ms (%.2f ms of processing time)" % (pyworld.__version__, in_filename, (t2-t1)*1e3, (tp2-tp1)*1e3))

    return dat_filename, fs, f0, sp, ap, t, rms_x

def process_world(in_signal, m, out_filename=None, cachefolder=None):
    """
    Processes **in_signal** according to parameters **m**, and return result or stores in **out_filename**.

    :param in_signal: Either a tuple with ``(x, fs)`` or a filename (string, or path).

    The first step is to analyse the sound file to extract its f0, spectral envelope and
    aperiodicity map. The results of this operation are cached in a pickle file.

    The parameters for this module are:

    :param f0: Either an absolute f0 value in Hertz ``{### Hz}``, a change in semitones ``{### st}`` or a ratio ``{\*###}``.

    :param vtl: Same for vocal-tract length (only semitones and ratio).

    :param duration: Either an absolute duration in seconds ``{~###s}``, an offset in seconds ``{+/-###s}``, or a ratio ``{\*###}``.

    Just to be clear, these parameters must be keys of the dictionary **m**.
    """

    try:
        os.access(in_signal)
        input_type = 'file'
    except TypeError as err:
        if len(in_signal)!=2:
            raise TypeError("`in_signal` has to be either a sequence with `(x, fs)` or a path-like object.")
        else:
            x, fs = in_signal
            input_type = 'seq'


    # Analysis
    if input_ype=='file':
        dat_filename, fs, f0, sp, ap, t, rms_x = world_analysis(in_filename, cachefolder, frame_period=None)
    else:
        t = np.arange(len(x))/fs
        rms_x = rms(x)
        f0, t, sp, ap = world_analysis_arr(x, fs, frame_period=None)

    if frame_period is None:
        frame_period = pyworld.default_frame_period

    # Modification of decomposition
    m = parse_arguments(m)

    nfft = (sp.shape[1]-1)*2
    f = np.arange( sp.shape[1] ) / nfft * fs
    t = np.arange( sp.shape[0] ) * frame_period / 1e3

    # F0
    if (m['f0'] is None) or (m['f0']['u'] is None and m['f0']['v']==1) or (m['f0']['u'] is not None and not m['f0']['~'] and not m['f0']['='] and m['f0']['v']==0):
        # No change
        new_f0 = f0
    elif m['f0']['u'] is None:
        new_f0 = f0*m['f0']['v']
    else:
        if m['f0']['u']=='Hz':
            if m['f0']['~']:
                m_f0 = np.exp(np.mean(np.log(f0[f0!=0])))
                new_f0 = f0 / m_f0 * m['f0']['v']
            elif m['f0']['=']:
                new_f0 = m['f0']['v']
                if len(new_f0)>len(f0):
                    new_f0 = new_f0[0:len(f0)]
                elif len(f0)>len(new_f0):
                    new_f0 = np.pad(new_f0, [(0,len(f0)-len(new_f0))])

            else:
                new_f0 = f0 + m['f0']['v']
        elif m['f0']['u']=='st':
            new_f0 = f0 * 2**(m['f0']['v']/12)

    # VTL
    if (m['vtl'] is None) or (m['vtl']['u'] is None and m['vtl']['v']==1) or (m['vtl']['u'] is not None and m['vtl']['v']==0):
        new_f = None
    else:
        if m['vtl']['u'] is None:
            vtl_ratio = m['vtl']['v']
        elif m['vtl']['u']=='st':
            vtl_ratio = 2**(m['vtl']['v']/12)
        new_f = f * vtl_ratio

    # Duration
    if (m['duration'] is None) or (m['duration']['u'] is None and m['duration']['v']==1) or (m['duration']['u'] is not None and m['duration']['v']==0 and not m['duration']['~']):
        new_t = None
    else:
        if m['duration']['u'] is None:
            # A ratio
            new_t = np.linspace(t[0], t[-1], int(m['duration']['v']*len(t)))
        elif m['duration']['u']=='s':
            if m['duration']['~']:
                # We assign a new duration
                new_t = np.linspace(t[0], t[-1], int(m['duration']['v']/frame_period*1e3))
            else:
                # We extend the duration with a certain offset
                new_duration = m['duration']['v'] + t[-1] #len(t)/pyworld.default_frame_period
                if new_duration<=0:
                    raise ValueError("[world] This is not good, the new duration is negative or null (%.3f s)... This is what we parsed: %s." % (new_duration, repr(m['duration'])))
                new_t = np.linspace(t[0], t[-1], int(new_duration/frame_period*1e3))

    # Now we rescale f0, sp and ap if necessary
    if new_f is None and new_t is None:
        # Both VTL and duration are unchanged
        new_sp = sp
        new_ap = ap
    else:
        if new_t is None:
            # Duration is not changed, we keep f0 as it is
            new_t = t
        else:
            # Duration is changed, we need to interpolate f0
            # This is a bit of a tricky business because there are zeros and we do
            # not want to interpolate those.
            uv = new_f0==0 # The unvoiced samples
            # We first interpolate over the unvoiced samples and stretch
            new_f0_tmp = new_f0[np.logical_not(uv)]
            new_f0 = spi.interp1d(t[np.logical_not(uv)], new_f0_tmp, kind='cubic', fill_value=(new_f0_tmp[0], new_f0_tmp[-1]), bounds_error=False, assume_sorted=True)(new_t)
            # Then we stretch the voice/unvoice information
            new_uv = spi.interp1d(t, uv*1.0, assume_sorted=True)(new_t)>.5
            new_f0[new_uv] = 0

        if new_f is None:
            # VTL is not changed
            new_f = f

        # Interp of spectral envelope and aperiodicity map
        new_sp = Fast2DInterp(t, f, sp)(new_t, new_f)
        new_ap = Fast2DInterp(t, f, ap)(new_t, new_f)

    new_f0, new_sp, new_ap = regularize_arrays(new_f0, new_sp, new_ap)
    y = pyworld.synthesize(new_f0, new_sp, new_ap, fs)

    y = ramp(y, fs, (5e-3, 5e-3))

    y = y / rms(y) * rms_x

    y, s = clipping_prevention(y)
    if s!=1:
        LOG.info("[world (v%s)] Clipping was avoided during processing of '%s' to '%s' by rescaling with a factor of %.3f (%.1f dB)." % (pyworld.__version__, in_filename, out_filename, s, 20*np.log10(s)))

    if out_filename is None:
        return y, fs
    else:
        sf.write(out_filename, y, fs)
        return out_filename, dat_filename

def rms(x):
    return np.sqrt(np.mean(x**2))

def clipping_prevention(x):
    m = np.max(abs(x))
    s = 1
    if m>=1.0:
        s = .98/m
        x = x*s
    return x, s

def ramp(x, fs, dur, shape='cosine'):
    """
    The underlying function to the `"ramp"` processing module.

    :param x: The input sound.

    :param fs: The sampling frequency.

    :param dur: The duration of the ramps (a two-element iterable).

    :param shape: The shape of the ramp ('cosine' or 'linear'). Defaults to 'cosine'.

    :return: The ramped sound.
    """

    if dur[0] != 0:
        n = int(fs*dur[0])
        w = np.linspace(0,1,n)
        if shape=='cosine':
            w = (1-np.cos(w*np.pi))/2
        if len(x.shape)>1:
            w.shape = (w.shape[0],1)
            w = np.tile(w, (1, x.shape[1]))
            x[0:n,:] = x[0:n,:] * w
        else:
            x[0:n] = x[0:n] * w

    if dur[1] != 0:
        n = int(fs*dur[1])
        w = np.linspace(1,0,n)
        if shape=='cosine':
            w = (1-np.cos(w*np.pi))/2
        if len(x.shape)>1:
            w.shape = (w.shape[0],1)
            w = np.tile(w, (1,x.shape[1]))
        x[-n:] = x[-n:] * w

    return x


def regularize_arrays(*args):
    """
    Making sure the arrays passed as arguments are in the right format for pyworld.
    """
    out = list()
    for x in args:
        out.append( np.require(x, requirements='C'))
    return tuple(out)


class Fast2DInterp():
    """
    Creates an interpolant object based on ``scipy.interpolate.RectBivariateSpline`` but
    dealing with out of range values.

    The constructor is: ``Fast2DInterp(x, y, z, ofrv=None)`` where ``x`` and ``y``
    are 1D arrays and ``z`` is a 2D array. The optional argument ``ofrv`` defines
    the value used for out of range inputs. If ``ofrv`` is ``None``, then the
    default behaviour of ``RectBivariateSpline`` is kept, i.e. the closest value is
    returned.

    The default type is ``linear``, which then makes use of ``scipy.interpolate.interp2d``.
    With ``cubic``, the ``RectBivariateSpline`` is used.

    Note that the class is not so useful in the end when used with ``linear``, but
    is useful if you want to use cubic-splines.
    """

    def __init__(self, x, y, z, ofrv=None, type='linear'):
        self.type = type

        if self.type=='cubic':
            self.interpolant = spi.RectBivariateSpline(x, y, z)
        elif self.type=='linear':
            self.interpolant = spi.interp2d(y, x, z, kind='linear')
        else:
            raise ValueError('Interpolant type unknown: "%s"' % type)

        self.x_range = (x[0], x[-1])
        self.y_range = (y[0], y[-1])

        # Out of range value:
        self.ofrv = ofrv

    def is_in_range(self, w, r):
        return np.logical_and(w>=r[0], w<=r[1])

    def __call__(self, x, y):
        return self.interp(x, y)

    def interp_(self, x, y):
        if self.type=='cubic':
            return self.interpolant(x, y)
        elif self.type=='linear':
            return self.interpolant(y, x)

    def interp(self, x, y):
        if (np.isscalar(x) or len(x)==1) and (np.isscalar(y) or len(y)==1):
            if self.ofrv is not None:
                if self.is_in_range(x, self.x_range) and self.is_in_range(y, self.y_range):
                    o = self.interp_(x, y)[0,0]
                else:
                    o = self.ofrv
            else:
                o = self.interp_(x, y)[0,0]
        else:
            o = self.interp_(x, y)

            if self.ofrv is not None:
                s = np.logical_and(self.is_in_range(xx, self.x_range), self.is_in_range(yy, self.y_range))
                o[s] = self.ofrv

        return o

def ramp(x, fs, dur, shape='cosine'):
    """
    The underlying function to the `"ramp"` processing module.
    :param x: The input sound.
    :param fs: The sampling frequency.
    :param dur: The duration of the ramps (a two-element iterable).
    :param shape: The shape of the ramp ('cosine' or 'linear'). Defaults to 'cosine'.
    :return: The ramped sound.
    """

    if dur[0] != 0:
        n = int(fs*dur[0])
        w = np.linspace(0,1,n)
        if shape=='cosine':
            w = (1-np.cos(w*np.pi))/2
        if len(x.shape)>1:
            w.shape = (w.shape[0],1)
            w = np.tile(w, (1, x.shape[1]))
            x[0:n,:] = x[0:n,:] * w
        else:
            x[0:n] = x[0:n] * w

    if dur[1] != 0:
        n = int(fs*dur[1])
        w = np.linspace(1,0,n)
        if shape=='cosine':
            w = (1-np.cos(w*np.pi))/2
        if len(x.shape)>1:
            w.shape = (w.shape[0],1)
            w = np.tile(w, (1,x.shape[1]))
        x[-n:] = x[-n:] * w

    return x


def cli(in_args=None, prog=None):
    # test parse_arguments

    import argparse

    parser = argparse.ArgumentParser(description='A comand line interface to PyWORLD.')

    if prog is not None:
        parser.prog = prog

    parser.add_argument('in_filename', help='The sound file to process.')
    parser.add_argument('out_filename', help='The file where we save the results.')

    parser.add_argument("--f0", help="""F0 modification, can take one of the following 3 forms:
    (1) '*' followed by a number, or instance '*2', in which case it is multiplicating ratio applied to the whole f0 contour.
    (2) A positive or negative number followed by a unit ('Hz' or 'st'). This will behave like an offset, adding so many Hertz or so many semitones to the f0 contour.
    (3) '~' followed by a number, followed by a unit (only 'Hz'). This will set the *average* f0 to the defined value.""")
    parser.add_argument("--vtl", help="""VTL modification, can take one of the following 2 forms: (1) '*' represents a multiplier for the vocal-tract length.
    Beware, this is not a multiplier for the spectral envelope, but its inverse. (2) Offsets are defined using the unit 'st' only, e.g. '-3.8st'.""")
    parser.add_argument("--duration", help="""Duration modification, can take one of the following 3 forms: (1) the '*' multiplier can also be used, followed by a ratio.
    (2) An offset can be defined in seconds (using unit 's'). (3) The absolute duration can be set using '~' followed by a value and the 's' unit.""")
    parser.add_argument("--cachefolder", help="The location of the cache folder (otherwise, .world files are saved in the same folder as the sound file.", default=None)

    if in_args is None:
        args = parser.parse_args()
    else:
        args = parser.parse_args(in_args)

    t0 = time.time()
    process_world(args.in_filename, vars(args), args.out_filename, args.cachefolder)
    print("Done in %.2f ms" % ((time.time()-t0)*1e3))


if __name__=='__main__':
    cli()
