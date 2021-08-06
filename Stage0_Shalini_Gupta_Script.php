<?php
function hamdist($slack,$twitter)
{
	$i=0;
	$count=0;
	for($i=0;$slack[$i]!='';$i++)
	{
		if($slack[$i]!=$twitter[$i])
		$count+=1;
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
