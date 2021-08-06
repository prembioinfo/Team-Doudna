<?php
function hamdist($slack,$twitter)
{
	$count=0;
	$i=0;
	while (isset($slack[$i]) != '')
    {
        if ($slack[$i] != $twitter[$i])
            $count++;
        $i++;
    }
	return $count;
}
$name = "Shalini";
$email = "shalinigupta0299@gmail.com";
$slack = "@Shalini";
$biostack = "Data analytics and Vaccine informatics";
$twitter = "@Shashaa";
echo $name," ",$email," ",$slack," ",$biostack," ",$twitter," ";
echo hamdist($slack,$twitter);
?>
