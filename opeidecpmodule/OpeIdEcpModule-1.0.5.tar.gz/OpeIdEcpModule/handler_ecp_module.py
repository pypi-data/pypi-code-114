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
import logging
import os
from OpeIdEcpModule.services.ecp_session_service import EcpSessionService

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def ecp_module_handler(ecp_session_info):
    """ECPセッションを生成する

    shib_idp_session、_shibsessionを取得する
    """
    logger.info("### START ECP SESSION SERVICE ###")
    ecp_session_service = EcpSessionService()
    try:
        if ecp_session_info.idp_ser_cer_file_name is None or ecp_session_info.idp_ser_cer_file_name == "":
            raise Exception("idp_ser_cer_file_name is an empty string or none")
        if not os.path.exists(ecp_session_info.idp_ser_cer_file_name):
            raise Exception(ecp_session_info.idp_ser_cer_file_name + " does not exist")

        if ecp_session_info.cli_cer_file_name is None or ecp_session_info.cli_cer_file_name == "":
            raise Exception("cli_cer_file_name is an empty string or none")
        if not os.path.exists(ecp_session_info.cli_cer_file_name):
            raise Exception(ecp_session_info.cli_cer_file_name + " does not exist")

        if ecp_session_info.cli_cer_file_key is None or ecp_session_info.cli_cer_file_key == "":
            raise Exception("cli_cer_file_key is an empty string or none")
        if not os.path.exists(ecp_session_info.cli_cer_file_key):
            raise Exception(ecp_session_info.cli_cer_file_key + " does not exist")

        if ecp_session_info.idp_request_url is None or ecp_session_info.idp_request_url == "":
            raise Exception("idp_request_url is an empty string or none")

        if ecp_session_info.sp_request_url is None or ecp_session_info.sp_request_url == "":
            raise Exception("sp_request_url is an empty string or none")

        session = ecp_session_service.get_ecp_session(ecp_session_info)
    except Exception as exception:
        res = {
            "error_code": "ECP_E_0001",
            "error_message": str(exception)
        }
        logger.info("### END ECP SESSION SERVICE ###")
        return res
    
    return session
