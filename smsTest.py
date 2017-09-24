import nexmo

api_key = 'ad65c147'
api_secret = '522982b4182a6cd9'

client = nexmo.Client(key=api_key, secret=api_secret)


response = client.send_message({'from': 'Python', 'to': '447947535729', 'text': 'Hello world'})

response = response['messages'][0]

if response['status'] == '0':
  print 'Sent message', response['message-id']

  print 'Remaining balance is', response['remaining-balance']
else:
  print 'Error:', response['error-text']
