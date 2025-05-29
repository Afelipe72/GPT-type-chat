from django.shortcuts import render
from django.http import JsonResponse
from chat.forms import inputForm
import ollama
from django.http import HttpResponse

def get_model_response(user_input) -> str:
    response = ollama.chat(
        model="deepseek-r1:1.5b",
        messages=[{"role": "user", "content": user_input}],
    )
    return response["message"]["content"]

def response_view(request):
    input_field_form = inputForm()
    return render(request, "chat/chat_template.html", {"input_field_form": input_field_form})

def ajax_response_view(request):
    if request.method == 'POST':
        # form name
        user_input = request.POST.get("input_field", "")
        model_reply = get_model_response(user_input)
        return JsonResponse({"response": model_reply})
    return JsonResponse({"error": "Invalid request"}, status=400)


def ajax_study(request):
    return render(request, "chat/ajax_study.html")

def get_message(request):
    return HttpResponse("Hello world!")

def say_hello(request):
    if request.method == 'POST':
        name = request.POST.get("nameInput")  
        print(name) 
        return HttpResponse(name)
    return HttpResponse("Not valid?")