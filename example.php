<?php

//находит финальную ссылку после всех редиректов для ссылки $text
function get_final_link($text) {
    $url = "http://83.143.112.43:4444";

    //сессия
    $ch = curl_init($url);

    //настройка:

    //результат должен быть str
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);

    //тип запроса- post
    curl_setopt($ch, CURLOPT_POST, true);

    // подготавливаем словарь
    curl_setopt($ch, CURLOPT_POSTFIELDS, ['url' => $text]);

    //выполняем ссесию
    $response = curl_exec($ch);

    // проверить на вшивость
    if (curl_errno($ch)) {
        // Если ошибка была, выводим сообщение об ошибке.
        echo "ОШИБКА ЗАПРОСА: " . curl_error($ch) . "\n";
        //закрываем сессию
        curl_close($ch);
        //делаем вид что так и было
        return $text;
    }

    //получаем код ответа
    $http_code = curl_getinfo($ch, CURLINFO_HTTP_CODE);

    //если успешно
    if ($http_code >= 200 && $http_code < 300) {
        //выводим сообщение об успехе
        //echo "УСПЕШНО.\n";
        //выводим ответ
        //echo "ОТВЕТ: " . $response . "\n\n";
        //закрыть сессию
        curl_close($ch);
        //вернуть финальную ссылку
        return $response;
    } else {
        //ошибка
        echo "ОШИБКА HTTP: " . $http_code . "\n";
        //закрыть сессию
        curl_close($ch);
        //будем считать что так и было
        return $text;
    }
}

//как пользоваться
//вместо https://minilink.pro/NtTd другое
//$final_link = get_final_link("https://minilink.pro/NtTd");
//echo "Final link: " . $final_link . "\n";

?>