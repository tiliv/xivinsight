from django.conf.urls import url, include

from rest_framework.routers import DefaultRouter

from . import api, views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'attacktype', api.AttackTypeViewSet)
router.register(r'combatant', api.CombatantViewSet)
router.register(r'current', api.CurrentViewSet)
router.register(r'damagetype', api.DamageTypeViewSet)
router.register(r'encounter', api.EncounterViewSet)
router.register(r'swing', api.SwingViewSet)

# The API URLs are now determined automatically by the router.
# Additionally, we include the login URLs for the browseable API.
urlpatterns = [
    url(r'^$', views.site),
    url(r'^api/act/', include(router.urls)),
    # url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
