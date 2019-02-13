class SuccessConstants(object):
    SUCCESS_RESPONSE = "Successful"
    PRODUCT_UPDATE_SUCCESS = "Product updated successfully."
    PRODUCT_CREATION_SUCCESS = "Product Created successfully."
    CATEGORY_CREATION_SUCCESS = "Category Created successfully."


class ErrorConstants(object):
    ERROR_RESPONSE = "Error"
    EXCEPTIONAL_ERROR = "Some Unexpected Exception Occured. Error is "
    PRODUCT_CREATION_ERROR = "Unable to create Product."
    PRODUCT_UPDATE_ERROR = "Unable to update Product. Maybe No Product with this ID exists."
    PRODUCT_NOT_FOUND = "No Product for the particular search has been found."
    PRODUCT_ID_MISSING = "Missing Product ID"
    PRODUCT_LISTING_ERROR = "Error in listing Products."
    PRODUCT_NAME_ERROR = "Product Name not provided."
    PRODUCT_NAME_ALREADY_EXISTS = "Product of that name already present."
    CATEGORY_NAME_NOT_PROVIDED = "Category Name not provided."
    CATEGORY_CREATION_ERROR = "Unable to create Category."
    CATEGORY_CREATION_ERROR = "Unable to create Category."
    CATEGORY_LISTING_ERROR = "Error in listing Categories."
    CATEGORY_NOT_FOUND = "No Category for the particular search has been found."


class Warn(object):
    PRODUCT_ID_REQUIRED = "Product ID required "