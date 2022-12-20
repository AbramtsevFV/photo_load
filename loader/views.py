from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

from loader.form import ImageForm


class HomePage(View):
    template_name = "loader/start_page.html"

    def get(self, request):
        form = ImageForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            img_obj = form.instance
            # Результат обработки
            result = 'На фото поза собаки'
            return render(request, self.template_name, {'form': form, 'img_obj': img_obj, 'result': result})
