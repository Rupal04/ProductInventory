import logging

from product_app.constants import ErrorConstants, SuccessConstants
from product_app.models import Product, Category
from product_app.response import PublishProductResponse, ErrorResponse, ProductListResponse, SuccessResponse, \
    PublishCategoryResponse, CategoryListResponse, ProductResponse

logger = logging.getLogger(__name__)

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
        category_ids = kwargs["category_ids"]
        name = kwargs["product_name"]
        quantity = kwargs["product_quantity"]
        price = kwargs["product_price"]

        if not Product.objects.filter(name=name):
            product_obj = Product.objects.create(name=name, quantity=quantity, price=price)
        else:
            response = ErrorResponse(msg=ErrorConstants.PRODUCT_NAME_ALREADY_EXISTS)
            return response

        if category_ids:
            for category_id in category_ids:
                category_obj = Category.objects.get(id=category_id)
                product_obj.category.add(category_obj)

        product_obj.save()
        response = PublishProductResponse(product_obj)
        return response

    except Exception as e:
        logger.error(ErrorConstants.PRODUCT_CREATION_ERROR + str(e), exc_info=True)
        return None


def get_products():
    try:
        product_obj = Product.objects.all()
        product_obj_list = []

        if product_obj:
            for product in product_obj:
                category_id_list = []
                categories = product.category.all().values()
                for category in categories:
                    category_id_list.append(category["id"])
                product_obj_dict = ProductResponse(id=product.id, name= product.name,
                                                   quantity=product.quantity, price=product.price,
                                                   category_ids = category_id_list)
                product_obj_list.append(product_obj_dict)

        else:
            response = ErrorResponse(msg=ErrorConstants.PRODUCT_NOT_FOUND)
            return response

        response = ProductListResponse(product_obj_list)
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

            product_obj.category.clear()
            if kwargs["category_ids"]:
                for category_id in kwargs["category_ids"]:
                    category_obj = Category.objects.get(id=category_id)
                    product_obj.category.add(category_obj)

            product_obj.save()

            response = SuccessResponse(msg=SuccessConstants.PRODUCT_UPDATE_SUCCESS)

        else:
            response = ErrorResponse(msg=ErrorConstants.PRODUCT_NOT_FOUND)

        return response

    except Exception as e:
        logger.error(ErrorConstants.PRODUCT_UPDATE_ERROR + str(e), exc_info=True)
        return None


def create_category(**kwargs):
    try:
        name = kwargs["category_name"]

        if not Category.objects.filter(name=name):
            category_obj = Category.objects.create(name=name)
        else:
            response = ErrorResponse(msg=ErrorConstants.CATEGORY_NAME_ALREADY_EXISTS)
            return response

        if kwargs["parent_category_id"]:
            category_obj.parent_category_id = kwargs["parent_category_id"]
            category_obj.save()

        response = PublishCategoryResponse(category_obj)
        return response

    except Exception as e:
        logger.error(ErrorConstants.CATEGORY_CREATION_ERROR + str(e), exc_info=True)
        return None


def get_categories():
    try:
        category_without_pid_list=[]
        category_with_pid_list=[]

        category_obj = Category.objects.all()

        if category_obj:
            for category in category_obj:
                if category.parent_category_id:
                    category_with_pid_dict = {"id": category.id, "name": category.name, "pid": category.parent_category_id}
                    category_with_pid_list.append(category_with_pid_dict)

                else:
                    category_without_pid_dict = {"id":category.id, "name":category.name}
                    category_without_pid_list.append(category_without_pid_dict)

            for dicts in category_with_pid_list:
                id = dicts["id"]
                category_with_same_pid = list(filter(lambda catgeory_with_pid: catgeory_with_pid['pid'] == id,
                                                     category_with_pid_list))
                if category_with_same_pid:
                    dicts["child_categories"] = category_with_same_pid

            for child_dicts in category_without_pid_list:
                id = child_dicts["id"]
                child_category_list_with_same_pid = list(filter(lambda child_catgeory_with_pid: child_catgeory_with_pid['pid'] == id,
                                                                category_with_pid_list))
                if child_category_list_with_same_pid:
                    child_dicts["child_categories"] = child_category_list_with_same_pid

        else:
            response = ErrorResponse(msg=ErrorConstants.CATEGORY_NOT_FOUND)
            return response

        response = CategoryListResponse(category_without_pid_list)
        return response
    except Exception as e:
        logger.error(ErrorConstants.PRODUCT_LISTING_ERROR + str(e), exc_info=True)
        return None
