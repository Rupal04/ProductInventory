class CacheNameSpace(object):
    PRODUCT_LIST = ["product_list", 1800]


def get_product_list():
    return CacheNameSpace.PRODUCT_LIST[0]
