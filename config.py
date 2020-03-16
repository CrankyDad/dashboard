# -*- coding:utf-8 -*-
signalk_host = 'localhost'
signalk_port = 80
dashboard = {
    'name': 'Curiosity',
    'time_format': '%H:%M',
    'assets': {
        'display_font': 'nasalization-rg.ttf',
        'body_font': 'Eurostile.ttf',
        'splash': 'voronoi1-splash.bmp'
    },
    'loading': {},
    'default': {
        'navigation.speedOverGround': {
            'label': 'SOG',
            'unit': 'kn',
            'conversion': 'm/s',
            'max_age': 30
        },
        'navigation.courseOverGroundTrue': {
            'label': 'COG',
            'unit': '°',
            'conversion': 'rad',
            'max_age': 20
        },
        'environment.depth.belowTransducer': {
            'label': 'Depth',
            'unit': 'm',
            'conversion': 'm',
            'max_age': 20
        },
        'environment.wind.speedTrue': {
            'label': 'Wind',
            'unit': 'kn',
            'conversion': 'm/s',
            'max_age': 30
        },
        'environment.inside.salon.temperature': {
            'label': 'Temp',
            'unit': '°C',
            'conversion': 'K',
            'max_age': 60
        },
        'environment.inside.salon.pressure': {
            'label': 'Baro',
            'unit': 'hPa',
            'conversion': 'Pa',
            'max_age': 60
        },
        'environment.inside.salon.humidity': {
            'label': 'Humid',
            'unit': '%',
            'conversion': 'int',
            'max_age': 60
        }
    },
   'not-under-way': {
        'environment.inside.salon.temperature': {
            'label': 'Temp',
            'unit': '°C',
            'conversion': 'K',
            'max_age': 60
        },
        'environment.inside.salon.pressure': {
            'label': 'Baro',
            'unit': 'hPa',
            'conversion': 'Pa',
            'max_age': 60
        },
        'environment.inside.salon.humidity': {
            'label': 'Humid',
            'unit': '%',
            'conversion': 'int',
            'max_age': 60
        },
        'environment.wind.speedTrue': {
            'label': 'Wind',
            'unit': 'kn',
            'conversion': 'm/s',
            'max_age': 30
        }
   },
   'anchored': {
        'navigation.anchor.currentRadius': {
            'label': 'Anchor',
            'unit': 'm',
            'conversion': 'm',
            'max_age': 10
        },
        'environment.depth.belowTransducer': {
            'label': 'Depth',
            'unit': 'm',
            'conversion': 'm',
            'max_age': 20
        },
        'environment.wind.speedTrue': {
            'label': 'Wind',
            'unit': 'kn',
            'conversion': 'm/s',
            'max_age': 30
        },
        'environment.inside.salon.temperature': {
            'label': 'Temp',
            'unit': '°C',
            'conversion': 'K',
            'max_age': 60
        },
        'environment.inside.salon.pressure': {
            'label': 'Baro',
            'unit': 'hPa',
            'conversion': 'Pa',
            'max_age': 60
        },
        'environment.inside.salon.humidity': {
            'label': 'Humid',
            'unit': '%',
            'conversion': 'int',
            'max_age': 60
        }
   },
  'sailing': {
        'navigation.speedOverGround': {
            'label': 'SOG',
            'unit': 'kn',
            'conversion': 'm/s',
            'max_age': 30
        },
        'navigation.courseOverGroundTrue': {
            'label': 'COG',
            'unit': '°',
            'conversion': 'rad',
            'max_age': 20
        },
        'environment.depth.belowTransducer': {
            'label': 'Depth',
            'unit': 'm',
            'conversion': 'm',
            'max_age': 20
        },
        'environment.inside.salon.pressure': {
            'label': 'Baro',
            'unit': 'hPa',
            'conversion': 'Pa',
            'max_age': 60
        },
        'environment.wind.speedTrue': {
            'label': 'Wind',
            'unit': 'kn',
            'conversion': 'm/s',
            'max_age': 30
        }
  }
# 'under-engine';
}
