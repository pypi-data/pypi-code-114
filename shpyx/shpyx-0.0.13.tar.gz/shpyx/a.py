#! /usr/bin/env python
import os
import subprocess

import cmd_runner
import signal

# result = shpyx.run("pwd", log_cmd=True)
# print(result)
import subprocess, sys
import tempfile


passwd= "prod-main-1.cknl7stvaahv.us-east-1.rds.amazonaws.com:5432/?Action=connect&DBUser=yossi&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=ASIAW3BCRA327NV6MZSC%2F20220317%2Fus-east-1%2Frds-db%2Faws4_request&X-Amz-Date=20220317T190525Z&X-Amz-Expires=900&X-Amz-SignedHeaders=host&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLWVhc3QtMSJIMEYCIQCLCNU%2BhykKmw4%2FnS2hBCNx5ieMMh%2B7kt4AIhYXJ9T%2BFwIhAJTD082TvielBS4kQALb7ZRiQJ%2F2nxmwA%2BTdjoWRY%2BHgKvgBCKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQARoMNDcwMzcxMzM3OTczIgxV1dWy3wvRneeKLxAqzAEFlf7w4HCBhwqVmWUsApOMc9E%2BqIHT4%2FsRH4PZ0GB9pxLOSjRcy3sV0sT0%2BnQvqrIQLeAUD1wH9ZmB83aIOrYsrdhaLOciqLIEFbnFTaOkc7Q%2FGWId16D0sb6Cg%2FDY9aEMjo7zUywlqQSf%2Br0pjLK1UZn433iORz7A1fptAteLV7xz3Kmh6SVEOxKv2k%2Fk6uotP8gmE7q9OfjwtdPWmGaxTOGxnLNLcEpRC5c62cSAg4FizVuLl1jfQiMLFJ8o57XhvGTyIOe5JaARvs4w9aXMkQY6lwH3DbAi9olzGKfbyAar5631ohumWyjIrqk18%2BfoEnoDc6LQHiYscCc4u3EBl3eWMI8mEeTSGs8oRBMABCv1FDdjmnG%2FmrF%2F9cwVHfVUsYGc4VXCDaBFsoJuJ52aSBwzcvt3Z6%2FvXi51jznEtsZ8FqFkuqYj9R%2Bq%2BQjmuEEQrdsOpStNAuJNMNxiWHkBgVBUF3Or3FANv7Ua&X-Amz-Signature=9bdb0d862c574841b28d734e8f1b823481a66599f8a3783cbc54703cf49808f1"
# exec 1> >(tee bashlog.txt) 2>&1
# /bin/bash -il
# cmd_runner.run("script -O /dev/null  -q -c 'PGPASSWORD=inch psql -h localhost -p 2345 -U inch -d inch_test_master'", log_output=True)
cmd_runner.run(f"script -O /dev/null -q -c 'psql -h 0.0.0.0 -p 40000 'dbname=inch user=yossi''",
               log_output=True)
cmd_runner.run(f"psql -h 0.0.0.0 -p 40000 'dbname=inch user=yossi'",
               log_output=True)
# print(cmd_runner.run("python", log_output=True))
