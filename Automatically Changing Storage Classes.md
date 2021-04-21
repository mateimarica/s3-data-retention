# Automatically Changing Storage Classes (Lifecycle transitions)

You can add rules to an S3 bucket to transition to a certain storage class after a certain number of days.



<br>

## Setting Lifecycle Transition to 0 days

While it seems like when setting a bucket to transition between storage classes after zero days should make all data in the bucket switch instantly, it doesn't. I suspect it takes 24-48 hours to transition between storage classes using a lifecycle, as described [here](https://forums.aws.amazon.com/thread.jspa?threadID=222539&tstart=0&messageID=693975#693975) by an AWS representative. However, I have not tested this.