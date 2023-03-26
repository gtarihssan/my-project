$(document).ready(function(){

    var myrep=`
    <p class="p1">mun</p>
    <p class="p2">username</p>
    <p class="p3">titre<p class="date">datee</p></p>
    <p class="p4">text</p>

    `

    $('.visit').click(function(){

        var dec_slugyy=$(this).data('value')
        
         $.ajax({
            
            url : '/visit_deccheck/',
            type : 'GET', 
            data : {
                dec_slugy : dec_slugyy
            },
            success : function(response){
                var myrep1=myrep.replace('mun', response.mun)
                .replace('username' , response.username)
                .replace('titre' , response.titre)
                .replace('datee' , response.date)
                .replace('text' , response.text)


                $('.dec_to_visit').html(myrep1)
            }


         })

    });

});