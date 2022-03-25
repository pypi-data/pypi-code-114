# coding: utf-8
# *****************************************************************************
# Copyright © NEC Corporation 2020. All rights reserved.
# This source code or any portion thereof must not be
# reproduced or used in any manner whatsoever.
# *****************************************************************************
# *****************************************************************************
# Python and this documentation is:
# Copyright © 2001-2020 Python Software Foundation. All rights reserved.
# Copyright © 2000 BeOpen.com. All rights reserved.
# Copyright © 1995-2000 Corporation for National Research Initiatives.
#             All rights reserved.
# Copyright © 1991-1995 Stichting Mathematisch Centrum. All rights reserved.
# *****************************************************************************

import json
import requests
from urllib.request import urlopen, Request
from lxml import etree
from OpeIdEcpModule import ecp_xslt_flagument


class EcpSessionService(object):
    """
    Ecpセッションサービス
    """

    def get_ecp_session(self, ecp_session_info):
        """ECPセッションを生成する

        Parameters
        ----------

        Returns
        -------
        session : dict
            shib_idp_session
            shibsession

        """

        # IDPサーバのサーバ証明書　ファイルバス＋証明書ファイル名
        idp_ser_cer_file_name = ecp_session_info.idp_ser_cer_file_name
        # クライアントの証明書　ファイルバス＋証明書ファイル名
        cli_cer_file_name = ecp_session_info.cli_cer_file_name
        # クライアントの秘密鍵
        cli_cer_file_key = ecp_session_info.cli_cer_file_key

        try:
            # SPへリクエスト
            sp_requests = setup_sp_requests(ecp_session_info.sp_request_url)

            with urlopen(
                    sp_requests, data=json.dumps({}).encode()
            ) as sp_res:
                body = sp_res.read().decode()
                # XSLT
                body_doc = etree.XML(body.strip())

                idp_req_xslt = etree.XSLT(
                    etree.XML(ecp_xslt_flagument.idp_request_xslt.encode())
                )
                idp_request_doc = idp_req_xslt(body_doc)

                relay_state_xslt = etree.XSLT(
                    etree.XML(ecp_xslt_flagument.relay_state_xslt.encode())
                )
                relay_state_doc = relay_state_xslt(body_doc)

            # IDPへリクエスト
            idp_req = setup_idp_requests(
                ecp_session_info.idp_request_url,
                idp_request_doc,
                cli_cer_file_name,
                cli_cer_file_key,
                idp_ser_cer_file_name,
            )

            shib_idp_session = idp_req.cookies.get_dict()["shib_idp_session"]

            body = str(idp_req.text)
            body_doc = etree.XML(body.encode())
            consumer_servise_doc = etree.XML(
                ecp_xslt_flagument.assertion_consumer_service_url_xlst.encode()
            )
            consumer_service_xslt = etree.XSLT(consumer_servise_doc)
            consumer_service_url = str(consumer_service_xslt(body_doc)).strip()

            sp_package_xslt = etree.XSLT(
                etree.XML(
                    ecp_xslt_flagument.sp_package_xslt.format(
                        str(relay_state_doc)
                    ).encode()
                )
            )
            sp_request_doc = sp_package_xslt(body_doc)

            # assertionConsumerServiceUrlへリクエスト
            assert_consumer_service_req = setup_assert_consumer_service_requests(
                shib_idp_session,
                consumer_service_url,
                sp_request_doc,
            )

            req_dict = assert_consumer_service_req.cookies.get_dict()

            s = "_shibsession"
            for d_key in req_dict:
                if s in d_key:
                    shibsession_key = d_key
                    shibsession_val = (
                        assert_consumer_service_req
                    ).cookies.get_dict()[d_key]
                    break

        except Exception as exception:
            raise exception

        return {
            "shib_idp_session": shib_idp_session,
            shibsession_key: shibsession_val,
        }


def setup_sp_requests(sp_request_url):
    req = Request(sp_request_url, method="POST")
    req.add_header("Accept", "application/vnd.paos+xml")
    req.add_header("User-Agent", "EOP")
    req.add_header(
        "PAOS",
        (
            'ver="urn:liberty:paos:2003-08";'
            '"urn:oasis:names:tc:SAML:2.0:profiles:SSO:ecp"'
        ),
    )

    return req


def setup_idp_requests(
        idp_request_url, idp_request_doc, cli_cer_file_name, cli_cer_file_key, idp_ser_cer_file_name
):
    headers = {
        "Accept": "*/*",
        "User-Agent": "EOP",
        "Content-Type": "text/xml; charset=utf-8",
    }

    req = requests.post(
        idp_request_url,
        data=str(idp_request_doc),
        headers=headers,
        verify=idp_ser_cer_file_name,
        cert=(
            cli_cer_file_name,
            cli_cer_file_key,
        ),
    )

    return req


def setup_assert_consumer_service_requests(
        shib_idp_session,
        consumer_service_url,
        sp_request_doc,
):
    headers = {
        "User-Agent": "EOP",
        "Content-Type": "text/html; application/vnd.paos+xml",
    }

    cookie = {"shib_idp_session": shib_idp_session}

    req = requests.post(
        consumer_service_url.strip(),
        data=str(sp_request_doc),
        headers=headers,
        cookies=cookie,
        allow_redirects=False,
    )

    return req


