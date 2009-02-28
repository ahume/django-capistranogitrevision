from settings import SITE_ROOT
import os

from django.core.cache import cache

def current_build(request):
    rev = cache.get('rev')
    if rev is None:
        try:
            rev = open(os.path.join(SITE_ROOT, "REVISION")).read().strip()
            cache.set('rev', rev)
        except:
            rev = ''

    return {
        'current_build': rev
    }