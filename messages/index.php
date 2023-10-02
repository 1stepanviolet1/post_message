<?php // vars ---

$title = 'Messages';


// !vars ---
?>

<?php require_once "../header.php"; ?>


<?php // main ---

require_once "./header_msgs.html";

exec(
	"python3 -u /var/www/messages/read_messages.py",
	$output,
	$exitcode
);

foreach ($output as $line)
	echo $line;

// !main ---
?>


<?php require_once "../footer.html"; ?>

