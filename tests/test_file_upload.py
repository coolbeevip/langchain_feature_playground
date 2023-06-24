import os
import json
import unittest
from service.api import app


class TestUploadEndpoint(unittest.TestCase):

    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def test_upload_file(self):
        # 设置要上传的文件
        file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'fixtures', 'test.txt'))
        file = {'file': open(file_path, 'rb')}

        # 使用POST请求提交文件
        response = self.app.post('/api/upload', data=file, content_type='multipart/form-data')

        # 检查响应状态码是否为200
        self.assertEqual(response.status_code, 200)

        # 检查响应消息是否为'File uploaded successfully'
        json_data = json.loads(response.get_data())
        self.assertEqual(json_data['message'], 'File uploaded successfully')


if __name__ == '__main__':
    unittest.main()
