from django.urls import path
from app.views import HomePage, SignUpPage, Dashboard, FileDelete


urlpatterns = [
    path("", HomePage.as_view(), name="login"),
    path("sign-up/", SignUpPage.as_view(), name="signup"),
    path("dashboard/", Dashboard.as_view(), name="dashboard"),
    path("dashboard/<str:logout>/", Dashboard.as_view(), name="dashboard"),
    path("file-delete/<int:id>/", FileDelete.as_view(), name="file-delete"),
]
