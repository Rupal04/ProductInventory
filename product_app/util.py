import logging
import redis
import json

from product_app.constants import ErrorConstants, SuccessConstants
from product_app.keys import get_product_list, CacheNameSpace
from product_app.models import Product
from product_app.response import PublishProductResponse, ErrorResponse, ProductListResponse, SuccessResponse

logger = logging.getLogger(__name__)
r_cache = redis.StrictRedis()

def to_dict(obj):
    """Represent instance of a class as dict.
        Arguments:
        obj -- any object
        Return:
        dict
        """

    def serialize(obj):
        """Recursively walk object's hierarchy."""
        if isinstance(obj, (bool, int, float)):
            return obj
        elif isinstance(obj, dict):
            obj = obj.copy()
            for key in obj:
                obj[key] = serialize(obj[key])
            return obj
        elif isinstance(obj, list):
            return [serialize(item) for item in obj]
        elif isinstance(obj, tuple):
            return tuple(serialize([item for item in obj]))
        elif hasattr(obj, '__dict__'):
            return serialize(obj.__dict__)
        else:
            return repr(obj)

    return serialize(obj)


def create_product(**kwargs):
    try:
        name = kwargs["product_name"]
        quantity = kwargs["product_quantity"]
        price = kwargs["product_price"]

        if not Product.objects.filter(name=name):
            product_obj = Product.objects.create(name=name, quantity=quantity, price=price)
        else:
            response = ErrorResponse(msg=ErrorConstants.PRODUCT_NAME_ALREADY_EXISTS)
            return response

        response = PublishProductResponse(product_obj)
        return response

    except Exception as e:
        logger.error(ErrorConstants.PRODUCT_CREATION_ERROR + str(e), exc_info=True)
        return None


def get_products():
    try:
        if 'product_list' in r_cache:
            product_obj_list_json = r_cache.get('product_list')
        else:
            product_obj = Product.objects.all()
            product_obj_list = []
            if product_obj:
                for product in product_obj:
                    product_obj_dict = {"id": product.id, "name": product.name, "price": product.price,
                                        "quantity": product.quantity}
                    product_obj_list.append(product_obj_dict)
                    product_obj_list_json = json.dumps(product_obj_list)
                r_cache.set(get_product_list(), product_obj_list_json, CacheNameSpace.PRODUCT_LIST[1])

            else:
                response = ErrorResponse(msg=ErrorConstants.PRODUCT_NOT_FOUND)
                return response

        response = ProductListResponse(json.loads(product_obj_list_json))
        return response

    except Exception as e:
        logger.error(ErrorConstants.PRODUCT_LISTING_ERROR + str(e), exc_info=True)
        return None


def update_product(pid, **kwargs):
    try:
        product_obj = Product.objects.filter(id=pid).first()
        if product_obj:
            if kwargs['product_name']:
                name = kwargs['product_name']
                product_obj.name = name

            if kwargs["product_quantity"]:
                quantity = kwargs["product_quantity"]
                product_obj.quantity = quantity

            if kwargs["product_price"]:
                price = kwargs["product_price"]
                product_obj.price = price

            product_obj.save()

            response = SuccessResponse(msg=SuccessConstants.PRODUCT_UPDATE_SUCCESS)

        else:
            response = ErrorResponse(msg=ErrorConstants.PRODUCT_NOT_FOUND)

        return response

    except Exception as e:
        logger.error(ErrorConstants.PRODUCT_UPDATE_ERROR + str(e), exc_info=True)
        return None
