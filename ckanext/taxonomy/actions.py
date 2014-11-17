import ckan.plugins.toolkit as toolkit
import ckan.logic as logic

from ckanext.taxonomy.models import Taxonomy, TaxonomyTerm

_check_access = logic.check_access

@toolkit.side_effect_free
def taxonomy_list(context, data_dict):
    """
    List all of the known taxonomies
    """
    _check_access('taxonomy_list', context, data_dict)

    model = context['model']
    items = model.Session.query(Taxonomy).order_by('title')
    return [ item.as_dict() for item in items.all() ]


@toolkit.side_effect_free
def taxonomy_show(context, data_dict):
    """
    Shows a single taxonomy, along with the terms it contains
    """
    _check_access('taxonomy_show', context, data_dict)

    model = context['model']
    id = data_dict.get('id')
    if not id:
        raise logic.NotFound()

    item = Taxonomy.get(id)
    if not item:
        raise logic.NotFound()

    return item.as_dict(with_terms=True)


def taxonomy_create(context, data_dict):
    """
    Creates a new taxonomy. Terms are not created here, they must be
    created using taxonomy_term_create with the taxonomy id from this
    call provided.
    """
    _check_access('taxonomy_create', context, data_dict)

    name = data_dict.get('name')
    title = data_dict.get('title')

    if not name:
        pass  # generate unique name from title

    t = Taxonomy(name=name, title=title)
    t.save()

    return t.as_dict()


def taxonomy_update(context, data_dict):
    """
    Update the details of the specified taxonomy.
    """
    _check_access('taxonomy_update', context, data_dict)

    pass


def taxonomy_delete(context, data_dict):
    """
    Delete the specific taxonomy, and as a result, all of the terms within
    it.
    """
    _check_access('taxonomy_delete', context, data_dict)

    pass


@toolkit.side_effect_free
def taxonomy_term_list(context, data_dict):
    """
    Lists all of the taxonomy terms for the given taxonomy.
    """
    pass


@toolkit.side_effect_free
def taxonomy_term_show(context, data_dict):
    """
    Shows a single taxonomy term and its children, the taxonomy id is not
    required, just a term_id.
    """
    pass


def taxonomy_term_create(context, data_dict):
    """
    Allows for the creation of a taxonomy term.
    """
    _check_access('taxonomy_term_create', context, data_dict)


def taxonomy_term_update(context, data_dict):
    """
    Allows a taxonomy term to be updated.
    """
    _check_access('taxonomy_term_update', context, data_dict)


def taxonomy_term_delete(context, data_dict):
    """
    Deletes a taxonomy term
    """
    _check_access('taxonomy_term_delete', context, data_dict)


