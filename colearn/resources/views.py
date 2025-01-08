from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.views.generic import ListView
from django.urls import reverse_lazy
from .models import Resource
from .forms import ResourceForm

class ResourceCreateView(CreateView):
    model = Resource
    form_class = ResourceForm
    template_name = 'resource_create.html'
    success_url = reverse_lazy('resource_list')  # Redirect to a resource list page after creation


def resource_detail(request, pk):
    resource = Resource.objects.get(pk=pk)
    return render(request, 'resource_detail.html', {'resource': resource})


class ResourceListView(ListView):
    """Display a list of resources."""
    model = Resource
    template_name = 'resource_list.html'
    context_object_name = 'resources'
    paginate_by = 10  # Pagination to display 10 resources per page

    def get_queryset(self):
        """Filter resources by search term and tag."""
        queryset = super().get_queryset()

        # Search by title (if a search term is provided)
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(title__icontains=query)

        # Filter by tag (if a tag is selected)
        tag_name = self.request.GET.get('tag')
        if tag_name:
            queryset = queryset.filter(tags__name=tag_name)

        return queryset