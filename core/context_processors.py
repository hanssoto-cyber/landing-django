"""
Context processors globales para el portafolio.
Las variables definidas aquí estarán disponibles en TODOS los templates.
"""


def redes_sociales(request):
    """Información de contacto y redes sociales accesible desde cualquier template."""
    return {
        'linkedin_url': 'https://www.linkedin.com/in/hans-soto-gonzalez-a142b8170/',
        'github_url': 'https://github.com/hanssoto-cyber',
        'email_contacto': 'hans.soto.g@gmail.com',
        'nombre_completo': 'Hans Soto',
    }