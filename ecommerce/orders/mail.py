import re

import boto3
from botocore.exceptions import ClientError


def clean_html(raw_html):
    cleaner = re.compile('<.*?>')
    clean_text = re.sub(cleaner, '', raw_html)
    return clean_text


# Replace sender@example.com with your "From" address.
# This address must be verified with Amazon SES.
SENDER = "Mukul Mantosh <mukulmantosh91@gmail.com>"

# If necessary, replace us-west-2 with the AWS Region you're using for Amazon SES.
AWS_REGION = "ap-south-1"

# The subject line for the email.
SUBJECT = "New Order Placed"

# The email body for recipients with non-HTML email clients.


# The HTML body of the email.
BODY_HTML = """<html>
<head></head>
<body>
  <h1>Order Successfully Placed !</h1>
  <p>Hi, Your new order has been successfully placed. You will receive more information shortly.</p>
</body>
</html>
            """

BODY_TEXT = clean_html(BODY_HTML)

# The character encoding for the email.
CHARSET = "UTF-8"

# Create a new SES resource and specify a region.
client = boto3.client('ses', region_name=AWS_REGION)


def order_notification(recipient):
    # Try to send the email.
    try:
        # Provide the contents of the email.
        response = client.send_email(
            Destination={
                'ToAddresses': [
                    recipient,
                ],
            },
            Message={
                'Body': {
                    'Html': {
                        'Charset': CHARSET,
                        'Data': BODY_HTML,
                    },
                    'Text': {
                        'Charset': CHARSET,
                        'Data': BODY_TEXT,
                    },
                },
                'Subject': {
                    'Charset': CHARSET,
                    'Data': SUBJECT,
                },
            },
            Source=SENDER,
            # If you are not using a configuration set, comment or delete the
            # following line
            # ConfigurationSetName=CONFIGURATION_SET,
        )
    # Display an error if something goes wrong.
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        print("Email sent! Message ID:"),
        print(response['MessageId'])
