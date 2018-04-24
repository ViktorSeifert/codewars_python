def strip_url_params(url, params_to_strip=[]):
    if "?" not in url:
        return url

    url_parts = url.split("?")

    params = {}

    for param in url_parts[1].split("&"):
        param_parts = param.split("=")

        if param_parts[0] not in params.keys() and param_parts[0] not in params_to_strip:
            params[param_parts[0]] = param_parts[1]

    new_params = []
    for param_name, param_value in params.items():
        new_params.append(param_name + "=" + param_value)

    return url_parts[0] + "?" + "&".join(new_params)


print(strip_url_params('www.codewars.com?a=1&b=2&a=2'))
print(strip_url_params('http://www.codewars.com?a=1&b=2&a=2'))
print(strip_url_params('http://www.codewars.com?a=1'))
print(strip_url_params('www.codewars.com?a=1&b=2&a=2', ['b']))
print(strip_url_params('www.codewars.com', ['b']))
