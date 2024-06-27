import promos

promotions = [func for name, func in inspect.getmembers(promos, inspect.isfunction)]
