from django.shortcuts import render, redirect
from .models import Textbook

def search(request):
   
    if request.method == 'POST':
        
        course_code = request.POST.get('course_code')
        if course_code: #this is here to ensure that the user doesnt search with an emply field if ykwim    
            return redirect('textbook_list', course_code=course_code) 
        
    return render(request, 'search.html')


def textbook_list(request, course_code):

    textbooks = Textbook.objects.filter(course_code=course_code, available=True) # search the database for textbooks matching the course code and availability

    if textbooks.exists():
        
        return render(request, 'textbook_list.html', {'textbooks': textbooks, 'course_code': course_code, 'no_results': False})
    else:
        # use a temporary course code If no textbooks are found and show a no results message
        temp_course_code = 'TEMP_COURSE'  # Temporary course code to display a message that no book is found for the course code provided
        message = f"No textbooks are currently available for {course_code}. Try another course or check back later."
        return render(request, 'textbook_list.html', {'course_code': course_code, 'no_results': True, 'message': message, 'temp_course_code': temp_course_code})
