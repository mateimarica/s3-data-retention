# Automatically Changing Storage Classes (Lifecycle transitions)

You can add rules to an S3 bucket to transition to a certain storage class...

* after a certain number of days.

* on a specific date.

Examples of setting these rules can be seen in the CDK stack code [here](https://github.com/mateimarica/s3-data-retention/blob/d15c14f17c52f5f5ee16d73846b0cb9af042aed1/cdk-data-retention-test/cdk_data_retention_test/cdk_data_retention_test_stack.py#L30).

<br>

## Setting Lifecycle Transition to 0 days

While it seems like when setting a bucket to transition between storage classes after zero days should make all data in the bucket switch instantly, it doesn't. I suspect it takes 24-48 hours to transition between storage classes using a lifecycle, as described [here](https://forums.aws.amazon.com/thread.jspa?threadID=222539&tstart=0&messageID=693975#693975) by an AWS representative. However, I have not tested this.