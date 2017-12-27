

def validate_file_extensionbib(value):
    import os
    from django.core.exceptions import ValidationError
    ext = os.path.splittext(value.name)[1]
    valid_extensions = ['.bib']
    if not ext.lower() in valid_extensions:
        raise ValidationError(u'Unsupported file extension. Please upload .bib file')


def validate_file_extensionpaper(value):
    import os
    from django.core.exceptions import ValidationError
    ext = os.path.splittext(value.name)[1]
    valid_extensions = ['.pdf', '.doc', '.docx', '.xls', '.xlsx']
    if not ext.lower() in valid_extensions:
        raise ValidationError(u'Unsupported file extension.')
