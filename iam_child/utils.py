def before_request():
    pass
    # print('Check if currently login to iam')


def after_request(response, request):
    pass
    # print(response)
    # print(dir(request))
    # query_string = str(request.query_string)
    # print(query_string.find('cmd=web_logout'))
    # validate()
    # if not query_string.find('cmd=web_logout'):
    #     print('LLLLLLLLL')
    #     validate()
