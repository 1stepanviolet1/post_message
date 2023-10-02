<?php // vars ---

$title = 'Results';


// !vars ---
?>

<?php require_once "../header.php"; ?>


<?php // main ---

$data_of_msg = 'name:'.$_POST['name'].';'
			   .'email:'.$_POST['email'].';'
			   .'msg:'.$_POST['msg'];
$cmd = 'echo "'.$data_of_msg.'" | python3 -u /var/www/post_msg/write_new_msg.py';


exec(
	$cmd,
	$output,
	$exitcode
);


echo "<br>";

echo "<div class=\"mx-4\">";
echo "<h1>".$output[0]."</h1> <br>";
echo "</div>";

for ($i = 1; $i < count($output); ++$i)
	echo "<h3>".$output[$i]."</h3> <br>";

echo "<div class=\"mx-4\">";
require_once "./return_to_main_page_btn.html";
echo "</div>";

// !main ---
?>


<?php require_once "../footer.html"; ?>

