var signed = false;
var name;
var experience = 0;
var age;
var pictureShownTime = 2500;
var practicePath = 'images\\practice\\';
var expPath = 'images\\exp\\';
var pairNum = 0;
var numOfPairs = 3;
var Pairs;
var startDate, endDate;
var imageArray = [];

$( document ).ready(
	preload([
		practicePath + 'pair_0\\horse1.png',
		practicePath + 'pair_1\\horse0.png',
		practicePath + 'pair_1\\horse1.png',
		practicePath + 'pair_2\\horse0.png',
		practicePath + 'pair_2\\horse1.png',		
	])
);

$(function() {
	$( "#dialog-confirmPractice" ).dialog({
	  resizable: false,
	  dialogClass: "no-close",
	  autoOpen:false,
	  closeOnEscape: false,
	  height: "auto",
	  width: 400,
	  modal: true,
	  buttons: {
		"לא": function() {
			endDate = new Date();
			time = (endDate - startDate)/1000 
			$( this ).dialog( "close" );
			startPractice();
		},
		"כן": function() {
			endDate = new Date();
			time = (endDate - startDate)/1000 
			$( this ).dialog( "close" );
			startPractice()
		}
	  }
	});
	} );
	
	$(function() {
	$( "#dialog-confirmExp" ).dialog({
	  resizable: false,
	  dialogClass: "no-close",
	  autoOpen:false,
	  closeOnEscape: false,
	  height: "auto",
	  width: 400,
	  modal: true,
	  buttons: {
		"לא": function() {
			
		},
		"כן": function() {
			
		}
	  }
	});
	} );
	
function answer(isYes){
	endDate = new Date();
			time = (endDate - startDate) 
			Pairs[pairNum].Experience = experience;
			Pairs[pairNum].Name = name;
			Pairs[pairNum].Age = age;
			Pairs[pairNum].RT = time;
			Pairs[pairNum].Resp = Number(isYes);
			Pairs[pairNum].isSame = Number(Pairs[pairNum].isSame);
			Pairs[pairNum].ACC = Pairs[pairNum].isSame == isYes ? 1 : 0;
			$('#isTheSameId').hide();
			pairNum++;
			startExp()
}	

function preload(arrayOfImages) {
    $(arrayOfImages).each(function(){
        $('<img/>')[0].src = this;
        // Alternatively you could use:
        // (new Image()).src = this;
    });
}

function checkUser(){
	if ($('#userId').val() == 'admin' && $('#pwdId').val() == '123456'){
		$('#formId').hide();
		$('#formDetailsId').show();
		$('#testedNameId').focus();		
		signed = true;
	}
	else {
		$('#InvalidUserId').show();
	}
}

function ValidateFields(){
	var isValid= true;
	if ($('#testedNameId').val() == ''){
		$('#nameFormGroup').addClass('has-error');
		isValid = false;
	}
	if ($('#testedAgeId').val() == ''){
		$('#ageFormGroup').addClass('has-error');
		isValid = false;
	}
	if (!isValid) return;
	name = $('#testedNameId').val()
	age = $('#testedAgeId').val()
	experience = $('#testedExpId').val() == '' ? 0 : $('#testedExpId').val()
	$('#formDetailsId').hide();	
	$('#guidlinesId').show();
	$('.navbar-fixed-top').slideUp();
}

function startPractice(){
	if (pairNum < numOfPairs){
		$('#guidlinesId').hide();
		$('#practiceId').show();
		setTimeout(showSecondImage, pictureShownTime);
	}
	else {
		pairNum = 0;
		numOfPairs = 0;
		$('#guidlines2Id').show();
	}
}

function showSecondImage(){
	$('#practiceId img').attr('src', practicePath + 'pair_' + pairNum + '\\horse1.png')
	pairNum++;
	setTimeout(showPrompt, pictureShownTime);
}

function showPrompt(){
	$('#practiceId').hide();	
	$('#practiceId img').attr('src', practicePath + 'pair_' + pairNum + '\\horse0.png')
	//$( "#dialog-confirmPractice" ).dialog( "open" )
	$('#isTheSamePractiveId').show();
	startDate = new Date();
}

function getDataAndstartExp(){
	$.ajax({
	    url: 'GetJsonData',
		type: 'GET',
		dataType: 'json',
	    success: function(data) {
			Pairs = data;
			numOfPairs = Pairs.length
			$('#guidlines2Id').hide();
			$('#practiceId img').attr('src', Pairs[pairNum].path1);
			startExp();
	    }	   
	});
}

function startExp(){
	if (pairNum < numOfPairs){		
		$('#practiceId').show();
		setTimeout(showExpSecondImage, pictureShownTime);
	}
	else{
		$('#guidlines3Id').show();
		var dateCSV = JSONToCSVConvertor(Pairs, 'results', true)
		$.ajax({
			url: 'SetResults',
			type: 'POST',
			data: {pairResults : JSON.stringify(Pairs)},
			contentType: 'application/json; charset=utf-8',
			success: function(data) {
				$.ajax({
					url: 'ReturnResults',
					type: 'GET',
				})
			}
		});
	}
}

function showExpSecondImage(){
	$('#practiceId img').attr('src', Pairs[pairNum].path2);
	setTimeout(showExpPrompt, pictureShownTime);
}

function showExpPrompt(){
	$('#practiceId').hide();
	if (pairNum + 1 < numOfPairs){ $('#practiceId img').attr('src', Pairs[pairNum + 1].path1); }	//set first image to prevent showing a flash of the second image when startExp is called
	//$( "#dialog-confirmExp" ).dialog( "open" );	
	$('#isTheSameId').show();
	startDate = new Date();
}

function JSONToCSVConvertor(JSONData, ResultFileName, ShowLabel) {
    var arrData = typeof JSONData != 'object' ? JSON.parse(JSONData) : JSONData;
    var CSV = '';
 
    //CSV += ResultTitle + '\r\n\n';
 
    if (ShowLabel) {
        var row = "";
 
        for (var index in arrData[0]) {
            row += index + ',';
        }
 
        row = row.slice(0, -1);
        CSV += row + '\r\n';
    }
 
    for (var i = 0; i < arrData.length; i++) {
        var row = "";
        for (var index in arrData[i]) {
            row += '"' + arrData[i][index] + '",';
        }
 
        row.slice(0, row.length - 1);
 
        CSV += row + '\r\n';
    }
 
    if (CSV == '') {
        alert("Invalid data");
        return "";
    }
 
    var fileName = "";
    fileName += ResultFileName.replace(/ /g, "_");
 
    if ((navigator.userAgent.indexOf('Trident') != -1 && navigator.userAgent.indexOf('MSIE') == -1) || navigator.userAgent.indexOf('MSIE') != -1) {
        var blob = new Blob([CSV], {
            type: "text/plain;charset=utf-8;",
        });
        navigator.msSaveOrOpenBlob(blob, fileName + '.csv' || "download");
    }
    else {
        var uri = 'data:text/csv;charset=utf-8,' + escape(CSV);
 
        var link = document.createElement("a");
        link.href = uri;
        link.style = "visibility:hidden";
        link.download = fileName + ".csv";
 
        document.body.appendChild(link);
        link.click();
        document.body.removeChild(link);
    }
	return CSV;
}
