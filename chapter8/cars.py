def make_car(manufacturer, model, **carinfo):
    carinfo['manufacturer'] = manufacturer
    carinfo['model'] = model
    return carinfo

car = make_car('subaru', 'outback', color='blue', tow_package=True)    

print(car)