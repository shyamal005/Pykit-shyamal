# tests/test_io.py

import unittest
import os
import tempfile
import json
from pykit import io

class TestIO(unittest.TestCase):

    def setUp(self):
       
        self.test_dir = tempfile.TemporaryDirectory()

    def tearDown(self):
       
        self.test_dir.cleanup()

    def test_read_write_json(self):
        filepath = os.path.join(self.test_dir.name, 'test.json')
        data = {'name': 'pykit', 'version': '0.1.0'}
        
        io.write_json(filepath, data)
        read_data = io.read_json(filepath)
        
        self.assertEqual(data, read_data)

    def test_atomic_write(self):
        filepath = os.path.join(self.test_dir.name, 'atomic.txt')
        content = "Hello, atomic world!"
        
       
        io.atomic_write(filepath, content)
        with open(filepath, 'r') as f:
            self.assertEqual(f.read(), content)
            
      
        with self.assertRaises(FileExistsError):
            io.atomic_write(filepath, "new content")
            
       
        new_content = "Hello again!"
        io.atomic_write(filepath, new_content, overwrite=True)
        with open(filepath, 'r') as f:
            self.assertEqual(f.read(), new_content)

    def test_read_lines(self):
        filepath = os.path.join(self.test_dir.name, 'lines.txt')
        lines_content = "first line\nsecond line\n third line with space \n"
        with open(filepath, 'w') as f:
            f.write(lines_content)
            
        
        lines = io.read_lines(filepath)
        self.assertEqual(lines, ['first line', 'second line', 'third line with space'])
        
       
        lines_no_strip = io.read_lines(filepath, strip_whitespace=False)
        self.assertEqual(lines_no_strip, ["first line\n", "second line\n", " third line with space \n"])

if __name__ == '__main__':

    unittest.main()
