import os
from typing import IO


from paretos.use_case.customer_record import CustomerRecord
from paretos.use_case.use_case import Parameter, UseCase
from paretos.use_case.use_case_api_http_session import UseCaseApiHttpSession


class UseCaseApiClient:
    def __init__(self, session: UseCaseApiHttpSession) -> None:
        self.__session = session

    def _get_customer_id(self):
        return self.__session.get_customer_id()

    def store_customer_record(self, record: CustomerRecord):
        data = {
            "customerId": record.customer_id,
            "company": record.company,
            "useCases": [
                {
                    "useCaseId": use_case.id,
                    "name": use_case.name,
                    "description": use_case.description,
                    "inputParameters": [
                        {
                            "parameterId": param.id,
                            "name": param.name,
                            "type": param.type,
                        }
                        for param in use_case.input_parameters
                    ],
                    "outputParameters": [
                        {
                            "parameterId": param.id,
                            "name": param.name,
                            "type": param.type,
                        }
                        for param in use_case.input_parameters
                    ],
                }
                for use_case in record.use_cases
            ],
        }

        self.__session.authenticated_request(
            path="customer/show", version="v4", contains_sensitive_data=False, data=data
        )

    def get_customer_record(self) -> CustomerRecord:
        data = {"customerId": self.__session.customer_id}
        result = self.__session.authenticated_request(
            path="customer/get", version="v4", contains_sensitive_data=False, data=data
        )

        return CustomerRecord(
            customer_id=result["customerId"],
            company=result["company"],
            use_cases=[
                UseCase(
                    id=use_case["useCaseId"],
                    name=use_case["name"],
                    description=use_case["description"],
                    input_parameters=[
                        Parameter(
                            id=param["parameterId"],
                            name=param["name"],
                            type=param["type"],
                        )
                        for param in use_case["inputParameters"]
                    ],
                    output_parameters=[
                        Parameter(
                            id=param["parameterId"],
                            name=param["name"],
                            type=param["type"],
                        )
                        for param in use_case["outputParameters"]
                    ],
                )
                for use_case in result["useCases"]
            ],
        )

    def put_use_case(self, use_case: UseCase):
        raise NotImplementedError()

    def upload_training_data_file(
        self,
        use_case_id: str,
        file_name: str,
        file_handle: IO[bytes],
        overwrite: bool = False,
    ):
        data = {
            # "customerId": self._get_customer_id(),
            "useCaseId": use_case_id,
            "overwrite": overwrite,
        }
        files = {"trainingDataFile": (file_name, file_handle)}
        self.__session.authenticated_request(
            path="trainingDataFiles/upload",
            version="v4",
            contains_sensitive_data=False,
            data=data,
            files=files,
        )

    def upload_training_data_file_from_path(
        self, use_case_id: str, file_path: str, overwrite: bool = False
    ):
        file_name = os.path.basename(file_path)
        with open(file_path, "rb") as fp:
            return self.upload_training_data_file(use_case_id, file_name, fp, overwrite)

    def list_training_data_files(self, use_case_id: str):
        raise NotImplementedError()

    def remove_trainig_data_file(self, use_case_id: str, file_url: str):
        raise NotImplementedError()
