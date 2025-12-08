from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.db.models import F
from .models import BlogPost


# CBV - классы для блога БЕЗ авторизации
class BlogPostListView(ListView):
    model = BlogPost
    template_name = 'blog/blogpost_list.html'
    context_object_name = 'blogposts'

    def get_queryset(self):
        # Выводим только опубликованные статьи
        return BlogPost.objects.filter(is_published=True)


class BlogPostDetailView(DetailView):
    model = BlogPost
    template_name = 'blog/blogpost_detail.html'
    context_object_name = 'blogpost'

    def get_object(self, queryset=None):
        # Получаем объект и увеличиваем счетчик просмотров
        obj = super().get_object(queryset)
        BlogPost.objects.filter(pk=obj.pk).update(views_count=F('views_count') + 1)
        obj.views_count += 1  # Обновляем объект для текущего контекста
        return obj


class BlogPostCreateView(CreateView):
    model = BlogPost
    template_name = 'blog/blogpost_form.html'
    fields = ['title', 'content', 'preview', 'is_published']
    success_url = reverse_lazy('blog:blogpost_list')


class BlogPostUpdateView(UpdateView):
    model = BlogPost
    template_name = 'blog/blogpost_form.html'
    fields = ['title', 'content', 'preview', 'is_published']

    def get_success_url(self):
        # Перенаправляем на страницу отредактированной статьи
        return reverse('blog:blogpost_detail', kwargs={'pk': self.object.pk})


class BlogPostDeleteView(DeleteView):
    model = BlogPost
    template_name = 'blog/blogpost_confirm_delete.html'
    success_url = reverse_lazy('blog:blogpost_list')