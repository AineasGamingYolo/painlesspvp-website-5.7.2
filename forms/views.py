from django.shortcuts import render
from django.core.mail import EmailMessage
from django.shortcuts import redirect
from django.template.loader import get_template
from django.contrib import messages
from django.conf import settings
from django.contrib import messages as messag

from .forms import ContactUsForm

def ContactUs(request):
    form_class = ContactUsForm

    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            contact_name = request.POST.get('contact_name')
            contact_email = request.POST.get('contact_email')
            subject = request.POST.get('subject')
            form_msg = request.POST.get('msg')

            # Email the profile with the contact information
            template = get_template('forms/contact_template.txt')
            context = {
                'contact_name': contact_name,
                'contact_email': contact_email,
                'form_msg': form_msg,
            }
            content = template.render(context)

            email = EmailMessage(
                subject,
                content,
                'noreply@painlesspvp.ml',
                ['plpvpsp@gmail.com'],
                headers = {'Reply-To': contact_email }
            )
            #send(fail_silently=False)
            email.send()
            return redirect('blog-home') and messag.success(request, f'We received your message! We will reply to your email that you provided usually within 48 hours!')

    return render(request, 'forms/ContactUs.html', {'form': form_class})

