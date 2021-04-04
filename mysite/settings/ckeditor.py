from .base import *

CKEDITOR_UPLOAD_PATH = 'uploads/'
# CKEDITOR_BASEPATH = os.path.join(STATIC_URL, 'ckeditor/ckeditor/')
CKEDITOR_CONFIGS = {
    'default': {
        'contentsCss': [
            'https://fonts.googleapis.com/css2?family=Fredoka+One&family=Nunito:wght@600&display=swap',
            'https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/css/bootstrap.min.css',
            os.path.join(STATIC_URL, 'css/base.css'),
        ],
        'skin': 'moono-lisa',
        'removePlugins': ['image'],
        'extraPlugins': ['autogrow', 'codesnippet', 'iframe', 'image2', 'table'],
        'codeSnippet_theme': 'atelier-dune.dark',
        'autoGrow_onStartup': True,
        'autoGrow_minHeight': '300',
        'width': '100%',
        'image2_prefillDimensions': False,
        'filebrowserBrowseUrl': '/browser/',
        # start font_names
        'font_names': 'Arial/Arial, Helvetica, sans-serif;' +
        'Comic Sans MS/Comic Sans MS, cursive;' +
        'Courier New/Courier New, Courier, monospace;' +
        'Georgia/Georgia, serif;' +
        'Lucida Sans Unicode/Lucida Sans Unicode, Lucida Grande, sans-serif;' +
        'Tahoma/Tahoma, Geneva, sans-serif;' +
        'Times New Roman/Times New Roman, Times, serif;' +
        'Trebuchet MS/Trebuchet MS, Helvetica, sans-serif;' +
        'Verdana/Verdana, Geneva, sans-serif;' +
        'Fredoka One, cursive;' +
        'Nunito, sans-serif;',
        # end font_names
        'toolbar': 'Custom',
        'toolbar_Custom': [
            # formatting
            ['Styles', 'Format'],
            ['Font', 'FontSize'],
            ['Bold', 'Italic', 'Underline', 'Strike'],
            ['Subscript', 'Superscript'],
            ['TextColor', 'BGColor'],
            ['JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock'],
            ['Outdent', 'Indent'],
            ['Link', 'Unlink'],
            # content
            ['NumberedList', 'BulletedList'],
            ['Image', 'Iframe', 'Table', 'HorizontalRule'],
            ['Blockquote', 'CreateDiv', 'CodeSnippet'],
            ['Smiley', 'SpecialChar'],
            # utilities
            ['Cut', 'Copy', 'Paste'],
            ['Find', 'Replace', 'SelectAll'],
            ['Maximize', 'ShowBlocks', 'Source'],
            ['Undo', 'Redo'],
        ],
    }
}
