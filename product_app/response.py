from product_app.constants import SuccessConstants, ErrorConstants


class SuccessResponse(object):
    def __init__(self, results=None, msg=SuccessConstants.SUCCESS_RESPONSE):
        if results is not None:
            self.results = results
        self.msg = msg
        self.success = True


class ErrorResponse(object):
    def __init__(self, msg=ErrorConstants.ERROR_RESPONSE):
        self.msg = msg
        self.success = False


class PublishProductResponse(object):
    def __init__(self, product_list, msg=SuccessConstants.PRODUCT_CREATION_SUCCESS):
        self.msg = msg
        self.product_id = product_list.id
        self.success = True


class ProductListResponse(object):
    def __init__(self, results=None, msg=SuccessConstants.SUCCESS_RESPONSE):
        if results is not None:
            self.results = results
        self.msg = msg
        self.success = True

class PublishCategoryResponse(object):
    def __init__(self, category_list, msg=SuccessConstants.CATEGORY_CREATION_SUCCESS):
        self.msg = msg
        self.category_id = category_list.id
        self.success = True

class CategoryListResponse(object):
    def __init__(self, results=None, msg=SuccessConstants.SUCCESS_RESPONSE):
        if results is not None:
            self.results = results
        self.msg = msg
        self.success = True


class ProductResponse(object):
    id = None
    name = None
    quantity = None
    price = None
    category_ids = []

    def __init__(self, id, name,quantity, price, category_ids):
        self.id = id
        self.name = name
        self.quantity = quantity
        self.price = price
        self.category_ids = category_ids
