from django.shortcuts import render, redirect
from django.urls import reverse
from core.forms import CTFForm
from core.models import Winner, Start
from django.http import JsonResponse


def home(request):
    started = Start.objects.filter(pk=1).exists()
    if started:
        start_date = Start.objects.get(pk=1).time
    else:
        start_date = ""
    form = CTFForm(request.POST or None)
    if form.is_valid() and started:
        w = Winner.objects.create(name=form.cleaned_data["name"])
        w.duration = w.end_time - start_date
        w.save()

    all_winners = Winner.objects.all().order_by("duration")
    return render(
        request,
        "home.html",
        {
            "form": form,
            "started": started,
            "start_date": start_date,
            "winners": all_winners,
        },
    )


def start_event(request):
    if not Start.objects.filter(pk=1).exists():
        s = Start.objects.create()
        s.save()
    return redirect(reverse("home"))


def get_winners(request):
    all_winners = Winner.objects.all().order_by("duration")
    return JsonResponse(
        {
            "winners_name": [w.name for w in all_winners],
            "winners_duration": [str(w.duration) for w in all_winners],
        }
    )
