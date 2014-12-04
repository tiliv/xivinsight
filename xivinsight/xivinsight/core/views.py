from django.views.decorators.csrf import requires_csrf_token
from django.shortcuts import render

@requires_csrf_token
def site(request):
    return render(request, "site.html", {})

