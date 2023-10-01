<?php // vars ---

$title = 'Results';


// !vars ---
?>

<?php require_once "../header.php"; ?>


<?php // main ---

$data_of_msg = 'name:'.$_POST['name'].';'
			   .'email:'.$_POST['email'].';'
			   .'msg:'.$_POST['msg'];
$cmd = 'echo "'.$data_of_msg.'" | python3 -u /var/www/post_msg/`write_new_msg.py';

echo $data_of_msg."<br>";

exec(
	$cmd,
	$output,
	$exitcode
);


//echo "<h1>".$output[0]."</h1> <br>";

//for ($i = 1; i < count($output); ++$i)
//	echo "<h3>".$output[i]."</h3> <br>";
echo $exitcode;

// !main ---
?>


<?php require_once "../footer.html"; ?>

