from django.test import TestCase
from django.contrib.auth.models import AnonymousUser, User
from django.utils import timezone
from ..models import Detail


class DetailTestCase(TestCase):
    
    def setUp(self):
        self.user: User = User.objects.create_user(
            username="test1",
            email="firsttest1.lasttest1@example.com",
            password="Easy.26!!"
        )
        self.anon_user = AnonymousUser()
        self.detail: Detail = Detail.objects.create(
            **{
                "user": self.user,
                "phone": "237 620 222 208",
                "married": "Yes",
                "kids": 2,
                "dob": timezone.datetime.date(timezone.datetime(1785, 2, 26)),
                "doh": timezone.datetime.date(timezone.datetime(2024, 1, 1)),
                "title": "Senior Data Scientist",
                "duration": 4,
            }
        )
    
    def tearDown(self):
        self.user = None
        self.anon_user = None
        self.detail = None
    
    def test_age_works(self):
        self.assertEqual(self.detail.age(), 239)
    
    def test_end_of_hire_date(self):
        dates = [
            timezone.datetime.date(timezone.datetime(2024, 1, 1) + timezone.timedelta(days=self.detail.duration*365)),
        ]
        for d in dates:
            with self.subTest(msg=f"MSG: {self.detail.doh}", d=d):
                self.assertEqual(self.detail.eoh(), d)
