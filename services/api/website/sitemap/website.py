from . import sitemap


@sitemap.register_generator
def website_generator():
    """
    This function generates the sitemap.xml file from this blueprint.
    """

    # Static pages
    yield 'website.home', {}

    # Dynamic pages

    for project in (
        'project',
        'santosderek',
        'vitality'
    ):
        yield 'website.project', {'project': project}
