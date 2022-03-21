import typing
from constructs import Construct
from aws_cdk import (
    CfnOutput,
    aws_route53,
    aws_certificatemanager
)


class DomainZone(Construct):
    conf: dict
    fqdn: str
    zone: aws_route53.IHostedZone
    records: dict=dict(
        a={},
        txt={},
        cname={},
        mx={},
        zone_delegation={}
    )

    def __init__(self, scope: Construct, id: str, *, fqdn: str, zone_id: str='', **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        self.fqdn = fqdn
        if zone_id:
            self.zone = aws_route53.HostedZone.from_hosted_zone_attributes(
                self,
                'zone',
                hosted_zone_id=zone_id,
                zone_name=fqdn
            )
        else:
            self.zone = aws_route53.HostedZone(
                self, 'zone',
                zone_name=fqdn
            )

    def txt(self, record_name: str, values: list):
        self.records['txt'][record_name] = aws_route53.TxtRecord(
            self, f"{record_name.replace('.', '-')}-txt",
            record_name=record_name,
            zone=self.zone,
            values=values
        )
        return self.records['txt'][record_name]
    
    def a(self, record_name: str, values: list):
        self.records['a'][record_name] = aws_route53.ARecord(
            self, f"{record_name.replace('.', '-')}-a",
            target=aws_route53.RecordTarget(values=values),
            zone=self.zone,
            record_name=record_name
        )
        return self.records['a'][record_name]

    def cname(self, record_name: str, domain_name: str):
        self.records['cname'][record_name] = aws_route53.CnameRecord(
            self, f"{record_name.replace('.', '-')}-cname",
            domain_name=domain_name,
            zone=self.zone,
            record_name=record_name
        )
        return self.records['cname'][record_name]

    def mx(self, record_name: str, values: list):
        mxvalues = []
        for mxv in values:
            mxvs = mxv.split(' ')
            mxvalues.append(
                aws_route53.MxRecordValue(host_name=mxvs[1], priority=int(mxvs[0]))
            )
        self.records['mx'][record_name] = aws_route53.MxRecord(
            self, f"{record_name.replace('.', '-')}-mx",
            values=mxvalues,
            zone=self.zone,
            record_name=record_name
        )
        return self.records['mx'][record_name]

    def zone_delegation(self, record_name: str, name_servers: list):
        self.records['zone_delegation'][record_name] = aws_route53.ZoneDelegationRecord(
            self, f"{record_name.replace('.', '-')}-zone",
            name_servers=name_servers,
            zone=self.zone,
            record_name=record_name
        )
        return self.records['zone_delegation'][record_name]


    def create_certificate(self, domain_name: str, subject_alternative_names: list=None, cert_authority: str=None):
        domid = domain_name.replace('.', '')
        self.cert = aws_certificatemanager.Certificate(
            self, f"{domid}-certificate",
            domain_name=domain_name,
            subject_alternative_names=subject_alternative_names,
            validation=aws_certificatemanager.CertificateValidation.from_dns(hosted_zone=self.zone)
        )
        CfnOutput(self, f"{domid}-certificate-arn", value=self.cert.certificate_arn, export_name=f"{domid}-cert-arn")
        return self.cert
