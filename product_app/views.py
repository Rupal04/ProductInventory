import logging

from rest_framework import viewsets, status
from rest_framework.response import Response

from product_app.constants import ErrorConstants
from product_app.response import ErrorResponse

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

    # update contact
    def update(self, request, pk=None):
        try:
            if not pk:
                logger.warning(Warn.CONTACT_ID_REQUIRED)
                response = SuccessResponse(msg=ErrorConstants.CONTACT_ID_MISSING)
                return Response(to_dict(response), status=status.HTTP_400_BAD_REQUEST)

            data = request.data

            c_id = pk
            phone_number = int(data.get("number", 0))
            contact_name = data.get("name", "")
            contact_email = data.get("email", "")

            update_contact_response = update_contact(c_id, phone_number=phone_number, contact_name=contact_name,
                                                     contact_email=contact_email)

            if not update_contact_response:
                response = ErrorResponse(msg=ErrorConstants.CONTACT_UPDATE_ERROR)
                return Response(to_dict(response), status=status.HTTP_500_INTERNAL_SERVER_ERROR)

            elif update_contact_response.success is False:
                response = ErrorResponse(msg=update_contact_response.msg)
                return Response(to_dict(response), status=status.HTTP_202_ACCEPTED)

            return Response(to_dict(update_contact_response), status=status.HTTP_200_OK)
        except Exception as e:
            logger.error(ErrorConstants.EXCEPTIONAL_ERROR + str(e), exc_info=True)
            response = ErrorResponse()
            return Response(to_dict(response), status=status.HTTP_500_INTERNAL_SERVER_ERROR)