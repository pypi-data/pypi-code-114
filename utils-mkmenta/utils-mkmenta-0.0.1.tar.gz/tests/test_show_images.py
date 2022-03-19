from mkutils import show_images


def test_show_images():
    show_images(['tests/resources/image.jpeg',
                 'tests/resources/image.jpeg',
                 'tests/resources/image.jpeg',
                 'tests/resources/image.jpeg'],
                cols=2, imheight=1000)
    # TODO: mock web server