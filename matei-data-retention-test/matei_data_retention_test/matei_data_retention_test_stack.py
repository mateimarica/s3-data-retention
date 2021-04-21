from aws_cdk import (
	core,
	aws_s3 as s3,
	aws_s3_deployment as s3_deployment
)
import datetime
import pytz

class MateiDataRetentionTestStack(core.Stack):

	def __init__(
    		self, 
		scope: core.Construct, 
		id: str, 
		sample_data_path: str,
		bucket_name: str,
		**kwargs
	) -> None:

		super().__init__(scope, id, **kwargs)
	
		# Creates a sample S3 bucket with a lifecycle rule
		sample_bucket = s3.Bucket(self, f'{id}.s3.bucket',
			bucket_name=bucket_name,
			lifecycle_rules=[
				s3.LifecycleRule(
					enabled=True,
					id=f'{id}.s3.lifecyclerule',
					transitions=[
						s3.Transition(
							storage_class=s3.StorageClass.INTELLIGENT_TIERING,

							# Note that this transition may take 24-48 hours, but you will be charged as if the transition happens instantly.
							transition_after=core.Duration.days(1),
							
							# You can also set the transition time to a specific date:
							#transition_date=datetime.datetime(
							#	year=2021, 
							#	month=5, 
							#	day=17,
							#	tzinfo=pytz.timezone("US/Eastern")
							#),
						)
					]
				)
			],
			removal_policy=core.RemovalPolicy.DESTROY
		)

		# Uploads some sample data to the S3 bucket to for testing storage class transitions
		s3_deployment.BucketDeployment(self, f'{id}.s3deployment.sampledata',
			destination_bucket=sample_bucket,
			sources=[
				s3_deployment.Source.asset(
					path=sample_data_path
				)
			]
		)
