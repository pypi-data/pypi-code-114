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
"""
XSLTフラグメント
"""

# ShibbolethからのレスポンスXMLからデータを抽出するXSLTフラグメント
consumer_url_xslt = """
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:ecp="urn:oasis:names:tc:SAML:2.0:profiles:SSO:ecp" xmlns:S="http://schemas.xmlsoap.org/soap/envelope/" xmlns:paos="urn:liberty:paos:2003-08">
 <xsl:output omit-xml-declaration="yes"/>
 <xsl:template match="/">
     <xsl:value-of select="/S:Envelope/S:Header/paos:Request/@responseConsumerURL" />
 </xsl:template>
</xsl:stylesheet>
""".strip()

relay_state_xslt = """
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:ecp="urn:oasis:names:tc:SAML:2.0:profiles:SSO:ecp" xmlns:S="http://schemas.xmlsoap.org/soap/envelope/">
 <xsl:output omit-xml-declaration="yes"/>
 <xsl:template match="/">
     <xsl:copy-of select="//ecp:RelayState" />
 </xsl:template>
</xsl:stylesheet>
""".strip()

idp_request_xslt = """
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:S="http://schemas.xmlsoap.org/soap/envelope/">
 <xsl:output omit-xml-declaration="yes"/>
    <xsl:template match="node()|@*">
      <xsl:copy>
         <xsl:apply-templates select="node()|@*"/>
      </xsl:copy>
    </xsl:template>
    <xsl:template match="S:Header" />
</xsl:stylesheet>
""".strip()

assertion_consumer_service_url_xlst = """
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:ecp="urn:oasis:names:tc:SAML:2.0:profiles:SSO:ecp" xmlns:S="http://schemas.xmlsoap.org/soap/envelope/">
 <xsl:output omit-xml-declaration="yes"/>
 <xsl:template match="/">
     <xsl:value-of select="S:Envelope/S:Header/ecp:Response/@AssertionConsumerServiceURL" />
 </xsl:template>
</xsl:stylesheet>
""".strip()

sp_package_xslt = """
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:soap11="http://schemas.xmlsoap.org/soap/envelope/">
 <xsl:output omit-xml-declaration="no" encoding="UTF-8"/>
    <xsl:template match="node()|@*">
      <xsl:copy>
         <xsl:apply-templates select="node()|@*"/>
      </xsl:copy>
    </xsl:template>
    <xsl:template match="soap11:Header">
      <soap11:Header>{}</soap11:Header>
    </xsl:template>
</xsl:stylesheet>
""".strip()
