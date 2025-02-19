from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import AIModel


# List of AI Models
def ai_model_list(request):
    models = AIModel.objects.all()

    # Return a JSON depending on request (to help with testing)
    if request.headers.get("Accept") == "application/json":
        models_list = list(models.values("id", "name", "description", "author", "created_at"))
        return JsonResponse(models_list, safe=False)
    
    return render(request, 'ai_manager/ai_model_list.html', {'models': models})

# Create a new AI Model
def ai_model_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        createdModel = AIModel.objects.create(name=name, description=description)

        if request.headers.get("Accept") == "application/json":
            return JsonResponse({"id": createdModel.id, "name": createdModel.name, "description": createdModel.description, "author": createdModel.author}, status=201)
        return redirect('ai_model_list')
    return render(request, 'ai_manager/ai_model_form.html')

# Update
def ai_model_update(request, pk):
    ai_model = get_object_or_404(AIModel, pk=pk)
    if request.method == 'POST':
        ai_model.name = request.POST.get('name')
        ai_model.author = request.POST.get('author')
        ai_model.description = request.POST.get('description')
        ai_model.save()

        if request.headers.get("Accept") == "application/json":
            return JsonResponse({
                "id": ai_model.id,
                "name": ai_model.name,
                "author": ai_model.author,
                "description": ai_model.description
            }, status=200)

        return redirect('ai_model_list')
    
    return render(request, 'ai_manager/ai_model_form.html', {'model': ai_model})

# Delete
def ai_model_delete(request, pk):
    ai_model = get_object_or_404(AIModel, pk=pk)
    if request.method == 'POST':
        ai_model.delete()

        if request.headers.get("Accept") == "application/json":
            return JsonResponse({"message": "AI Model deleted successfully"}, status=204)
        
        return redirect('ai_model_list')
    return render(request, 'ai_manager/ai_model_confirm_delete.html', {'model': ai_model})
