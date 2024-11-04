import io
import unittest
import pandas as pd
from app import app

class FlaskIntegrationTestCase(unittest.TestCase):

    def setUp(self):
        app.config['TESTING']= True
        self.client = app.test_client()

    
    def test_about_post(self):
        # Simulate posting data to the /about route
        response = self.client.post("/about", json={"content": "This is the about section content."})
        
        # Check if the post request was successful
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'About section updated successfully', response.data)

        def test_project_get(self):

            # Simulate getting data from the /Project route
            response= self.client.get("/Project")

        # Check if the request was successful
            self.assertEqual(response.status_code,200)
            self.assertIn(b'<!DOCTYPE html>' ,response.data)


# Including this line allows the script to be executed as a standalone program, running all the test cases in the file.

if __name__ == "__main__":
    # This function is a built-in command for running all test cases defined in the file.
    # It automatically discovers and runs all methods that start with test_ 
    unittest.main()

    # every module (file) has a built-in variable called __name__.
    # When a file is run directly, __name__ is set to "__main__".
    # However, if the file is imported into another file,
    # __name__ will be set to the module's name instead.