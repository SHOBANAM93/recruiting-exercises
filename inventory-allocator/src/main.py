import json


class Warehouse:

    def __init__(self, inventory_items):
        for key, value in inventory_items.items():
            setattr(self, key, value)


def compute_shipment(ware_list, order_obj):
    shipment_list = []
    for ware in ware_list:

        ware_dict = {}
        for item, value in order_obj.items():
            if value != 0 and item in ware.inventory:
                if ware.inventory[item] - value >= 0:
                    ware_dict[item] = value
                    order_obj[item] = 0
                    ware.inventory[item] -= value
                elif ware.inventory[item] != 0:
                    ware_dict[item] = ware.inventory[item]
                    order_obj[item] -= ware.inventory[item]
                    ware.inventory[item] -= value
        if ware_dict:
            shipment_list.append({ware.name: ware_dict})

    for item, value in order_obj.items():
        if value != 0:
            return []

    return shipment_list


if __name__ == '__main__':
    # input the order
    order = json.loads(input("Order: "))

    flag = True
    warehouse_list = []
    while flag:
        warehouse_input = input("Warehouse object: ")
        if warehouse_input == "-1":
            break
        warehouse_dict = json.loads(warehouse_input)
        warehouse_object = Warehouse(warehouse_dict)
        warehouse_list.append(warehouse_object)

    compute_shipment(warehouse_list, order)
