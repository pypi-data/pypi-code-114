import os
import xarray as xr

def get_fv3_grid(res='C384',tile=1):
    cdir = os.path.abspath(__file__)[:-11]
    gridname = "{}_grid_spec.tile{}.nc".format(res,str(int(tile)))
    fname = "{}{}".format(cdir,gridname)
    o = xr.open_dataset(fname)
    o = o.rename({'grid_xt':'x',
                  'grid_yt':'y',
                  'grid_latt':'latitude',
                  'grid_lont':'longitude',
                  'grid_lat':'lat_b',
                  'grid_lon':'lon_b',
                  'grid_x':'x_b',
                  'grid_y':'y_b'}).drop('time')
    return o.squeeze().set_coords(['latitude','longitude','lat_b','lon_b'])

