"""
This is intended to serve as an interface for File Transformations. 
Specifically for attributes that are intended for use with a web UI.
We can then use a standard template and inject details from the 
specific transformation as we know the methods and properties available.
"""
from abc import ABC, abstractmethod, abstractproperty
from dataclasses import dataclass, field
import os
from typing import List, Optional

from igi_file_transformation_contract.result import TransformationResult


class IFileTransformer(ABC):
    """
    Base class for IGI File Transformers. Acts as an interface/contract.

    Please note this interface specifies requirements for use in a web service.
    Additional methods e.g. for console use can be included in sub-classes, but
    are not required to implement this interface.
    """

    @abstractproperty
    def title(self) -> str:
        pass

    @abstractproperty
    def user_description(self) -> str:
        """
        A user friendly description of the task that can be displayed on the webpage.
        """
        pass

    @abstractmethod
    def try_transform_file(self, in_path: str, out_path: str, **kwargs) -> TransformationResult:
        pass

    @abstractmethod
    def transform_file(self, in_path: str, out_path: str, **kwargs) -> str:
        pass

    @abstractproperty
    def result_disclaimer(self) -> str:
        """
        Advice on what to check in output etc.
        """
        pass

    @abstractproperty
    def accepts_file_extensions(self) -> List[str]:
        """ 
        A list of specific extensions supported e.g. ['.xlsx', '.xls', ...].
        Note: the web service will return an error if you try to upload a file 
        that is not in this list of extensions.
        """
        pass

    # subclasses not *required* to override @property members, but can
    @property
    def target_file_ext(self) -> str:
        """
        Extention for target output file - any overrides should include the . prefix
        """
        return '.xlsx'

    @property
    def user_description_image_uri(self) -> Optional[str]:
        """
        Optional image uri to be displayed with user description.
        """
        return None

    @property
    def result_disclaimer_image_uri(self) -> Optional[str]:
        """
        Optional image uri to be displayed with result disclaimer.
        """
        return None

    @property
    def tile_image_uri(self) -> Optional[str]:
        """
        Optional image uri to be displayed if services are listed as tiles.
        """
        return None

    def has_user_description_image(self) -> bool:
        return bool(self.user_description_image_uri)

    def has_result_disclaimer_image(self) -> bool:
        return bool(self.result_disclaimer_image_uri)

    def has_tile_image(self) -> bool:
        return bool(self.tile_image_uri)

    def get_default_output_path(self, in_path, suffix: str='_transformed') -> str:
        directory, filename = os.path.split(in_path)
        output_filename = self.get_default_output_filename(filename, suffix)
        return os.path.join(directory, output_filename)

    def get_default_output_filename(self, in_fname: str, suffix: str='_transformed') -> str:
        base_name, _ = os.path.splitext(in_fname)
        out_fname = f"{base_name}{suffix}{self.target_file_ext}"
        return out_fname


@dataclass
class ExtChecker:
    """
    Determines whether the ext of the filename (or path) is accepted.
    the allow_zips arg allows you to return true for '.zip' even if not
    in the accepted list. Use if you will check the unzipped file exts
    are supported before processing.
    """
    transformer: IFileTransformer
    file_name_or_path: str
    allow_zips: bool
    accept_exts: List[str] = field(init=False)
    ext_is_valid: bool = field(init=False)
    file_ext: str = field(init=False)

    def __post_init__(self):
        self.update_for_file()

    def update_for_file(self, filename: str = None):
        if filename:
            self.file_name_or_path = filename
        self.file_ext = os.path.splitext(self.file_name_or_path)[-1].lower()
        self.accept_exts = [e.lower() for e in 
                            self.transformer.accepts_file_extensions]
        if self.allow_zips:
            self.accept_exts = sorted(list(set(self.accept_exts + ['.zip'])))
        self.ext_is_valid = self.file_ext in self.accept_exts
