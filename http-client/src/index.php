<html>
<head>
 <title>App page</title>
</head>
    <body>
      <h2>App page</h2>
       <h3>Summ operands:</h3>
//блок 1
 <?php
 if (isset($_POST['first']) && isset($_POST['second'])){
 $myCurl = curl_init();
 curl_setopt_array($myCurl, array(
 CURLOPT_URL =>
'http://nginxserver/api/'.$_POST['first'].'/'.$_POST['second'],
 CURLOPT_RETURNTRANSFER => true,
 CURLOPT_HEADER => false,
 ));
 $response = curl_exec($myCurl);
 curl_close($myCurl);

 echo "Ответ на Ваш запрос: ".$response;
 }
 ?>
 <form action="index.php" method="post">
 <label for="first_operand">First operand </label>
 <input type="number" name="first" id="first" required>
 <label for="second_operand">Second operand </label>
 <input type="number" name="second" id="second" required>
 <input type="submit" value="RUN!">
 </form>
 <h3>Get image</h3>
//блок 2
 <?php
 if (isset($_POST['image'])){
//функция генерации рандомной строки для именования картинки
 function generateRandomString($length = 10) {
 $characters =
'0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ';
 $charactersLength = strlen($characters);
 $randomString = '';
 for ($i = 0; $i < $length; $i++) {
 $randomString .= $characters[rand(0, $charactersLength
- 1)];
 }
 return $randomString;
 }
 $myCurl = curl_init();
 curl_setopt_array($myCurl, array(
 CURLOPT_URL => 'http://nginxserver/api/img',
 CURLOPT_RETURNTRANSFER => true,
 CURLOPT_HEADER => false,
 ));
 $response = curl_exec($myCurl); //получена json-строка
 curl_close($myCurl);
 $response_array = json_decode($response, true); //декодирование json-строки в ассоциативный массив[29]
 var_dump($response_array);//вывод на страницу json-строки результата
 $base64_code = $response_array['image_base64'];
 $encoding = $response_array['encoding'];
 $image_path = "./images/".generateRandomString().".jpg";//путь к картинке относительный
 $image_path_full= "/var/www/html/".$image_path; // абсолютный путь к картинке
 $fp = fopen($image_path_full, "w+");// открытие файла на запись[30]
 fwrite($fp, base64_decode($base64_code)); //запись в файл декодированных байтов[31]
 fclose($fp);// закрытие файла
 echo '<img src="'.$image_path.'">'; // вывод картинки на страницу
 }
 ?>
            <form action="index.php" method="post">
             <input type="hidden" name="image" id ="image" value=1/>
            <input type="submit" value="GET IMAGE!">
        </form>
    </body>
</html>
