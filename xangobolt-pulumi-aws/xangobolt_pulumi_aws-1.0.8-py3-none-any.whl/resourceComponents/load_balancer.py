from arpeggio.cleanpeg import NOT, prefix
import pulumi
from pulumi import ComponentResource, ResourceOptions, StackReference, Input, Output
from resources import lb, autoscaling, route53, sm


def ECS_LB(stem, props, snet_ids=None, sg_ids=None, vpc_id=None, asg_name=None, hcp=None, dns_zone=None, dns_name=None, sec_id=None, secret=None, provider=None, parent=None, depends_on=None):
    ecs_lb = lb.AppLoadBalancer(
        stem,
        props, 
        snet_ids=snet_ids,
        sg_ids=sg_ids,
        parent=parent,
        depends_on=depends_on,
        provider=provider
    )

    # Create Target Group
    ecs_tg = lb.TargetGroup(
        stem, 
        props, 
        vpc_id=vpc_id,
        hcp=hcp,
        parent=parent,
        depends_on=depends_on,
        provider=provider
    )

    # Create Forward Listener
    fw_listener = lb.Listener_SSL(
        stem,
        props,
        lb_arn=ecs_lb.arn,
        tg_arn=ecs_tg.arn,
        # cert_arn="arn:aws:acm:ca-central-1:554290308952:certificate/8286748f-e183-4648-a2f5-a4d31b16fa48",
        # cert_arn="arn:aws:acm:ca-central-1:917340184633:certificate/0c8d2e2e-d0f2-48a6-b15f-9145d088dbea",
        cert_arn="arn:aws:acm:ca-central-1:917340184633:certificate/018246f1-51d6-4e96-83a8-621284b648a3",
        parent=parent,
        depends_on=ecs_tg,
        provider=provider
    )

    # Create Redirect Listener
    r_listener = lb.Listener(
        stem,
        props,
        lb_arn=ecs_lb.arn,
        parent=parent,
        depends_on=ecs_lb,
        provider=provider
    )

    # # Create Target Group Attachment
    # tga = lb.TargetGroupAttachment(
    #     stem,
    #     props,
    #     port=40000,
    #     tg_arn=ecs_tg.arn,
    #     instance_id="i-05e8f826c88984538",
    #     parent=parent,
    #     depends_on=depends_on,
    #     provider=provider
    # )

    # Create ASG attachment to Target group
    # tga = autoscaling.AutoScaleingGroupAttachment(
    #     stem,
    #     props,
    #     tg_arn=ecs_tg.arn,
    #     asg_name=asg_name,
    #     parent=parent,
    #     depends_on=depends_on,
    #     provider=provider
    # )

    # Create DNS Record
    dnsrecord = Output.all(dnsname=ecs_lb.dns_name).apply(lambda args: route53.Record(
            dns_name,
            props,
            zone_id=dns_zone,
            type='A',
            name=dns_name, 
            lbz_name='dualstack.'+args['dnsname'], 
            lbz_id=ecs_lb.zone_id,
            parent=parent,
            depends_on=depends_on,
            provider=provider
        )
    )

    pulumi.export('lbName', ecs_lb.dns_name)
    pulumi.export('lbID', ecs_lb.zone_id)
    return ecs_tg

    


