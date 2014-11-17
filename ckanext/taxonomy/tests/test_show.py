import ckan.logic as logic

from ckanext.taxonomy.tests.test_helpers import TaxonomyTestCase

from nose.tools import raises

class TestShowTaxonomy(TaxonomyTestCase):

    def test_show_valid_name(self):
        res = logic.get_action('taxonomy_show')(
            TestShowTaxonomy.empty_context,
            {'id': 'taxonomy-one'})

    def test_show_valid_id(self):
        res = logic.get_action('taxonomy_show')(
            TestShowTaxonomy.empty_context,
            {'id': TestShowTaxonomy.taxonomies[0]['id']})

    @raises(logic.NotFound)
    def test_show_missing_name(self):
        res = logic.get_action('taxonomy_show')(
            TestShowTaxonomy.empty_context,
            {'id': 'non-existent'})

    @raises(logic.NotFound)
    def test_show_missing_id(self):
        res = logic.get_action('taxonomy_show')(
            TestShowTaxonomy.empty_context,
            {'id': '1234'})

    def test_list(self):
        res = logic.get_action('taxonomy_list')({}, {})
        assert len(res) == 2, len(res)

    def test_show_term_valid(self):
        pass

    def test_show_term_missing(self):
        pass

    def test_term_list(self):
        pass
