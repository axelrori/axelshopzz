from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'appname': 'AxelShopzz',
        'name': 'Serafino Theodore Axel Rori',
        'class': 'PBP F'
    }

    return render(request, "main.html", context)