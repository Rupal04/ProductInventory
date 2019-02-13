import logging

from rest_framework import viewsets, status
from rest_framework.response import Response

from product_app.constants import ErrorConstants, Warn
from product_app.response import ErrorResponse, SuccessResponse
from product_app.util import to_dict, create_product, get_products, update_product, create_category, get_categories

logger = logging.getLogger(__name__)

class CategoryViewSet(viewsets.ViewSet):
    # add category
    def create(self, request):
        try:
            data = request.data

            category_name = data.get("name", "")

            if category_name is None:
                response = ErrorResponse(msg=ErrorConstants.CATEGORY_NAME_NOT_PROVIDED)
                return Response(to_dict(response), status=status.HTTP_400_BAD_REQUEST)

            parent_cat_id = data.get("parent_category_id", "")

            create_category_response = create_category(category_name=category_name, parent_category_id=parent_cat_id)

            if not create_category_response:
                response = ErrorResponse(msg=ErrorConstants.CATEGORY_CREATION_ERROR)
                return Response(to_dict(response), status=status.HTTP_500_INTERNAL_SERVER_ERROR)

            elif create_category_response.success is False:
                response = ErrorResponse(msg=create_category_response.msg)
                return Response(to_dict(response), status=status.HTTP_202_ACCEPTED)

            return Response(to_dict(create_category_response), status=status.HTTP_200_OK)

        except Exception as e:
            logger.error(ErrorConstants.EXCEPTIONAL_ERROR + str(e), exc_info=True)
            response = ErrorResponse()
            return Response(to_dict(response), status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    # retrieve all contact list
    def list(self, request):
        try:
            category_list_response = get_categories()

            if not category_list_response:
                response = ErrorResponse(msg=ErrorConstants.CATEGORY_LISTING_ERROR)
                return Response(to_dict(response), status=status.HTTP_404_NOT_FOUND)

            elif category_list_response.success is False:
                response = ErrorResponse(msg=category_list_response.msg)
                return Response(to_dict(response), status=status.HTTP_202_ACCEPTED)

            return Response(to_dict(category_list_response), status=status.HTTP_200_OK)
        except Exception as e:
            logger.error(ErrorConstants.EXCEPTIONAL_ERROR + str(e), exc_info=True)
            response = ErrorResponse()
            return Response(to_dict(response), status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class ProductViewSet(viewsets.ViewSet):
    # add product
    def create(self, request):
        try:
            data = request.data

            product_name = data.get("name", "")
            product_quantity = int(data.get("quantity", 0))
            product_price = int(data.get("price", 0))
            category_ids = data.get("category_ids", [])

            if product_name is None:
                response = ErrorResponse(msg=ErrorConstants.PRODUCT_NAME_ERROR)
                return Response(to_dict(response), status=status.HTTP_400_BAD_REQUEST)

            create_product_response = create_product(category_ids=category_ids, product_name=product_name,
                                                     product_quantity=product_quantity, product_price=product_price)

            if not create_product_response:
                response = ErrorResponse(msg=ErrorConstants.PRODUCT_CREATION_ERROR)
                return Response(to_dict(response), status=status.HTTP_500_INTERNAL_SERVER_ERROR)

            elif create_product_response.success is False:
                response = ErrorResponse(msg=create_product_response.msg)
                return Response(to_dict(response), status=status.HTTP_202_ACCEPTED)

            return Response(to_dict(create_product_response), status=status.HTTP_200_OK)

        except Exception as e:
            logger.error(ErrorConstants.EXCEPTIONAL_ERROR + str(e), exc_info=True)
            response = ErrorResponse()
            return Response(to_dict(response), status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    # retrieve all product list
    def list(self, request):
        try:
            product_list_response = get_products()

            if not product_list_response:
                response = ErrorResponse(msg=ErrorConstants.PRODUCT_LISTING_ERROR)
                return Response(to_dict(response), status=status.HTTP_404_NOT_FOUND)

            elif product_list_response.success is False:
                response = ErrorResponse(msg=product_list_response.msg)
                return Response(to_dict(response), status=status.HTTP_202_ACCEPTED)

            return Response(to_dict(product_list_response), status=status.HTTP_200_OK)
        except Exception as e:
            logger.error(ErrorConstants.EXCEPTIONAL_ERROR + str(e), exc_info=True)
            response = ErrorResponse()
            return Response(to_dict(response), status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    # update product
    def update(self, request, pk=None):
        try:
            if not pk:
                logger.warning(Warn.PRODUCT_ID_REQUIRED)
                response = SuccessResponse(msg=ErrorConstants.PRODUCT_ID_MISSING)
                return Response(to_dict(response), status=status.HTTP_400_BAD_REQUEST)

            data = request.data

            pid = pk
            product_name = data.get("name", "")
            product_quantity = int(data.get("quantity", 0))
            product_price = int(data.get("price", 0))

            update_product_response = update_product(pid, product_name=product_name, product_quantity=product_quantity,
                                                     product_price=product_price)

            if not update_product_response:
                response = ErrorResponse(msg=ErrorConstants.PRODUCT_UPDATE_ERROR)
                return Response(to_dict(response), status=status.HTTP_500_INTERNAL_SERVER_ERROR)

            elif update_product_response.success is False:
                response = ErrorResponse(msg=update_product_response.msg)
                return Response(to_dict(response), status=status.HTTP_202_ACCEPTED)

            return Response(to_dict(update_product_response), status=status.HTTP_200_OK)
        except Exception as e:
            logger.error(ErrorConstants.EXCEPTIONAL_ERROR + str(e), exc_info=True)
            response = ErrorResponse()
            return Response(to_dict(response), status=status.HTTP_500_INTERNAL_SERVER_ERROR)