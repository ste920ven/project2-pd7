<?php
// File name: pixlr.php
if (isset($_REQUEST['image'])) {
    // GET
    $url = $_REQUEST['image'];
    $path = "./" . $_REQUEST['title'] . "." . $_REQUEST['type'];
    // SAVE IMAGE
    $fp = fopen($path, 'w');
    $ch = curl_init($url);
    curl_setopt($ch, CURLOPT_FILE, $fp);
    $data = curl_exec($ch);
    curl_close($ch);
    fclose($fp);
} elseif (isset($_FILES['image']['tmp_name'])) {
    // POST
    $type = $_REQUEST['type'];
    $title = $_REQUEST['title'];
    $path = "./" . $title . "." . $type;
    move_uploaded_file($_FILES['image']['tmp_name'], $path);
} else {
    // IMAGE LOADING
    $image = 'http://developer.pixlr.com/_image/example3.jpg';
    $imagePathParts = explode("/", $image);
    $title = array_pop($imagePathParts);
    $title = substr($title, 0, -4);
    $pixlrURL = "http://www.pixlr.com/express/?";
    $pixlrURL.= "target=".PATH_TO_YOUR_SITE."pixlr.php&";
    $pixlrURL.= "method=GET&";
    $pixlrURL.= "referer=localhost&";
    $pixlrURL.= "image=" . $image . "&";
    $pixlrURL.= "title=" . $title . "&";
    $pixlrURL.= "locktarget=true&locktitle=true";
    header("Location: " . $pixlrURL);
}
?>
