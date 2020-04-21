import boto3
from botocore.exceptions import ClientError

def email_client(sender, to_add, message):
    email = boto3.client('ses',region_name="eu-west-2")
    try:
        email_response = email.send_email(
                                 Destination={
                                     'ToAddresses': [
                                         to_add,
                                     ],
                                 },
                                 Message={
                                         'Subject' : { 'Data': "daily Stats"},
                                         'Body': {
                                             'Text': {'Data': message},

                                         }


                                 },
                                 Source=sender,
                                 # If you are not using a configuration set, comment or delete the
                                 # following line
        #                        # ConfigurationSetName=CONFIGURATION_SET,
                             )
    except ClientError as e:
        print(e.email_response['Error']['Message'])
    else:
        print("Email sent! Message ID:"),
        print(email_response['MessageId'])
    return email_response['MessageId']
