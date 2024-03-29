from django.urls import path
from .views import getAllCourses, getCourseData, getAllSchedules, getTheScheduleGuru

urlpatterns = [
    path('all/',  getAllCourses, name="courses-all"),
    path('<str:course_slug>/',  getCourseData, name="course-data"),
    path('schedules/<str:course_level_id>/',  getAllSchedules, name="schedules-all"),
    path('schedule/guru/<str:course_level_id>/',  getTheScheduleGuru, name="schedules-guru"),
]