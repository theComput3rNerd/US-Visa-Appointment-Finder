import boto3

client = boto3.client('sns', region_name='us-east-2')

response = client.publish(
    TopicArn='arn:aws:sns:us-east-2:702250566201:Appointment-Availability',
#    TargetArn='string',
#    PhoneNumber='string',
    Message='m',
    Subject='s',
#    MessageStructure='string',
#    MessageAttributes={
   #     'string': {
 #           'DataType': 'string',
 #           'StringValue': 'string',
   #         'BinaryValue': b'bytes'
 #       }
 #   },
  #  MessageDeduplicationId='string',
 #   MessageGroupId='string'*
)