from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

# In-memory storage for users and products
users = {
    'john_doe': {
        'password': 'password123',
        'orders': [
            {
                'product_id': 1,
                'product_name': 'Product1',
                'quantity': 2,
                'total_price': 200
            },
            {
                'product_id': 3,
                'product_name': 'Product3',
                'quantity': 1,
                'total_price': 300
            }
        ]
    },
    'jane_smith': {
        'password': 'securepass',
        'orders': []
    }
}

products = {
    1: {'name': 'Product1', 'price': 100},
    2: {'name': 'Product2', 'price': 200},
    3: {'name': 'Product3', 'price': 300}
}

def pro(request):
    return render(request, 'pro.html', {'products': products})

def register_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username in users:
            return HttpResponse("Username already exists. Try a different one.")
        users[username] = {'password': password, 'orders': []}
        return redirect('login')
    return render(request, 'register.html')

def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username in users and users[username]['password'] == password:
            return redirect('products', username=username)
        return HttpResponse("Invalid credentials.")
    return render(request, 'login.html')

def display_products_view(request, username):
    if username not in users:
        return redirect('login')
    product_list = products.values()
    return render(request, 'products.html', {'products': product_list, 'username': username})

def place_order_view(request, username):
    if username not in users:
        return redirect('login')
    if request.method == "POST":
        product_id = int(request.POST.get('product_id'))
        quantity = int(request.POST.get('quantity'))
        if product_id not in products:
            return HttpResponse("Invalid product ID.")
        order = {
            'product_id': product_id,
            'product_name': products[product_id]['name'],
            'quantity': quantity,
            'total_price': products[product_id]['price'] * quantity
        }
        users[username]['orders'].append(order)
        return HttpResponse("Order placed successfully.")
    return render(request, 'place_order.html', {'products': products, 'username': username})

def view_orders_view(request, username):
    if username not in users:
        return redirect('login')
    user_orders = users[username]['orders']
    return render(request, 'view_orders.html', {'orders': user_orders, 'username': username})
