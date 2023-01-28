import logging

logging.basicConfig(filename = 'error.handling.log', format = '‘%(asctime)s %(message)s' , level = logging.DEBUG)

animals = [
    {
      'name': 'elephant',
      'qty': 22
    },

    {
      'name': 'tiger',
      'qty': 22
    },

    {
      'name': 'elephant',
      'qty': 22
    }
  ]

try:

  logging.info(f'Looking for name in {animals}')

  print(animals[0]['name'])

  print(animals[3]['name'])

except Exception as ex:

  logging.warning(ex)