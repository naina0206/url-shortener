from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import URL

def home(request):
    if request.method == "POST":
        long_url = request.POST.get("url")
        if long_url:
            obj, created = URL.objects.get_or_create(original_url=long_url)
            short_url = request.build_absolute_uri(f"s/{obj.short_code}/")
            stats_url = request.build_absolute_uri(f"stats/{obj.short_code}/")
            return render(request, "shortener/home.html", {
                "short_url": short_url,
                "stats_url": stats_url,
                "code": obj.short_code
            })
    return render(request, "shortener/home.html")

def redirect_url(request, code):
    url = get_object_or_404(URL, short_code=code)
    url.clicks += 1
    url.last_clicked = timezone.now()
    url.save()
    return redirect(url.original_url)

def stats(request, code):
    url = get_object_or_404(URL, short_code=code)
    short_url = request.build_absolute_uri(f"s/{url.short_code}/")
    
    # Calculate time since creation
    time_since_creation = timezone.now() - url.created_at
    days_old = time_since_creation.days
    hours_old = time_since_creation.seconds // 3600
    
    # Calculate average clicks per day
    if days_old > 0:
        avg_clicks_per_day = round(url.clicks / days_old, 1)
    else:
        avg_clicks_per_day = url.clicks
    
    context = {
        "url": url,
        "short_url": short_url,
        "days_old": days_old,
        "hours_old": hours_old,
        "avg_clicks_per_day": avg_clicks_per_day,
        "has_clicks": url.clicks > 0,
    }
    return render(request, "shortener/stats.html", context)
