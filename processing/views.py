from django.shortcuts import render, redirect
from django.db.models import Sum
from django.views.decorators.csrf import csrf_exempt
from .utils.get_stores_names import list_stores
from .utils.convert_file import converter
from .forms import UploadFileForm
from .models import DataPost


@csrf_exempt
def upload(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)

        if form.is_valid():
            converter(request)

            return redirect("list/")
    else:
        form = UploadFileForm()
    return render(request, "cnab/upload.html", {"form": form})


def rendering(request):
    if request.method == "GET":
        stores = DataPost.objects.all()

        stores_list = []

        stores_names = list_stores(stores)

        for name in stores_names:
            store = DataPost.objects.filter(store_name=name)[0]
            value = DataPost.objects.filter(store_name=name).aggregate(total=Sum("value"))

            store.total = round(int(value["total"]) / 100, 2)

            stores_list.append(store)

        return render(request, "cnab/list.html", {"stores_list": stores_list})
