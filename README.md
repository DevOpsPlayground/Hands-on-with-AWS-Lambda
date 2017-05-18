https://github.com/ForestTechnologiesLtd/devopsplayground11-lambda

# Hands On Serverless Computing with Lambda

The topics for this hands-on session will be AWS Lambda, function as a service (FaaS). During this Playground you will create a website hosted on AWS S3 using AWS Lambda and Amazon API Gateway to add dynamic functionality to the site.

## Labs

1. 001 - Build Static Website with s3 Bucket
1. 002 - CORS - Sharing resources between s3 Buckets
1. 003 - Web Services with Lambda (Python)
1. 004 - Posting Data with Lambda
1. 005 - Kinesis - Realtime Data Processing

#### Login

- __AWS Console:__ `https://devopsplayground.signin.aws.amazon.com/console`
- __Username:__ `<TBA>`
- __Password:__ `<TBA>`


- __Region:__ Oregon

#### Prerequisites
- Login to AWS account
- Permissions to create S3 Buckets
- Permissions to write and execute lambda functions

#### Checkout code from GitHub

```bash
git clone https://github.com/ForestTechnologiesLtd/devopsplayground11-lambda.git
cd devopsplayground11-lambda
```

### Lab-001 - Build Static Website with s3 Bucket

__Goal:__ Create a static website using s3 bucket

__AWS Services:__ S3 (Static Web hosting)

```bash
cd lab-001_website
```

1. Create a new s3 Bucket
  1. __Name and region__
    - __Name:__ `<your name>.playground11`
    - __Region:__ `US West (Oregon)`
    - __Copy settings from an existing bucket:__ Leave blank  
    - Click 'Next'
  1. __Set Properties:__
    - Click 'Next'
  1. __Set Permissions:__
    - Click 'Next'
  1. __Review:__
    - Click 'Create Bucket'
1. Upload files from folder `lab-001_website`
  1. __Select files__
    - (all files minus `css` folder)
    - Click 'Next'
  1. __Set Permissions__
    - Manage Group Permissions > Everyone (Read)/Make public
    - Click 'Next'
  - __Set Properties__
    - Click 'Upload'
1. Create subfolder `css` using S3 web console
  1. Goto bucket `<your name>.playground11`
    - Click Create folder
    - __Name:__ `css`
    - Click 'Save'
  - Upload remaining files from `css` folder same steps as 2.
1. Enable __Staitic website hosting__
  - Properties > Static website hosting
1. Select 'Use this bucket to host a Website'
  - __Index document:__ index.html
  - __Error document:__ error.html
  - Click 'Save'
1. Open the __Endpoint__ in a web browser.
 - `http://<your name>.playground11.s3-website-us-west-2.amazonaws.com`
1. Lab End.



### Lab-002 - CORS - Sharing resources between s3 Buckets

__Goal:__ Share resources from another s3 bucket with website from __lab-001_website__.

__AWS Services:__ S3 (Static Web hosting, CORS)

```bash
cd lab-002_cors
```

1. Edit the file `cors.html` change the link and replace it with the text __YOUR_NAME__ with your bucket name.
  - __REPLACE:__ YOUR_NAME.playground11
  - __WITH:__ <YOUR NAME>.playground11
```html
<script type="text/javascript">
  $(document).ready(function(){
      $("button").click(function(){
          $("#s3_cors").load("http://YOUR_NAME.playground11.s3-website-us-west-2.amazonaws.com/demo_text.txt");
      });
  });
</script>
```
1. Upload files from `cors.html, demo_text.html` folder `lab-002_website` to bucket `<your name>.playground11` your static website from __Lab-001__.
  1. __Select files__
    - (`cors.html, demo_text.txt`)
    - Click 'Next'
  1. __Set Permissions__
    - Manage Group Permissions > Everyone (Read)/Make public
    - Click 'Next'
  1. __Set Properties__
    - Accept defaults, click 'Upload'
1. Enable __Staitic website hosting__
     - Properties > Static website hosting
1. Select 'Use this bucket to host a Website'
     - __Index document:__ index.html
     - __Error document:__ error.html
     - Click 'Save'
1. Open the __Endpoint__ in a web browser.
   - `http://<your name>.playground11.s3-website-us-west-2.amazonaws.com`
1. With a web browser visit the static website from __Lab-001__ and click on the menu item 'CORS' the __RED__ text __"LAB NOT STARTED"__ should disappeared if not refresh the web page.
1. Click on the button __Get External Content__. Javascript code you edited at the start of this lab has now pull text from the file `demo_text`.

In order to understand CORS (Cross Origin Resource Sharing) you need to create another bucket, which this lab will pull resources from.

1. Create a new s3 Bucket
  1. __Name and region__
    - __Name:__ `<your name>.cors.playground11`
    - __Region:__ `US West (Oregon)`
    - __Copy settings from an existing bucket:__ Leave blank  
  1. __Set Properties:__
    - Click 'Next'
  1. __Set Permissions:__
    - Click 'Next'
  1. __Review:__
    - Click 'Create Bucket'
1. Upload files from the folder `lab-002_cors\cors_bucket` to your new bucket `<your name>.cors.playground11`
  1. __Select files__
    - (`cors_demo_text.txt, index.html, error.html`)
    - Click 'Next'
  1. __Set Permissions__
    - Manage Group Permissions > Everyone (Read)/Make public
    - Click 'Next'
  1. __Set Properties__
    - Accept defaults, click 'Upload'
1. Enable __Staitic website hosting__
     - Properties > Static website hosting
1. Select 'Use this bucket to host a Website'
     - __Index document:__ index.html
     - __Error document:__ error.html
     - Click 'Save'
1. Open the __Endpoint__ in a web browser.
  - `http://<your name>.cors.playground11.s3-website-us-west-2.amazonaws.com`
1. Edit the file `lab-002_cors\cors.html` change the Javascript link again to the new link from the new S3 bucket website.
  - __REPLACE:__ `YOUR_NAME.playground11`
  - __WITH:__ `<YOUR NAME>.cors.playground11`
  - __NOTE:__ The filename change at end of url: `cors_demo_text.txt`
```html
<script type="text/javascript">
$(document).ready(function(){
    $("button").click(function(){
        $("#s3_cors").load("http://YOUR_NAME.cors.playground11.s3-website-us-west-2.amazonaws.com/cors_demo_text.txt");
    });
});
</script>
```
1. Click on the button __Get External Content__. You will notice that nothing happens. If you Enable the Javascript console you notice in Safari the error:
```
[Error] Origin http://meetup.playground11.s3-website-us-west-2.amazonaws.com is not allowed by Access-Control-Allow-Origin.
[Error] Failed to load resource: Origin http://meetup.playground11.s3-website-us-west-2.amazonaws.com is not allowed by Access-Control-Allow-Origin. (cors_demo_text.txt, line 0)
[Error] XMLHttpRequest cannot load http://meetup.cors.playground11.s3-website-us-west-2.amazonaws.com/cors_demo_text.txt due to access control checks.
```
This occurs because web browsers expect resources to be requested from the same domain. To resolve this issue AWS S3 has a feature called CORS (Cross Origin Resource Sharing) if you enable this feature this will allow the webpage to request the content from another bucket.
1. With bucket `<your name>.cors.playground11` enable CORS configuration, add a new policy.
  - Permissions > CORS configuration
  - __NOTE:__ Replace url in `<AllowedOrigin>` tag with your static website link from lab-001.
```
<?xml version="1.0" encoding="UTF-8"?>
<CORSConfiguration xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
<CORSRule>
    <AllowedOrigin>http://<your name>.playground11.s3-website-us-west-2.amazonaws.com</AllowedOrigin>
    <AllowedMethod>GET</AllowedMethod>
    <MaxAgeSeconds>3000</MaxAgeSeconds>
    <AllowedHeader>Authorization</AllowedHeader>
</CORSRule>
</CORSConfiguration>
```
  - Click "Save"
1. Click on the button Get External Content. You will see __CORS Working....!__ now.
1. Lab End.


### Lab-003 - Web Services with Lambda (Python)

__Goal:__ Create a lambda function that generates a random number and expose the function as a web service via API Gateway.

__AWS Services:__ S3, Lambda, API Gateway,

```bash
cd lab-002_lambda
```
##### Create Lambda function

1. Services > Compute > Lambda
1. Create New function
  1. __Select blueprint__
    - Select runtime: python 2.7
    - Filter: hello-world-python
  1. __Configure triggers__
    - Click 'Next'
  1. __Configure function__
    - Name: `<your name>_generateRandomNumber`
    - Description: Function that generates a random number between 0 and 100
    - Runtime: Python 2.7
    - Lambda function code: Copy and Paste the code from file `lab-003_lambda\getSimpleRandomNumber.py` into the window. Leave the __Code entry type: Edit code inline__.
    - __Lambda function handler and role__
        - Handler: `lambda_function.lambda_handler`
        - Role*: Choose an existing role
        - Existing role*: `lambdaExecutionRole`
    - Accept Defaults for other settings
    - Click 'Next'
  1. __Review__
    - Click 'Create function'
    - __NOTE:__ Congratulations! Your Lambda function "meetup_generateRandomNumber" has been successfully created. You can now click on the "Test" button to input a test event and test your function.
1. Testing your function
  - Click 'Test'
  - Input test event
    - Sample event template : Hello World
    ```json
{}
    ```
    - Click 'Save and test'
    - You will see the message __Execution result: succeeded(logs)__ and a random number in a box with a dotted line.
1. View Lambda logs
  - Click the link 'logs' in the title labeled __Execution result: succeeded(logs)__
  - Click the log Group and look for the line: `Random No. [ 21 ]`. As the number is random it should look similar.

```python
from __future__ import print_function
from random import randint

print('Loading function')

def lambda_handler(event, context):
    myNumber = randint(0,100)
    print("Random No. [ %s ]" % myNumber)
    return myNumber

```

##### Create API Gateway




### Lab-004 - Posting Data with Lambda

__Goal:__ Using a form a the s3 Bucket website that is processed using Lambda. You will upload a form to the website and write a lambda function and expose that function using API Gateway using mapping tempaltes to process the POST from the form.

__AWS Services:__ S3, Lambda, API Gateway,

```bash
cd lab-004_mapping_templates
```

1. Upload the lab-004_mapping_templates to s3 website.

### Lab-005 - Kinesis, Realtime Data Processing wth Lambda, DynamoDB and API Gateway

__Goal:__ Using AWS Kinesis Streams to create a real-time data reporting using Lambda function to

__AWS Services:__ S3, Lambda, API Gateway, Kinesis Streams, DynamoDB

```bash
cd lab-005_kinesis

```
