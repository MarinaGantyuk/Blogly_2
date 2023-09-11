from app import app
import unittest

class TestSimpleRoutes(unittest.TestCase):
    async def test_edit_userbefore(self):
        tester = app.test_client(self)
        response = await tester.post("/users/4/edit", data={
            "first_name": "Angelina",
            "last_name": "Jolie",
            "image_url": "picture.png"
        })
        self.assertEqual(response.status_code, 302)


    async def test_home(self):
        tester = app.test_client(self)
        response = tester.get('/users', content_type='html/text')
        self.assertIn(b'Angelina', response.data)
        self.assertEqual(response.status_code, 200)

    async def test_edit_user(self):
        tester = app.test_client(self)
        response = await tester.post("/users/4/edit", data={
            "first_name": "Marina",
            "last_name": "Jolie",
            "image_url": "picture.png"
        })
        self.assertEqual(response.status_code, 302)

    async def test_user_afterupdate(self):
        tester = app.test_client(self)
        response = tester.get('/users', content_type='html/text')
        self.assertIn(b'Marina', response.data)
        self.assertEqual(response.status_code, 200)
        
    async def test_user_detailpage(self):
        tester = app.test_client(self)
        response = tester.get('/users/4', content_type='html/text')
        self.assertIn(b'Marina', response.data)
        self.assertEqual(response.status_code, 200)

    async def test_user_add_post(self):
        tester = app.test_client(self)
        response = await tester.post("/users/4/posts/new", data={
            "title": "Hi world",
            "content": "Happy",
            
        })
        self.assertEqual(response.status_code, 302)

    async def test_post_presentondetailpage(self):
        tester = app.test_client(self)
        response = tester.get('/users/4', content_type='html/text')
        self.assertIn(b'Hi world', response.data)
        self.assertEqual(response.status_code, 200)

    
        
        

