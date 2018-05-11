class LambdaResponse:

    def __init__(self, isBase64Encoded, statusCode, headers, body):
        self.isBase64Encoded = isBase64Encoded
        self.statusCode = statusCode
        self.headers = headers
        self.body = body
