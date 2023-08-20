from rest_framework import serializers
from .models import Course, Levels, Plans, Schedule, ScheduleTiming
from home.serializers import FAQsSerializer
from datetime import date
from user.serializers import kidInfoSerializer
from home.models import Review

class PlansSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plans
        fields = ['id', 'name','slug', 'description', 'price', 'discounted_price', 'discount_percent']

class CourseSerializerSmall(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'name','course_icon', 'slug']

class LevelsSerializer(serializers.ModelSerializer):
    to_course = CourseSerializerSmall(many=False, read_only=True)
    class Meta:
        model = Levels
        fields = ['id', 'name', 'description', 'num_classes', 'frequency', 'duration', 'starts_from', 'to_course']

class CourseSerializer(serializers.ModelSerializer):
    my_levels = LevelsSerializer(many=True, read_only=True)
    course_faqs = FAQsSerializer(many=True, read_only=True)
    review_count = serializers.SerializerMethodField()
    average_rating = serializers.SerializerMethodField() 
    max_capacity = serializers.SerializerMethodField() 

    class Meta:
        model = Course
        fields = [
            'id', 'name','course_icon', 'course_banner', 'slug', 
            'overview', 'about_guru', 'my_levels', 'course_faqs', 
            'review_count', 'average_rating', 'max_capacity'
        ]

    def get_review_count(self, obj):
        return Review.objects.filter(to_course=obj).count()
    
    def get_average_rating(self, obj):
        reviews = Review.objects.filter(to_course=obj)
        if reviews.exists():
            total_rating = sum(review.rating for review in reviews)
            average = total_rating / reviews.count()
            return round(average, 2)  # Round the average to 2 decimal places
        return 0.0  # Return 0 if there are no reviews
    
    def get_max_capacity(self, obj):
        return obj.get_max_capacity()
    

class ScheduleTimingSerializer(serializers.ModelSerializer):
    day = serializers.SerializerMethodField()
    class Meta:
        model = ScheduleTiming
        fields = ['id', 'date', 'start_time', 'end_time', 'day']
    
    def get_day(self, obj):
        return obj.date.strftime("%A")

class ScheduleSerializer(serializers.ModelSerializer):
    timing = ScheduleTimingSerializer(many=True, read_only=True)
    to_course = CourseSerializer(many=False, read_only=True)
    class Meta:
        model = Schedule
        fields = ('id', 'schedule_name', 'start_date', 'end_date', 'seats_left', 'timing', 'to_course')
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        current_date = date.today()
        
        if instance.end_date < current_date:
            """If end date has passed, return an empty representation"""
            representation = {}
        
        return representation   