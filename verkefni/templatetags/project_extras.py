from django import template

register = template.Library()

@register.filter
def project_images(project):
    return [
        img for img in [
            project.image1,
            project.image2,
            project.image3,
            project.image4,
            project.image5,
            project.image6
        ] if img
    ]