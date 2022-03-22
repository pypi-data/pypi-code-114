from .base_verifications import Verification


class CustomizedVerification(Verification):
    """Расширяемый класс верификации"""

    verification_map = {}

    def verify(self) -> None:
        for attr, call in self.verification_map.items():
            call(attr)

        super().verify()
