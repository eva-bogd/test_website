from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import ServiceForm
from .models import Service, Order


def home(request):
    services = Service.objects.all()
    context = {'services': services}
    return render(request, 'home.html', context)


def service_detail(request, service_id):
    service = get_object_or_404(Service, id=service_id)
    context = {'service': service}
    return render(request, 'services/service_detail.html', context)


@login_required
def service_create(request):
    form = ServiceForm(request.POST or None, files=request.FILES or None)
    if form.is_valid():
        service = form.save(commit=False)
        service.executor = request.user
        form.save()
        return redirect('users:profile', username=request.user)
    context = {'form': form}
    return render(request, 'services/service_create.html', context)


@login_required
def service_edit(request, service_id):
    service = get_object_or_404(Service, id=service_id)
    if request.user != service.executor:
        return redirect('services:service_detail', service_id=service.id)
    form = ServiceForm(
        request.POST or None,
        files=request.FILES or None,
        instance=service
    )
    if form.is_valid():
        form.save()
        return redirect('services:service_detail', service_id=service.id)
    context = {
        'form': form,
        'service': service,
        'is_edit': True
    }
    return render(request, 'services/service_create.html', context)


@login_required
def service_delete(request, service_id):
    service = get_object_or_404(Service, id=service_id)
    user = request.user
    if user != service.executor:
        return redirect('services:service_detail', service_id=service.id)
    service.delete()
    return redirect('users:profile', username=user.username)


@login_required
def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    context = {'order': order}
    return render(request, 'services/order_detail.html', context)


@login_required
def to_order(request, service_id):
    service = get_object_or_404(Service, id=service_id)
    user = request.user
    if user == service.executor:
        return redirect('services:service_detail', service_id=service.id)
    order = Order.objects.create(
        service=service,
        customer=user,
        executor=service.executor,
        name=service.name,
        description=service.description,
        price=service.price,
        status='TODO')
    return redirect('services:order_detail', order_id=order.id)


@login_required
def change_order_status(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    user = request.user
    if user == order.executor:
        allowed_statuses = ['TODO', 'IN_PROGRESS', 'IN_REVIEW', 'CANCEL']
    elif user == order.customer:
        allowed_statuses = ['TODO', 'TO_FIX', 'DONE', 'CANCEL']
    else:
        return redirect('services:service_detail', order_id=order_id)
    new_status = request.POST.get('new_status')
    if new_status in allowed_statuses:
        order.status = new_status
        order.save()
    return redirect('services:order_detail', order_id=order_id)
