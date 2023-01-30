# desafio_cnab
 Aplicação desenvolvida para upload, armazenamento e exibição de dados de um arquivo CNAB. A atividade do sexto módulo da formação em desenvolvimento Full Stack da Kenzie Academy Brasil.
 <br />

## Ferramentas utilizadas
* HTML
* Python
* Django

## Configuração do ambiente

Faça o clone do repositório e inicie o ambiente virtual
```bash
>python -m venv venv

após criar o ambiente ative-o:
>source venv/bin/activate
```

verifique as dependência do projeto e efetue a instalaçao:

```bash
>pip install -r requirements.txt
```

Agora será necessário configurar as migrações:
```bash
>python manage.py makemigration

após criar o ambiente ative-o:
>python manage.py migrate
```

Agora com o ambiente devidamente configurado, basta apenas rodar a aplicação:
```bash
> python manage.py runserver
```


