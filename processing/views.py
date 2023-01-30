from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.db.models import Sum
from .forms import UploadFileForm
from .models import DataPost
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def upload_file(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)

        if form.is_valid():
            uploaded_file = request.FILES["file"]

            for line in uploaded_file:
                str_line = line.decode()

                type = str_line[0]
                date = f"{str_line[1:5]}-{str_line[5:7]}-{str_line[7:9]}"
                value = str_line[9:19]
                cpf = str_line[19:30]
                card = str_line[30:42]
                hour = f"{str_line[42:44]}:{str_line[44:46]}:{str_line[46:48]}",
                owner = str_line[48:62]
                store_name = str_line[62:80]

                DataPost.objects.create(
                    type=type,
                    date=date,
                    value=int(value) / 100,
                    cpf=cpf,
                    card=card,
                    hour=hour,
                    owner=owner,
                    store_name=store_name,
                )
                return HttpResponseRedirect("list/")

    else:
        form = UploadFileForm()
    return render(request, "cnab/upload.html", {"form": form})


def render(request):
    stores = DataPost.objects.all()
    stores_list = []

    for name in stores:
        store = DataPost.objects.filter(store_name=name)[0]
        total_balance = DataPost.objects.filter(store_name=name).aggregate(total=Sum("value"))
        store.total = total_balance["total"] / 100
        stores_list.append(store)

    return render(request, "cnab/list.html", {"stores_list": stores_list})
