# django-field-tutorial

Django ORM and Relationship Field

認識 [Django](https://www.djangoproject.com/)  **OneToOneField** , **ForeignKey** ,**ManyToManyField**  📝

為什麼我會把這三個特別拿出來講呢 ？ 因為他會影響到你設計資料庫，更影響到你的整體架構。

* [Youtube Tutorial - part1](https://youtu.be/b2W7aJjbbC0)

* [Youtube Tutorial - OneToOneField - part2](https://youtu.be/tYV2pmpTGEU)

* [Youtube Tutorial - ForeignKey - part3](https://youtu.be/1RkipG5YQO0)

* [Youtube Tutorial - ManyToManyField - part4](https://youtu.be/f3YZIHUTzMg)

建議對 [Django](https://github.com/django/django) 不熟悉的朋友，可以先觀看我之前寫的文章（ 先認識一下 [Django](https://github.com/django/django) ）

* [Django 基本教學 - 從無到有 Django-Beginners-Guide](https://github.com/twtrubiks/django-tutorial)

## 我可以從這篇學到什麼

* OneToOneField
* ForeignKey
* ManyToManyField

## 安裝套件

請在 cmd ( 命令提示字元 ) 輸入以下指令

```python
pip install django==4.2.3
```

如果你想要使用 PostgreSQL, 請多安裝

```python
pip install psycopg2==2.9.6
```

並且修改 [settings.py](https://github.com/twtrubiks/django-field-tutorial/blob/master/django_field_tutorial/settings.py)

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER': 'myuser',
        'PASSWORD': 'password123',
        'HOST': 'localhost',
        'PORT': 5432,
    }
}
```

## 教學

我們先透過 OneToOneField_tutorial 來認識基本的流程，所以請將 [settings.py](https://github.com/twtrubiks/django-field-tutorial/blob/master/django_field_tutorial/settings.py) 裡的 INSTALLED_APPS修改一下，修改如下

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'OneToOneField_tutorial',
    # 'ForeignKey_tutorial',
    # 'ManyToManyField_tutorial',
]
```

在 OneToOneField_tutorial 的 [models.py](https://github.com/twtrubiks/django-field-tutorial/blob/master/OneToOneField_tutorial/models.py) 裡，有我們事先寫好的 model，

我們先 makemigrations

```python
python manage.py makemigrations OneToOneField_tutorial
```

接著你應該會看到這類的文件訊息

```cmd
Migrations for 'OneToOneField_tutorial':
  OneToOneField_tutorial\migrations\0001_initial.py
    - Create model Profile
```

接著我們再透過 sqlmigrate 指令來看 migration 將會執行的 SQL，

下面這行並不會馬上執行你的 SQL

```cmd
python manage.py sqlmigrate OneToOneField_tutorial 0001
```

接著你應該會看到這類的文件訊息

```cmd
BEGIN;
--
-- Create model Profile
--
CREATE TABLE "OneToOneField_tutorial_profile" ("user_id" integer NOT NULL PRIMARY KEY REFERENCES "auth_user" ("id"), "date_of_birth" date NULL);
COMMIT;
```

上面這些資訊能幫助你更了解對資料庫做了什麼事情

***sqlmigrate 這個指令是可以省略的，我建議可以執行這個指令多去了解將會執行的 SQL***

最後我們再 migrate

( 這行才會幫你執行 SQL )

```python
python manage.py migrate
```

***不管你對 model 做了任何的 新增，修改，刪除，請記得一定要再執行 makemigrations 以及 migrate***

以上是基本的流程，接著我要進入今天的主題 :grin:

## OneToOneField

 OneToOneField 官方文件的參考

[https://docs.djangoproject.com/en/4.2/topics/db/examples/one_to_one/](https://docs.djangoproject.com/en/4.2/topics/db/examples/one_to_one/)

[https://docs.djangoproject.com/en/4.2/ref/models/fields/#django.db.models.OneToOneField](https://docs.djangoproject.com/en/4.2/ref/models/fields/#django.db.models.OneToOneField)

在 OneToOneField_tutorial 的 [models.py](https://github.com/twtrubiks/django-field-tutorial/blob/master/OneToOneField_tutorial/models.py) 裡，有我們事先寫好的 model，

 [models.py](https://github.com/twtrubiks/django-field-tutorial/blob/master/OneToOneField_tutorial/models.py) 裡面的程式碼如下

```python
class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        primary_key=True
    )
    date_of_birth = models.DateField(blank=True, null=True)

    def __str__(self):
        return f'Profile for user {self.user.username}'
```

OneToOneField 我們最常用的時機就是擴充 ( extends )，舉個例子，

Django 的 User Model 預設已經有一些存在的 field ，但很多時候我們

常常需要增加一些額外的資料，像是需要記錄使用者的生日，這時候

OneToOneField 就派上用場了。建立一個 Profile 的 model，透過

OneToOneField 和 User Model 建立 ***一對一 （ one-to-one ）*** 的關係。

我在再透過 python console 來把玩一下，

我們先建立一個 user

```python
from django.contrib.auth.models import User

# create user
user = User.objects.create_user(username='user1',email='user@test.com',password='password123')
```

接著再加入 Profile

```python
from OneToOneField_tutorial.models import Profile

import datetime

# create profile
profile=Profile.objects.create(user=user,date_of_birth=datetime.datetime(2017,2,3))
```

```python
profile.user
> <User: user1>
```

也可以反查

```python
# via user get profile
user = User.objects.get(username='user1')
user.profile
> <Profile: Profile for user user1>
```

為什麼可以反查？

原因是 Profile model 裡的 user 被我們設定為  primary key。

P.S 在 model 裡的 on_delete=models.CASCADE ，

可以幫助你刪除資料時一併刪除。

其他的一些例子

```python
# 找出 username 開頭是 user
Profile.objects.filter(user__username__startswith="user")
> <QuerySet [<Profile: Profile for user user1>]>

# 排除 username 開頭是 user
Profile.objects.exclude(user__username__contains="user")
> <QuerySet []>
```

## ForeignKey

ForeignKey 官方文件的參考

[https://docs.djangoproject.com/en/4.2/topics/db/examples/many_to_one/](https://docs.djangoproject.com/en/4.2/topics/db/examples/many_to_one/)

[https://docs.djangoproject.com/en/4.2/ref/models/fields/#django.db.models.ForeignKey](https://docs.djangoproject.com/en/4.2/ref/models/fields/#django.db.models.ForeignKey)

在 ForeignKey_tutorial 的 [models.py](https://github.com/twtrubiks/django-field-tutorial/blob/master/ForeignKey_tutorial/models.py) 裡，有我們事先寫好的 model，

 [models.py](https://github.com/twtrubiks/django-field-tutorial/blob/master/ForeignKey_tutorial/models.py) 裡面的程式碼如下

```python

class Reporter(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Article(models.Model):
    headline = models.CharField(max_length=100)
    pub_date = models.DateField()
    reporter = models.ForeignKey(
        Reporter,
        related_name='articles',
        on_delete=models.CASCADE,
        db_index=True # 預設為 True, 會自動幫你建立 index
    )

    # reporter = models.ForeignKey(
    #     Reporter,
    #     on_delete=models.CASCADE)

    def __str__(self):
        return self.headline

    class Meta:
        # ref
        # https://docs.djangoproject.com/en/4.2/ref/models/options/#ordering
        ordering = ["headline"]

        # unique_together = ['headline', 'reporter']
        # indexes = [
        #     models.Index(name='headline_reporter_index', fields=['headline','reporter'],)
        # ]

        # index 建議使用 Meta.indexes, db_index 未來可能會棄用
        # ref
        # https://docs.djangoproject.com/en/4.2/ref/models/fields/#db-index
```

以上面這個例子來說，我們有一個  Reporter 記者 model 以及一個 Article 文章 model。

在 Article model 中，我們定義了 ForeignKey ，因為一篇文章只屬於一個記者的，而一

個記者可以寫很多篇文章，所以是屬於 ***多對一 （ many-to-one ）*** 的關係。

註解掉的部份是要和大家解釋，假如你沒有定義 `related_name` 這個屬性，這樣當你需

要反查回去時，你需要使用 Django model 的名稱再加上 `_set`，以範例來說，就是 `article_set`。

我在再透過 python console 來把玩一下，

```python

from ForeignKey_tutorial.models import Reporter,Article

# create reporter
reporter = Reporter.objects.create(first_name='John', last_name='Smith', email='john@example.com')

import datetime

date=datetime.datetime(2017,2,3)

# create article
article = Article.objects.create(headline="This is a test", pub_date=date, reporter=reporter)
```

```python
# via article get reporter
article.reporter
> <Reporter: John Smith>
```

```python
article.reporter.id
> 1
```

也可以反查

```python

reporter.articles.all()

# if not set related_name
# reporter.article_set.all()

> <QuerySet [<Article: This is a test>]>

```

上面兩個結果是一樣的，只是差在是否有設定 `related_name`

透過 Reporter object，建立一個 Article object

```python
# create an article via the reporter object:
new_article = reporter.articles.create(headline="John's second story", pub_date=date)

# new_article = reporter.article_set.create(headline="John's second story", pub_date=date)

new_article.reporter
> <Reporter: John Smith>

```

其他的一些例子

```python
# 將 article2 的 reporter 從 John Smith -> Tony Shen
reporter2 = Reporter.objects.create(first_name='Tony', last_name='Shen', email='tony@example.com')
article2 = Article.objects.get(headline="This is a test")
article2.reporter
> <Reporter: John Smith>
reporter2.articles.add(article2)
article2.reporter
> <Reporter: Tony Shen>
```

其他的一些例子

```python
reporter.articles.filter(headline__startswith="This")
> <QuerySet [<Article: This is a test>]>

Article.objects.filter(reporter__first_name="John")
> <QuerySet [<Article: John's second story>, <Article: This is a test>]>

# 列出全部 reporter id 為 1 或 2 的
Article.objects.filter(reporter__in=[1, 2])

# 列出全部 reporter id 為 reporter 物件, 放 id 或 物件 都可以
Article.objects.filter(reporter__in=[reporter])

# 列出全部 reporter id 為 1 或 2 的, 並且根據 headline 下去做 distinct
# ref postgresql
# https://docs.djangoproject.com/en/4.2/ref/models/querysets/#distinct
Article.objects.filter(reporter__in=[1, 2]).order_by("headline").distinct("headline")
```

## ManyToManyField

 ManyToManyField 官方文件的參考

[https://docs.djangoproject.com/en/4.2/topics/db/examples/many_to_many/](https://docs.djangoproject.com/en/4.2/topics/db/examples/many_to_many/)

[https://docs.djangoproject.com/en/4.2/ref/models/fields/#django.db.models.ManyToManyField](https://docs.djangoproject.com/en/4.2/ref/models/fields/#django.db.models.ManyToManyField)

在 ManyToManyField 的 [models.py](https://github.com/twtrubiks/django-field-tutorial/blob/master/ManyToManyField_tutorial/models.py) 裡，有我們事先寫好的 model，

 [models.py](https://github.com/twtrubiks/django-field-tutorial/blob/master/ManyToManyField_tutorial/models.py) 裡面的程式碼如下

```python

class Image(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    created = models.DateField(auto_now_add=True)
    users_like = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='images_like'
    )

```

以上面這個例子來說，我們建立一個 Image model ，一張圖片可以有很多使用者喜歡，

而一個使用者也可以喜歡多張圖片，所以他們是 ***多對多（ many-to-many ）*** 的關係。

當你建立多對多（ many-to-many ）的關係時，你會發現被多建立一張表，這張表是用來

記錄多對多的關係。

註解掉的部份是要和大家解釋，假如你沒有定義 `related_name` 這個屬性，這樣當你需要

反查回去時，你需要使用 Django model 的名稱再加上 `_set`，以範例來說，就是 `image_set`

再透過 python console 來把玩一下，

建立 user

```python

from django.contrib.auth.models import User

user1 = User.objects.create_user(username='user1',email='user@test.com',password='password123')

user2 = User.objects.create_user(username='user2',email='user2@test.com',password='password123')

```

```python

from ManyToManyField_tutorial.models import Image

# create image
image = Image.objects.create(title='img1')

# add users via image
image.users_like.add(user1)
image.users_like.add(user2)

# get users via image
image.users_like.all()
> <QuerySet [<User: user1>, <User: user2>]>

# get images via users
user1.images_like.all()
> <QuerySet [<Image: Image object>]>

```

## 後記

 這次介紹了 [Django](https://www.djangoproject.com/)  的 **OneToOneField** , **ForeignKey** , **ManyToManyField** ，

 除了幫助大家更了解他們的關係之外，更簡單介紹適合的情境，希望能對大

 家在設計架構時有幫助，這三個 Field 看似簡單，但值得深入去了解他 :satisfied:。

## 執行環境

* Python 3.8

## Reference

* [Django](https://www.djangoproject.com/)

## License

MIT license