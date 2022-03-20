def provider_factory(variant, payment=None):
    from djp_sepa.providers import DirectDebitProvider, PaymentPledgeProvider  # noqa
    from payments.paypal import PaypalProvider  # noqa
    from payments.sofort import SofortProvider  # noqa

    if not payment:
        raise KeyError("Could not configure payment provider without a payment.")
    if not payment.group:
        raise KeyError(
            "Could not configure payment provider for a payment without an invoice group."
        )
    if not payment.group.client:
        raise KeyError(
            "Could not configure payment provider for an invoice group without a client."
        )

    client = payment.group.client

    if variant == "sofort" and client.sofort_enabled:
        return SofortProvider(
            key=client.sofort_api_key, id=client.sofort_api_id, project_id=client.sofort_project_id
        )

    if variant == "paypal" and client.paypal_enabled:
        return PaypalProvider(
            client_id=client.paypal_client_id,
            secret=client.paypal_secret,
            capture=client.paypal_capture,
            endpoint="https://api.paypal.com",
        )

    if variant == "pledge" and client.pledge_enabled:
        return PaymentPledgeProvider()

    if variant == "sdd" and client.sdd_enabled:
        return DirectDebitProvider(
            creditor=client.sdd_creditor,
            creditor_identifier=client.sdd_creditor_identifier,
            iban=client.sdd_iban,
            bic=client.sdd_bic,
        )

    return KeyError("Provider not found or not configured for client.")
