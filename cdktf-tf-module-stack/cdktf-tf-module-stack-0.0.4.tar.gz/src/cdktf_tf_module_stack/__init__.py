'''
# cdktf-tf-module-stack

A drop-in replacement for cdktf.TerraformStack that let's you define Terraform modules as construct.

## Setup

### Node.js

Run `yarn add cdktf-tf-module-stack` (or `npm install --save cdktf-tf-module-stack`) to install the package.

### Python

Run `pip install cdktf-tf-module-stack` to install the package.

## Usage

```python
import { App } from "cdktf";
import { TFModuleStack } from "cdktf-tf-module-stack";
import { NullProvider, Resource } from "@cdktf/provider-null";

class MyAwesomeModule extends TFModuleStack {
  constructor(scope: Construct, id: string) {
    super(scope, id);

    new NullProvider(this, "null");
    new Resource(this, "resource");
  }
}

const app = new App();
new MyAwesomeModule(app, "my-awesome-module");
app.synth();
```

This will synthesize a Terraform JSON file that looks like this:

```json
{
  "resource": {
    "null_resource": {
      "resource": {}
    }
  },
  "terraform": {
    "required_providers": {
      "null": {
        "source": "null",
        "version": "~> 2.0"
      }
    }
  }
}
```

Please note that the provider section is missing, so that the Terraform Workspace using the generated module can be used with any provider matching the version.
'''
import abc
import builtins
import datetime
import enum
import typing

import jsii
import publication
import typing_extensions

from ._jsii import *

import cdktf
import constructs


class TFModuleStack(
    cdktf.TerraformStack,
    metaclass=jsii.JSIIMeta,
    jsii_type="cdktf-tf-module-stack.TFModuleStack",
):
    def __init__(self, scope: constructs.Construct, id: builtins.str) -> None:
        '''
        :param scope: -
        :param id: -

        :stability: experimental
        '''
        jsii.create(self.__class__, self, [scope, id])

    @jsii.member(jsii_name="toTerraform")
    def to_terraform(self) -> typing.Any:
        return typing.cast(typing.Any, jsii.invoke(self, "toTerraform", []))


__all__ = [
    "TFModuleStack",
]

publication.publish()
