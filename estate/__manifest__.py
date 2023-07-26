{
    "name": "Estate",  # The name that will appear in the App list
    "version": "1.1.2",  # Version
    "application": True,  # This line says the module is an App, and not a module
    "depends": ["base", "sale", "mail"],  # dependencies
    "data": [
        'security/ir.model.access.csv',
        'views/estate_cancel_property.xml',
        'views/estate_property_offer_views.xml',
        'views/estate_property_info_views.xml',
        'views/estate_property_type_views.xml',
        'views/estate_property_views.xml',
        'views/estate_menus.xml',
    ],
    "installable": True,
    "license" : "LGPL-3",
}
