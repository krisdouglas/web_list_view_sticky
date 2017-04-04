{
    'name': 'List View Fixed Table Header',
    'version': '10.0.1',
    'category': 'Tools',
    'sequence': 15,
    'summary': 'Web List View Fixed Table Header',
    'description': """
Web List View Fixed Table Header
=================================
* Fixed (sticky) list view table header, very helpful when dealing with many records.
""",
    'author': 'Andre Leander, upgraded to V9 by Stella Fredö in Sweeden, upgrades to V10 by Kris Douglas in England',
    'website': 'krisdouglas@gmail.com',
    'depends': ['web','base'],
    'data': [
        'views/web_list_view_sticky.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}
