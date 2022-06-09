from rest_framework.test import APITestCase
from rest_framework import status


class StockTestApi(APITestCase):

    def create_stock(self):
        example_data = {
            "name": "example product",
            "stock_value": 45,
        }
        response = self.client.post("/stock/api/", example_data)
        return response


class StockListTest(StockTestApi):

    def test_create(self):
        response = self.create_stock()
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_stock_list(self):
        response = self.client.get("/stock/api/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class StockDetailTest(StockTestApi):

    def test_stock_detail(self):
        example_data = self.create_stock()
        response = self.client.get(f"/stock/api/{example_data.data['id']}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_stock_update(self):
        example_data = self.create_stock()
        new_data = {
            "name": "update product",
            "stock_value": 100,
        }
        response = self.client.put(f"/stock/api/{example_data.data['id']}/", new_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
