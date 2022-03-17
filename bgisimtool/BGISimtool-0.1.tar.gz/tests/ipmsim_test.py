

# ------------------------------------------------------------------------------
# Imports
# ------------------------------------------------------------------------------
from bgisimtool.process_results import check_inputs
from bgisimtool.ipmsim import IpmsimResult
from bgisimtool.histogram import HistogramV2
import numpy as np
import matplotlib.pyplot as plt
import cProfile
from bgisimtool.mathfunc import process_vipm_histogram, get_expected_bin_content_gaussian


file = "/Users/swannlevasseur/HL-LHC/simulation/precision_study/files/results/0000.csv"
files = [file]
file_list = ["/Users/swannlevasseur/HL-LHC/simulation/precision_study/files/results/0000.csv.gz",
             "/Users/swannlevasseur/HL-LHC/simulation/precision_study/files/results/0001.csv.gz",
             "/Users/swannlevasseur/HL-LHC/simulation/precision_study/files/results/0002.csv.gz",
             "/Users/swannlevasseur/HL-LHC/simulation/precision_study/files/results/0003.csv.gz",
             "/Users/swannlevasseur/HL-LHC/simulation/precision_study/files/results/0004.csv.gz",
             "/Users/swannlevasseur/HL-LHC/simulation/precision_study/files/results/0005.csv.gz",
             "/Users/swannlevasseur/HL-LHC/simulation/precision_study/files/results/0006.csv.gz",
             "/Users/swannlevasseur/HL-LHC/simulation/precision_study/files/results/0007.csv.gz",
             "/Users/swannlevasseur/HL-LHC/simulation/precision_study/files/results/0008.csv.gz",
             "/Users/swannlevasseur/HL-LHC/simulation/precision_study/files/results/0009.csv.gz",
             "/Users/swannlevasseur/HL-LHC/simulation/precision_study/files/results/0010.csv.gz",
             "/Users/swannlevasseur/HL-LHC/simulation/precision_study/files/results/0011.csv.gz",
             "/Users/swannlevasseur/HL-LHC/simulation/precision_study/files/results/0012.csv.gz",
             "/Users/swannlevasseur/HL-LHC/simulation/precision_study/files/results/0013.csv.gz",
             "/Users/swannlevasseur/HL-LHC/simulation/precision_study/files/results/0014.csv.gz",
             "/Users/swannlevasseur/HL-LHC/simulation/precision_study/files/results/0015.csv.gz",
             "/Users/swannlevasseur/HL-LHC/simulation/precision_study/files/results/0016.csv.gz",
             "/Users/swannlevasseur/HL-LHC/simulation/precision_study/files/results/0017.csv.gz",
             "/Users/swannlevasseur/HL-LHC/simulation/precision_study/files/results/0018.csv.gz"]
data = IpmsimResult(filename_s=file_list, scale="um", position_bin_width=55, drift_bin_width=10)
a = HistogramV2()
a.fill_from_positions(data.data['final x'], bin_width=55)
t = process_vipm_histogram(a)
print(a._bin_content)
a.conditional_bining()
print(a._bin_content)
a.reframe((-500, 500))
print(a._bin_content)

data.final_hist.reframe((-500, 500))

cm = 1/2.54
fig, ax = plt.subplots(figsize=(25*cm, 20*cm))
ax.plot(a._bin_center, a._bin_content)
ax.plot(data.final_hist._bin_center, data.final_hist._bin_content)
plt.show()

data = IpmsimResult(filename_s=file_list, scale="um", position_bin_width=55, drift_bin_width=10, m_map=True)
data = IpmsimResult()
data.fill_from_all_files_with_extension("/Users/swannlevasseur/HL-LHC/simulation/precision_study/files/results/", ".gz")
data.calc_psf(x_bin_size=10e-6, y_bin_size=10e-6)
x_center = int(data.psf_x_bin_center.shape[0] / 2)
y_center = int(data.psf_y_bin_center.shape[0] / 2)

fig, ax = plt.subplots(figsize=(25*cm, 20*cm))
hist, bin_edge = np.histogram(data.psf_distributions[x_center-5:x_center+5, y_center], 30)
ax.plot(bin_edge[0:-1] / 1e-6, hist)
plt.show()

cm = 1/2.54
fig, ax = plt.subplots(figsize=(25*cm, 20*cm))
for dist in data.psf_distributions[x_center-40:x_center+40, y_center]:
    hist, bin_edge = np.histogram(dist, 50)
    ax.plot(bin_edge[0:-1]/ 1e-6, hist)

plt.show()

# profiling
data.energy_x_hist.fillFromRawPosition(data.data['final EK_x eV'], 50)
np.histogram(data.data['final EK_x eV'], 61)

min_pos = min(data.data["final EK_x eV"])
max_pos = max(data.data["final EK_x eV"])
bin_number = int((max_pos - min_pos) / 100) + 1
a = HistogramV2()
a.fill_from_positions(data.data["final EK_x eV"], bin_width=10)
a.conditional_bining()
cProfile.run('IpmsimResult(filename_s=file_list)')
cProfile.run('data.energy_x_hist.fill_from_raw_position_numpy(data.data["final EK_x eV"], 10)')
cProfile.run('data.energy_x_hist.fillFromRawPosition(data.data["final EK_x eV"], 50)')
cProfile.run('a.fill_from_raw_position_numpy(data.data["final EK_x eV"], bin_width=50)')


cProfile.run('data = IpmsimResult(filename_s=file_list, scale="um", position_bin_width=55, drift_bin_width=10)')
cProfile.run('data = IpmsimResult(filename_s=file_list, scale="um", position_bin_width=55, drift_bin_width=10, m_map=True)')

# test of np.histogram
hist, bin_edge = np.histogram(data.data['initial x'], bins=100)
cm = 1/2.54
fig, ax = plt.subplots(figsize=(25*cm, 20*cm))
plot = ax.scatter(bin_edge[0:-1],hist)
plt.show()
# for each pixel,
cm = 1/2.54
fig, ax = plt.subplots(figsize=(25*cm, 20*cm))
#plot = ax.pcolormesh(t[0], t[1], t[3], cmap='RdBu', shading='gouraud')
plot = ax.contourf(data.psf_x_bin_center/1e-6, data.psf_y_bin_center/1e-6, data.psf_stdevs/1e-6, 100, cmap='RdBu')
ax.set_title('PSF = f(x,y) = stdev(x_init(x,y) - x_final(x,y))')
ax.set_xlabel('Initial electron X position [um]')
ax.set_ylabel('Initial electron Y position [um]')
#plot = plt.pcolormesh(t[0], t[1], t[2], cmap='RdBu')
cbar = plt.colorbar(plot)
cbar.ax.set_ylabel('PSF [um]')
plt.savefig('psf_xy.pdf')
plt.show()

fig, ax = plt.subplots(figsize=(25*cm, 20*cm))
ax.scatter(data.psf_x_bin_center[:,172]/1e-6, data.psf_stdevs[:,172]/1e-6)
ax.set_title('PSF = f(x,y) = stdev(x_init(x,y) - x_final(x,y)) for y=0')
ax.set_xlabel('Initial electron X position [um]')
ax.set_ylabel('PSF [um]')
#plt.show()
plt.savefig('psf_x_y0.pdf')

fig, ax = plt.subplots(figsize=(25*cm, 20*cm))
ax.scatter(data.psf_x_bin_center[:,172]/1e-6, data.psf_stdevs[:,172]/1e-6)
ax.set_title('PSF = f(x,y) = stdev(x_init(x,y) - x_final(x,y)) for y=0')
ax.set_xlabel('Initial electron X position [um]')
ax.set_ylabel('PSF [um]')
#plt.show()
plt.savefig('psf_x_y0.pdf')

fig, ax = plt.subplots(figsize=(25*cm, 20*cm), subplot_kw={"projection": "3d"})
surf = ax.plot_surface(data.psf_x_bin_center/1e-6, data.psf_y_bin_center/1e-6, data.psf_stdevs/1e-6, cmap='RdBu',
                       linewidth=0, antialiased=False)
# Add a color bar which maps values to colors.
fig.colorbar(surf, shrink=0.5, aspect=5)

plt.show()