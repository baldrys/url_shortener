import string
import random


from django.conf import settings

SHORTCODE_MIN =  getattr(settings, "SHORTCODE_MIN", 6)

def code_generator(size=SHORTCODE_MIN, chars=string.ascii_letters + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def create_shortcode(instance, size=SHORTCODE_MIN):
    # Не можем импортировать .models потому что импортируем этот модуль
    # в сами модели, поэтому надо получить название класса из экземпляра
    Klass = instance.__class__
    new_code = code_generator(size=size)
    is_code_exists = Klass.objects.filter(shortcode=new_code).exists()
    # Рекурсия нужна для того что бы гарантировать уникальность случайной строки
    if is_code_exists:
        return create_shortcode(size=size)
    return new_code