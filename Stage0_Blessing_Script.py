# Hamming distance
def hamming_dist (slack_username, twitter_handle):
	i = 0
	count = 0
	while(i < len (slack_username)):
		if(slack_username[i] != twitter_handle[i]):
			count += 1
		i += 1
	return count

name= 'Blessing Olabosoye'
email= 'bleznolap@gmail.com'
slack_username= '@Blessing'
biostack= 'Genomics'
twitter_handle= '@Olabosoye_BP'
ham = hamming_dist (slack_username, twitter_handle)
print('Name- %s,Email- %s,Slack Username- %s,Biostack- %s,Twitter Handle- %s,Hamming Distance- %i' %(name, email, slack_username, biostack, twitter_handle, ham))





