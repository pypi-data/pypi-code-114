# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
import uuid

import vobject

from trytond import __version__
from trytond.model import Unique, fields
from trytond.pool import Pool, PoolMeta
from trytond.report import Report


class Party(metaclass=PoolMeta):
    __name__ = 'party.party'
    uuid = fields.Char('UUID', required=True,
            help='Universally Unique Identifier')
    vcard = fields.Binary('VCard')

    @classmethod
    def __setup__(cls):
        super(Party, cls).__setup__()
        t = cls.__table__()
        cls._sql_constraints += [
            ('uuid_uniq', Unique(t, t.uuid),
                'The UUID of the party must be unique.'),
            ]

    @staticmethod
    def default_uuid():
        return str(uuid.uuid4())

    @classmethod
    def create(cls, vlist):
        Collection = Pool().get('webdav.collection')

        parties = super(Party, cls).create(vlist)
        # Restart the cache for vcard
        Collection._vcard_cache.clear()
        return parties

    @classmethod
    def copy(cls, parties, default=None):
        if default is None:
            default = {}
        new_parties = []
        for party in parties:
            current_default = default.copy()
            current_default['uuid'] = cls.default_uuid()
            current_default['vcard'] = None
            new_party, = super(Party, cls).copy([party],
                default=current_default)
            new_parties.append(new_party)
        return new_parties

    @classmethod
    def write(cls, parties, values, *args):
        Collection = Pool().get('webdav.collection')

        super(Party, cls).write(parties, values, *args)
        # Restart the cache for vcard
        Collection._vcard_cache.clear()

    @classmethod
    def delete(cls, parties):
        Collection = Pool().get('webdav.collection')

        super(Party, cls).delete(parties)
        # Restart the cache for vcard
        Collection._vcard_cache.clear()

    def vcard2values(self, vcard):
        '''
        Convert vcard to values for create or write
        '''
        Address = Pool().get('party.address')

        res = {}
        res['name'] = vcard.fn.value
        if not hasattr(vcard, 'n'):
            vcard.add('n')
            vcard.n.value = vobject.vcard.Name(vcard.fn.value)
        res['vcard'] = vcard.serialize()
        if not self.id:
            if hasattr(vcard, 'uid'):
                res['uuid'] = vcard.uid.value
            res['addresses'] = []
            to_create = []
            for adr in vcard.contents.get('adr', []):
                vals = Address.vcard2values(adr)
                to_create.append(vals)
            if to_create:
                res['addresses'].append(('create', to_create))
            res['contact_mechanisms'] = []
            to_create = []
            for email in vcard.contents.get('email', []):
                vals = {}
                vals['type'] = 'email'
                vals['value'] = email.value
                to_create.append(vals)
            if to_create:
                res['contact_mechanisms'].append(('create', to_create))
            to_create = []
            for tel in vcard.contents.get('tel', []):
                vals = {}
                vals['type'] = 'phone'
                if hasattr(tel, 'type_param') \
                        and 'cell' in tel.type_param.lower():
                    vals['type'] = 'mobile'
                vals['value'] = tel.value
                to_create.append(vals)
            if to_create:
                res['contact_mechanisms'].append(('create', to_create))
        else:
            i = 0
            res['addresses'] = []
            addresses_todelete = []
            for address in self.addresses:
                try:
                    adr = vcard.contents.get('adr', [])[i]
                except IndexError:
                    addresses_todelete.append(address.id)
                    i += 1
                    continue
                if not hasattr(adr, 'value'):
                    addresses_todelete.append(address.id)
                    i += 1
                    continue
                vals = Address.vcard2values(adr)
                res['addresses'].append(('write', [address.id], vals))
                i += 1
            if addresses_todelete:
                res['addresses'].append(('delete', addresses_todelete))
            try:
                new_addresses = vcard.contents.get('adr', [])[i:]
            except IndexError:
                new_addresses = []
            to_create = []
            for adr in new_addresses:
                if not hasattr(adr, 'value'):
                    continue
                vals = Address.vcard2values(adr)
                to_create.append(vals)
            if to_create:
                res['addresses'].append(('create', to_create))

            i = 0
            res['contact_mechanisms'] = []
            contact_mechanisms_todelete = []
            for cm in self.contact_mechanisms:
                if cm.type != 'email':
                    continue
                try:
                    email = vcard.contents.get('email', [])[i]
                except IndexError:
                    contact_mechanisms_todelete.append(cm.id)
                    i += 1
                    continue
                vals = {}
                vals['value'] = email.value
                res['contact_mechanisms'].append(('write', [cm.id], vals))
                i += 1
            try:
                new_emails = vcard.contents.get('email', [])[i:]
            except IndexError:
                new_emails = []
            to_create = []
            for email in new_emails:
                if not hasattr(email, 'value'):
                    continue
                vals = {}
                vals['type'] = 'email'
                vals['value'] = email.value
                to_create.append(vals)
            if to_create:
                res['contact_mechanisms'].append(('create', to_create))

            i = 0
            for cm in self.contact_mechanisms:
                if cm.type not in ('phone', 'mobile'):
                    continue
                try:
                    tel = vcard.contents.get('tel', [])[i]
                except IndexError:
                    contact_mechanisms_todelete.append(cm.id)
                    i += 1
                    continue
                vals = {}
                vals['value'] = tel.value
                res['contact_mechanisms'].append(('write', [cm.id], vals))
                i += 1
            try:
                new_tels = vcard.contents.get('tel', [])[i:]
            except IndexError:
                new_tels = []
            to_create = []
            for tel in new_tels:
                if not hasattr(tel, 'value'):
                    continue
                vals = {}
                vals['type'] = 'phone'
                if hasattr(tel, 'type_param') \
                        and 'cell' in tel.type_param.lower():
                    vals['type'] = 'mobile'
                vals['value'] = tel.value
                to_create.append(vals)
            if to_create:
                res['contact_mechanisms'].append(('create', to_create))

            if contact_mechanisms_todelete:
                res['contact_mechanisms'].append(('delete',
                    contact_mechanisms_todelete))
        return res


class Address(metaclass=PoolMeta):
    __name__ = 'party.address'

    def vcard2values(self, adr):
        '''
        Convert adr from vcard to values for create or write
        '''
        pool = Pool()
        Country = pool.get('country.country')
        Subdivision = pool.get('country.subdivision')

        vals = {}
        vals['street'] = adr.value.street or ''
        vals['city'] = adr.value.city or ''
        vals['postal_code'] = adr.value.code or ''
        if adr.value.country:
            countries = Country.search([
                    ('rec_name', '=', adr.value.country),
                    ], limit=1)
            if countries:
                country, = countries
                vals['country'] = country.id
                if adr.value.region:
                    subdivisions = Subdivision.search([
                            ('rec_name', '=', adr.value.region),
                            ('country', '=', country.id),
                            ], limit=1)
                    if subdivisions:
                        subdivision, = subdivisions
                        vals['subdivision'] = subdivision.id
        return vals


class ActionReport(metaclass=PoolMeta):
    __name__ = 'ir.action.report'

    @classmethod
    def __setup__(cls):
        super(ActionReport, cls).__setup__()
        new_ext = ('vcf', 'VCard file')
        if new_ext not in cls.extension.selection:
            cls.extension.selection.append(new_ext)


class VCard(Report):
    __name__ = 'party_vcarddav.party.vcard'

    @classmethod
    def render(cls, report, report_context):
        return ''.join(cls.create_vcard(party).serialize()
            for party in report_context['records'])

    @classmethod
    def convert(cls, report, data):
        return 'vcf', data

    @classmethod
    def create_vcard(cls, party):
        '''
        Return a vcard instance of vobject for the party
        '''
        if party.vcard:
            vcard = vobject.readOne(str(party.vcard))
        else:
            vcard = vobject.vCard()
        if not hasattr(vcard, 'n'):
            vcard.add('n')
        vcard.n.value = vobject.vcard.Name(party.full_name)
        if not hasattr(vcard, 'fn'):
            vcard.add('fn')
        vcard.fn.value = party.full_name
        if not hasattr(vcard, 'uid'):
            vcard.add('uid')
        vcard.uid.value = party.uuid
        if not hasattr(vcard, 'prodid'):
            vcard.add('prodid')
            vcard.prodid.value = ('-//m9s.biz//trytond-webdav %s//EN'
                % __version__)

        i = 0
        for address in party.addresses:
            try:
                adr = vcard.contents.get('adr', [])[i]
            except IndexError:
                adr = None
            if not adr:
                adr = vcard.add('adr')
            if not hasattr(adr, 'value'):
                adr.value = vobject.vcard.Address()
            adr.value.street = address.street and address.street + (
                address.name and (" / " + address.name) or '') or ''
            adr.value.city = address.city or ''
            if address.subdivision:
                adr.value.region = address.subdivision.name or ''
            adr.value.code = address.postal_code or ''
            if address.country:
                adr.value.country = address.country.name or ''
            i += 1
        try:
            older_addresses = vcard.contents.get('adr', [])[i:]
        except IndexError:
            older_addresses = []
        for adr in older_addresses:
            vcard.contents['adr'].remove(adr)

        email_count = 0
        tel_count = 0
        url_count = 0
        for cm in party.contact_mechanisms:
            if cm.type == 'email':
                try:
                    email = vcard.contents.get('email', [])[email_count]
                except IndexError:
                    email = None
                if not email:
                    email = vcard.add('email')
                email.value = cm.value
                if not hasattr(email, 'type_param'):
                    email.type_param = 'internet'
                elif 'internet' not in email.type_param.lower():
                    email.type_param += ',internet'
                email_count += 1
            elif cm.type in ('phone', 'mobile', 'fax'):
                try:
                    tel = vcard.contents.get('tel', [])[tel_count]
                except IndexError:
                    tel = None
                if not tel:
                    tel = vcard.add('tel')
                tel.value = cm.value
                if cm.type == 'mobile':
                    if not hasattr(tel, 'type_param'):
                        tel.type_param = 'cell'
                    elif 'cell' not in tel.type_param.lower():
                        tel.type_param += ',cell'
                elif cm.type == 'fax':
                    if not hasattr(tel, 'type_param'):
                        tel.type_param = 'fax'
                else:
                    if not hasattr(tel, 'type_param'):
                        tel.type_param = 'voice'
                tel_count += 1
            elif cm.type == 'website':
                try:
                    url = vcard.contents.get('url', [])[url_count]
                except IndexError:
                    url = None
                if not url:
                    url = vcard.add('url')
                url.value = cm.value
                url_count += 1

        try:
            older_emails = vcard.contents.get('email', [])[email_count:]
        except IndexError:
            older_emails = []
        for email in older_emails:
            vcard.contents['email'].remove(email)

        try:
            older_tels = vcard.contents.get('tel', [])[tel_count:]
        except IndexError:
            older_tels = []
        for tel in older_tels:
            vcard.contents['tel'].remove(tel)

        try:
            older_urls = vcard.contents.get('url', [])[url_count:]
        except IndexError:
            older_urls = []
        for url in older_urls:
            vcard.contents['url'].remove(url)
        # print(repr(vcard.serialize()))
        # vcard.prettyPrint()
        return vcard
