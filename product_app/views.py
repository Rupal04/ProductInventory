import logging

from rest_framework import viewsets, status
from rest_framework.response import Response

from product_app.constants import ErrorConstants, Warn
from product_app.response import ErrorResponse, SuccessResponse
from product_app.util import to_dict, create_product, get_products, update_product

logger = logging.getLogger(__name__)

class CategoryViewSet(viewsets.ViewSet):
    # add category
    def create(self, request):
        try:
            data = request.data

            phone_number = int(data.get("number", 0))
            contact_name = data.get("name", "")
            contact_email = data.get("email")

            if contact_email is None:
                response = ErrorResponse(msg=ErrorConstants.EMAIL_NOT_PROVIDED)
                return Response(to_dict(response), status=status.HTTP_400_BAD_REQUEST)

            create_contact_response = create_contact(phone_number=phone_number, contact_name=contact_name,
                                                     contact_email=contact_email)

            if not create_contact_response:
                response = ErrorResponse(msg=ErrorConstants.CONTACT_CREATION_ERROR)
                return Response(to_dict(response), status=status.HTTP_500_INTERNAL_SERVER_ERROR)

            elif create_contact_response.success is False:
                response = ErrorResponse(msg=create_contact_response.msg)
                return Response(to_dict(response), status=status.HTTP_202_ACCEPTED)

            return Response(to_dict(create_contact_response), status=status.HTTP_200_OK)

        except Exception as e:
            logger.error(ErrorConstants.EXCEPTIONAL_ERROR + str(e), exc_info=True)
            response = ErrorResponse()
            return Response(to_dict(response), status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    # retrieve all contact list
    def list(self, request):
        try:
            contact_list_response = get_contacts()

            if not contact_list_response:
                response = ErrorResponse(msg=ErrorConstants.CONTACT_LISTING_ERROR)
                return Response(to_dict(response), status=status.HTTP_404_NOT_FOUND)

            elif contact_list_response.success is False:
                response = ErrorResponse(msg=contact_list_response.msg)
                return Response(to_dict(response), status=status.HTTP_202_ACCEPTED)

            return Response(to_dict(contact_list_response), status=status.HTTP_200_OK)
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

            if product_name is None:
                response = ErrorResponse(msg=ErrorConstants.PRODUCT_NAME_ERROR)
                return Response(to_dict(response), status=status.HTTP_400_BAD_REQUEST)

            create_product_response = create_product(product_name=product_name, product_quantity=product_quantity,
                                                     product_price=product_price)

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