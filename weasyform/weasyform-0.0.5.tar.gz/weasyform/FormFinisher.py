import pydyf
from typing import Callable
from .WeasyForm import WeasyForm
from weasyform import Document
from weasyprint.document import Matrix


from .fields.signature import Signature


class FormFinisher:
    def __init__(self, inject_empty_cryptographic_signature: bool = False):
        self.inject_empty_cryptographic_signature = inject_empty_cryptographic_signature

    def __call__(self, pdf_document: Document, pdf: pydyf.PDF):
        weasy_form = WeasyForm(pdf)

        for page in pdf_document.pages:
            for form_element in page.form_elements:
                element_type, element_name, rectangle = form_element
                if element_type == 'signature':
                    zoom = 1
                    scale = zoom * 0.75
                    matrix = Matrix(scale, 0, 0, -scale, 0, page.height * scale)
                    x1, y1 = matrix.transform_point(*rectangle[:2])
                    x2, y2 = matrix.transform_point(*rectangle[2:])

                    signature = Signature.add_field(
                        weasy_form,
                        signature_field_name=element_name,
                        signature_box=(x1, y1, x2, y2)
                    )

                    if self.inject_empty_cryptographic_signature:
                        form_signature = weasy_form.append_empty_cryptographic_signature()

                        signature.update({
                            'V': form_signature.reference
                        })

