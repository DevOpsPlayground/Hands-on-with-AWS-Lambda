https://github.com/ForestTechnologiesLtd/devopsplayground11-lambda

# Hands On Serverless Computing with Lambda

The topics for this hands-on session will be AWS Lambda, function as a service (FaaS). During this Playground you will create a website hosted on AWS S3 using AWS Lambda and Amazon API Gateway to add dynamic functionality to the site.

## Labs

1. 001 - Build Static Website with s3 Bucket
1. 002 - CORS - Sharing resources between s3 Buckets
1. 003 - Web Services with Lambda (Python)
1. 004 - Posting Data with Lambda
1. 005 - Kinesis - Realtime Data Processing

### Login

__AWS Console:__ https://devopsplayground.signin.aws.amazon.com/console
__Username:__ `<TBA>`
__Password:__ `<TBA>`

### Prerequisites
- Login to AWS account
- Permissions to create S3 Buckets
- Permissions to write and execute lambda functions

### Checkout code from GitHub

```bash
git clone https://github.com/ForestTechnologiesLtd/devopsplayground11-lambda.git
cd devopsplayground11-lambda
```

### 001 - Build Static Website with s3 Bucket

__Goal:__ Create a static website using s3 bucket

__AWS Services:__ S3 (Static Web hosting)

```bash
cd lab-001_website
```

1. Create s3 Bucket
 - __Name:__ `<your name>.playground11`
 - __Region:__ `US West (Oregon)`
 - Set Properties: Click 'Next'
 - Set Permissions: Click 'Next'
 - Review: Click 'Create Bucket'

1. Upload files from folder `lab-001_website`
  - __Select files__ (all file & folders), you will need to create subfolders manually in bucket.
  - __Set Permissions__ Manage Group Permissions > Everyone (Read)/Make public
  - Accept defaults, click 'Next'
  - __Set Properties__ Accept defaults, click 'Upload'
1. Create subfolder `css`
  - Click 'Save'
  - Upload remaining files from `css` folder same steps as 2.
1. Properties > Static website hosting
1. Select 'Use this bucket to host a Website'
 - __Index document:__ index.html
 - __Error document:__ error.html
 - Click 'Save'
1. Open the __Endpoint__ in a web browser.
 - `http://<your name>.playground11.s3-website-us-west-2.amazonaws.com`
1. Lab End.



### 002 - CORS - Sharing resources between s3 Buckets

__Goal:__ Share resources from another s3 bucket with website from __lab-001_website__.

__AWS Services:__ S3 (Static Web hosting, CORS)

```bash
cd lab-002_cors
```

1. Create a new s3 Buckets
```
<your name>.cors.playground11
```
1. Upload the code from folder __lab-002_cors__. Remember to make the file public.
1. Enable static website
1. Permissions > CORS configuration
```
<?xml version="1.0" encoding="UTF-8"?>
<CORSConfiguration xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
<CORSRule>
    <AllowedOrigin>http://static.meetup.ecs-digital.co.uk.s3-website-us-west-2.amazonaws.com</AllowedOrigin>
    <AllowedMethod>GET</AllowedMethod>
    <MaxAgeSeconds>3000</MaxAgeSeconds>
    <AllowedHeader>Authorization</AllowedHeader>
</CORSRule>
</CORSConfiguration>
```


### 003 - Web Services with Lambda (Python)

__Goal:__ Create a lambda function that generates a random number and expose the function as a web service via API Gateway.

__AWS Services:__ S3, Lambda, API Gateway,

```bash
cd lab-002_lambda

```

### 004 - Posting Data with Lambda

__Goal:__ Using a form a the s3 Bucket website that is processed using Lambda. You will upload a form to the website and write a lambda function and expose that function using API Gateway using mapping tempaltes to process the POST from the form.

__AWS Services:__ S3, Lambda, API Gateway,

```bash
cd lab-004_mapping_templates
```

1. Upload the lab-004_mapping_templates to s3 website.

### 005 - Kinesis - Realtime Data Processing

__Goal:__ Using AWS Kinesis Streams to create a real-time data reporting using Lambda function to

__AWS Services:__ S3, Lambda, API Gateway, Kinesis Streams, DynamoDB

```bash
cd lab-005_kinesis

```
