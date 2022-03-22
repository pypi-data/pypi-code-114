import argparse
import os
import json

import scaffoldmaker.scaffolds as sc

from opencmiss.exporter.webgl import ArgonSceneExporter as WebGLExporter
from opencmiss.exporter.thumbnail import ArgonSceneExporter as ThumbnailExporter
from opencmiss.zinc.context import Context

from sparc.curation.tools.manifests import ManifestDataFrame
from sparc.curation.tools.ondisk import OnDiskFiles
from sparc.curation.tools.utilities import convert_to_bytes
from sparc.curation.tools.scaffold_annotations import get_errors, fix_error, get_confirmation_message


def create_dataset(dataset_dir, mesh_config_file, argon_document):
    # Create dataset
    _create_folders(dataset_dir)
    _generate_mesh(os.path.join(dataset_dir, "primary"), mesh_config_file)
    _generate_web_gl((os.path.join(dataset_dir, "derivative", "Scaffold")), argon_document)
    # Dataset annotation
    _annotate_scaffold(dataset_dir)


def _create_folders(path):
    folder_dir = [
        os.path.join(path, "derivative", "Scaffold"),
        os.path.join(path, "docs"),
        os.path.join(path, "primary")
    ]

    for filename in folder_dir:
        _create_folder(filename)


def _create_folder(path):
    try:
        os.makedirs(path)
    except OSError:
        print("Creation of the directory %s failed" % path)
    else:
        print("Successfully created the directory %s" % path)


def _generate_mesh(output_dir, mesh_config_file):
    context = Context("MeshGenerator")
    region = context.createRegion()
    f = open(mesh_config_file)
    scaffoldConfig = json.load(f)
    scaffoldType = scaffoldConfig["generator_settings"]["scaffoldPackage"]
    scaffoldPackage = sc.Scaffolds_decodeJSON(scaffoldType)
    scaffoldPackage.generate(region, applyTransformation=False)
    file_name = os.path.join(output_dir, "scaffold_mesh.exf")
    region.writeFile(file_name)


def _generate_web_gl(output_dir, argon_document):
    exporter = WebGLExporter(output_dir)
    _export_file(exporter, argon_document)
    exporter = ThumbnailExporter(output_dir)
    _export_file(exporter, argon_document)


def _export_file(exporter, argon_document):
    exporter.set_filename(argon_document)
    exporter.set_parameters({
        "prefix": 'scaffold',
        "numberOfTimeSteps": None,
        "initialTime": None,
        "finishTime": None,
    })
    exporter.export()


def _annotate_scaffold(dataset_dir):
    errors = _get_current_errors(dataset_dir)
    previous_error = []
    while len(errors) != 0:
        for error in errors:
            print(error.get_error_message())
            fix_error(error)
            if error.get_error_message() in previous_error:
                print("This error can't be fixed automatically.")
                break
            else:
                previous_error.append(error.get_error_message())
        errors = _get_current_errors(dataset_dir)


def _get_current_errors(dataset_dir):
    max_size = convert_to_bytes('3MiB')
    OnDiskFiles().setup_dataset(dataset_dir, max_size)
    ManifestDataFrame().setup_dataframe(dataset_dir)
    return get_errors()


def main():
    parser = argparse.ArgumentParser(description='Create a Scaffold based SPARC dataset from a scaffold description file and an Argon document.')
    parser.add_argument("dataset_dir", help='root directory for new dataset.')
    parser.add_argument("mesh_config_file", help='mesh config JSON file to generate mesh exf file.')
    parser.add_argument("argon_document", help='argon document file to generate webGL files.')

    args = parser.parse_args()
    dataset_dir = args.dataset_dir
    mesh_config_file = args.mesh_config_file
    argon_document = args.argon_document

    # Create dataset
    create_dataset(dataset_dir, mesh_config_file, argon_document)


if __name__ == "__main__":
    main()
