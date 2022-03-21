from typing import Tuple, TYPE_CHECKING
import pydyf
from ..exceptions import SignatureException, PdfException

if TYPE_CHECKING:
    from ..WeasyForm import WeasyForm


class SignatureFormField(pydyf.Dictionary):
    def __init__(self, field_name: str, on_page: pydyf.Dictionary = None, box: pydyf.Array = None, annotation_flag: int = 132):
        rect = box if box else pydyf.Array([0, 0, 0, 0])

        data = {
            'FT': '/Sig',
            'T': pydyf.String(field_name),
            'Type': '/Annot',
            'Subtype': '/Widget',
            'F': annotation_flag,
            'Rect': rect,
        }

        if on_page:
            data['P'] = on_page.reference

        super(SignatureFormField, self).__init__(data)


class Signature:
    def __init__(self,
                 signer_pdf: 'WeasyForm',
                 signature_field_name: str,
                 on_page_number: int = 0,
                 signature_box: Tuple[int, int, int, int] = None,
                 ):
        self.signer_pdf = signer_pdf
        self.signature_field_name = signature_field_name
        self.signature_box = signature_box

        self.page_object = signer_pdf.find_page(on_page_number)

    def create_signature_field(self, signature_field_has_to_exists: bool = False) -> pydyf.Dictionary:
        acro_form = self.signer_pdf.catalog.get('AcroForm')
        if acro_form:
            fields = acro_form.get('Fields')
            if fields is None:
                raise PdfException('Mangled PDF: /Fields are missing in /AcroForm')
            form_field_signatures = [field for field in fields]

            found_suitable_signature_field = None
            for found_signature_field in self.signer_pdf.find_form_fields('/Sig', self.signature_field_name):
                # is registered in Fields?
                if found_signature_field.reference not in form_field_signatures:
                    continue

                # What is here is our sig field
                # Check if it is not already signed
                has_value = found_signature_field.get('V')
                if has_value:
                    raise SignatureException('Requested /Sig field with name {} is already filled.'.format(self.signature_field_name))

                found_suitable_signature_field = found_signature_field

            if not found_suitable_signature_field and signature_field_has_to_exists:
                raise SignatureException('Requested required /Sig field with name {} Was not found.'.format(self.signature_field_name))

            if found_suitable_signature_field:
                return found_suitable_signature_field
        else:
            # Create AcroForm
            fields = pydyf.Array([])
            acro_form = pydyf.Dictionary({
                'AcroForm': pydyf.Dictionary({
                    'Fields': fields
                })
            })

            self.signer_pdf.catalog.update(acro_form)

        signature_field = SignatureFormField(
            self.signature_field_name,
            self.page_object,
            pydyf.Array([i for i in self.signature_box])
        )

        self.signer_pdf.add_object(signature_field)

        fields.append(signature_field.reference)

        self.signer_pdf.register_annotation(self.page_object, signature_field)

        return signature_field

    def set_signature_flags(self, flag: int = 3):
        acro_form = self.signer_pdf.catalog.get('AcroForm')
        acro_form.update(pydyf.Dictionary({
            'SigFlags': flag
        }))

    def create_visible_signature_box(self, signature_field: pydyf.Dictionary, display: bool = True):
        llx, lly, urx, ury = self.signature_box
        w = abs(urx - llx)
        h = abs(ury - lly)
        if w and h:
            ap_dict = pydyf.Dictionary()
            if display:
                ap_stream = pydyf.Stream([], {
                    'BBox': pydyf.Array([0, h, w, 0]),
                    'Resources': pydyf.Dictionary(),
                    'Type': '/XObject',
                    'Subtype': '/Form',
                })
                ap_stream.push_state()

                # Background
                ap_stream.push_state()
                ap_stream.set_color_rgb('0.95', '0.95', '0.95')
                ap_stream.rectangle(0, 0, w, h)
                ap_stream.fill()
                ap_stream.pop_state()

                # Border
                ap_stream.set_line_width('0.5')
                ap_stream.rectangle(0, 0, w, h)
                ap_stream.stroke()
                ap_stream.pop_state()

            else:
                ap_stream = pydyf.Stream([], {
                    'BBox': pydyf.Array([0, h, w, 0]),
                    'Resources': pydyf.Dictionary(),
                    'Type': '/XObject',
                    'Subtype': '/Form',
                })

            self.signer_pdf.add_object(ap_stream)
            ap_dict['N'] = ap_stream.reference

            signature_field['AP'] = ap_dict

    @staticmethod
    def add_field(
            signer_pdf: 'WeasyForm',
            signature_field_name: str,
            on_page_number: int = 0,
            signature_box: Tuple[int, int, int, int] = None,
            is_signature_visible: bool = True,
            signature_field_has_to_exists: bool = False
    ) -> pydyf.Dictionary:
        signature = Signature(
            signer_pdf,
            signature_field_name=signature_field_name,
            on_page_number=on_page_number,
            signature_box=signature_box,
        )

        signature_field = signature.create_signature_field(signature_field_has_to_exists)
        signature.set_signature_flags()

        if signature_box:
            signature.create_visible_signature_box(signature_field, is_signature_visible)

        return signature_field

