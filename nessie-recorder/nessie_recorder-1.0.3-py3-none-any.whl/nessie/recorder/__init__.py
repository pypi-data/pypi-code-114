import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from pathlib import Path
import struct
import click
import h5py
from scipy.signal import resample
from scipy.optimize import curve_fit
from crccheck.crc import Crc16Ccitt
from collections import namedtuple
from collections import namedtuple


G = 9.832
ADC_BITS = 14
R1 = 240
R2 = 976

BUFFER_SIZE = 64

labels = {
    "v_dc": "DC voltage",
    "i_dc": "DC current",
    "v_ac": "AC voltage",
    "i_ac": "AC current",
    "acc_x": "Acceleration X",
    "acc_y": "Acceleration Y",
    "acc_z": "Acceleration Z",
}

units = {
    "v_dc": "Voltage [V]",
    "i_dc": "Current [mA]",
    "v_ac": "Voltage [V]",
    "i_ac": "Current [mA]",
    "acc_x": "Acceleration [m/$s^2$]",
    "acc_y": "Acceleration [m/$s^2$]",
    "acc_z": "Acceleration [m/$s^2$]",
}

plot_scales = {
    "v_dc": 1.0,
    "i_dc": 1000.0,
    "v_ac": 1.0,
    "i_ac": 1000.0,
    "acc_x": 1.0,
    "acc_y": 1.0,
    "acc_z": 1.0,
}

ChCfg = namedtuple(
    "ChCfg",
    [
        "vrange_volt",
        "irange_ma",
        "ratio_pcnt",
        "interval_s",
        "duration_ms",
        "vharvest_mv",
        "mode",
    ],
)
RecCfg = namedtuple("RecCfg", ["dc", "ac", "acc_range", "rate"])

Sample = namedtuple(
    "Sample", ["v_dc", "i_dc", "v_ac", "i_ac", "acc_x", "acc_y", "acc_z"]
)


def parse_ch_cfg(data_bin):
    cfg_ch_vals = struct.unpack("<iiiiiii", data_bin)
    return ChCfg(
        cfg_ch_vals[0],
        cfg_ch_vals[1],
        cfg_ch_vals[2],
        cfg_ch_vals[3],
        cfg_ch_vals[4],
        cfg_ch_vals[5],
        cfg_ch_vals[6],
    )


def bin2acc(val_bin, acc_range):
    if val_bin & (1 << 9):
        val_bin |= 0xFC00

    mg_per_lsb = 3.9 * (acc_range / 2)
    val_mg = val_bin * mg_per_lsb

    return val_mg / 1000 * G


def bin2v(val_bin, v_range):
    v_fullscale = v_range / 5
    return val_bin / (2**14) * (R1 + R2) / R1 * v_fullscale


def bin2i(val_bin, i_range_ma):
    return val_bin / (2**14) * i_range_ma / 1000


def parse_samples(data_bin, n_samples, cfg: RecCfg):
    samples_bin = np.frombuffer(data_bin, "i2")
    samples_bin = np.reshape(samples_bin, (n_samples, 7))
    res = list()
    for i in range(n_samples):
        samples = {
            "acc_x": bin2acc(samples_bin[i, 0], cfg.acc_range),
            "acc_y": bin2acc(samples_bin[i, 1], cfg.acc_range),
            "acc_z": bin2acc(samples_bin[i, 2], cfg.acc_range),
            "v_dc": bin2v(samples_bin[i, 3], cfg.dc.vrange_volt),
            "i_dc": bin2i(samples_bin[i, 4], cfg.dc.irange_ma),
            "v_ac": bin2v(samples_bin[i, 5], cfg.ac.vrange_volt),
            "i_ac": bin2i(samples_bin[i, 6], cfg.ac.irange_ma),
        }
        res.append(samples)
    return res


def read_block(f, cfg, offsets=None):
    header_bin = f.read(8)
    if header_bin == b"":
        return
    marker, counter = struct.unpack("<II", header_bin)
    if marker != 0xFFFFFFFF:
        raise Exception("Invalid marker")
    # print(f"Block {counter}")

    data_bin = f.read(14 * BUFFER_SIZE)
    crc_data = struct.unpack("<H", f.read(2))[0]
    if crc_data != Crc16Ccitt.calc(data_bin):
        raise Exception("CRC check of data block failed")

    samples = parse_samples(data_bin, BUFFER_SIZE, cfg)
    t_blck = counter * BUFFER_SIZE * 1.0 / cfg.rate
    for i in range(BUFFER_SIZE):
        samples[i]["time"] = t_blck + i / cfg.rate
        if offsets is not None:
            samples[i]["i_dc"] -= offsets["i_dc"]
            samples[i]["i_ac"] -= offsets["i_ac"]

    return samples


def get_samples(f, cfg):
    block = read_block(f, cfg)
    df = pd.DataFrame(block)
    offsets = df.mean()
    block = read_block(f, cfg, offsets)

    while block is not None:

        for sample in block:
            yield sample
        block = read_block(f, cfg, offsets)


def get_blocks(f, cfg):
    block = read_block(f, cfg)
    df = pd.DataFrame(block)
    offsets = df.mean()
    block = read_block(f, cfg, offsets)

    while block is not None:
        yield block
        block = read_block(f, cfg, offsets)


class HDFLog(object):
    def __init__(self, file: str, mode: str = "r"):
        if mode == "r":
            self._mode = "r"
        elif mode == "w":
            self._mode = "w"
        else:
            raise Exception()

        self._path = Path(file)

    def __enter__(self):
        self._hf = h5py.File(self._path, self._mode)
        if self._mode == "w":
            self._hf.create_dataset(
                "time",
                (0,),
                dtype="f8",
                maxshape=(None,),
                # This makes writing more efficient, see HDF5 docs
                chunks=(BUFFER_SIZE,),
                compression="lzf",
            )
            for k in labels.keys():
                self._hf.create_dataset(
                    k,
                    (0,),
                    dtype="f8",
                    maxshape=(None,),
                    # This makes writing more efficient, see HDF5 docs
                    chunks=(BUFFER_SIZE,),
                    compression="lzf",
                )
        return self

    def __exit__(self, *exc):
        self._hf.flush()
        self._hf.close()

    def write(self, block):
        # First, we have to resize the corresponding datasets
        old_set_length = self._hf["time"].shape[0]
        new_set_length = old_set_length + len(block)

        df = pd.DataFrame(block)
        for k in self._hf.keys():
            self._hf[k].resize((new_set_length,))
            self._hf[k][old_set_length:] = df[k].values


@click.group()
def cli():
    pass


@cli.command(short_help="Extract binary data and store as csv or hdf file")
@click.option("--infile", "-i", type=click.Path(exists=True), required=True)
@click.option("--outfile", "-o", type=click.Path(), required=True)
@click.option("--filetype", "-t", type=click.Choice(["csv", "hdf5"]))
def extract(infile, outfile, filetype):

    outpath = Path(outfile)
    if filetype is None:
        if outpath.suffix == ".csv":
            filetype = "csv"
            click.echo("Filetype is csv")
        elif outpath.suffix == ".h5":
            filetype = "hdf5"
            click.echo("Filetype is hdf5")
        else:
            raise click.UsageError(
                "No filetype provided and can't guess from output filename"
            )

    with open(infile, "rb") as f:
        header_string = f.read(16)
        if header_string != b"NESSIE_RECORDER\0":
            raise Exception("No valid nessie recorder file")

        cfg_data_bin = f.read(64)
        cfg_crc = struct.unpack("<H", f.read(2))[0]
        if cfg_crc != Crc16Ccitt.calc(cfg_data_bin):
            raise Exception("CRC check of config failed")

        cfg_ch_dc = parse_ch_cfg(cfg_data_bin[:28])
        cfg_ch_ac = parse_ch_cfg(cfg_data_bin[28:56])
        cfg_acc_range = struct.unpack("<i", cfg_data_bin[56:60])[0]
        cfg_rate = struct.unpack("<i", cfg_data_bin[60:64])[0]
        cfg = RecCfg(cfg_ch_dc, cfg_ch_ac, cfg_acc_range, cfg_rate)

        if filetype == "csv":
            df = pd.DataFrame(list(get_samples(f, cfg)))
            df.to_csv(outpath, index=False)
        else:
            with HDFLog(outpath, "w") as log:
                for block in get_blocks(f, cfg):
                    log.write(block)


@cli.command(short_help="Plots data from csv or hdf file")
@click.option("--infile", "-i", type=click.Path(exists=True), required=True)
@click.option("--filetype", "-t", type=click.Choice(["csv", "hdf5"]))
@click.option("--decimate", "-d", type=int, default=1)
def plot(infile, filetype, decimate):

    inpath = Path(infile)
    if filetype is None:
        if inpath.suffix == ".csv":
            filetype = "csv"
            click.echo("Filetype is csv")
        elif inpath.suffix == ".h5":
            filetype = "hdf5"
            click.echo("Filetype is hdf5")
        else:
            raise click.UsageError("No filetype provided and can't guess from filename")

    if filetype == "csv":
        df = pd.read_csv(inpath)
        df = df.iloc[::decimate, :]
    else:
        data_dict = {}
        with h5py.File(inpath, "r") as hf:
            for k in hf.keys():
                data_dict[k] = hf[k][::decimate]

        df = pd.DataFrame(data_dict)

    _, axes = plt.subplots(7, 1, sharex=True)

    for i, k in enumerate(labels.keys()):

        axes[i].plot(df["time"], df[k] * plot_scales[k])
        axes[i].set_ylabel(units[k])
        axes[i].set_title(labels[k])

    axes[i].set_xlabel("Time [s]")
    plt.show()


@cli.command(short_help="Convert recorded data to solarbox trace")
@click.option("--infile", "-i", type=click.Path(exists=True), required=True)
@click.option("--filetype", "-t", type=click.Choice(["csv", "hdf5"]))
@click.option("--channel", "-c", type=click.Choice(["dc", "ac"]))
@click.option("--outfile", "-o", type=click.Path(), required=True)
@click.option("--mapping", "-m", type=click.Path(), required=True)
def convert(infile, filetype, channel, outfile, mapping):
    inpath = Path(infile)
    if filetype is None:
        if inpath.suffix == ".csv":
            filetype = "csv"
            click.echo("Filetype is csv")
        elif inpath.suffix == ".h5":
            filetype = "hdf5"
            click.echo("Filetype is hdf5")
        else:
            raise click.UsageError("No filetype provided and can't guess from filename")

    if filetype == "csv":
        df = pd.read_csv(inpath)
    else:
        data_dict = {}
        with h5py.File(inpath, "r") as hf:
            for k in hf.keys():
                data_dict[k] = hf[k][:]

        df = pd.DataFrame(data_dict)

    if channel == "dc":
        x = df["v_dc"] * df["i_dc"]
    else:
        x = df["v_ac"] * df["i_ac"]

    Fs = int(round(1.0 / df["time"].diff().mean()))
    click.echo(f"Input sampling rate {int(Fs)}Hz")
    if Fs == 1000:
        x_1k = x
    else:
        click.echo("Resampling to 1kHz")
        x_1k = resample(x, len(x) * 1000 // Fs)

    df_conv = pd.read_csv(mapping)

    def f_obj(x, m):
        return m * x

    popt, pcov = curve_fit(f_obj, df_conv["recorder"], df_conv["solarbox"])

    click.echo(
        f"Conversion equation: y={popt[0]:.2f}*x, residual error: {pcov[0][0]:.3f}"
    )

    y = x_1k * popt[0]

    y[y < 0] = 0.0
    if any(y > 100.0):
        raise ValueError("Output value > 100% detected")
    np.savetxt(outfile, y, delimiter=",")


if __name__ == "__main__":
    cli()
