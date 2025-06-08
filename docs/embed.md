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

<br>
<br>
<br>
<br>

## Outros testes

1.Embed



![Alt text](https://open-geodata.readthedocs.io/pt/latest/assets/amn/file.pdf){ type=application/pdf style="min-height:50vh;width:100%" }

<br>

1. Obtendo dddd

[dssdsdaddsa]('./assets/amn/file.pdf'){ type=application/pdf }

[ssss](http://127.0.0.1:8000/pt/latest/assets/amn/file.pdf)
