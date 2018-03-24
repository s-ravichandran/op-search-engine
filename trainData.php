<?
	if($_POST['execute']) {
		$output = shell_exec('python train.py > data/featureFile.txt');
		// echo $output;
		// file_put_contents("data/featureFile.txt", "");
		$o = file('data/featureFile.txt');
		// print_r($o);
		$o[1] = str_replace("'",'"',$o[1]);
		$data = json_decode($o[1],TRUE);
		// print_r($data);
		// print $data;
		$i = 0;
		foreach($data as $key => $value){
			$labels[] = $key;
			$values[] = $value;
			$i++;
		}
	}
?>
<script type="text/javascript">
	
	var data = {
	
	labels : [<? foreach($data as $key => $value){ echo '"'.$key.'",'; } ?>],
	datasets : [
		{
			fillColor : "rgba(236, 240, 241,1.0)",
			strokeColor : "rgba(192, 57, 43,1.0)",
			data : [<? foreach($data as $key => $value){ echo $value.","; } ?>]
		}
	]
};

options = {
	scaleFontColor : "#FFF"
};

//Get context with jQuery - using jQuery's .get() method.
	var ctx = $("#featureChart").get(0).getContext("2d");
	//This will get the first returned node in the jQuery collection.
	var myNewChart = new Chart(ctx);

	new Chart(ctx).Bar(data,options);
</script>
<div class="row">
	<div class="col-md-8">
		
	</div>
	<div class="col-md-4">
		<canvas id="featureChart" width="400" height="400"></canvas>	
	</div>
</div>
