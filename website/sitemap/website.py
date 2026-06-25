from website.routes.website import PROJECT_PAGES

from . import sitemap


@sitemap.register_generator
def website_generator():
    """
    This function generates the sitemap.xml file from this blueprint.
    """

    # Static pages
    yield 'website.home', {}

    # Dynamic pages
    for project in PROJECT_PAGES:
        yield 'website.project', {'project': project}
