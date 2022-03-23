class ModelRepository:
    def __init__(self, url, branch=None, access_token=None):
        self.url = url
        self.branch = branch if branch is not None else "main"
        self.access_token = access_token

    def __repr__(self):
        res = f"{self.__module__}.{self.__class__.__name__}("
        res += f"\n      url={self.url}"
        res += f"\n      branch={self.branch}"
        res += "\n    )"
        return res


class ModelParams:
    def __init__(self, url, config_url="", upload=False, credentials=None):
        self.url = url
        self.config_url = config_url
        self.upload = upload
        self.credentials = credentials

    def __repr__(self):
        res = f"{self.__module__}.{self.__class__.__name__}("
        res += f"\n      url={self.url}"
        res += f"\n    )"
        return res


class Model:
    """
    Provides model related functionality.
    It can be created through the :class:`efemarai.project.Project.create_model` method.

    Example:

    .. code-block:: python
        :emphasize-lines: 2

        import efemarai as ef
        ef.Session().project("Name").create_model(...)
    """

    @staticmethod
    def create(project, name, repository, params):
        """
        Create a model. A more convenient way is to use :func:`project.create_model`.
        """
        if name is None or repository is None or params is None:
            return None

        repository = ModelRepository(**repository)
        params = ModelParams(**params)

        session = project._session
        response = session._put(
            f"api/model/undefined/{project.id}",
            json={
                "name": name,
                "repository_url": repository.url,
                "branch": repository.branch,
                "access_token": repository.access_token,
                "model_url": params.url,
                "model_config_url": params.config_url,
                "upload_params": params.upload,
                "projectId": project.id,
            },
        )
        model_id = response["id"]

        if params.upload:
            session._upload(params.url, f"api/model/{model_id}/upload")
            if params.config_url:
                session._upload(params.config_url, f"api/model/{model_id}/upload")

        return Model(project, model_id, name, repository, params)

    def __init__(self, project, id, name, repository, params):
        self.project = (
            project  #: (:class:`efemarai.project.Project`) Associated project.
        )
        self.id = id
        self.name = name  #: (str) Name of the model.
        self.repository = repository
        self.params = params

    def __repr__(self):
        res = f"{self.__module__}.{self.__class__.__name__}("
        res += f"\n  id={self.id}"
        res += f"\n  name={self.name}"
        res += f"\n  repository={self.repository}"
        res += f"\n  params={self.params}"
        res += f"\n)"
        return res

    def delete(self):
        """
        Delete the model. You cannot delete an object that is used in a stress test or a baseline (delete those first). This cannot be undone.
        """
        self.project._session._delete(f"api/model/{self.id}/{self.project.id}")
