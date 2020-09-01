import unittest
import main


class ShipmentTestCase(unittest.TestCase):
    def test_one_warehouse_shipment_1(self):
        warehouse_list = [{"name": "owd", "inventory": {"apple": 1}}]
        order = {"apple": 1}
        output = [{"owd": {"apple": 1}}]

        warehouse_object_list = []
        for warehouse in warehouse_list:
            warehouse_object_list.append(main.Warehouse(warehouse))

        self.assertEqual(main.compute_shipment(warehouse_object_list, order), output)

    def test_one_warehouse_shipment_2(self):
        warehouse_list = [{"name": "owd", "inventory": {"apple": 1, "banana": 5}}]
        order = {"apple": 1, "banana": 2}
        output = [{"owd": {"apple": 1, "banana": 2}}]

        warehouse_object_list = []
        for warehouse in warehouse_list:
            warehouse_object_list.append(main.Warehouse(warehouse))

        self.assertEqual(main.compute_shipment(warehouse_object_list, order), output)

    def test_multiple_warehouse_shipment(self):
        warehouse_list = [{"name": "owd", "inventory": {"apple": 5}}, {"name": "dm", "inventory": {"apple": 5}}]
        order = {"apple": 10}
        output = [{"owd": {"apple": 5}}, {"dm": {"apple": 5}}]

        warehouse_object_list = []
        for warehouse in warehouse_list:
            warehouse_object_list.append(main.Warehouse(warehouse))

        self.assertEqual(main.compute_shipment(warehouse_object_list, order), output)

    def test_multiple_warehouse_shipment_2(self):
        warehouse_list = [{"name": "owd", "inventory": {"apple": 5, "orange": 10}},
                          {"name": "dm", "inventory": {"banana": 5, "orange": 10}}]
        order = {"apple": 5, "banana": 5, "orange": 5}
        output = [{"owd": {"apple": 5, "orange": 5}}, {"dm": {"banana": 5}}]

        warehouse_object_list = []
        for warehouse in warehouse_list:
            warehouse_object_list.append(main.Warehouse(warehouse))

        self.assertEqual(main.compute_shipment(warehouse_object_list, order), output)

    def test_unavailability_warehouse_shipment_1(self):
        warehouse_list = [{"name": "owd", "inventory": {"apple": 0}}]
        order = {"apple": 1}
        output = []

        warehouse_object_list = []
        for warehouse in warehouse_list:
            warehouse_object_list.append(main.Warehouse(warehouse))

        self.assertEqual(main.compute_shipment(warehouse_object_list, order), output)

    def test_unavailability_warehouse_shipment_2(self):
        warehouse_list = [{"name": "owd", "inventory": {"apple": 1}}]
        order = {"apple": 2}
        output = []

        warehouse_object_list = []
        for warehouse in warehouse_list:
            warehouse_object_list.append(main.Warehouse(warehouse))

        self.assertEqual(main.compute_shipment(warehouse_object_list, order), output)

    def test_unavailability_warehouse_shipment_3(self):
        warehouse_list = [{"name": "owd", "inventory": {"apple": 1, "banana": 1}}]
        order = {"apple": 2, "banana": 1}
        output = []

        warehouse_object_list = []
        for warehouse in warehouse_list:
            warehouse_object_list.append(main.Warehouse(warehouse))

        self.assertEqual(main.compute_shipment(warehouse_object_list, order), output)

    def test_unavailability_warehouse_shipment_4(self):
        warehouse_list = []
        order = {"apple": 2, "banana": 1}
        output = []

        warehouse_object_list = []
        for warehouse in warehouse_list:
            warehouse_object_list.append(main.Warehouse(warehouse))

        self.assertEqual(main.compute_shipment(warehouse_object_list, order), output)

    def test_unavailability_warehouse_shipment_5(self):
        warehouse_list = [{"name": "owd", "inventory": {"apple": 1, "banana": 1}}]
        order = {}
        output = []

        warehouse_object_list = []
        for warehouse in warehouse_list:
            warehouse_object_list.append(main.Warehouse(warehouse))

        self.assertEqual(main.compute_shipment(warehouse_object_list, order), output)

    def test_unavailability_warehouse_shipment_6(self):
        warehouse_list = [{"name": "owd", "inventory": {"apple": 1, "banana": 1}}]
        order = {"mango": 1}
        output = []

        warehouse_object_list = []
        for warehouse in warehouse_list:
            warehouse_object_list.append(main.Warehouse(warehouse))

        self.assertEqual(main.compute_shipment(warehouse_object_list, order), output)


if __name__ == '__main__':
    unittest.main()
