from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from pytils.translit import slugify
from blogging.models import Blog


class BlogListView(ListView):
    model = Blog

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset().order_by(*args, **kwargs)
        queryset = queryset.filter(is_published=True)
        return queryset


class BlogDetailView(DetailView):
    model = Blog

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.view_count += 1
        self.object.save()
        return self.object


class BlogCreateView(CreateView):
    model = Blog
    fields = ('title', 'body', 'image', 'create_at', 'slug', 'is_published',)
    success_url = reverse_lazy('blogging:list')

    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.title)
            new_blog.save()

        return super().form_valid(form)


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ('title', 'body', 'image', 'create_at', 'slug', 'is_published',)

    def get_success_url(self):
        return reverse('blogging:detail', args=[self.kwargs.get('pk')])


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('blogging:list')


def publication(request, pk):
    publication_item = get_object_or_404(Blog, pk=pk)
    if publication_item.is_published:
        publication_item.is_published = False
    else:
        publication_item.is_published = True
    publication_item.save()
    return redirect(reverse('blogging:list'))
