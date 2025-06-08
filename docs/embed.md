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

saddsdsadasdsa
dsa
dsa
das
d
sadsadsadsads

![Alt text]('assets/amn/file.pdf'){ type=application/pdf }

[dssdsdaddsa]('assets/amn/file.pdf'){ type=application/pdf }

## Exemplo: Embedando PDF

<object data="assets/amn/file.pdf" type="application/pdf" width="100%" height="600px">
    <p>Seu navegador não suporta PDF embedado. <a href="assets/amn/file.pdf">Clique aqui para baixar o PDF</a>.</p>
</object>

[Baixar PDF](assets/amn/file.pdf)
