<?php
    $regexp = '~(\d\d)(\w)~';
    $alvo = '12a34b56c';
    $achou = preg_match($regexp, $alvo, $match);
    echo $match[0];
