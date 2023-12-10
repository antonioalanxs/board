from django.shortcuts import render


class ErrorMiddleware:
    """
    Middleware for rendering a generic error page with the corresponding error status code.

    Attributes:
        get_response (`function`): Django's middleware function to get the response from a request.      
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        """
        Handles the incoming request and response.

        If the response has an error status code, it renders the error page with this code. Otherwise, it returns the response as is.

        Args:
            request (`HttpRequest`): The incoming HTTP request.

        Returns:
            `HttpResponse`: The HTTP response.
        """
        response = self.get_response(request)

        status_code = response.status_code

        if self._error(status_code):
            return render(
                request,
                "config/error.html",
                status=status_code,
            )

        return response

    def _error(self, status_code):
        """
        Checks whether the provided HTTP status code indicates an error.

        Args:
            status_code (`int`): The HTTP status code.

        Returns:
            `bool`: True if the status code indicates an error, False otherwise.
        """
        return status_code >= 400
