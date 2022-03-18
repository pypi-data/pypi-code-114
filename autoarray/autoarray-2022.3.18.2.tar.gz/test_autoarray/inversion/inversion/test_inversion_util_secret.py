import numpy as np
import pytest

import autoarray as aa
from autoarray.inversion.inversion import inversion_util_secret
from autoarray.inversion.inversion.factory import inversion_from as Inversion


def test__w_tilde_curvature_interferometer_from():

    noise_map = np.array([1.0, 2.0, 3.0])
    uv_wavelengths = np.array([[0.0001, 2.0, 3000.0], [3000.0, 2.0, 0.0001]])

    grid = aa.Grid2D.uniform(shape_native=(2, 2), pixel_scales=0.0005)

    w_tilde = inversion_util_secret.w_tilde_curvature_interferometer_from(
        noise_map_real=noise_map, uv_wavelengths=uv_wavelengths, grid_radians_slim=grid
    )

    assert w_tilde == pytest.approx(
        np.array(
            [
                [1.25, 0.75, 1.24997, 0.74998],
                [0.75, 1.25, 0.74998, 1.24997],
                [1.24994, 0.74998, 1.25, 0.75],
                [0.74998, 1.24997, 0.75, 1.25],
            ]
        ),
        1.0e-4,
    )


def test__curvature_matrix_via_w_tilde_preload_from():

    noise_map = np.array([1.0, 2.0, 3.0, 4.0, 5.0, 6.0])
    uv_wavelengths = np.array(
        [[0.0001, 2.0, 3000.0, 50000.0, 200000.0], [3000.0, 2.0, 0.0001, 10.0, 5000.0]]
    )

    grid = aa.Grid2D.uniform(shape_native=(3, 3), pixel_scales=0.0005)

    w_tilde = inversion_util_secret.w_tilde_curvature_interferometer_from(
        noise_map_real=noise_map, uv_wavelengths=uv_wavelengths, grid_radians_slim=grid
    )

    mapping_matrix = np.array(
        [
            [1.0, 0.0, 0.0],
            [0.0, 0.0, 1.0],
            [0.0, 1.0, 0.0],
            [0.0, 1.0, 0.0],
            [0.0, 0.0, 1.0],
            [0.0, 0.0, 1.0],
            [1.0, 0.0, 0.0],
            [0.0, 0.0, 1.0],
            [1.0, 0.0, 0.0],
        ]
    )

    curvature_matrix_via_w_tilde = aa.util.leq.curvature_matrix_via_w_tilde_from(
        w_tilde=w_tilde, mapping_matrix=mapping_matrix
    )

    w_tilde_preload = inversion_util_secret.w_tilde_curvature_preload_interferometer_from(
        noise_map_real=noise_map,
        uv_wavelengths=uv_wavelengths,
        shape_masked_pixels_2d=(3, 3),
        grid_radians_2d=grid.native,
    )

    pix_indexes_for_sub_slim_index = np.array(
        [[0], [2], [1], [1], [2], [2], [0], [2], [0]]
    )

    pix_size_for_sub_slim_index = np.ones(shape=(9,)).astype("int")
    pix_weights_for_sub_slim_index = np.ones(shape=(9, 1))

    native_index_for_slim_index = np.array(
        [[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]]
    )

    sub_slim_indexes_for_pix_index, sub_slim_weights_for_pix_index, sub_slim_sizes_for_pix_index = aa.util.mapper.sub_slim_indexes_for_pix_index(
        pix_indexes_for_sub_slim_index=pix_indexes_for_sub_slim_index,
        pix_weights_for_sub_slim_index=pix_weights_for_sub_slim_index,
        pix_pixels=3,
    )

    curvature_matrix_via_preload = inversion_util_secret.curvature_matrix_via_w_tilde_curvature_preload_interferometer_from(
        curvature_preload=w_tilde_preload,
        pix_indexes_for_sub_slim_index=pix_indexes_for_sub_slim_index,
        pix_size_for_sub_slim_index=pix_size_for_sub_slim_index,
        pix_weights_for_sub_slim_index=pix_weights_for_sub_slim_index,
        native_index_for_slim_index=native_index_for_slim_index,
        pix_pixels=3,
    )

    assert curvature_matrix_via_w_tilde == pytest.approx(
        curvature_matrix_via_preload, 1.0e-4
    )


def test__curvature_matrix_via_w_tilde_two_methods_agree():

    noise_map = np.array([1.0, 2.0, 3.0, 4.0, 5.0, 6.0])
    uv_wavelengths = np.array(
        [[0.0001, 2.0, 3000.0, 50000.0, 200000.0], [3000.0, 2.0, 0.0001, 10.0, 5000.0]]
    )

    grid = aa.Grid2D.uniform(shape_native=(3, 3), pixel_scales=0.0005)

    w_tilde = inversion_util_secret.w_tilde_curvature_interferometer_from(
        noise_map_real=noise_map, uv_wavelengths=uv_wavelengths, grid_radians_slim=grid
    )

    w_tilde_preload = inversion_util_secret.w_tilde_curvature_preload_interferometer_from(
        noise_map_real=noise_map,
        uv_wavelengths=uv_wavelengths,
        shape_masked_pixels_2d=(3, 3),
        grid_radians_2d=grid.native,
    )

    native_index_for_slim_index = np.array(
        [[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]]
    )

    w_tilde_via_preload = inversion_util_secret.w_tilde_via_preload_from(
        w_tilde_preload=w_tilde_preload,
        native_index_for_slim_index=native_index_for_slim_index,
    )

    assert (w_tilde == w_tilde_via_preload).all()


def test__identical_inversion_values_for_two_methods():
    real_space_mask = aa.Mask2D.unmasked(
        shape_native=(7, 7), pixel_scales=0.1, sub_size=1
    )

    grid = aa.Grid2D.from_mask(mask=real_space_mask)

    pix = aa.pix.DelaunayMagnification(shape=(7, 7))

    pixelization_grid = aa.Grid2D.manual_slim(
        [[0.1, 0.1], [1.1, 0.6], [2.1, 0.1], [0.4, 1.1], [1.1, 7.1], [2.1, 1.1]],
        shape_native=(3, 2),
        pixel_scales=1.0,
    )

    pixelization_grid = aa.Grid2DSparse(
        grid=pixelization_grid, sparse_index_for_slim_index=None
    )

    mapper = pix.mapper_from(
        source_grid_slim=grid,
        source_pixelization_grid=pixelization_grid,
        settings=aa.SettingsPixelization(use_border=False),
    )

    reg = aa.reg.Constant(coefficient=0.0)

    visibilities = aa.Visibilities.manual_slim(
        visibilities=[
            1.0 + 0.0j,
            1.0 + 0.0j,
            1.0 + 0.0j,
            1.0 + 0.0j,
            1.0 + 0.0j,
            1.0 + 0.0j,
            1.0 + 0.0j,
        ]
    )
    noise_map = aa.VisibilitiesNoiseMap.ones(shape_slim=(7,))
    uv_wavelengths = np.ones(shape=(7, 2))

    interferometer = aa.Interferometer(
        visibilities=visibilities,
        noise_map=noise_map,
        uv_wavelengths=uv_wavelengths,
        real_space_mask=real_space_mask,
        settings=aa.SettingsInterferometer(transformer_class=aa.TransformerDFT),
    )

    inversion_w_tilde = Inversion(
        dataset=interferometer,
        linear_obj_list=[mapper],
        regularization_list=[reg],
        settings=aa.SettingsInversion(check_solution=False, use_w_tilde=True),
    )

    inversion_mapping_matrices = Inversion(
        dataset=interferometer,
        linear_obj_list=[mapper],
        regularization_list=[reg],
        settings=aa.SettingsInversion(check_solution=False, use_w_tilde=False),
    )

    assert (inversion_w_tilde.data == inversion_mapping_matrices.data).all()
    assert (inversion_w_tilde.noise_map == inversion_mapping_matrices.noise_map).all()
    assert inversion_w_tilde.mapper_list[0] == inversion_mapping_matrices.mapper_list[0]
    assert (
        inversion_w_tilde.regularization_list[0]
        == inversion_mapping_matrices.regularization_list[0]
    )
    assert (
        inversion_w_tilde.regularization_matrix
        == inversion_mapping_matrices.regularization_matrix
    ).all()

    assert inversion_w_tilde.curvature_matrix == pytest.approx(
        inversion_mapping_matrices.curvature_matrix, 1.0e-8
    )
    assert inversion_w_tilde.curvature_reg_matrix == pytest.approx(
        inversion_mapping_matrices.curvature_reg_matrix, 1.0e-8
    )
    assert inversion_w_tilde.reconstruction == pytest.approx(
        inversion_mapping_matrices.reconstruction, 1.0e-2
    )
    assert inversion_w_tilde.mapped_reconstructed_image == pytest.approx(
        inversion_mapping_matrices.mapped_reconstructed_image, 1.0e-2
    )
    assert inversion_w_tilde.mapped_reconstructed_data == pytest.approx(
        inversion_mapping_matrices.mapped_reconstructed_data, 1.0e-2
    )


# def test__inversion_interferometer__via_mapper(
#     interferometer_7_no_fft,
#     rectangular_mapper_7x7_3x3,
#     delaunay_mapper_9_3x3,
#     voronoi_mapper_9_3x3,
#     regularization_constant,
# ):
#
#     inversion = aa.Inversion(
#         dataset=interferometer_7_no_fft,
#         linear_obj_list=[rectangular_mapper_7x7_3x3],
#         regularization_list=[regularization_constant],
#         settings=aa.SettingsInversion(use_w_tilde=True, check_solution=False),
#     )
#
#     assert isinstance(inversion.mapper_list[0], aa.MapperRectangularNoInterp)
#     assert isinstance(inversion.leq, aa.LEqInterferometerWTilde)
#     assert inversion.mapped_reconstructed_data == pytest.approx(
#         1.0 + 0.0j * np.ones(shape=(7,)), 1.0e-4
#     )
#     assert (np.imag(inversion.mapped_reconstructed_data) < 0.0001).all()
#     assert (np.imag(inversion.mapped_reconstructed_data) > 0.0).all()
#     assert inversion.log_det_curvature_reg_matrix_term == pytest.approx(10.2116, 1.0e-4)
#
#     inversion = aa.Inversion(
#         dataset=interferometer_7_no_fft,
#         linear_obj_list=[delaunay_mapper_9_3x3],
#         regularization_list=[regularization_constant],
#         settings=aa.SettingsInversion(use_w_tilde=True, check_solution=False),
#     )
#
#     assert isinstance(inversion.mapper_list[0], aa.MapperDelaunay)
#     assert isinstance(inversion.leq, aa.LEqInterferometerWTilde)
#     assert inversion.mapped_reconstructed_data == pytest.approx(
#         1.0 + 0.0j * np.ones(shape=(7,)), 1.0e-4
#     )
#     assert (np.imag(inversion.mapped_reconstructed_data) < 0.0001).all()
#     assert (np.imag(inversion.mapped_reconstructed_data) > 0.0).all()
#     assert inversion.log_det_curvature_reg_matrix_term == pytest.approx(
#         14.49772, 1.0e-4
#     )
#
#     inversion = aa.Inversion(
#         dataset=interferometer_7_no_fft,
#         linear_obj_list=[voronoi_mapper_9_3x3],
#         regularization_list=[regularization_constant],
#         settings=aa.SettingsInversion(use_w_tilde=True, check_solution=False),
#     )
#
#     assert isinstance(inversion.mapper_list[0], aa.MapperVoronoiNoInterp)
#     assert isinstance(inversion.leq, aa.LEqInterferometerWTilde)
#     assert inversion.mapped_reconstructed_data == pytest.approx(
#         1.0 + 0.0j * np.ones(shape=(7,)), 1.0e-4
#     )
#     assert (np.imag(inversion.mapped_reconstructed_data) < 0.0001).all()
#     assert (np.imag(inversion.mapped_reconstructed_data) > 0.0).all()
#     assert inversion.log_det_curvature_reg_matrix_term == pytest.approx(14.4977, 1.0e-4)
