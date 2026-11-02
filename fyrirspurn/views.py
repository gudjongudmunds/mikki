
from django.shortcuts import render, redirect
from .forms import InquiryForm

def fyrirspurn_view(request):
    if request.method == 'POST':
        form = InquiryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('confirmation')  # Redirect to confirmation page
    else:
        form = InquiryForm()
    return render(request, 'fyrirspurn/fyrirspurn.html', {'form': form})

def confirmation_view(request):
    return render(request, 'fyrirspurn/confirmation.html')