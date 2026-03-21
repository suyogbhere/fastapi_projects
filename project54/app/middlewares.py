from fastapi import Request



#Creating 1st Middleware
async def my_first_middleware(request: Request, call_next):
    print("1st Middleware: Before processing the request")
    print(f"Request : {request.method} {request.url}")

    response = await call_next(request)

    print("1st Middleware: After processing the request, before returning response")
    print(f"Response status code: {response.status_code}")
    return response



#Creating 2nd Middleware
async def my_second_middleware(request: Request, call_next):
    print("2nd Middleware: Before processing the request")
    print(f"Request : {request.method} {request.url}")

    response = await call_next(request)

    print("2nd Middleware: After processing the request, before returning response")
    print(f"Response status code: {response.status_code}")
    return response
