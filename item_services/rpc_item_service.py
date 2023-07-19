from modernrpc.core import rpc_method
from .models import ItemModel
from item_services.constant.constant import ITEM_TYPE

# api gateway
@rpc_method
def create_item(item_data):
    try:
        if item_data['type'] not in ITEM_TYPE:
            return "type is unknown"
        item_objects = ItemModel.objects.filter(name=item_data['name'])
        if item_objects.exists():
                data_response = {
                    "status": 403,
                    "message": f"item {item_objects.name} already exist",
                }
                return data_response
        price_type = {}
        for price in item_data['prices']:
            price_type[price['priceFor']]=price['price']
        if price_type.get("regular", None) is None:
            return "price type regular should be fill"
        item_object = ItemModel.objects.create(
            name=item_data['name'],
            item_type=item_data['type'],
            regular_price=price_type['regular'],
            vip_price=price_type.get("VIP", None),
            wholesale_price=price_type.get("wholesale", None)
        )
        data_response = {
            "status": 201,
            "message": "create item is success",
            "data": {
                "uuid": item_object.uuid,
                "name": item_object.name,
                "type": item_object.item_type,
                "prices": item_data['prices'],
                        "created_at":item_object.created_at,
                        "updated_at":item_object.updated_at,
                }
        }
        return data_response
    except Exception as e:
        data_response = {
            "status": 500,
            "message": "server error",
            "data": str(e)
        }
        return data_response

@rpc_method
def find_all_item():
    try:
        all_item = ItemModel.objects.all()
        data = []
        for item in all_item:
            item_data = {
                'uuid': item.uuid,
                'name': item.name,
                'type': item.item_type,
                'prices':[
                    {
                    "priceFor": "regular",
                    "price": item.regular_price
                    },
                    {
                    "priceFor": "VIP",
                    "price": item.vip_price
                    },
                    {
                    "priceFor": "wholesale",
                    "price": item.wholesale_price
                    }
                ],
                'created_at': item.created_at,
                'updated_at': item.updated_at,
            }
            data.append(item_data)
        data_response = {
            "status": 200,
            "message": "list user",
            "data": data
        }
        return data_response
    except Exception as e:
        data_response = {
            "status": 404,
            "message": "item not is exist",
            "data": str(e)
        }
        return data_response

@rpc_method
def find_item_by_uuid(item_uuid):
    try:
        item_object = ItemModel.objects.get(uuid=item_uuid)
        data_response = {
            "status": 200,
            "message": "user is exist",
            "data": {
                    'uuid': item_object.uuid,
                    'name': item_object.name,
                    'type': item_object.item_type,
                    'prices':[
                        {
                        "priceFor": "regular",
                        "price": item_object.regular_price
                        },
                        {
                        "priceFor": "VIP",
                        "price": item_object.vip_price
                        },
                        {
                        "priceFor": "wholesale",
                        "price": item_object.wholesale_price
                        }
                    ],
                    'created_at': item_object.created_at,
                    'updated_at': item_object.updated_at,
                }
        }
        return data_response
    except Exception as e:
        data_response = {
            "status": 404,
            "message": "item not is exist",
            "data": str(e)
        }
        return data_response

@rpc_method
def update_item_by_uuid(item_uuid, item_data):
    try:
        if item_data.get('type', None) is not None and item_data.get('type', None) not in ['hats', 'tops', 'shorts']:
            return "type is unknown"
        
        item_objects = ItemModel.objects.get(uuid=item_uuid)
        if item_data.get('name', None) is not None:
            item_objects.name = item_data['name']
        if item_data.get('type', None) is not None:
            item_objects.user_type = item_data['type']
        if len(item_data['prices']) > 0:
            price_type = {}
            for price in item_data['prices']:
                price_type[price['priceFor']]=price['price']
            if price_type.get('regular', None) is not None:
                item_objects.regular_price = price_type['regular']
            if price_type.get('VIP', None) is not None:
                item_objects.vip_price = price_type['VIP']
            if price_type.get('wholesale', None) is not None:
                item_objects.wholesale_price = price_type['wholesale']

        item_objects.save()
        data_response = {
            "status": 200,
            "message": "user is updated",
            "data": {
                    'uuid': item_objects.uuid,
                    'name': item_objects.name,
                    'type': item_objects.item_type,
                    'prices':[
                        {
                        "priceFor": "regular",
                        "price": item_objects.regular_price
                        },
                        {
                        "priceFor": "VIP",
                        "price": item_objects.vip_price
                        },
                        {
                        "priceFor": "wholesale",
                        "price": item_objects.wholesale_price
                        }
                    ],
                    'created_at': item_objects.created_at,
                    'updated_at': item_objects.updated_at,
                }
        }
        return data_response
    except Exception as e:
        data_response = {
            "status": 404,
            "message": "item not is exist",
            "data": str(e)
        }
        return data_response

@rpc_method
def delete_item_by_uuid(item_uuid):
    try:
        item_objects = ItemModel.objects.get(uuid=item_uuid)
        item_objects.delete()
        data_response = {
            "status": 200,
            "message": "item data deleted",
        }
        return data_response
    except Exception as e:
        data_response = {
            "status": 404,
            "message": "item not is exist",
            "data": str(e)
        }
        return data_response

# transaciton service
@rpc_method
def filter_item_by_name(item_data):
    try:
        for item in item_data['transaction']:
            item_objects = ItemModel.objects.filter(name=item['item'])
            if not item_objects.exists():
                data_response = {
                    "status": 404,
                    "message": f"item {item['item']} not exist",
                }
                return data_response
        data_response = {
            "status": 200,
            "message": "item is exist",
        }
        return data_response
    except Exception as e:
        data_response = {
            "status": 404,
            "message": "item not is exist",
            "data": str(e)
        }
        return data_response

@rpc_method
def get_item_by_name(item_name):
    try:
        item_object = ItemModel.objects.get(name=item_name)
        data_response = {
            "status": 200,
            "message": "user exist",
            "data": {
                "uuid":item_object.uuid,
                "name":item_object.name,
                "item_type":item_object.item_type,
                "price":{
                    "regular":item_object.regular_price,
                    "VIP":item_object.vip_price,
                    "wholesale":item_object.wholesale_price
                },
            }
        }
        return data_response
    except Exception as e:
        data_response = {
            "status": 404,
            "message": "item not is exist",
            "data": str(e)
        }
        return data_response