from django.shortcuts import redirect, render
from home.models import About, Photography, Social, Contact, Post, ContactMessage
import requests
import logging
import json
from datetime import datetime
from dateutil.relativedelta import relativedelta


def index(request):
    context = {}
    context["active"] = "index"
    posts = Post.objects.filter(active=True).order_by("-pk")
    about_details = About.objects.all().first()

    # hitting facts api
    api_url = 'https://api.api-ninjas.com/v1/facts?limit={}'.format(1)
    response = requests.get(api_url, headers={'X-Api-Key': 'gA4JOe0gMb+nNXzM9r2gFA==Jhrz1oNfKoYdpydA'})
    if response.status_code == requests.codes.ok:
        context["fact"] = json.loads(response.text)[0]["fact"]
    else:
        logging.info("Error:", response.status_code, response.text)
        context["fact"] = "Say \"Boogie Boogie Woogie\" 3 times infront of a mirror and see the magic."

    context["about_details"] = about_details
    context["posts"] = posts
    return render(request, "home/index.html", context)

def about(request):
    context = {}
    context["active"] = "about"
    about_details = About.objects.all().first()
    social_details = Social.objects.all().first()
    context["about_details"] = about_details
    context["social_details"] = social_details
    return render(request, "home/about.html", context)

def contact(request):
    context = {}
    context["active"] = "contact"

    if request.method == "POST":
        ContactMessage.objects.create(
            name=request.POST["name"],
            email=request.POST["email"],
            subject=request.POST["subject"],
            message=request.POST["message"]
        )
        return redirect(contact)

    contact_obj = Contact.objects.all().first()
    context["contact_obj"] = contact_obj
    return render(request, "home/contact.html", context)

def photography(request):
    context = {}
    context["active"] = "photography"
    images = Photography.objects.filter(active=True).order_by("-pk")
    context["images"] = images
    return render(request, "home/photography.html", context)

def post(request, pk):
    context = {}
    context["active"] = ""
    post_obj = Post.objects.get(pk=pk)
    latest_posts = Post.objects.all().order_by("-pk")[:3]
    categories = {
        "Fashion": Post.objects.filter(tags__contains="fashion").count(),
        "Technology": Post.objects.filter(tags__contains="technology").count(),
        "Travel": Post.objects.filter(tags__contains="travel").count(),
        "Food": Post.objects.filter(tags__contains="food").count(),
        "Photography": Post.objects.filter(tags__contains="photography").count()
    }
    current_date = datetime.now().date()
    archives_obj = {}
    for i in range(6):
        date = current_date - relativedelta(months=i)
        archives_obj[f'{date.strftime("%B")} {date.strftime("%Y")}'] = Post.objects.filter(created_at__month=date.month).count()

    if post_obj.image_1:
        post_obj.description = post_obj.description.replace(
            "{image_1}", f'<img src="{post_obj.image_1.url}" alt="" class="img-fluid">'
        )
    if post_obj.image_2:
        post_obj.description = post_obj.description.replace(
            "{image_2}", f'<img src="{post_obj.image_2.url}" alt="" class="img-fluid">'
        )
    if post_obj.image_3:
        post_obj.description = post_obj.description.replace(
            "{image_3}", f'<img src="{post_obj.image_3.url}" alt="" class="img-fluid">'
        )

    context["post_obj"] = post_obj
    context["categories"] = categories
    context["latest_posts"] = latest_posts
    context["archives_obj"] = archives_obj
    return render(request, "home/single.html", context)

