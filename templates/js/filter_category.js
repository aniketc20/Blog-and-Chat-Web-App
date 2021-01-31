var csrf = $("input[name=csrfmiddlewaretoken]").val();
$("#{{ category.id }}").on('click', function() {
    var mainContainer = document.getElementById("result");
    $.ajax({
        url: '',
        type: 'post',
        data: {
            text: $(this).attr("id"),
            csrfmiddlewaretoken: csrf
        },
        success: function(response){
            //console.log(response.data);
            $("#all_blogs").hide();
            //$("#all_blogs").show();
            //$('.col-lg-6').html($('.col-lg-6',response.data[0]).html());
            for (var i = 0; i < response.data.length; i++) {
                console.log(response.data[i][1]);
                //var div = document.getElementsByClassName("card-title");
                var div = document.createElement("div");
                //$(".card-title").html(response.data[i][1])
                //mainContainer.innerHTML = 'Name: ' + response.data[i][1] + ' ';
                div.innerHTML = 'Name: ' + response.data[i][1] + ' ';
                mainContainer.appendChild(div);
            }
        }
    })
  });

$("#all").on('click', function() {
    var mainContainer = document.getElementById("result");
    $.ajax({
        url: '',
        type: 'post',
        data: {
            text: $(this).attr("id"),
            csrfmiddlewaretoken: csrf
        },
        success: function(response){
            //console.log(response.data);
            $("#all_blogs").show();
            //$("#all_blogs").show();
            //$('.col-lg-6').html($('.col-lg-6',response.data[0]).html());
            for (var i = 0; i < response.data.length; i++) {
                console.log(response.data[i][1]);
                //var div = document.getElementsByClassName("card-title");
                var div = document.createElement("div");
                //$(".card-title").html(response.data[i][1])
                //mainContainer.innerHTML = 'Name: ' + response.data[i][1] + ' ';
                div.innerHTML = 'Name: ' + response.data[i][1] + ' ';
                mainContainer.appendChild(div);
            }
        }
    })
  });