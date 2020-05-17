# SF-D4   
## Связь в slack:  @Игорь   

## Запуск  
1. Скачать папку buri  
2. В этой папке запустить сервер: python manage.py runserver  
3. Получить информацию по издательствам и их книгам здесь: http://127.0.0.1:8000/publishings/  
4. Админпанель: http://127.0.0.1:8000/admin/   
   (login: admin  password: sf123456)  
5. Список url-ов:  
   urlpatterns = [  
    path('admin/', admin.site.urls),  
    path('', views.books_list),  
    path('index/', views.index),  
    path('index/book_increment/', views.book_increment),  
    path('index/book_decrement/', views.book_decrement),  
    path('publishings/', views.publishings),  
]
