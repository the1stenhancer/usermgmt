from django.test import TestCase
from django.test import Client, RequestFactory
from django.utils.translation import activate
from ..views import home, references, users


class NonAuthTestCase(TestCase):

    def setUp(self):
        self.c: Client = Client()
        self.rf: RequestFactory = RequestFactory()
    
    def tearDown(self):
        self.c = None
    
    def test_home_response_status_code_200(self):
        activate("en")
        res = self.c.get("/en/")
        self.assertEqual(res.status_code, 200)
    
    def test_home_view(self):
        activate("fr")
        request = self.rf.get("/fr/")
        resp = home(request)
        self.assertEqual(resp.status_code, 200)
    
    def test_references_view(self):
        activate("en")
        request = self.rf.get("/en/references")
        resp = references(request)
        self.assertEqual(resp.status_code, 200)
    
    def test_users_view(self):
        activate("fr")
        request = self.rf.get("/fr/users", {"page": 1})
        resp = users(request)
        print(resp)
        self.assertEqual(resp.status_code, 200)
