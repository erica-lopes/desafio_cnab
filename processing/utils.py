from .models import DataPost
import datetime


def handle_uploaded_file(request):
    loading = request.FILES["file"]

    for line in loading:
        type: line[0]
        date: line[1:9]
        value: line[9:19]
        cpf: line[19:30]
        card: line[30:42]
        hour: line[42:48]
        owner: line[48:62]
        store_name: line[62:80]

        new_date = datetime.datetime(int(date[0:4]), int(date[4:6]), int(date[6:8])).strftime("%Y-%m-%d")
        new_hour = datetime.time(int(hour[0:2]), int(hour[2:4]), int(hour[4:6])).strftime("%H:%M:%S")

        converted_data = {
            "type": int(type),
            "date": new_date,
            "value": int(value),
            "cpf": cpf,
            "card": card,
            "hour": new_hour,
            "owner_name": owner,
            "store_name": store_name,
        }

        instance = DataPost.objects.create(**converted_data)
        instance.save()
