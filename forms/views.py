from django.shortcuts import render
from django.urls import reverse
from django.core.mail import EmailMessage, BadHeaderError
from django.shortcuts import redirect
from django.template.loader import get_template
from django.conf import settings
from django.contrib import messages as messag
from django.http import HttpResponseRedirect, HttpResponse

from django.views.generic import TemplateView

from .forms import ContactUsForm, ApplyForStaffForm

import requests

def ContactUs(request):
    form_class = ContactUsForm
    if request.method == 'POST':
        form = form_class(request.POST)

        if form.is_valid():
            ''' Begin reCAPTCHA validation '''
            recaptcha_response = request.POST.get('g-recaptcha-response')
            data = {
                'secret': settings.RECAPTCHA_SECRET_KEY,
                'response': recaptcha_response
            }
            r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
            result = r.json()
            ''' End reCAPTCHA validation '''
            if result['success']:
                contact_name = request.POST.get('contact_name')
                contact_email = request.POST.get('contact_email')
                subject = request.POST.get('subject')
                msg = request.POST.get('msg')

                # Email the profile with the contact information
                template = get_template('form/contact_template.txt')
                context = {
                    'contact_name': contact_name,
                    'contact_email': contact_email,
                    'msg': msg,
                }
                content = template.render(context)

                email = EmailMessage(
                    subject,
                    content,
                    'noreply@painlesspvp.ml',
                    ['plpvpsupteam@gmail.com'],
                    headers={'Reply-To': contact_email}
                )
                # send(fail_silently=False)
                email.send()
                messag.success(request, f'We received your message! We will reply to your email that you provided usually within 48 hours!')
                return HttpResponseRedirect(reverse('blog-home'))
            else:
                messag.warning(request, 'Invalid reCAPTCHA. Please try again.')
    form = form_class()

    return render(request, 'form/ContactUs.html', {'form': form, })


def ApplyForStaff(request):
    form_class = ApplyForStaffForm
    if request.method == 'POST':
        form = form_class(request.POST)

        if form.is_valid():
            ''' Begin reCAPTCHA validation '''
            recaptcha_response = request.POST.get('g-recaptcha-response')
            data = {
                'secret': settings.RECAPTCHA_SECRET_KEY,
                'response': recaptcha_response
            }
            r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
            result = r.json()
            ''' End reCAPTCHA validation '''
            rank_choices = form.cleaned_data['rank_choices']
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            ign = form.cleaned_data['ign']
            age = form.cleaned_data['age']
            timezone = form.cleaned_data['timezone']
            time_spend = form.cleaned_data['time_spend']
            why_do_u_want_to_be_staff = form.cleaned_data['why_do_u_want_to_be_staff']
            why_us = form.cleaned_data['why_us']
            mod_how_will_deal_with_a_case = form.cleaned_data['mod_how_will_deal_with_a_case']
            mod_previous_experiences = form.cleaned_data['mod_previous_experiences']
            helper_how_will_deal_with_a_case = form.cleaned_data['helper_how_will_deal_with_a_case']
            helper_previous_experiences = form.cleaned_data['helper_previous_experiences']
            builder_previous_build_experiences = form.cleaned_data['builder_previous_build_experiences']
            builder_one_of_best_builds = form.cleaned_data['builder_one_of_best_builds']

            if result['success']:


                if rank_choices == 'dev':

                    kind_of_dev = form.cleaned_data['dev_kind_of_dev']
                    dev_creations = form.cleaned_data['dev_creations']

                    # Email the profile with the contact information
                    template = get_template('form/app_template.txt')
                    context = {
                      'rank_choices': rank_choices,
                      'name': name,
                      'email': email,
                      'ign': ign,
                      'age': age,
                      'timezone': timezone,
                      'time_spend': time_spend,
                      'why_do_u_want_to_be_staff': why_do_u_want_to_be_staff,
                      'why_us': why_us,
                      'kind_of_dev': kind_of_dev,
                      'dev_creations': dev_creations
                    }

                    content = template.render(context)

                    email = EmailMessage(
                        'Staff Application',
                        content,
                        'noreply@painlesspvp.ml',
                        ['plpvpsupteam@gmail.com'],
                        headers={'Reply-To': email}
                    )

                    # send(fail_silently=False)
                    email.send()
                    messag.success(request,
                                   f'We received your application! We will reply to your email that you provided usually within a week!')
                    return HttpResponseRedirect(reverse('blog-home'))

                if rank_choices == 'mod':

                    # Email the profile with the contact information
                    template = get_template('form/app_template.txt')
                    context = {
                      'rank_choices': rank_choices,
                      'name': name,
                      'email': email,
                      'ign': ign,
                      'age': age,
                      'timezone': timezone,
                      'time_spend': time_spend,
                      'why_do_u_want_to_be_staff': why_do_u_want_to_be_staff,
                      'why_us': why_us,
                      'mod_how_will_deal_with_a_case': mod_how_will_deal_with_a_case,
                      'mod_previous_experiences': mod_previous_experiences
                    }
                    content = template.render(context)

                    email = EmailMessage(
                        'Staff Application',
                        content,
                        'noreply@painlesspvp.ml',
                        ['plpvpsupteam@gmail.com'],
                        headers={'Reply-To': email}
                    )
                    # send(fail_silently=False)
                    email.send()
                    messag.success(request, f'We received your application! We will reply to your email that you provided usually within a week!')
                    return HttpResponseRedirect(reverse('blog-home'))

                if request.POST.get('rank_choices') == 'helper':

                    # Email the profile with the contact information
                    template = get_template('form/app_template.txt')
                    context = {
                      'rank_choices': rank_choices,
                      'name': name,
                      'email': email,
                      'ign': ign,
                      'age': age,
                      'timezone': timezone,
                      'time_spend': time_spend,
                      'why_do_u_want_to_be_staff': why_do_u_want_to_be_staff,
                      'why_us': why_us,
                      'mod_how_will_deal_with_a_case': mod_how_will_deal_with_a_case,
                      'mod_previous_experiences': mod_previous_experiences
                    }
                    content = template.render(context)

                    email = EmailMessage(
                        'Staff Application',
                        content,
                        'noreply@painlesspvp.ml',
                        ['plpvpsupteam@gmail.com'],
                        headers={'Reply-To': email}
                    )
                    # send(fail_silently=False)
                    email.send()
                    messag.success(request, f'We received your application! We will reply to your email that you provided usually within a week!')
                    return HttpResponseRedirect(reverse('blog-home'))

                elif request.POST.get('rank_choices') == 'builder':

                    # Email the profile with the contact information
                    template = get_template('form/app_template.txt')
                    context = {
                      'rank_choices': rank_choices,
                      'name': name,
                      'email': email,
                      'ign': ign,
                      'age': age,
                      'timezone': timezone,
                      'time_spend': time_spend,
                      'why_do_u_want_to_be_staff': why_do_u_want_to_be_staff,
                      'why_us': why_us,
                      'mod_how_will_deal_with_a_case': mod_how_will_deal_with_a_case,
                      'mod_previous_experiences': mod_previous_experiences
                    }
                    content = template.render(context)

                    email = EmailMessage(
                        'Staff Application',
                        content,
                        'noreply@painlesspvp.ml',
                        ['plpvpsupteam@gmail.com'],
                        headers={'Reply-To': email}
                    )
                    # send(fail_silently=False)
                    email.send()
                    messag.success(request, f'We received your application! We will reply to your email that you provided usually within a week!')
                    return redirect('blog-home')

            else:
                messag.warning(request, 'Invalid reCAPTCHA. Please try again.')
    form = form_class()

    return render(request, 'form/Apply_For_Staff.html', {'form': form, })
