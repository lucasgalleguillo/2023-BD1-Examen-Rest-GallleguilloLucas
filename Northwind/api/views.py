from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse
from .models import *
from django.db.models import Sum
# Create your views here.

@api_view(["GET", "POST"])
def getAllCustomers(request):
    if request.method == "GET":         
        customers = Customers.objects.all()
        customersSerializers = CustomerSerializer(customers, many=True)
        return Response(customersSerializers.data, status=status.HTTP_200_OK)
    elif request.method == "POST":
        customerNuevo = CustomerSerializer(data = request.data)

        if customerNuevo.is_valid():
            customerNuevo.save()
            return Response(customerNuevo.data, status=status.HTTP_202_ACCEPTED)
        return Response(customerNuevo.errors ,status=status.HTTP_400_BAD_REQUEST)
    
@api_view(["GET", "PUT", "DELETE"])
def getCustomerById(request, pk):
    try:
        customer = Customers.objects.get(customerid=pk)
    except Exception:
        return Response(status=status.HTTP_204_NO_CONTENT)
    if request.method == 'GET':
        serializer = CustomerSerializer(customer)
        return Response(serializer.data, status=status.HTTP_200_OK)
    if request.method == 'PUT':

        request.data['customerid'] = pk


        if 'companyname' not in request.data:
            request.data['companyname'] = customer.companyname
        
        serializer = CustomerSerializer(customer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':
        # borrar el customer seleccionado y ademas borrar todas las Orders que dependan de ese customer
        customer.delete()
        return Response(status=status.HTTP_200_OK)
    


    # --- SUPPLIERS ------------------------------------------------------------------------------------
@api_view(["GET", "POST"])
def getAllSuppliers(request):
    if request.method == "GET":         
        suppliers = Suppliers.objects.all()
        suppliersSerializers = SupplierSerializer(suppliers, many=True)
        return Response(suppliersSerializers.data, status=status.HTTP_200_OK)
    elif request.method == "POST":
        supplierNuevo = SupplierSerializer(data = request.data)
        if supplierNuevo.is_valid():
            supplierNuevo.save()
            return Response(supplierNuevo.data, status=status.HTTP_200_OK)
        return Response(supplierNuevo.errors ,status=status.HTTP_400_BAD_REQUEST)
    
@api_view(["GET", "PUT", "DELETE"])
def getSupplierById(request, pk):
    try:
        supplier = Suppliers.objects.get(supplierid=pk)
    except Exception:
        return Response(status=status.HTTP_204_NO_CONTENT)
    if request.method == 'GET':
        serializer = SupplierSerializer(supplier)
        return Response(serializer.data, status=status.HTTP_200_OK)
    if request.method == 'PUT':
        request.data['supplierid'] = pk
    
        serializer = SupplierSerializer(supplier, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':
        supplier.delete()
        return Response(status=status.HTTP_200_OK)



# --- CATEGORIES ------------------------------------------------------------------------------------
@api_view(["GET", "POST"])
def getAllCategories(request):
    if request.method == "GET":         
        categories = Categories.objects.all()
        categoriesSerializers = CategorieSerializer(categories, many=True)
        return Response(categoriesSerializers.data, status=status.HTTP_200_OK)
    elif request.method == "POST":

        categorieNuevo = CategorieSerializer(data = request.data)
        if categorieNuevo.is_valid():
            categorieNuevo.save()
            return Response(categorieNuevo.data, status=status.HTTP_200_OK)
        return Response(categorieNuevo.errors ,status=status.HTTP_400_BAD_REQUEST)
    
@api_view(["GET", "PUT", "DELETE"])
def getCategoryById(request, pk):
    try:
        categorie = Categories.objects.get(categoryid=pk)
    except Exception:
        return Response(status=status.HTTP_204_NO_CONTENT)
    if request.method == 'GET':
        serializer = CategorieSerializer(categorie)
        return Response(serializer.data, status=status.HTTP_200_OK)
    if request.method == 'PUT':
        request.data['categoryid'] = pk
    
        serializer = CategorieSerializer(categorie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':
        categorie.delete()
        return Response(status=status.HTTP_200_OK)



# --- PRODUCTS ------------------------------------------------------------------------------------
@api_view(["GET", "POST"])
def getAllProducts(request):
    if request.method == "GET":         
        products = Products.objects.all()
        productSerializers = ProductSerializer(products, many=True)
        return Response(productSerializers.data, status=status.HTTP_200_OK)
    elif request.method == "POST":
        productNuevo = ProductSerializer(data=request.data)
        if productNuevo.is_valid():
            productNuevo.save()
            return Response(productNuevo.data, status=status.HTTP_200_OK)
        return Response(productNuevo.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET", "PUT", "DELETE"])
def getProductById(request, pk):
    try:
        product = Products.objects.get(productid=pk)
    except Exception:
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    if request.method == 'GET':
        serializer = ProductSerializer(product)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    if request.method == 'PUT':
        request.data['productid'] = pk
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        product.delete()
        return Response(status=status.HTTP_200_OK)





# --- ORDERS ------------------------------------------------------------------------------------

@api_view(["GET", "POST"])
def getAllOrders(request):
    if request.method == "GET":         
        orders = Orders.objects.all()
        orderSerializers = OrderSerializer(orders, many=True)
        return Response(orderSerializers.data, status=status.HTTP_200_OK)
    elif request.method == "POST":
        orderNuevo = OrderSerializer(data=request.data)
        if orderNuevo.is_valid():
            orderNuevo.save()
            return Response(orderNuevo.data, status=status.HTTP_200_OK)
        return Response(orderNuevo.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET", "PUT", "DELETE"])
def getOrderById(request, pk):
    try:
        order = Orders.objects.get(orderid=pk)
    except Exception:
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    if request.method == 'GET':
        serializer = OrderSerializer(order)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    if request.method == 'PUT':
        request.data['orderid'] = pk
        serializer = OrderSerializer(order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        order.delete()
        return Response(status=status.HTTP_200_OK)




# --- ORDER_DETAILS ------------------------------------------------------------------------------------

@api_view(["GET", "POST"])
def getAllOrderDetails(request):
    if request.method == "GET":         
        order_details = Orderdetails.objects.all()
        orderDetailsSerializers = OrderdetailSerializer(order_details, many=True)
        return Response(orderDetailsSerializers.data, status=status.HTTP_200_OK)
    elif request.method == "POST":
        orderDetailNuevo = OrderdetailSerializer(data=request.data)
        if orderDetailNuevo.is_valid():
            orderDetailNuevo.save()
            return Response(orderDetailNuevo.data, status=status.HTTP_200_OK)
        return Response(orderDetailNuevo.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET", "PUT", "DELETE"])
def getOrderDetailById(request, pk, pk2):
    try:
        order_detail = Orderdetails.objects.get(orderid=pk, productid=pk2)
    except Exception:
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    if request.method == 'GET':
        serializer = OrderdetailSerializer(order_detail)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    if request.method == 'PUT':
        request.data['orderid'] = pk
        request.data['productid'] = pk2
        serializer = OrderdetailSerializer(order_detail, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        order_detail.delete()
        return Response(status=status.HTTP_200_OK)






# --- EMPLOYEES ------------------------------------------------------------------------------------

@api_view(["GET", "POST"])
def getAllEmployees(request):
    if request.method == "GET":         
        employees = Employees.objects.all()
        employeeSerializers = EmployeeSerializer(employees, many=True)
        return Response(employeeSerializers.data, status=status.HTTP_200_OK)
    elif request.method == "POST":
        employeeNuevo = EmployeeSerializer(data=request.data)
        if employeeNuevo.is_valid():
            employeeNuevo.save()
            return Response(employeeNuevo.data, status=status.HTTP_200_OK)
        return Response(employeeNuevo.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET", "PUT", "DELETE"])
def getEmployeeById(request, pk):
    try:
        employee = Employees.objects.get(employeeid=pk)
    except Exception:
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    if request.method == 'GET':
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    if request.method == 'PUT':
        request.data['employeeid'] = pk
        serializer = EmployeeSerializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        employee.delete()
        return Response(status=status.HTTP_200_OK)



# ---------------------------------------- PRUEBAS -------------------------------------------

# @api_view(["GET"])
# def punto1(request):   
#     categoria = request.query_params.get("categoryid")
#     cantidadEsperada = request.query_params.get("CantidadEsperada")
#     order = Orders.objects.filter()
#     ordenesDetails = Orderdetails.objects.filter(productid__categoryid = categoria) 
#     resultados = []
#     for e in ordenesDetails:
#         precioTotal = 0
#         precioTotal += e.calcularSubTotalSubTotal()
#         ordenes = e.orderid.objects.all()

#         for i in ordenes:
#             empleado = ordenes.employeeid
#             for a in empleado:
#                 resultado = {
#                     "id" : a.employeeid,
#                     "nombre" : a.firstname + " " + a.lastname,
#                     "GananciasTotales" : precioTotal,
#                     "HireDate" : a.hiredate,
#                 }
#                 if precioTotal >= cantidadEsperada:
#                     resultados.append(resultado)
#     serializados = Punto1Serializer(resultados, many=True)
#     return Response(serializados.data)



@api_view(['GET'])
def punto1(request):
    # Obtener parámetros de la solicitud
    categoria = request.query_params.get("categoryid")
    cantidadEsperada = float(request.query_params.get("cantidad", 0))

    if not Categories.objects.filter(categoryid=categoria).exists():
        return Response(status=status.HTTP_404_NOT_FOUND)

    detalles_ordenes = Orderdetails.objects.filter(
        productid__categoryid=categoria,
    )

    resultados = []
    for detalle in detalles_ordenes:
        empleado = detalle.orderid.employeeid
        ganancias_totales = detalles_ordenes.filter(
            orderid__employeeid=empleado
        ).aggregate(Sum(int('quantity') * int('unitprice')))['quantity__sum']

        if ganancias_totales >= cantidadEsperada:
            resultado = {
                "id": empleado.employeeid,
                "nombre": f"{empleado.firstname} {empleado.lastname}",
                "GananciasTotales": ganancias_totales,
                "HireDate": empleado.hiredate,
            }
            resultados.append(resultado)

    if not resultados:
        return Response(status=status.HTTP_204_NO_CONTENT)

    serializados = Punto1Serializer(resultados, many=True)
    return Response(serializados.data)
    
