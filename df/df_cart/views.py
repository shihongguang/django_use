from django.shortcuts import render

# Create your views here.

def cart(request):
    return render(request, "df_cart/cart.html")

def add_cart(request):
    user_id = request.session.get("user_id",0)
    print(user_id)
    news = request.GET
    gid = news.get("id")
    num = news.get("num")
    print(gid)
    print(num)


    return render(request, "df_cart/cart.html")