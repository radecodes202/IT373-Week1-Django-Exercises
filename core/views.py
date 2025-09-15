from django.shortcuts import render

def home(request):
    """View for the home page"""
    return render(request, 'home.html')

def about(request):
    """View for the about page with student information"""
    context = {
        'name': 'Niño Junehll B. Edar',  # Replace with your actual name
        'student_id': '2023-02128',  # Replace with your actual student ID
    }
    return render(request, 'about.html', context)