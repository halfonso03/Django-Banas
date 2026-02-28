from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import Article

class TestSite(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="sampleuser", email="h@yahoo.com", password='password'
        )
        
        self.article = Article.objects.create(
            title="Axehandle Hounds Ravage Minnesota",
            text = "lkasjdl lkaj kjskdj kasl lkjsakdj lak jsjk kk kja k askdjlkj ;asldj lalkjsk dkkd kdkf kdk kdk d kjkjlksdf lkdlkjf",
            author = self.user
        )
        
    def test_article_title(self):
        article = Article(title='Axehandle Hounds Ravage Minnesota')
        self.assertEqual(str(article), article.title)
        
    def test_setting_all(self):
        self.assertEqual(f'{self.article.title}', 'Axehandle Hounds Ravage Minnesota')
        self.assertEqual(f'{self.article.author}', 'sampleuser')
        self.assertEqual(f'{self.article.text}', 'lkasjdl lkaj kjskdj kasl lkjsakdj lak jsjk kk kja k askdjlkj ;asldj lalkjsk dkkd kdkf kdk kdk d kjkjlksdf lkdlkjf')
    
    def test_response(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Axehandle Hounds Ravage Minnesota')
        self.assertTemplateUsed(response, 'home.html')
        
    def test_article_detail_view(self):
        response = self.client.get('/article/1/')
        bad_response = self.client.get('/article/2/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(bad_response.status_code, 404)
        self.assertContains(response, 'Axehandle Hounds Ravage Minnesota')
        self.assertTemplateUsed(response, 'article_detail.html')
    

    def test_article_creation(self):
        response = self.client.post(reverse('add_article'), {
            'title': 'sample title', 'text': 'sample text', 'author': self.user
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'sample title')
        self.assertContains(response, 'sample text')
        
        
    def test_article_update(self):
       response = self.client.post(reverse('article_edit', args='1'), {
           'title':'new title',
           'text': 'new text'
       })
       self.assertEqual(response.status_code, 200)

    def test_article_delete(self):
        response = self.client.get(reverse('article_delete', args='1'))
        self.assertEqual(response.status_code, 200)
        