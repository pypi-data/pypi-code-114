class EcpSessionInfo(object):
    """
    環境変数


    idp_ser_cer_file_name: 必須
    idp_cli_cer_file_name: 必須
    idp_cli_cer_file_key: 必須
    sp_request_url: 必須
    idp_request_url: 必須


    """

    def __init__(self,
                 idp_ser_cer_file_name=None,
                 cli_cer_file_name=None,
                 cli_cer_file_key=None,
                 sp_request_url=None,
                 idp_request_url=None
                 ):
        self.idp_ser_cer_file_name = idp_ser_cer_file_name
        self.sp_request_url = sp_request_url
        self.idp_request_url = idp_request_url
        self.cli_cer_file_name = cli_cer_file_name
        self.cli_cer_file_key = cli_cer_file_key
