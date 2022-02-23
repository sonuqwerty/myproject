from django import template

register = template.Library()

@register.filter(name = 'isexistincart')
def isexistincart(product,cart):
    keys = cart.keys()
    print(keys)
    for id in keys:
        if int(id) == product.id:
            return True
    return False 

@register.filter(name = "cartquantity")
def cartquantity(product,cart):
    keys = cart.keys()
    print(keys)
    for id in keys:
        if int(id) == product.id:
            return cart.get(id)
    return False 
@register.filter(name = "total")
def total(product,cart):
    return product.price * cartquantity(product,cart)


@register.filter(name = "grand_total")
def grand_total(product,cart):
    sum = 0 
    for p in product:
        sum += total(p,cart)
    return sum

@register.filter(name = "multiplyprice")
def multiplyprice(num1,num2):
    return num1*num2


    return product.price * cartquantity(product,cart)
