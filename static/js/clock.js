var intVal, myclock;

	$(window).resize(function(){
		window.location.reload()
	});

	$(document).ready(function(){

		var audioElement = new Audio("");

		//clock plugin constructor
		$('#myclock').thooClock({
			size:$(document).height()/1.4,
			onAlarm:function(){
				//all that happens onAlarm
				$('#alarm1').show();
				alarmBackground(0);
				//audio element just for alarm sound
				document.body.appendChild(audioElement);
				var canPlayType = audioElement.canPlayType("audio/ogg");
				if(canPlayType.match(/maybe|probably/i)) {
					audioElement.src = 'http://nicesnippets.com/demo/alarm.ogg';
				} else {
					audioElement.src = 'http://nicesnippets.com/demo/alarm.mp3';
				}
				// erst abspielen wenn genug vom mp3 geladen wurde
				audioElement.addEventListener('canplay', function() {
					audioElement.loop = true;
					audioElement.play();
				}, false);
			},
			showNumerals:true,
			brandText:'THOOYORK',
			brandText2:'Germany',
			onEverySecond:function(){
				//callback that should be fired every second
			},
			//alarmTime:'15:10',
			offAlarm:function(){
				$('#alarm1').hide();
				audioElement.pause();
				clearTimeout(intVal);
				$('body').css('background-color','#FCFCFC');
			}
		});

	});



	$('#turnOffAlarm').click(function(){
		$.fn.thooClock.clearAlarm();
	});


	$('#set').click(function(){
		var inp = $('#altime').val();
		$.fn.thooClock.setAlarm(inp);
	});

	
	function alarmBackground(y){
			var color;
			if(y===1){
				color = '#CC0000';
				y=0;
			}
			else{
				color = '#FCFCFC';
				y+=1;
			}
			$('body').css('background-color',color);
			intVal = setTimeout(function(){alarmBackground(y);},100);
	}


 var _gaq = _gaq || [];
  _gaq.push(['_setAccount', 'UA-36251023-1']);
  _gaq.push(['_setDomainName', 'jqueryscript.net']);
  _gaq.push(['_trackPageview']);

  (function() {
    var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
    ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
    var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
  })();
