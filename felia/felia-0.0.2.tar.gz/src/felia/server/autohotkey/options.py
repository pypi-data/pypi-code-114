from django.conf import settings

from server.autohotkey.constant import Mode_Include

DEFAULT_NAMES = (
    'verbose_name',
    'mode',
    'help_text',
)


class Options:
    """Meta, AHK属性选项"""
    def __init__(self, meta):
        self.meta = meta
        self.local_cmds = []

        # 附加选项
        self.verbose_name = None
        self.mode = None
        self.help_text = None

        self.base_dir = settings.BASE_DIR / 'autohotkey' / 'bin'

    def add_field(self, field):
        self.local_cmds.append(field)

    def contribute_to_class(self, cls, name):
        from django.db.models.options import camel_case_to_spaces
        cls._meta = self
        self.ahk = cls
        # First, construct the default values for these options.
        self.object_name = cls.__name__
        self.cmd_name = self.object_name.lower()
        self.verbose_name = camel_case_to_spaces(self.object_name)
        self.mode = Mode_Include

        # Store the original user-defined values for each option,
        # for use when serializing the model definition
        self.original_attrs = {}

        # 下一步, 从'class Meta'处理任何重载的值。
        if self.meta:
            meta_attrs = self.meta.__dict__.copy()
            for name in self.meta.__dict__:
                # Ignore any private attributes that Django doesn't care about.
                # NOTE: We can't modify a dictionary's contents while looping
                # over it, so we loop over the *original* dictionary instead.
                if name.startswith('_'):
                    del meta_attrs[name]
            for attr_name in DEFAULT_NAMES:
                if attr_name in meta_attrs:
                    setattr(self, attr_name, meta_attrs.pop(attr_name))
                    self.original_attrs[attr_name] = getattr(self, attr_name)
                elif hasattr(self.meta, attr_name):
                    setattr(self, attr_name, getattr(self.meta, attr_name))
                    self.original_attrs[attr_name] = getattr(self, attr_name)

        del self.meta
