# Hands On Serverless Computing with Lambda

The topics for this hands-on session will be AWS Lambda, function as a service (FaaS). During this Playground you will create a website hosted on AWS S3 using AWS Lambda and Amazon API Gateway to add dynamic functionality to the site.

## Labs

1. 001 - Build Status Website with s3 Bucket
1. 002 - CORS - Sharing resources between s3 Buckets
1. 003 - Web Services with Lambda (Python)
1. 004 - Posting Data with Lambda
1. 005 - Kinesis - Realtime Data Processing


### Prerequisites
- [ ] AWS Account - S3, Lambda, API Gateway, DynamoDB, Kinesis
- [ ] IAM Policies Setup
- [ ] Checkout GitHub lab


### IAM Policies

The lab will need some IAM policies.
- Create a role called __lambdaExecutionRole__
- Lambda and Kinesis

### Get code GitHub

```bash
git clone https://github.com/ForestTechnologiesLtd/devopsplayground11-lambda.git
cd devopsplayground11-lambda
```

### 001 - Build Status Website with s3 Bucket

__Goal:__ Create a static website using s3 bucket

__AWS Services:__ S3 (Static Web hosting)

```bash
cd lab-001_website
```

1. Create s3 Bucket
```
<your name>.meetup.ecs-digital.co.uk
```
1. Upload files - Set Permissions Everyone (Read)/Make public
1. Properties > Static website hosting
 - __Index document:__ index.html
 - __Error document:__ error.html
1. Open the __Endpoint__ in a web browser.
1. Lab End.



### 002 - CORS - Sharing resources between s3 Buckets

__Goal:__ Share resources from another s3 bucket with website from __lab-001_website__.

__AWS Services:__ S3 (Static Web hosting, CORS)

```bash
cd lab-002_cors
```

1. Create a new s3 Buckets
```
<your name>.cors.meetup.ecs-digital.co.uk
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
