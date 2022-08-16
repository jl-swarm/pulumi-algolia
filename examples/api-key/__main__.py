"""A Python Pulumi program"""

import pulumi
from sw_pulumi_algolia import ApiKey

# Create an API Key
key = ApiKey("my-api-key", acls=["search"], description="Test API Key", indexes=["test-index"])
pulumi.export("api-key", key.key)
