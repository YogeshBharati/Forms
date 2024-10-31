from django.shortcuts import render
from .forms import FeedbackForm
from .models import Feedback

def feedback(request):
    form = FeedbackForm()
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            interested_course = form.cleaned_data['interested_course']
            message = form.cleaned_data['message']
            Feedback.objects.create(name=name, email=email, phone=phone,interested_course=interested_course, message=message)
            return render(request, 'CourseInquaryapp/success_form.html', {'name': name})
    return render(request, 'CourseInquaryapp/feedback.html', {'form': form})

