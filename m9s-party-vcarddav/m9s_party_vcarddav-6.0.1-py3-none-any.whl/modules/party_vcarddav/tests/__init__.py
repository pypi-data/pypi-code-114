# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.

try:
    from trytond.modules.party_vcarddav.tests.test_party_vcarddav import suite
except ImportError:
    from .test_party_vcarddav import suite

__all__ = ['suite']
