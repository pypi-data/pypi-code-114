from biolib.biolib_binary_format import BioLibBinaryFormatBasePackage
from biolib.biolib_binary_format.base_package import IndexableBuffer, InMemoryIndexableBuffer
from biolib.biolib_binary_format.common_types import FilesInfo
from biolib.biolib_binary_format.module_output import ModuleOutput
from biolib.typing_utils import TypedDict, List


class UnencryptedModuleOutputMetadata(TypedDict):
    version: int
    type: int
    stdout_length: int
    stderr_length: int
    files_info_length: int
    files_data_length: int


unencrypted_module_output_metadata_lengths = UnencryptedModuleOutputMetadata(
    # Note: order is important
    version=1,
    type=1,
    stdout_length=8,
    stderr_length=8,
    files_info_length=8,
    files_data_length=8,
)


class UnencryptedModuleOutputError(BaseException):
    pass


class UnencryptedModuleOutput(BioLibBinaryFormatBasePackage):
    _TYPE = 11
    _VERSION = 1

    _FILE_PATH_LENGTH_BYTES = 4
    _FILE_DATA_LENGTH_BYTES = 8

    def __init__(self, buffer: IndexableBuffer):
        super().__init__()
        self._buffer = buffer

    def _get_metadata(self) -> UnencryptedModuleOutputMetadata:
        if not self._buffer:
            raise UnencryptedModuleOutputError(
                'You must construct this class with a buffer to get its metadata'
            )

        metadata = {}
        for field_name, field_length in unencrypted_module_output_metadata_lengths.items():
            value = self._buffer.get_data_with_pointer_as_int(length_bytes=field_length)  # type: ignore
            if field_name == 'version' and value != UnencryptedModuleOutput._VERSION:
                raise Exception('Version does not match')

            if field_name == 'type' and value != UnencryptedModuleOutput._TYPE:
                raise Exception('Type does not match')

            metadata[field_name] = value

        return UnencryptedModuleOutputMetadata(**metadata)  # type: ignore

    def convert_to_serialized_module_output(self) -> bytes:
        if not self._buffer:
            raise UnencryptedModuleOutputError(
                'You must construct this class with a buffer to convert to module output'
            )

        metadata = self._get_metadata()

        exit_code = self._buffer.get_data_with_pointer_as_int(length_bytes=2)
        stdout = self._buffer.get_data_with_pointer(length_bytes=metadata['stdout_length'])
        stderr = self._buffer.get_data_with_pointer(length_bytes=metadata['stderr_length'])

        files_info_serialized = InMemoryIndexableBuffer(
            self._buffer.get_data_with_pointer(length_bytes=metadata['files_info_length'])
        )
        files_info: List[FilesInfo] = []
        while files_info_serialized.pointer <= len(files_info_serialized) - 1:  # subtract 1 as pointer is 0-indexed
            path_length = files_info_serialized.get_data_with_pointer_as_int(length_bytes=4)
            files_info.append({
                'path': files_info_serialized.get_data_with_pointer(length_bytes=path_length).decode(),
                'data_length': files_info_serialized.get_data_with_pointer_as_int(length_bytes=8)
            })

        files = {}
        for file_info in files_info:
            files[file_info['path']] = self._buffer.get_data_with_pointer(
                length_bytes=file_info['data_length']
            )

        return ModuleOutput().serialize(
            exit_code=exit_code,
            files=files,
            stderr=stderr,
            stdout=stdout,
        )

    @staticmethod
    def create_from_serialized_module_output(module_output_serialized: bytes) -> bytes:
        module_output_dict = ModuleOutput(module_output_serialized).deserialize()

        bbf_data = bytearray()
        bbf_data.extend(UnencryptedModuleOutput._VERSION.to_bytes(1, 'big'))
        bbf_data.extend(UnencryptedModuleOutput._TYPE.to_bytes(1, 'big'))

        # Length of stdout and stderr
        bbf_data.extend(len(module_output_dict['stdout']).to_bytes(8, 'big'))
        bbf_data.extend(len(module_output_dict['stderr']).to_bytes(8, 'big'))

        files_info = bytearray()
        files_data = bytearray()
        for path, data in module_output_dict['files'].items():
            encoded_path = path.encode()
            files_info.extend(len(encoded_path).to_bytes(4, 'big'))
            files_info.extend(encoded_path)
            files_info.extend(len(data).to_bytes(8, 'big'))

            files_data.extend(data)

        bbf_data.extend(len(files_info).to_bytes(8, 'big'))
        bbf_data.extend(len(files_data).to_bytes(8, 'big'))

        bbf_data.extend(module_output_dict['exit_code'].to_bytes(2, 'big'))
        bbf_data.extend(module_output_dict['stdout'])
        bbf_data.extend(module_output_dict['stderr'])
        bbf_data.extend(files_info)
        bbf_data.extend(files_data)

        return bbf_data
