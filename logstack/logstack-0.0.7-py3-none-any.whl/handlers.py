# Python imports

# Third party imports
import boto3

# Self imports


class DjangoCloudWatchHandler:
    def __init__(
        self, 
        log_level: str, 
        log_group_name: str,
        cloud_watch_aws_id: str,
        cloud_watch_aws_key: str,
        cloud_watch_aws_region: str,
    ) -> None:

        self.log_level = log_level
        self.log_group_name = log_group_name
        self.cloud_watch_aws_id = cloud_watch_aws_id
        self.cloud_watch_aws_key = cloud_watch_aws_key
        self.cloud_watch_aws_region = cloud_watch_aws_region
    
    def get_handler_data(self) -> dict:
        boto3_logs_client = self._get_boto_client()
        cloud_watch_handler = {
            'level': self.log_level,
            'class': 'watchtower.CloudWatchLogHandler',
            'boto3_client': boto3_logs_client,
            'log_group_name': self.log_group_name,
            'formatter': 'aws',
        }
        return cloud_watch_handler
    
    def _get_boto_client(self) -> object:
        boto3_logs_client = boto3.client(
            'logs',
            aws_access_key_id=self.cloud_watch_aws_id,
            aws_secret_access_key=self.cloud_watch_aws_key,
            region_name=self.cloud_watch_aws_region
        )
        return boto3_logs_client