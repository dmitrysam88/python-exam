$('#selectExam').change(function () {
   $('#descriptionsExam').children('div').hide();
   $('#descriptionsExam').children('#'+$('#selectExam :selected').val()).show();
});