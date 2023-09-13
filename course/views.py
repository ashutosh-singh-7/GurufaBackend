from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Course, Plans, Levels, Schedule
from .serializers import CourseSerializer, LevelsSerializer, PlansSerializer, ScheduleSerializer
from datetime import date, datetime, timedelta
from django.db.models import Min


@api_view(http_method_names=['GET'])
def getAllCourses(request):    
    courses = Course.objects.filter(is_active=True)
    course_serializer = CourseSerializer(courses, many=True)

    data = {            
        'courses': course_serializer.data
    }
    return Response(data)               

# @api_view(['GET'])
# def getAllSchedules(request, course_id):
#     try:
#         course = Course.objects.get(id=course_id)
#         plan = Plans.objects.get(slug=request.GET.get('plan_slug'))
#         schedules = Schedule.objects.filter(to_course=course, plan=plan, is_active=True)
#         serializer = ScheduleSerializer(schedules, many=True)
        
#         return Response(serializer.data)
#     except Course.DoesNotExist or Plans.DoesNotExist:
#         return Response({'error': 'Course or Plan not found.'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def getAllSchedules(request, course_id):
    try:
        course = Course.objects.get(id=course_id)
        plan = Plans.objects.get(slug=request.GET.get('plan_slug'))
        
        # Filter schedules with a start date in the future
        now = datetime.now()
        schedules_all = Schedule.objects.filter(to_course=course, plan=plan, is_active=True)
        schedules = []
        for schedule in schedules_all:
            timings = schedule.timing.filter(is_active=True)
            earliest_date = timings.aggregate(earliest_date=Min('date'))['earliest_date']
            earliest_timing = timings.filter(date=earliest_date)[0]
            schedule_time = datetime.combine(earliest_timing.date, earliest_timing.start_time)
            if(schedule_time > now):
                schedules.append(schedule)
        
        serializer = ScheduleSerializer(schedules, many=True)
        
        return Response(serializer.data)
    except (Course.DoesNotExist, Plans.DoesNotExist):
        return Response({'error': 'Course or Plan not found.'}, status=status.HTTP_404_NOT_FOUND)