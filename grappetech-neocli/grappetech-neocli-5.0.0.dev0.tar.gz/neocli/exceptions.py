class InvalidBranchException(Exception):
	pass


class InvalidRemoteException(Exception):
	pass


class PatchError(Exception):
	pass


class CommandFailedError(Exception):
	pass


class NeoCLINotFoundError(Exception):
	pass


class ValidationError(Exception):
	pass

class CannotUpdateReleaseNeoCLI(ValidationError):
	pass

class FeatureDoesNotExistError(CommandFailedError):
	pass


class NotInNeoCLIDirectoryError(Exception):
	pass
