# Hands On Serverless Computing with Lambda

The topics for this hands-on session will be AWS Lambda, function as a service (FaaS). During this Playground you will create a website hosted on AWS S3 using AWS Lambda and Amazon API Gateway to add dynamic functionality to the site.

1. [GitHub - README.md](https://github.com/ForestTechnologiesLtd/devopsplayground11-lambda)
1. [Labs Static Website sample](http://meetup.playground11.s3-website-us-west-2.amazonaws.com/index.html)
1. All labs were done in US Oregon Region

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


#### Prerequisites
- Login to AWS account
- Permissions to create S3 Buckets
- Permissions to write and execute lambda functions
- __Region:__ Oregon

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
  1. __Set Properties__
      - Click 'Upload'
1. Create subfolder `css` using S3 web console
  1. Goto bucket `<your name>.playground11`
      - Click Create folder
      - __Name:__ `css`
      - Click 'Save'
  1. Upload remaining files from `css` folder same steps as 2.
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
    ```
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
            - __Handler:__ `lambda_function.lambda_handler`
            - __Role*:__ Choose an existing role
            - __Existing role*:__ `lambdaExecutionRole`
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


__lambda_function.lambda_handler__
```python
from __future__ import print_function
from random import randint

print('Loading function')

def lambda_handler(event, context):
    myNumber = randint(0,100)
    print("Random No. [ %s ]" % myNumber)
    return myNumber

```

##### Exposing Lambda via API Gateway

1. Create new API
    - Check 'New API'
    - __Name:__ `<your name>pg11`
    - __Description:__ test lab api
    - Click 'Create API'
1. Add a New Child Resource
    - APIs > `<your name>pg11` > Resources
    - __Configure as proxy resource:__ Leave blank
    - __Resource Name:__ Random Number
    - __Resource Path:__ `/random-number`
    - __Enable API Gateway CORS:__ Yes
1. Add a GET method to resource __/random-number__
    - Actions > Create Method
    - Under the resource a drop down will appear select __GET__ method and click the 'tick'.
1. /random-number __GET__ - Setup
    - __Integration type:__ Lambda Function
    - __Use Lambda Proxy integration:__ Leave blank
    - __Lambda Region:__ `us-west-2`
    - __Lambda Function:__ `<your name>_generateRandomNumber`
    - Click 'Save'
       - Confirm the dialog 'Add Permission to Lambda Function', Click 'OK'

##### Testing Lambda via API Gateway

1. Click __GET__ method under __/random-number__
1. Click __TEST__ link in the box labeled 'Client
1. At the bottom of the new view Click 'Test' button
1. Under __Response Body__ you should see a random number. Click the blue button labelled 'Test' again at the bottom of the screen and you will see a new number appear.
1. Test completed successfully

##### Deploy API

1. Click Resources select __/__
1. Select __Actions__ and select __Deploy API__
    - Deploy API
    - __Deployment stage:__ [New Stage]
        - __Stage Name:__ dev
        - __Stage description:__ Pre-production development stage
    - __Deployment description:__
1. __Remember Invoke URL:__ `https://3xtidh28cf.execute-api.us-west-2.amazonaws.com/dev`


##### Test API Deployment

1. Entering the Invoke URL into the web browser.
    - __NOTE:__ You will have to enter the method name e.g. `/random-number` to the end of the ___Invoke URL___
    - `https://3xtidh28cf.execute-api.us-west-2.amazonaws.com/dev/random-number`
1. You should see a random number appear in the web browser.

##### Integrate API into static website

```bash
cd lab-003_lambda
```

1.  Edit the file `apigw.html` change the link and replace replace the string 'MY_API_GW_REQUEST' with the API Gateway Invoke URL with method name `/random-number` in it. e.g. `https://3xtidh28cf.execute-api.us-west-2.amazonaws.com/dev/random-number`
1. Update the file to S3 bucket `<Your name>.playground11` remember to set read permission for everyone.
1. load the website in a web browser
1. Click the button labelled 'Get External Content'
    - __IT WILL FAIL...!__
    - View Javascript in your website and you'll see message like `CORS header 'Access-Control-Allow-Origin' missing`.
        - Previous lab we did a example of CORS we need to enable the API here to all the website to access the link from a diffent site.
1. `/random-number`, __GET__ method then Actions > __Enable CORS__
1. You need to redeploy the API, __Deploy API__
    - __Development stage:__ dev
    - __Development description:__ lab-003
1. Refesh the web page, __API Gateway__
    - press button __Get External Content__
1. Lab End.

### Lab-004 - Posting Data with Lambda

__Goal:__ Using a form a the s3 Bucket website that is processed using Lambda. You will upload a form to the website and write a lambda function and expose that function using API Gateway using mapping tempaltes to process the POST from the form.

__AWS Services:__ S3, Lambda, API Gateway,

```bash
cd lab-004_mapping_templates
```

##### Create Lambda function

1. Services > Compute > Lambda
1. Create New function
    1. __Select blueprint__
        - Select runtime: python 2.7
        - Filter:
    1. __Configure triggers__
        - Click 'Next'
    1. __Configure function__
        - Name: `<your name>_myHelloMsg`
        - Description: Function that presents a nice greeting
        - Runtime: Python 2.7
        - Lambda function code: Copy and Paste the code from file `lab-004_lambda\myHelloMsg.py` into the window. Leave the __Code entry type: Edit code inline__.
        ```python
        def lambda_handler(event, context):
            # TODO implement
            print("Event is %s" % event)
            name = event.get("name") or "No msg submitted"
            return "Hello from Lambda: %s " % (name)
        ```
        - __Lambda function handler and role__
            - __Handler:__ `lambda_function.lambda_handler`
            - __Role*:__ Choose an existing role
            - __Existing role*:__ `lambdaExecutionRole`
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
      {
          "name":"Hello is it me your looking for..."
      }
      ```
      - Click 'Save and test'
      - You will see the message __Execution result: succeeded(logs)__ dotted line box the output from the function: "Hello from Lambda: Hello is it mean your looking for... "
1. View Lambda logs
    - Click the link 'logs' in the title labeled __Execution result: succeeded(logs)__
    - Click the log Group and look for the line: `Event is {u'name': u'Hello is it mean your looking for...'} `.


#### Configuring API Gateway

##### /hello - GET - Integration Request

1. Create New Resource on /
    - APIs > `<your name>pg11` > Resources
    - __Configure as proxy resource:__ Leave blank
    - __Resource Name:__ hello
    - __Resource Path:__ `/hello`
    - __Enable API Gateway CORS:__ Yes
    - Click 'Create Resource'
1. Add a GET method to resource __/hello__
    - Click Resource '/hello'
    - Actions > Create Method
    - Under the resource a drop down will appear select __GET__ method and click the 'tick'.
1. /hello __GET__ - Setup
    - Click '/hello' GET Resource
    - __Integration type:__ Lambda Function
    - __Use Lambda Proxy integration:__ Leave blank
    - __Lambda Region:__ `us-west-2`
    - __Lambda Function:__ `<your name>_myHelloMsg`
    - Click 'Save'
       - Confirm the dialog 'Add Permission to Lambda Function', Click 'OK'
1. Method Execution - GET
    - __Integation type:__ Lambda Function
    - __Use Lambda Proxy integration:__ Leave Blank
    - __Lambda Region:__ `us-west-2`
    - __Lambda Function:__ `<your name>_myHelloMsg`
    - __Invoke with caller credentials:__ Leave Blank
    - __Credentials cache:__ Do not add caller credentials to cache key
    __Body Mapping Templates - GET__
    - __Request body passthrough:__ When there are no templates defined (recommended)
    - Add Mapping Template:
        - __Content-Type:__ `application/json`  
        - __Body Mapping Template__
        ```json
        {
            "name":"$input.params('name')"
        }
        ```
    - Click 'Save'
1. Deploy API
    - Select __Actions__ and select __Deploy API__
    - __Stage Name:__ dev
    - __Stage description:__ Pre-production development stage
1. __Remember Invoke URL:__ `https://......execute-api.us-west-2.amazonaws.com/dev`

##### /hello - POST - Integration Request
1. Add a GET method to resource __/hello__
    - Click Resource '/hello'
    - Actions > Create Method
    - Under the resource a drop down will appear select __POST__ method and click the 'tick'.
1. /hello __POST__ - Setup
    - Click '/hello' POST Resource
    - __Integration type:__ Lambda Function
    - __Use Lambda Proxy integration:__ Leave blank
    - __Lambda Region:__ `us-west-2`
    - __Lambda Function:__ `<your name>_myHelloMsg`
    - Click 'Save'
       - Confirm the dialog 'Add Permission to Lambda Function', Click 'OK'
1. Method Execution - POST
    - __Integation type:__ Lambda Function
    - __Use Lambda Proxy integration:__ Leave Blank
    - __Lambda Region:__ `us-west-2`
    - __Lambda Function:__ `<your name>_myHelloMsg`
    - __Invoke with caller credentials:__ Leave Blank
    - __Credentials cache:__ Do not add caller credentials to cache key
    __Body Mapping Templates - GET__
    - __Request body passthrough:__ When there are no templates defined (recommended)
    - Add Mapping Template:
        - __Content-Type:__ `application/json`  
        - __Body Mapping Template__
        ```json
        {
            "name":"$input.params('name')"
        }
        ```
    - Click 'Save'
1. Deploy API
    - Select __Actions__ and select __Deploy API__
    - __Stage Name:__ dev
    - __Stage description:__ Pre-production development stage
1. __Remember Invoke URL:__ `https://......execute-api.us-west-2.amazonaws.com/dev`


##### Upload new lab page `maptempl.html` to website.

1. Edit the file `maptempl.html` from folder `lab-004_mapping_templates`
    - __REPLACE:__ `MY_API_GW_GET_REQUEST`
    - __WITH:__ `https://......execute-api.us-west-2.amazonaws.com/dev/hello`
1. Upload file `maptempl.html` from folder `lab-004_mapping_templates` to S3 bucket `<your name>.playground11`
    1. __Select files__
       - (`maptempl.html`)
       - Click 'Next'
    1. __Set Permissions__
       - Manage Group Permissions > Everyone (Read)/Make public
       - Click 'Next'
    1. __Set Properties__
       - Accept defaults, click 'Upload'









##### /hello - POST - Integration Request

1. Method Execution - POST
    - __Integation type:__ Lambda Function
    - __Use Lambda Proxy integration:__ Leave Blank
    - __Lambda Region:__ us-west-2
    - __Lambda Function:__ myHelloMsg
    - __Invoke with caller credentials:__ Leave Blank
    - __Credentials cache:__ Do not add caller credentials to cache key

1. Body Mapping Templates - POST
    - Request body passthrough: When there are no templates defined (recommended)
    - Content-Type: `application/x-www-form-urlencoded`

__Body Mapping Template__
```velocity
## convert HTML POST data or HTTP GET query string to JSON

## get the raw post data from the AWS built-in variable and give it a nicer name
#if ($context.httpMethod == "POST")
 #set($rawAPIData = $input.path('$'))
#elseif ($context.httpMethod == "GET")
 #set($rawAPIData = $input.params().querystring)
 #set($rawAPIData = $rawAPIData.toString())
 #set($rawAPIDataLength = $rawAPIData.length() - 1)
 #set($rawAPIData = $rawAPIData.substring(1, $rawAPIDataLength))
 #set($rawAPIData = $rawAPIData.replace(", ", "&"))
#else
 #set($rawAPIData = "")
#end

## first we get the number of "&" in the string, this tells us if there is more than one key value pair
#set($countAmpersands = $rawAPIData.length() - $rawAPIData.replace("&", "").length())

## if there are no "&" at all then we have only one key value pair.
## we append an ampersand to the string so that we can tokenise it the same way as multiple kv pairs.
## the "empty" kv pair to the right of the ampersand will be ignored anyway.
#if ($countAmpersands == 0)
 #set($rawPostData = $rawAPIData + "&")
#end

## now we tokenise using the ampersand(s)
#set($tokenisedAmpersand = $rawAPIData.split("&"))

## we set up a variable to hold the valid key value pairs
#set($tokenisedEquals = [])

## now we set up a loop to find the valid key value pairs, which must contain only one "="
#foreach( $kvPair in $tokenisedAmpersand )
 #set($countEquals = $kvPair.length() - $kvPair.replace("=", "").length())
 #if ($countEquals == 1)
  #set($kvTokenised = $kvPair.split("="))
  #if ($kvTokenised[0].length() > 0)
   ## we found a valid key value pair. add it to the list.
   #set($devNull = $tokenisedEquals.add($kvPair))
  #end
 #end
#end

## next we set up our loop inside the output structure "{" and "}"
{
#foreach( $kvPair in $tokenisedEquals )
  ## finally we output the JSON for this pair and append a comma if this isn't the last pair
  #set($kvTokenised = $kvPair.split("="))
 "$util.urlDecode($kvTokenised[0])" : #if($kvTokenised[1].length() > 0)"$util.urlDecode($kvTokenised[1])"#{else}""#end#if( $foreach.hasNext ),#end
#end
}
```




1. Upload the lab-004_mapping_templates to s3 website.


### Lab-005 - Kinesis, Realtime Data Processing wth Lambda, DynamoDB and API Gateway

__Goal:__ Using AWS Kinesis Streams to create a real-time data reporting using Lambda function to

__AWS Services:__ S3, Lambda, API Gateway, Kinesis Streams, DynamoDB

```bash
cd lab-005_kinesis

```
