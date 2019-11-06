from app.utils import slugify


def test_slugify():
    input_text = 'This is a title'
    output_text = 'this_is_a_title'

    assert slugify(input_text) == output_text
