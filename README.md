# chatgpt-foodbot

ChatGPT-FoodBot is a simple food suggestion app built on django, utilizing OpenAI ChatGPT API.

## Set OpenAI key
1. Rename '''.env.sample''' to '''.env'''
2. Change the value for '''OPENAI_API_KEY''', '''ALLOWED_HOSTS=127.0.0.1''' and '''SECRET_KEY'''

## Build image
1. Use command '''docker-compose build''' to build image

## Run container
1. Run command '''docker compose up''' to run app in development server

## Access app
1. Go to 127.0.0.1:8001/foodbot
2. Enter your food cravings, i.e. Western, Chinese..
3. Sample app screenshot:

![foodbot](https://user-images.githubusercontent.com/47896683/227992825-751a4ac1-ba5c-427f-8d13-76e7014c90d7.png)
