<?php
/**
 * Created by PhpStorm.
 * User: juliano
 * Date: 24/06/18
 * Time: 19:25
 */

function listaCategorias($conexao){
    $categorias = array();
    $query = "select * from categorias";
    $resultado = mysqli_query($conexao, $query);

    while($categoria = mysqli_fetch_assoc($resultado)){
        array_push($categorias, $categoria);
    }

    return $categorias;
}