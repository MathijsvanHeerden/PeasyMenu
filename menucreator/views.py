from django.http import HttpResponse, HttpResponseBadRequest
from .models import *
from django.template import loader
# Create your views here.


def index(request):
    menus = Menu.objects.filter(owner=request.user)
    template = loader.get_template('menu_links.html')
    context = {'menus': menus}
    return HttpResponse(template.render(context, request))


def wordpress(request, menu_id):
    menu = Menu.objects.filter(owner=request.user, id=menu_id).first()
    if menu is not None:
        form_string = "<h1> {} </h1> \n".format(menu.name)

        for category in menu.menucategory_set.all():
            form_string += "<h3> {} </h3> \n".format(category.name)

            for menuitem in category.menu_items.all():
                form_string += "<label> {} </label>".format(menuitem.name)
                form_string += "[checkbox* {} {}]".format(menuitem.name, menuitem.price)
                form_string += "[number {} min:0 max:{}]".format(menuitem.name, menuitem.max_quantity)

            return HttpResponse(form_string, content_type="text/plain")
    return HttpResponseBadRequest("This aint your menu boyyy")

