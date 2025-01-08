import json
from django.shortcuts import render,redirect
from django.db.models import F
from inventory_management.models import Category, Movement, Product, Sales, Status, Stock_Movement, Supplier
from django.utils.html import json_script
# Create your views here.

def dashboard(request):
    context={}
    products=Product.objects.all()
    sales=Sales.objects.all().values()
    context['table_data']=sales
    context['status_count']={}
    context['status_count']['pending']=sales.filter(status="pending").count()
    context['status_count']['completed']=sales.filter(status="completed").count()
    context['status_count']['cancelled']=sales.filter(status="cancelled").count()
    details={}
    for i in products:
        details[i.id]=i.name
    
    context['products_list']=products.order_by('stock').values()
    
    
    for i in context['table_data']:
        print(i) # {'id': 1, 'product_id': 1, 'status': 'pending', 'quantity': 10, 'total_price': 900000, 'date': datetime.date(2025, 1, 6)}
        print(i['product_id'])
        print(details[i['product_id']])
        i['product_name']=details[i['product_id']]


    print(context)
    """
    {'sales': <QuerySet [{'id': 1, 'product_id': 1, 'status': 'pending', 'quantity': 10, 'total_price': 900000, 'date': datetime.date(2025, 1, 6)}, {'id': 2, 'product_id': 1, 'status': 'completed', 'quantity': 10, 'total_price': 900000, 'date': datetime.date(2025, 1, 13)}, {'id': 3, 'product_id': 1, 'status': 'pending', 'quantity': 11, 'total_price': 990000, 'date': datetime.date(2025, 1, 9)}]>}
    """

    # my_data = {
    #     'name': 'Example Data',
    #     'value': 42,
    #     'items': [1, 2, 3],
    #     'nested': {'a': 'hello', 'b': 'world'}
    # }
    # context = {'my_data_json': json.dumps(my_data)}

    # return render(request, 'inventory_management/sales.html', context)
    return render(request, 'inventory_management/dashboard.html',context=context) 

# Product
def products(request):
    context={}
    products=Product.objects.all().values()
    context['table_data']=products
    # context['categorys']=category_list
    print(context)
    return render(request, 'inventory_management/products.html',context=context) 

def add_product(request):
    context={}
    if request.method == 'POST':
        # Get form data
        product_name = request.POST.get('product_name')
        category = request.POST.get('category')
        supplier = request.POST.get('supplier')
        price = request.POST.get('price')
        description = request.POST.get('description')
        stock_quantity = request.POST.get('stock_quantity')
        supplier_obj=Supplier.objects.get(name=supplier)
        # Process the form data (e.g., save to database)
        # ...

        # Optionally, provide feedback to the user
        print(f"{category=}")
        print(f"{supplier=}")
        print(f"{price=}")
        print(f"{description=}")
        # context = {'success_message': 'Form submitted successfully!'}
        context['product_add']=True
        context['product_name']=product_name

        product=Product(name=product_name,
                        description=description,
                        category=category,
                        price=price,
                        stock=stock_quantity,
                        supplier=supplier_obj)
        product.save()
        return redirect('products')
        # return render(request, 'inventory_management/products.html', context)
    else:
        suppliers=Supplier.objects.all()
        supplier_list=[]
        category_list=[]
        for supplier in suppliers:
            supplier_list.append(supplier.name)
        for category in Category:
            category_list.append(category.value)
        context['suppliers']=supplier_list
        context['table_data']=products
        context['categorys']=category_list
        print(context)
        return render(request, 'inventory_management/add_product.html', context)
    # return render(request, 'inventory_management/add_product.html', context)
    # context={}
    # return render(request, 'inventory_management/add_product.html',context=context)  

def remove_product(request,id):
    product=Product.objects.filter(id=id)
    product.delete()
    return redirect('products')

def edit_product(request,id):
    context={}
    if request.method == 'POST':
        # Get form data
        product_name = request.POST.get('product_name')
        category = request.POST.get('category')
        supplier = request.POST.get('supplier')
        price = request.POST.get('price')
        description = request.POST.get('description')
        stock_quantity = request.POST.get('stock_quantity')
        print(f"{supplier=}")
        supplier_obj=Supplier.objects.get(name=supplier)
        
        context['product_add']=True
        context['product_name']=product_name

        product=Product.objects.filter(id=id).update(name=product_name,
                        description=description,
                        category=category,
                        price=price,
                        stock=stock_quantity,
                        supplier=supplier_obj)
        return redirect('products')
    else:
        product=Product.objects.filter(id=id).values()
        suppliers=Supplier.objects.all()
        supplier_list=[]
        category_list=[]
        for supplier in suppliers:
            supplier_list.append(supplier.name)
        for category in Category:
            category_list.append(category.value)
        # supplier_obj=Supplier.objects.get(name=supplier)
        
        context['suppliers']=supplier_list
        context['table_data']=products
        context['categorys']=category_list
        context['product']=product[0]
        context['supplier_name']=Product.objects.get(pk=id).supplier.name
        print(f"{context=}")
        return render(request, 'inventory_management/add_product.html', context)



# Supplier

def suppliers(request):
    suppliers=Supplier.objects.all().values()
    context={}
    context['table_data']=suppliers
    # print(suppliers)
    return render(request, 'inventory_management/suppliers.html',context=context) 

def add_supplier(request):
    context={}
    if request.method == 'POST':
        # Get form data
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        address = request.POST.get('address')
        context['supplier_add']=True
        context['supplier_name']=name
        supplier=Supplier(name=name,email=email,phone_number=phone_number,address=address)
        supplier.save()
        # suppliers(request,context)
        return redirect('suppliers')
    else:
        return render(request, 'inventory_management/add_supplier.html', context)

def remove_supplier(request,id):
    supplier=Supplier.objects.filter(id=id)
    supplier.delete()
    return redirect('suppliers')

def edit_supplier(request,id):
    context={}
    if request.method == 'POST':
        # Get form data
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        address = request.POST.get('address')
        context['supplier_add']=True
        context['supplier_name']=name
        Supplier.objects.filter(id=id).update(name=name,email=email,phone_number=phone_number,address=address)
        return redirect('suppliers')
    else:
        supplier=Supplier.objects.filter(id=id).values()
        context['supplier']=supplier[0]
        print(f"{context=}")
        return render(request, 'inventory_management/add_supplier.html', context)


# Stocks
    
def stock_movement(request):
    context={}
    if request.method == 'POST':
        # Get form data
        product_name = request.POST.get('product_name')
        movemet_type = request.POST.get('movemet_type')
        quantity = request.POST.get('quantity')
        date = request.POST.get('date')
        note = request.POST.get('note')

        print(f"{product_name=}")
        print(f"{movemet_type=}")
        print(f"{quantity=}")
        print(f"{date=}")
        print(f"{note=}")

        product=Product.objects.get(name=product_name)
        movement=Movement(movemet_type)
        stock_movement=Stock_Movement(product=product,
                                      movemet_type=movement.value,
                                      quantity=quantity,
                                      date=date,
                                      note=note)
        updated_quantity=0
        if(movement.value=="in"):
            updated_quantity=product.stock + int(quantity)
        elif(int(quantity)<product.stock):
            updated_quantity=product.stock - int(quantity)
        else:
            raise ValueError("Input value must be with in stock range") 
        
        Product.objects.filter(name=product_name).update(stock=updated_quantity)
        stock_movement.save()
        # suppliers(request,context)
        return redirect('products')
    else:
        #GET request for rendring form
        products=Product.objects.all()
        product_list=[]
        for i in products:
            product_list.append(i.name)
        context['product_list']=product_list
        return render(request, 'inventory_management/stock_movement.html', context)

    
# Sales
    
def sales(request):
    context={}
    if request.method == 'POST':
        # Get form data
        product_name = request.POST.get('product_name')
        quantity = request.POST.get('quantity')
        date = request.POST.get('date')
        status = request.POST.get('status')

        print(f"{product_name=}")
        print(f"{quantity=}")
        print(f"{date=}")
        print(f"{status=}")

        product=Product.objects.get(name=product_name)
        status=Status(status)
        sales=Sales(product=product,
                    status=status.value,
                    quantity=quantity,
                    date=date,
                    total_price=int(quantity)*product.price)
        updated_quantity=0
        if(status.name==Status.PENDING or status.name==Status.CANCELLED):
            updated_quantity=0
        elif(int(quantity)<product.stock):
            updated_quantity=product.stock - int(quantity)
        else:
            raise ValueError("Input value must be with in stock range") 
        
        Product.objects.filter(name=product_name).update(stock=updated_quantity)
        sales.save()
        # suppliers(request,context)
        return redirect('products')
    else:
        #GET request for rendring form
        products=Product.objects.all()
        product_list=[]
        for i in products:
            details={}
            details['name']=i.name
            details['quantity']=i.stock
            product_list.append(details)
        context['product_list']=product_list
        return render(request, 'inventory_management/sales.html', context)

def sales_update(request,id):
    context={}
    if request.method == 'POST':
        # Get form data
        product_name = request.POST.get('product_name')
        quantity = request.POST.get('quantity')
        date = request.POST.get('date')
        status = request.POST.get('status')

        print(f"{product_name=}")
        print(f"{quantity=}")
        print(f"{date=}")
        print(f"{status=}")

        product=Product.objects.get(name=product_name)
        status=Status(status)
        sales=Sales(product=product,
                    status=status.value,
                    quantity=quantity,
                    date=date,
                    total_price=int(quantity)*product.price)
        updated_quantity=0
        if(status.name==Status.PENDING or status.name==Status.CANCELLED):
            updated_quantity=0
        elif(int(quantity)<product.stock):
            updated_quantity=product.stock - int(quantity)
        else:
            raise ValueError("Input value must be with in stock range") 
        
        Product.objects.filter(name=product_name).update(stock=updated_quantity)
        sales.save()
        # suppliers(request,context)
        return redirect('products')
    else:
        #GET request for rendring form
        products=Product.objects.all()
        sales=Sales.objects.filter(id=id).values()[0]
        context['sales']=sales
        
        product_list=[]
        for i in products:
            details={}
            details['name']=i.name
            details['quantity']=i.stock
            product_list.append(details)
            if(i.id==sales['product_id']):
                context['sales']['product_name']=i.name
        context['product_list']=product_list
        
        print(context)

        return render(request, 'inventory_management/sales.html', context)


def sales_status_update(request,id,status):

    sale=Sales.objects.filter(id=id).update(status=status)
    context={}
    return redirect('dashboard')


