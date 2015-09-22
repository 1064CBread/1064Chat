from flask import Blueprint

blueprint = Blueprint(__name__, __name__)
print('I. AM. ' + str(blueprint.name).upper() + '.')
