import io
import pydyf
import shutil
import datetime
from typing import List


class WeasyForm:

    def __init__(self, pdf: pydyf.PDF):
        self.pdf = pdf
        self.catalog = pdf.catalog

    def get_pages(self):
        page_objects = list(filter(lambda _object: isinstance(_object, pydyf.Dictionary) and _object.get('Type') == '/Page', self.pdf.objects))
        pages = {}
        for index, page_object in enumerate(page_objects):
            pages[index] = page_object

        return pages

    def get_signatures(self):
        signature_objects = list(filter(lambda _object: isinstance(_object, pydyf.Dictionary) and _object.get('Type') == '/Sig', self.pdf.objects))
        signatures = {}
        for signature_object in signature_objects:
            signatures[signature_object.reference] = signature_object

        return signatures

    def find_page(self, page_number: int) -> pydyf.Dictionary:
        return self.get_pages()[page_number]

    def find_form_fields(self, field_type: str, field_title: str = None) -> List[pydyf.Dictionary]:
        def _form_field_filter(_object: pydyf.Object):

            if not isinstance(_object, pydyf.Dictionary):
                return False

            if _object.get('FT') != field_type:
                return False

            if field_title and pydyf.String(field_title).data != _object.get('T').data:
                return False

            return True

        return list(filter(_form_field_filter, self.pdf.objects))

    def register_annotation(self, page_object: pydyf.Dictionary, annotation_object: pydyf.Dictionary) -> None:
        found_annots = page_object.get('Annots')
        if found_annots:
            found_annots.extend(annotation_object.reference)
        else:
            annots = pydyf.Dictionary({
                'Annots': pydyf.Array([annotation_object.reference])
            })

            page_object.update(annots)

    def add_object(self, object_) -> None:
        self.pdf.add_object(object_)

    def append_empty_cryptographic_signature(self):
        signature_max_length = 16384 * 2
        date = datetime.datetime.utcnow()
        date = date.strftime('%Y%m%d%H%M%S+00\'00\'')
        form_signature = pydyf.Dictionary({
            'Type': '/Sig',
            'Filter': '/Adobe.PPKLite',
            'SubFilter': '/ETSI.CAdES.detached',
            'ByteRange[0 ********** ********** **********]': '/M(D:{date})'.format(date=date),
            #'Contents<{zeros}>'.format(zeros='0' * signature_max_length): ''
        })

        self.pdf.add_object(form_signature)

        return form_signature

    def write(self, target: str = None):
        file_obj = io.BytesIO()
        self.pdf.write(file_obj)
        if target is None:
            return file_obj.getvalue()
        else:
            file_obj.seek(0)
            if hasattr(target, 'write'):
                shutil.copyfileobj(file_obj, target)
            else:
                with open(target, 'wb') as fd:
                    shutil.copyfileobj(file_obj, fd)
