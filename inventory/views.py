from datetime import datetime

from django.shortcuts import render, redirect

from inventory.forms import ItemForm, DrugForm
from .models import *


def ItemPage(request):
    form = ItemForm(request.POST)
    if request.method == 'POST':
        if request.POST or form.is_valid():
            if request.user.userType == 'Client' or request.user.userType == 'Nurse':
                obj = Item.objects.create(name=request.POST['name'],
                                          category=request.POST['category'],
                                          quantity=request.POST['quantity'],
                                          )
                obj.save()
                if request.user.is_authenticated:
                    return redirect('inventory:addItem')
                else:
                    return render(request, 'authentication/views/error.html', {})
    return render(request, 'inventory/add_inventory.html', {'form': form})

def DrugPage(request):
    form = DrugForm(request.POST)
    if request.method == 'POST':
        if request.POST or form.is_valid():
            if request.user.userType == 'Client' or request.user.userType == 'Nurse':
                today = datetime.now()
                obj = Drug.objects.create(name=request.POST['name'],
                                          category=request.POST['category'],
                                          quantity=request.POST['quantity'],
                                          genericName=request.POST['genericName'],
                                          date_updated=today)
                obj.save()
                if request.user.is_authenticated:
                    return redirect('inventory:addDrug')
                else:
                    return render(request, 'authentication/views/error.html', {})
    return render(request, 'inventory/add_drugs_page.html', {'form': form})

def itemList(request):

    item = Item.objects.all()

    context = {
        'item' : item
    }

    return render(request, 'inventory/views/inventory_items_table.html', context)

def drugList(request):

    drug = Drug.objects.all()

    context = {
        'drug' : drug
    }

    return render(request, 'inventory/views/inventory_drugs_table.html', context)

def delete_item(request, id):
    item = Item.objects.get(id=id)
    if request.user.userType == 'Client' or request.user.userType == 'Nurse':
        item.delete()
        return redirect('inventory:items_list')
    else:
        return render(request, 'authentication/views/error.html', {})

def delete_drug(request, id):
    d = Drug.objects.get(id=id)
    if request.user.userType == 'Client' or request.user.userType == 'Nurse':
        d.delete()
        return redirect('inventory:drugs_list')
    else:
        return render(request, 'authentication/views/error.html', {})


def edit_item(request, id):
    item = Item.objects.get(id=id)
    if request.user.userType == 'Client' or request.user.userType == 'Nurse':
        if request.method == 'POST':
            if request.POST:
                print(item.name)
                item.name = request.POST['name']
                item.category = request.POST['category']
                item.quantity = request.POST['quantity']
                print(item.name)
                item.save()

                return redirect('inventory:items_list')
        else:
            return render(request, 'inventory/edit_item.html', {'item': item})
    else:
        return render(request, 'authentication/views/error.html', {})

def edit_drug(request, id):
    drug = Drug.objects.get(id=id)
    if request.user.userType == 'Client' or request.user.userType == 'Nurse':
        if request.method == 'POST':
            if request.POST:
                print(drug.name)
                drug.name = request.POST['name']
                drug.genericName = request.POST['genericName']
                drug.category = request.POST['category']
                drug.quantity = request.POST['quantity']
                print(drug.name)
                drug.save()

                return redirect('inventory:drugs_list')
        else:
            return render(request, 'inventory/edit_drug.html', {'drug': drug})
    else:
        return render(request, 'authentication/views/error.html', {})


