<?php // vars ---

$title = "Hi, php :)";


// !vars ---
?>

<?php require_once "./header.php"; ?>

<?php // main ---

require_once "./greeting.html";

echo "<h5>Share the post or read others!</h4>";

for ($i = 0; $i < 2; ++$i)
	echo "<br>";


require_once "./read_msg_btn.html";
echo "<br>";
require_once "./new_msg_btn.html";

// !main ---
?>


<?php require_once "./footer.html"; ?>

