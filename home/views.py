from django.shortcuts import render, HttpResponse
import os
from django.http import JsonResponse
import openai

openai.api_key = 'OPENAI_API_KEY'



# Create your views here.


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def features(request):
    return render(request, 'features.html')

def pricing(request):
    return render(request, 'pricing.html')

def waitlist(request):
    return render(request, 'waitlist.html')

def chatbot(request):
    return render(request, 'chatbot.html')

def chatAPI(request):
    if request.method == 'POST':
        prompt  = request.POST["prompt"]

        prompt = [str(arg) if arg is not None else "None" for arg in prompt]
        # parse args to comma seperated string
        prompt = ", ".join(prompt)
        messages = [
            {
                "role": "system",
                "content": f"You are ChatGPT, a language model trained by OpenAI. Your role is to provide helpful and informative responses. The user has provided the following prompt: ```{prompt}``` Please respond accordingly.",
            },
            {"role": "user", "content": prompt},
        ]

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages,
            temperature=0.1,
            max_tokens=None,
            top_p=1,
            frequency_penalty=5,
            presence_penalty=2
        )
        print(response)
    # response = {"this": "that"}
        return JsonResponse(response)
    return HttpResponse("Bad Request")


# def chat_ai_response(function, args, description, model="gpt-3.5-turbo"):
#     # For each arg, if any are None, convert to "None":
#     args = [str(arg) if arg is not None else "None" for arg in args]
#     # parse args to comma seperated string
#     args = ", ".join(args)
#     messages = [
#         {
#             "role": "system",
#             "content": f"You are now the following python function: ```# {description}\n{function}```\n\nOnly respond with your `return` value.",
#         },
#         {"role": "user", "content": args},
#     ]

#     response = chatAPI(
#         model=model, messages=messages, temperature=0
#     )

#     return response





