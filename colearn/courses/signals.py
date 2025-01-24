from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import CourseEnrollment

@receiver(post_save, sender=CourseEnrollment)
def handle_course_enrollment(sender, instance, created, **kwargs):
    if created:
        # Actions to take when a new enrollment is created
        print(f"{instance.student.username} enrolled in {instance.course.title}")
        # Example: Send a welcome email
        # send_welcome_email(instance.student, instance.course)
        # Update course enrollment count
        instance.course.enrollment_count += 1
        instance.course.save()
