# Manually Changing Storage Classes

## AWS Portal

1. Within S3, navigate to the file whose storage class you want to change.

2. Select the file > **Actions** dropdown > **Edit storage class**

3. Here you can change the storage class, as well as see what each storage class does.

<br>

## AWS Command-line Interface

```
aws s3 cp s3://<bucket key> s3://<bucket key> --storage-class <storage class>
```

Example usage:

```
aws s3 cp s3://BUCKET/KEY s3://BUCKET/KEY --storage-class STANDARD_IA
```

<br>

See the storage class options [here](https://docs.aws.amazon.com/cli/latest/reference/s3/cp.html#options), under `--storage-class`.

<br>


> **WARNING:** If Versioning is on, the above command does not change the storage class of the object. It creates a new object with the requested storage class (e.g. STANDARD_IA), but keeps the original version in whatever storage class it was uploaded (e.g. STANDARD). You'll be paying for both copies.