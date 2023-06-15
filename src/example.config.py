API_KEY = ''

SYSTEM_ROLE = 'Seja um tradutor. Não remova os campos especiais ' \
    'do texto e não traduza os campos especiais. Um campo ' \
    'especial começa com { e termina com }.'

USER_ROLE = 'Por favor, traduza o seguinte texto, preservando campos ' \
    'especiais (incluse outros campos não listados), quebras de linha ' \
    '(\\n) e tags HTML. Os campos especiais do tipo ' \
    '{{mf|<masculino>|<feminino>}} ' \
    'possuem texto dentro do campos especial, como por exemplo: ' \
    '{{mf|texto masculino|texto feminino}}. ' \
    'Já os campos especiais do tipo {{q|<campo1>|<campo2>}} possuem texto ' \
    'entre o campo especial, como por exemplo ' \
    '{{q|<valor que nao pode ser traduzido>}}' \
    '<texto que nao precisa ser traduzido>{{/q}}. ' \
    'Traduza apenas os campos especiais do tipo' \
    '{{mf|<masculino>|<feminino>}}, mas nao traduza os campos do tipo ' \
    '{{q|<campo1>|<campo2>}}. Se houver apenas uma palavra, não traduza. ' \
    'Tente preservar a mesma quantidade de palavras sem deixar muito ' \
    'diferente do texto original. ' \
    'Aqui está o texto:'
