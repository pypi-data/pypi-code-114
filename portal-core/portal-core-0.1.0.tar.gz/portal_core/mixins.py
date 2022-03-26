import csv
import email.utils

from django.http import HttpResponse


class CsvResponseMixin(object):
    """ CSVダウンロード用 """
    filename = 'csvfile.csv'
    content_type = 'text/csv; charset=UTF-8'

    def get_filename(self):
        return self.filename

    def get_context_disposition(self):
        """ Get RFC 2231 formated Context Disposition """
        context_disposition = 'attachment; filename*='
        name = email.utils.encode_rfc2231(self.get_filename(), charset='UTF-8')
        return context_disposition + name

    def render_to_csv(self, data, fieldnames=None, with_bom=True,
                      fail_silent=True):
        response = HttpResponse(content_type=self.content_type)
        response['Content-Disposition'] = self.get_context_disposition()
        if with_bom:
            response.write('\ufeff')
        if fieldnames:
            writer = csv.DictWriter(
                response, fieldnames=fieldnames, quoting=csv.QUOTE_NONNUMERIC)
            writer.writeheader()
        else:
            writer = csv.writer(response, quoting=csv.QUOTE_NONNUMERIC)
        for row in data:
            try:
                writer.writerow(row)
            except:
                if fail_silent:
                    pass
                else:
                    raise
        return response
