from django.shortcuts import render
from django.views import generic
from .models import MealItem


class MenuList(generic.ListView):
    queryset = MealItem.objects.order_by("-date_created")
    template_name = "index.html"


class MenuItemDetail(generic.DetailView):
    model = MealItem
    template_name = "menu_item_details.html"