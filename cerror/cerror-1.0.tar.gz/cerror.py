from __future__ import annotations

__version__ = '1.0' # type: ignore
__all__ = [         # type: ignore
    '__version__',
    'error',
    'warning',
    'annotations',
    'ModuleError',
    'ModuleWarning',
    'TypeWarning',
    'NameWarning',
    'VersionWarning',
    'NonetypeWarning',
    'AttributeWarning',
    'IteratorWarning',
    'IteratorError',
    'JsonDecoderWarning',
    'JsonEncoderWarning',
    'ConfigParserWarning',
    'ConfigParserError',
    'DecoratorWarning',
    'DecoratorError',
    'NonetypeAttributeWarning',
    'AnnotationWarning',
    'AnnotationError',
    'CoroutineError',
    'CoroutineWarning',
    'PrintWarning',
    'PrintError',
    'DictUpdateError',
    'DictUpdateWarning',
    'ConstantUpdateError',
    'ConstantUpdateWarning',
    'ArgumentError',
    'ArgumentWarning',
    'FunctionError',
    'FunctionWarning',
    'CodeError',
    'CodeWarning',
    'ZipFileError',
    'ZipFileWarning',
    'NamedTupleError',
    'NamedTupleWarning',
    'NotFoundError',
    'NotFoundWarning',
    'VariableError',
    'VariableWarning',
    'PackageError',
    'PackageWarning',
    'TypedDictError',
    'TypedDictWarning',
    'LimitedError',
    'LimitedWarning',
    'TarFileError',
    'TarFileWarning',
    'ObjectWarning',
    'ObjectError',
    'SequenceUpdateError',
    'SequenceUpdateWarning',
    'CallError',
    'CallWarning'
]

def error(cause: str | type[Exception] | type[BaseException], message: str = ...) -> type[Exception] | type[BaseException]:
    if isinstance(cause, (type, Exception, BaseException)):
        cause = cause.__name__
    
    return type(cause, (Exception, BaseException), {'message': message if message is not ... else None, '__init__': Exception.__init__})

def warning(cause: str | type[Warning], *, message: str = ...) -> type[Warning]:
    if isinstance(cause, (type, Warning)):
        cause = cause.__name__

    return type(cause, (Warning, ), {'message': message if message is not ... else None, '__init__': Warning.__init__})

ModuleError = error('ModuleError')
ModuleWarning = warning('ModuleWarning')
TypeWarning = warning('TypeWarning')
NameWarning = warning('NameWarning')
VersionWarning = warning('VersionWarning')
NonetypeWarning = warning('NonetypeWarning')
AttributeWarning = warning('AttributeWarning')
IteratorWarning = warning('IteratorWarning')
IteratorError = error('IteratorError')
JsonDecoderWarning = warning('JsonDecoderWarning')
JsonEncoderWarning = warning('JsonEncoderWarning')
ConfigParserWarning = warning('ConfigParserWarning')
ConfigParserError = error('ConfigParserError')
DecoratorWarning = warning('DecoratorWarning')
DecoratorError = error('DecoratorError')
NonetypeAttributeWarning = warning('NonetypeAttributeWarning')
AnnotationWarning = warning('AnnotationWarning')
AnnotationError = error('AnnotationError')
CoroutineError = error('CoroutineError')
CoroutineWarning = warning('CouroutineWarning')
PrintWarning = error('PrintWarning')
PrintError = error('PrintError')
DictUpdateError = error('DictUpdateError')
DictUpdateWarning = warning('DictUpdateWarning')
ConstantUpdateError = error('ConstantUpdateError')
ConstantUpdateWarning = warning('ConstantUpdateWarning')
ArgumentError = error('ArgumentError')
ArgumentWarning = warning('ArgumentWarning')
FunctionError = error('FunctionError')
FunctionWarning = warning('FunctionWarning')
CodeError = error('CodeError')
CodeWarning = warning('CodeWarning')
ZipFileError = error('ZipFileError')
ZipFileWarning = warning('ZipFileWarning')
NamedTupleError = warning('NamedTupleError')
NamedTupleWarning = warning('NamedTupleWarning')
NotFoundError = error('NotFoundError')
NotFoundWarning = warning('NotFoundWarning')
VariableError = error('VariableError')
VariableWarning = warning('VariableWarning')
PackageError = error('PackageError')
PackageWarning = warning('PackageWarning')
TypedDictError = error('TypedDictError')
TypedDictWarning = warning('TypedDictWarning')
LimitedError = error('LimitedError')
LimitedWarning = warning('LimitedWarning')
TarFileError = error('TarFileError')
TarFileWarning = warning('TarFileWarning')
ObjectWarning = warning('ObjectWarning')
ObjectError = error('ObjectError')
SequenceUpdateError = error('SequenceUpdateError')
SequenceUpdateWarning = warning('SequenceUpdateWarning')
CallError = error('CallError')
CallWarning = warning('CallWarning')

# for _global in list(globals().keys()):
#    if not _global.startswith('__') or _global == '__version__':
#        __all__.append(_global)

# import pprint
# pprint.pprint(__all__, indent=4)