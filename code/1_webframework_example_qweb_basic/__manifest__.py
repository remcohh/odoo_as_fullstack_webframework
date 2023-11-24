# __manifest__.py
{
    'name': 'webframework_example_qweb_basic',
    'version': '0.1',
    'author': 'Remco Huijdts',
    'category': 'Education',
    'depends': ['base'],
    'data': [
        'views/menu.xml',
        "security/ir.model.access.csv",
        'views/book.xml',
    ],
    'installable': True,
    'application': True,
}
