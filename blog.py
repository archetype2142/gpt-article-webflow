import openai
import sys
import time
import datetime
import os
import json
import ast
from slugify import slugify
from re import sub
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.environ.get('CHATGPT_TOKEN')

def generate_Topics(count = 10):
	response = openai.Completion.create(
	  model="text-davinci-003",
	  prompt="List {count} cryptocurrency-related article titles, format it in a python list".format(count = count),
	  temperature=1,
	  max_tokens=200,
	  top_p=1.0,
	  frequency_penalty=0.52,
	  presence_penalty=0.5
	)
	return response['choices'][0]['text']

# function to call to gpt
def ask_ChatGPT(system_intel, prompt): 
	result = openai.ChatCompletion.create(
		model="gpt-3.5-turbo",
		temperature=0.5,
		messages = [{"role": "system", "content" : system_intel},
		{"role": "user", "content" : prompt}])
	return result['choices'][0]['message']['content']


if(len(sys.argv) > 2):
	topics = [sys.argv[2]]
else:
	topics = generate_Topics(sys.argv[1]).replace('\n', '')
	topics = ast.literal_eval(topics)

for topic in topics:
	print(topic)

	response = openai.Image.create(
	  prompt="Futuristic Cryptocurrency illustration in van gough style",
	  n=1,
	  size="1024x1024"
	)
	image_url = response['data'][0]['url']

	print(image_url)

	# defining system intel and prompt for gpt
	system_intel = "You are an expert in Blockchain Technologies and Cryptocurrencies."
	prompt = """Write a blog of 300 words on {}""".format(topic)

	# call to gpt
	output = ask_ChatGPT(system_intel, prompt)

	# generating unix timestamp for current date
	present_date = datetime.datetime.now()
	unix_timestamp = datetime.datetime.timestamp(present_date)*1000

	# converting output to dict format
	output_dict = {
		'article': {
			'name': topic,
			'slug': slugify(topic),
			'body': output,
			'image_url': image_url
		}
	}

	# exporting output
	with open('./articles/output_{}.json'.format(unix_timestamp), 'w') as fp:
	    json.dump(output_dict, fp)

