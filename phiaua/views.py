from django.http import JsonResponse
from phiaua.models import Khuán


def khuan(request, khuan_id):
    khuán = Khuán.objects.prefetch_related('luī').first()
    return JsonResponse({
        'iunn': khuán.iūnn,
        'suan': list(khuán.luī.values('id', 'miâ', 'siktsuí')),
    })
