{
    'name': 'MMC Convert',  # Name of the module
    'version': '1.2.1',  # Module version
    'summary': 'MMC Excel Converter for Odoo simplifies data management by allowing users to easily import their data from .csv or Excel formats into Odoo. The app includes templates for streamlined data importing.',  # Short summary
    'live_test_url':'https://account.mmcconvert.com/login',
    'description': """
okok       
    """,  # Detailed description
    'author': 'MMC Convert',  # Author name
    'website': 'https://www.mmcconvert.com/',  # Author's website
    'license': 'LGPL-3',  # License type
    'category': 'CATEGORY',  # Module category
    'depends': ['base'],  # Dependencies (other modules)
    'data': [
         'security/ir.model.access.csv',
        'views/mmc_convert_view.xml',
    ],
    'installable': True,  # Whether the module can be installed
    'application': True,  # Whether the module is an application
    'auto_install':True,  # Whether the module should be auto-installed
    'images': [
        'static/description/banner.gif',  # Default app icon (light)
        'static/description/icon.png',  # Default app icon (light)
        'static/description/thumbnail_light.png',  # Default thumbnail (light)
        'static/description/img.png' 
    ],
}