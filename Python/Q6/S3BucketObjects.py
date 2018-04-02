import boto3

s3 = boto3.resource('s3')
bucket = s3.Bucket('train')
s3_files = open("s3_files.txt", "w+")
for obj in bucket.objects.all():
    print(obj.key)
    s3_files.write(obj.key+"\n")
s3_files.close()
