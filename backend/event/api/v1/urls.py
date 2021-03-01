from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import (
    VendorViewSet,
    LocationViewSet,
    FavoritesViewSet,
    VendorDetailViewSet,
    CategoryViewSet,
    FaqViewSet,
    PresenterViewSet,
    ScheduleViewSet,
    MyScheduleViewSet,
    SponsorViewSet,
)

router = DefaultRouter()
router.register("presenter", PresenterViewSet)
router.register("vendor", VendorViewSet)
router.register("sponsor", SponsorViewSet)
router.register("myschedule", MyScheduleViewSet)
router.register("vendordetail", VendorDetailViewSet)
router.register("schedule", ScheduleViewSet)
router.register("location", LocationViewSet)
router.register("faq", FaqViewSet)
router.register("favorites", FavoritesViewSet)
router.register("category", CategoryViewSet)

urlpatterns = [
    path("", include(router.urls)),
]