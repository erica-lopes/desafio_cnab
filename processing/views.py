from django.shortcuts import render, redirect
from .forms import UploadFile
from .utils import handle_uploaded_file
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def upload_file(request):
    if request.method == "POST":
        form = UploadFile(request.POST, request.FILES)

        if form.is_valid():
            handle_uploaded_file(request.FILES["file"])
            return redirect("upload/")
    else:
        form = UploadFile()
    return render(request, "cnab/upload.html", {"form": form})
