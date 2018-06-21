<?php
    $regexp = '~-~';
    $alvo = '31-12-2007';
    $novo_texto = '/';
    $resultado = preg_replace($regexp, $novo_texto, $alvo);
    echo $resultado;
