import requests
for x in xrange(0,100):
	url = 'http://colexh.com/n/account/assets/signin.php'
	caption = 'The message is:'

	form_data = {
		'user':'love_this_spamming'+str(x)+'@gmail.com',
		'pass':'not_a_password',
		}
	response = requests.post(url, data=form_data)


	print response
print "done"