from django.shortcuts import render
from django.views import generic
from .models import MealItem


class MenuList(generic.ListView):
    queryset = MealItem.objects.order_by("-date_created")
    template_name = "index.html"

    def get_context_data(self):
        context = {"meals": ["Pizza"],
                   "ingredients": ["Flour", "Salt"]}
        return context


class MenuItemDetail(generic.DetailView):
    model = MealItem
    template_name = "menu_item_details.html"