"""A Python Pulumi program"""

import pulumi
from sw_pulumi_algolia import Index

# Create an index named 'test-index'
Index("my-index", name="test-index")
