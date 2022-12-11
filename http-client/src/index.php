<html>
<head>
    <title>App page</title>
</head>
<body>
    <h2>App page</h2>
    <h3>Replace Text:</h3>
    <?php
    if (isset($_POST['s'])){
        $myCurl = curl_init();
    curl_setopt_array($myCurl, array(
        CURLOPT_URL => 'http://nginxserver/api/'.$_POST['s'],
        CURLOPT_RETURNTRANSFER => true,
        CURLOPT_HEADER => false,
    ));
    $response = curl_exec($myCurl);
    $return= curl_exec($myCurl);
    curl_close($myCurl);

    echo "Ответ на Ваш запрос: ".$response;
    }
    ?>
    <form action="index.php" method="post">
    <label for="first_operand">First operand </label>
    <input type="text" name="s" id="s" required>
    <input type="submit" value="RUN!">
</body>
</html>