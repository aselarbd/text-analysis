from rest_framework import routers
from SampleAPI.SampleAPI_API import SampleAPIViewSet


router = routers.DefaultRouter()
router.register('SampleAPI', SampleAPIViewSet, 'SampleAPI')

urlpatterns = router.urls
