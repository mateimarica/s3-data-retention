#!/usr/bin/env python3

from aws_cdk import core

from cdk_data_retention_test.cdk_data_retention_test_stack import CdkDataRetentionTestStack


app = core.App()
CdkDataRetentionTestStack(app, "cdk-data-retention",
	bucket_name='cdk-data-bucket',
	sample_data_path='./sample_data/'
)

app.synth()
