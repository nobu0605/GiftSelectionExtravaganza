<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Gift Selector</title>
</head>
<body>
    <h1>Gift Selector</h1>

    <?php
    $gifts = [
        "Book", "Toy", "Gadget", "Video Game", "Headphones",
        "Smartphone", "Laptop", "Watch", "Shoes", "Wallet",
        "Headset", "Camera", "Drone", "Smart Watch", "Bluetooth Speaker"
    ];

    if ($_SERVER['REQUEST_METHOD'] === 'GET' && isset($_GET['indices'])) {
        $query_string = http_build_query(['indices' => $_GET['indices']]);
        $query_string = urldecode($query_string);

        $query_string = preg_replace('/indices\[\d+\]/', 'indices[]', $query_string);
       
        $output = shell_exec("python3 gift_selector.py \"$query_string\"");
        if ($output) {
            echo $output;
        } else {
            echo "<h1>Error: Failed to execute Python script.</h1>";
        }
        exit;
    }
    ?>

    <form method="GET" action="gift_selector.php">
        <p>Select your gifts:</p>
        <?php
        foreach ($gifts as $index => $gift) {
            echo "<input type='checkbox' name='indices[]' value='{$index}'> {$gift}<br>";
        }
        ?>
        <button type="submit">Submit</button>
    </form>
</body>
</html>
