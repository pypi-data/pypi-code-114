class Email:
    """Email.
    """

    def mask(self, email):
        """Mask an email

        Args:
            email (str): The email address to mask

        Returns:
            A string of the masked email address
        """

        # Mask the email address
        mask_email = email + ".invalid"

        return mask_email