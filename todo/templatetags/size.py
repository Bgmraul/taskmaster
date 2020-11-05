from django import template

register = template.Library()

SIZES = {
    1: ('XS','Extra Small'),
    2: ('S', 'Small'),
    3: ('M', 'Medium'),
    4: ('L', 'Large'),
    5: ('XL' 'Extra Large')
}

@register.filter
def as_task_size(size_level, format="short"):
    size = SIZES.get(size_level, size_level)
    index = 0
    if format=='extend':
        index = 1
    
    return size[index]
