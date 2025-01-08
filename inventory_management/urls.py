from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

# http://127.0.0.1:8000/v1/
urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("products", views.products, name="products"),
    path("add-product", views.add_product, name="add_product"),
    path("suppliers", views.suppliers, name="suppliers"),
    path("add-supplier", views.add_supplier, name="add_supplier"),
    path("remove-supplier/<int:id>", views.remove_supplier, name="remove_supplier"),
    path("remove-product/<int:id>", views.remove_product, name="remove_product"),
    path("edit-supplier/<int:id>", views.edit_supplier, name="edit_supplier"),
    path("edit-product/<int:id>", views.edit_product, name="edit_product"),
    path("stock-movement", views.stock_movement, name="stock_movement"),
    path("sales", views.sales, name="sales"),
    path("sales-update/<int:id>",views.sales_update,name="sales_update"),
    path("update-status/<int:id>/<str:status>",views.sales_status_update,name="sales_status_update")

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
