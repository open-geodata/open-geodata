<!--- file: docs/howto/embedding_pdf.md --->

{% with pdf_file = "assets/amn/file.pdf" %}

{% set solid_filepdf = '<i class="fas fa-file-pdf"></i>' %}
{% set empty_filepdf = '<i class="far fa-file-pdf"></i>' %}

## Example: Embedding a PDF file

<object data="{{ pdf_file }}" type="application/pdf">
    <embed src="{{ pdf_file }}" type="application/pdf" />
</object>

## Example: Creating a link to a PDF file

<a href="{{ pdf_file }}" class="image fit">{{ solid_filepdf }}</a>

{% endwith %}
