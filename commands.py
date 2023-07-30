user_1 = User.objects.create_user(username='User_1')

user_2 = User.objects.create_user(username='User_2')

from NewsPortal import *

author_1 = Author.objects.create(author=user_1)

author_2 = Author.objects.create(author=user_2)

category_1 = Category.objects.create(category='Кино')

category_2 = Category.objects.create(category='Музыка')

category_3 = Category.objects.create(category='Политика')

category_4 = Category.objects.create(category='Игры')

author1 = Author.objects.get(id=1)

author2 = Author.objects.get(id=2)

post_1 = Post.objects.create(type_post='AR', headline='Заогловок для статьи_1',
							 text='Большой текст статьи_1', to_author=author1)

post_2 = Post.objects.create(type_post='AR', headline='Заогловок для статьи_2',
							 text='Большой текст статьи_2', to_author=author1)

post_3 = Post.objects.create(type_post='NW', headline='Заогловок для новости_1',
							 text='Большой текст новости_1', to_author=author2)

Post.objects.get(id=1).to_many_category.add(Category.objects.get(id=1))

Post.objects.get(id=2).to_many_category.add(Category.objects.get(id=3))

Post.objects.get(id=3).to_many_category.add(Category.objects.get(id=2))

Post.objects.get(id=3).to_many_category.add(Category.objects.get(id=4))

comm_1 = Comment.objects.create(text='Текст комментария_1', comm_user=user_1, comm_post=post_1)

comm_2 = Comment.objects.create(text='Текст комментария_1', comm_user=user_2, comm_post=post_1)

comm_3 = Comment.objects.create(text='Текст комментария_1', comm_user=user_1, comm_post=post_2)

comm_4 = Comment.objects.create(text='Текст комментария_1', comm_user=user_1, comm_post=post_3)