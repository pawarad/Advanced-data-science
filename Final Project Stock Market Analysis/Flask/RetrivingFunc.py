
# coding: utf-8

# In[1]:


from boto.s3.connection import S3Connection
import os

def RetrivingData():

	conn = S3Connection('AKIAJQ7VKPEF3XSGEUIA','CTkdVK0ftphqlXoc4Y+kkOHs6nDw5PTQ/aFay4X4')
	bucket = conn.get_bucket('finalads')

	for key in bucket.list():
		print(key.name)
	if key.name.endswith('/'):
    	if not os.path.exists('./'+key.name):
    	os.makedirs('./'+key.name)
    	else:
		res = key.get_contents_to_filename('./'+key.name)
return df