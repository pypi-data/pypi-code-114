from django.core.files import File as DjangoFile


class File:
    def __init__(self, path):
        self.path = path
        self.validate()

    @property
    def filename(self):
        return self.path.split('/')[-1]

    @property
    def prefix(self):
        return self.filename.split('.')[0]

    @property
    def suffix(self):
        if len(self.filename.split('.')) >= 2:
            return self.filename.split('.')[-1]
        return ''

    @property
    def identifier(self):
        """ File or Category name """
        return self.prefix.split('_')[0]

    @property
    def image_nr(self):
        if len(self.prefix.split('_')) >= 2:
            return self.prefix.split('_')[-1]
        return ''

    def validate(self):
        assert str(self) == self.filename

    def get_django_file(self):
        return DjangoFile(file=open(self.path, 'rb'), name=self.filename)

    def get_siblings(self, files):
        siblings = []
        for file in files:
            if file.identifier == self.identifier:
                siblings.append(file)
        return siblings

    def __str__(self):
        return '{}{}{}{}{}'.format(
            self.identifier,
            '_' if self.image_nr else '',
            self.image_nr,
            '.' if self.suffix else '',
            self.suffix,
        )
