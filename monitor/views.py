from django.shortcuts import render, HttpResponse
import json


from django.core.mail import send_mail


def mail(request):
    content = request.POST.get("content")
    tos = request.POST.get("tos")
    subject = request.POST.get("subject")
    try:
        send_mail(subject, content, 'jwh5566@163.com', ['%s'%tos], fail_silently=False)
        log = {"log": "ok"}
        return HttpResponse(json.dumps(log), content_type='application/json')
    except Exception, e:
        error = {"error": e}
        return HttpResponse(json.dumps(error), content_type='application/json')