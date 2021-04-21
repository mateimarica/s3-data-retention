#!/usr/bin/env python3

from aws_cdk import core

from matei_data_retention_test.matei_data_retention_test_stack import MateiDataRetentionTestStack


app = core.App()
MateiDataRetentionTestStack(app, "matei-data-retention-test7",
	bucket_name='matei-data-bucket',
	sample_data_path='./sample_data/'
)

app.synth()
