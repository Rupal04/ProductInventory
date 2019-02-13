class CacheNameSpace(object):
    PRODUCT_LIST = ["product_list", 1800]
    CATEGORY_LIST = ["category_list", 1800]

def get_product_list():
    return CacheNameSpace.PRODUCT_LIST[0]

def get_category_list():
    return CacheNameSpace.CATEGORY_LIST[0]
